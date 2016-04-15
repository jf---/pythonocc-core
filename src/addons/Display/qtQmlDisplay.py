#!/usr/bin/env python

##Copyright 2009-2014 Thomas Paviot (tpaviot@gmail.com)
##
##This file is part of pythonOCC.
##
##pythonOCC is free software: you can redistribute it and/or modify
##it under the terms of the GNU Lesser General Public License as published by
##the Free Software Foundation, either version 3 of the License, or
##(at your option) any later version.
##
##pythonOCC is distributed in the hope that it will be useful,
##but WITHOUT ANY WARRANTY; without even the implied warranty of
##MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##GNU Lesser General Public License for more details.
##
##You should have received a copy of the GNU Lesser General Public License
##along with pythonOCC.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import print_function

import logging
import sys

from OCC.BRepPrimAPI import BRepPrimAPI_MakeBox

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
log = logging.getLogger(__name__)

from OCC.Display import OCCViewer

from PyQt5.QtCore import Qt, QUrl, pyqtSlot, QMutex, pyqtProperty, pyqtSignal, QObject
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import qmlRegisterType
from PyQt5.QtQuick import QQuickItem, QQuickView, QQuickWindow

# --------------------------------------------------------------------------
# these are names of actions that invoke the OpenGL viewport to be redrawn
# such actions need to be invoked through the QQuickview.window().update method
# this way, all command that redraw the viewport are invoked synchronously
# --------------------------------------------------------------------------

ON_ZOOM = "on_zoom"
ON_ZOOM_AREA = "on_zoom_area"
ON_ZOOM_FACTOR = "on_zoom_factor"
ON_ZOOM_FITALL = "on_zoom_fitall"
ON_DYN_ZOOM = "on_dyn_zoom"
ON_DYN_ROT = "on_dyn_rot"
ON_DYN_PAN = "on_dyn_pan"
ON_MOVE_TO = "on_move_to"
ON_SHIFT_SELECT = "on_shift_select"
ON_SELECT = "on_select"
ON_SELECT_AREA = "on_select_area"


class point(object):
    def __init__(self, obj=None):
        self.x = 0
        self.y = 0
        if obj is not None:
            self.set(obj)

    def set(self, obj):
        self.x = obj.x()
        self.y = obj.y()


class Mutex(QMutex):
    def __init__(self):
        QMutex.__init__(self)

    def __enter__(self):
        print("lock")
        self.lock()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("unlock")
        self.unlock()


class qtQmlBaseViewer(QQuickItem):
    ''' The base Qt Widget for an OCC viewer
    '''

    def __init__(self, parent=None):
        super(qtQmlBaseViewer, self).__init__(parent)
        self.windowChanged.connect(self.handleWindowChanged)

        # self.setFlag(self.ItemHasContents, True)
        self.setFlag(self.ItemAcceptsDrops, True)

        self._display = None

        # for interconnection with rendering thread
        self.mutex = Mutex()

        # -----
        # STATE
        # -----

        self._inited = False

        # TODO: rename...
        # is the OCCViewer initialized?
        self._renderer_bound = False

        # QPoint stored on mouse press
        self._point_on_mouse_press = [0, 0]

        # QPoint stored on mouse move
        self._point_on_mouse_move = [0, 0]

        # stores the delta between self._point_on_mouse_press and self._point_on_mouse_move
        self._delta_event_pos = None
        self._current_action = self.current_action = None

        # mouse button state
        self._is_right_mouse_button_surpressed = False
        self._is_left_mouse_button_surpressed = False

        # -----
        # STATE
        # -----

    @pyqtProperty("QVariantList") #, notify=sigUpdateMouseDelta)
    def point_on_mouse_press(self):
        # print("on mouse press {}".format(self._point_on_mouse_press))
        return self._point_on_mouse_press

    @point_on_mouse_press.setter
    def point_on_mouse_press(self, coord):
        print("point_on_mouse_press was set to: {}".format(coord))
        self._point_on_mouse_press = coord

    @pyqtProperty("QVariantList")
    def point_on_mouse_move(self):
        return self._point_on_mouse_move

    @point_on_mouse_move.setter
    def point_on_mouse_move(self, val):
        self._point_on_mouse_move = val

    @pyqtProperty("QVariantList")
    def delta_mouse_event_pos(self):
        """delta between previous_event and next_event"""
        pos_a = self._point_on_mouse_press
        pos_b = self._point_on_mouse_move
        try:
            dX = pos_a.x() - pos_b.x()
            dY = pos_a.y() - pos_b.y()
            return [dX, dY]
        except AttributeError:
            return [-1, -1]

    @property
    def is_right_mouse_button_surpressed(self):
        return self._is_right_mouse_button_surpressed

    @is_right_mouse_button_surpressed.setter
    def is_right_mouse_button_surpressed(self, value):
        self._is_right_mouse_button_surpressed = value

    @property
    def is_left_mouse_button_surpressed(self):
        return self._is_left_mouse_button_surpressed

    @is_left_mouse_button_surpressed.setter
    def is_left_mouse_button_surpressed(self, value):
        self._is_left_mouse_button_surpressed = value

    def GetHandle(self):
        ''' returns an the identifier of the GUI widget.
        It must be an integer
        '''
        win_id = self._winId
        if type(win_id) is not int:  # cast to int using the int() funtion
            win_id = int(win_id)
        return win_id


class qtQmlViewer3d(qtQmlBaseViewer):

    # sigUpdateMouseDelta = pyqtSignal()


    def __init__(self, *kargs):
        super(qtQmlViewer3d, self).__init__()
        self._drawbox = False
        self._zoom_area = False
        self._select_area = False
        self._inited = False
        self._leftisdown = False
        self._middleisdown = False
        self._rightisdown = False
        self._selection = None
        self._drawtext = True
        self.dragStartPos = point()
        # self.sigUpdateMouseDelta.connect(self.on_update_mouse_delta)

    def on_update_mouse_delta(self):
        print("updated mouse delta!!!!")

    @pyqtSlot()
    def InitDriver(self):
        self._display = OCCViewer.Viewer3d(self.GetHandle())
        self._display.Create()
        # background gradient
        self._display.set_bg_gradient_color(206, 215, 222, 128, 128, 128)
        # background gradient
        self._display.display_trihedron()
        self._display.SetModeShaded()
        self._display.EnableAntiAliasing()
        self._inited = True
        # dict mapping keys to functions
        self._SetupKeyMap()

        box = BRepPrimAPI_MakeBox(1, 1, 1).Shape()
        self._display.DisplayShape(box)
        self._display.FitAll()

    def on_zoom_area(self):
        dx, dy = self.delta_mouse_event_pos

        tolerance = 2
        if abs(dx) <= tolerance and abs(dy) <= tolerance:
            # zooming at a near nil value can segfault the opengl viewer
            pass
        else:
            if not self.is_right_mouse_button_surpressed:
                coords = [self.point_on_mouse_press[0],
                          self.point_on_mouse_press[1],
                          self.point_on_mouse_move[0],
                          self.point_on_mouse_move[1]]
                self._display.ZoomArea(*coords)

    def on_zoom_factor(self):
        self._display.ZoomFactor(self.zoom_factor)

    def on_zoom_fitall(self):
        """ handle fitting the scene in the viewport

        invoked on pressing "f"

        """
        self._display.FitAll()

    def on_zoom(self):
        self._zoom_area = True

    def on_dyn_zoom(self):
        """ handle zooming of the viewport

        through the shift + right mouse button

        """
        self._display.DynamicZoom(self.point_on_mouse_press[0],
                                  self.point_on_mouse_press[1],
                                  self.point_on_mouse_move[0],
                                  self.point_on_mouse_move[1]
                                  )
        self.point_on_mouse_press = self._point_on_mouse_move

    def on_dyn_rot(self):
        """ handle rotation of the viewport

        """
        print ("rotate view, start: {}, current: {}".format(self.point_on_mouse_press, self.point_on_mouse_move))
        self._display.Rotation(*self.point_on_mouse_move)
        # self.point_on_mouse_press = self.point_on_mouse_move


    def on_dyn_pan(self):
        """ handle panning of the viewport

        """
        dx, dy = self.delta_mouse_event_pos
        self.point_on_mouse_press = self._point_on_mouse_move
        self._display.Pan(-dx, dy)

    def on_move_to(self):
        # Relays mouse position in pixels theXPix and theYPix to the
        # interactive context selectors
        # This is done by the view theView passing this position to the main
        # viewer and updating it
        # Functions in both Neutral Point and local contexts

        # TODO: 6.9.1 changes this, important...
        # If theToRedrawOnUpdate is set to false, callee should call
        # RedrawImmediate() to highlight detected object.
        print(" no specific action -> MoveTo")
        self._display.MoveTo(*self.point_on_mouse_move)

    def on_select(self):
        self._display.Select(*self.point_on_mouse_move)

    def on_shift_select(self):
        self._display.ShiftSelect(*self.point_on_mouse_move)

    def on_select_area(self):
        pass
        # TODO: not really implemented
        # self._display.SelectArea(Xmin, Ymin, Xmin+dx, Ymin+dy)

    def _dispatch_camera_command_actions(self):
        """ dispatches actions that involve zooming, panning or rotating
        the viewport. Any of these actions invokes redrawing the view.
        This is why its relevant that these are handled in a specific method

        This method is to be called **exclusisely** from the .paintEvent method
        since here it can be interwoven with the overpainting routines

        Returns
        -------

        perform_action : bool
            True if any actions were performed, and implicitly the viewport
            was redrawn
            False otherwise

        """
        perform_action = False
        # if self.current_action:
        #     print("handling camera action:", self.current_action)

        try:
            if self.current_action is not None:
                action = getattr(self, self.current_action)
                action()
        except Exception:
            log.exception("could not invoke camera command action {0}".format(self.current_action))

        else:
            perform_action = True

        finally:
            self.current_action = None

        return perform_action

    def _SetupKeyMap(self):
        def set_shade_mode():
            self._display.DisableAntiAliasing()
            self._display.SetModeShaded()

        self._key_map = {ord('W'): self._display.SetModeWireFrame,
                         ord('S'): set_shade_mode,
                         ord('A'): self._display.EnableAntiAliasing,
                         ord('B'): self._display.DisableAntiAliasing,
                         ord('H'): self._display.SetModeHLR,
                         ord('F'): self._display.FitAll,
                         ord('G'): self._display.SetSelectionMode}

    def keyPressEvent(self, event):
        code = event.key()
        if code in self._key_map:
            self._key_map[code]()
        else:
            msg = "key: {0}\nnot mapped to any function".format(code)
            log.info(msg)

    def focusInEvent(self, event):
        if self._inited:
            self._display.Repaint()

    def focusOutEvent(self, event):
        if self._inited:
            self._display.Repaint()

    def update(self):
        window = self.window()
        if window:
            # print("update")
            self.window().update()

    # def paint(self):
    #
    #     sender = self.sender()
    #     print("sender painter: ", sender)
    #
    #     if self._inited:
    #         print("repainting....")
    #         self._display.Context.UpdateCurrentViewer()

    def paint(self):
        """ handles all actions that redraw the viewport

        actions like panning, zooming and rotating the view invoke
        redrawing it therefore, these actions need to be performed
        in the paintEvent method this way, redrawing the view takes place
        synchronous with the overpaint action

        not respecting this order would lead to a jittering view

        See Also
        --------
        this method is also invoked through the self.update method, see the
        mouseMoveEvent method

        """
        if self._inited:
            pass
            # with self.mutex:
            # glViewport()
            # print("paint")
            # action = self._dispatch_camera_command_actions()
            # if not action:
            #     # print ("extra redraw???")
            #     self._display.View.Redraw()
            # time.sleep(.1)

    def wheelEvent(self, event):
        delta = event.angleDelta().y()

        if delta > 0:
            self.zoom_factor = 1.3
        else:
            self.zoom_factor = 0.7
        self.current_action = ON_ZOOM_FACTOR
        # self.point_on_mouse_move = event
        # self.paint()
        self.update()

    @pyqtSlot(int, int, int)
    def mousePressEvent(self, mouse_button, x, y):
        self.point_on_mouse_press = [x, y]
        print("start rotation at {}, {}".format(x,y))
        self._display.StartRotation(x,y)

        if mouse_button == Qt.RightButton:
            self.is_right_mouse_button_surpressed = True

        elif mouse_button == Qt.LeftButton:
            self.is_left_mouse_button_surpressed = True

        elif mouse_button == Qt.MidButton:
            pass
            # self.is_left_mouse_button_surpressed = True

        # if mouse_button == Qt.RightButton: # and modifiers == mouse_buttonQt.ShiftModifier:
        #     # ON_ZOOM_AREA
        #     self._drawbox = True

        # elif mouse_button == Qt.LeftButton and modifiers == Qt.ShiftModifier:
        #     # ON_SELECT_AREA
        #     self._drawbox = True
        #     self._select_area = True

        self.is_right_mouse_button_surpressed = True

    @pyqtSlot(int, int)
    def mouseReleaseEvent(self, x, y):
        self.sync()
        # self.point_on_mouse_move = [x, y]
        # print("mouse release")
        self.on_select()

        # if mouse_button == Qt.RightButton:
        #     self.is_right_mouse_button_surpressed = False
        #     # if modifiers == Qt.ShiftModifier:
        #     #     self.current_action = ON_ZOOM_AREA
        #
        # if mouse_button == Qt.LeftButton:
        #     self.is_left_mouse_button_surpressed = False
        #     self.on_select()
        #
        #     if self._select_area:
        #         self.current_action = ON_SELECT_AREA
        #     # elif modifiers == mouse_buttonQt.ShiftModifier:
        #     #     self.current_action = ON_SHIFT_SELECT
        #     else:
        #         self.current_action = ON_SELECT

        self._drawbox = False
        self._select_area = False

        # self.update()

    def drawBox(self, event):
        tolerance = 2
        pt = point(event.pos())
        dx = pt.x - self.dragStartPos.x
        dy = pt.y - self.dragStartPos.y
        if abs(dx) <= tolerance and abs(dy) <= tolerance:
            pass
        else:
            self._drawbox = [self.dragStartPos.x, self.dragStartPos.y, dx, dy]
        self.update()

    @pyqtSlot(int, int, int)
    def mouseMoveEvent(self, mouse_button, x, y):

        print( "mouse button: {}".format(mouse_button))

        # self.sync()
        self.point_on_mouse_move = [x, y]

        # rotate
        if mouse_button == Qt.LeftButton:  # and not modifiers == Qt.ShiftModifier:
            # self.current_action = ON_DYN_ROT
            self.on_dyn_rot()

        # dynamic zoom
        elif mouse_button == Qt.RightButton:  # and not modifiers == Qt.ShiftModifier:
            # self.current_action = ON_DYN_ZOOM
            self.on_dyn_zoom()

        # dynamic panning
        elif mouse_button == Qt.MidButton:
            # self.current_action = ON_DYN_PAN
            self.on_dyn_pan()

        # zoom window, overpaints rectangle
        elif mouse_button == Qt.RightButton:  # and modifiers == Qt.ShiftModifier:
            # self.current_action = ON_ZOOM_AREA
            # self.on_dyn
            pass

        # select area
        elif mouse_button == Qt.LeftButton:  # and modifiers == Qt.ShiftModifier:
            # self.current_action = ON_SELECT_AREA
            self.on_select_area()

        else:
            # Live selection...
            # print("moveto...")
            self._display.MoveTo(x, y)
            return
            # self._display.Context.InitSelected()
            # if not self._display.Context.HasNextDetected():
            #     return
            #
            # print ("detection!")

        self.update()

    def sync(self):
        # print("sync")
        # view_size = self.window().size() * self.window().devicePixelRatio()

        # with self.mutex:
        if not self._renderer_bound:
            win = self.window()
            # win.beforeSynchronizing.connect(self.paint, Qt.DirectConnection)
            win.beforeRendering.connect(self.paint, Qt.DirectConnection)
            self._renderer_bound = True

            # self._display.OnResize()

    @pyqtSlot()
    def cleanup(self):
        print("OMG, cleanup, do something....")
        pass

    def handleWindowChanged(self, win):
        """

        Parameters
        ----------
        win : QQuickWindow
        """
        print("window changed")
        if win:
            win.beforeRendering.connect(self.sync, Qt.DirectConnection)
            # win.beforeSynchronizing.connect(self.sync, Qt.DirectConnection)
            # win.mousePressEvent.connect(self.mousePressEvent)
            win.setClearBeforeRendering(False)

    def geometryChanged(self, rec1, rec2):
        if self._inited:
            self._display.OnResize()
            print("r1, r2: {}, {}".format(rec1, rec2))
        super(qtQmlViewer3d, self).geometryChanged(rec1, rec2)


if __name__ == '__main__':
    import os
    import sys

    os.environ["QSG_RENDER_LOOP"] = "basic"

    app = QGuiApplication(sys.argv)
    qmlRegisterType(qtQmlViewer3d, "OCC", 1, 0, "OCCView")

    view = QQuickView()
    qtQmlViewer3d._winId = view.winId()

    view.setResizeMode(QQuickView.SizeRootObjectToView)
    view.setSource(
        QUrl.fromLocalFile(
            os.path.join(os.path.dirname(__file__), 'SimpleQml.qml')))
    view.show()

    # engine = QQmlApplicationEngine()
    # context = engine.rootContext()
    # qml_path = os.path.join(os.path.dirname(__file__), 'SimpleQml.qml')
    # engine.load(qml_path)

    sys.exit(app.exec_())
