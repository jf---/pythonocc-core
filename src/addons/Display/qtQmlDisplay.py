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
# from OCC.Display.backend import get_qt_modules
#
# QtCore, QtGui, QtWidgets, QtOpenGL = get_qt_modules()


from PyQt5.QtCore import Qt, pyqtProperty, QRectF, QUrl, QRect, pyqtSlot, QObject
from PyQt5.QtGui import QColor, QGuiApplication, QPainter, QPen
from PyQt5.QtQml import qmlRegisterType, QQmlListProperty
from PyQt5.QtQuick import QQuickItem, QQuickPaintedItem, QQuickView, QQuickWindow



class point(object):
    def __init__(self, obj=None):
        self.x = 0
        self.y = 0
        if obj is not None:
            self.set(obj)

    def set(self, obj):
        self.x = obj.x()
        self.y = obj.y()


class qtQmlBaseViewer(QQuickItem):
    ''' The base Qt Widget for an OCC viewer
    '''

    def __init__(self, parent=None):
        QQuickPaintedItem.__init__(self, parent)
        self.windowChanged.connect(self.handleWindowChanged)

        self._display = None
        self._inited = False

        self._renderer_bound = False

        # enable Mouse Tracking
        # self.setMouseTracking(True)
        # Strong focus
        # self.setFocusPolicy(Qt.WheelFocus)

        # required for overpainting the widget
        # self.setAttribute(Qt.WA_PaintOnScreen)
        # self.setAttribute(Qt.WA_NoSystemBackground)
        # self.setAutoFillBackground(False)

        # self.setFlag(self.ItemHasNoContents, False);


        # Qt backend bookkeeping
        # from OCC.Display.backend import have_pyside, have_pyqt4, have_pyqt5, \
        #     have_backend
        #
        self._have_pyside = False #have_pyside()
        self._have_pyqt4 = False #have_pyqt4()
        self._have_pyqt5 = True #have_pyqt5()
        self._have_backend = True # have_backend()

    def GetHandle(self):
        ''' returns an the identifier of the GUI widget.
        It must be an integer
        '''
        win_id = self._winId
        if type(win_id) is not int:  # cast to int using the int() funtion
            win_id = int(win_id)
        return win_id

class qtQmlViewer3d(qtQmlBaseViewer):
    def __init__(self, *kargs):
        qtQmlBaseViewer.__init__(self, *kargs)
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

        box = BRepPrimAPI_MakeBox(1,1,1).Shape()
        self._display.DisplayShape(box)
        self._display.FitAll()

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

    def paint(self):

        sender = self.sender()
        print ("sender painter: ", sender)

        if self._inited:
            print("repainting....")
            self._display.Context.UpdateCurrentViewer()

    def ZoomAll(self, evt):
        self._display.FitAll()

    def wheelEvent(self, event):
        print("wheel sender: ", self.sender())
        if self._have_pyqt5:
            delta = event.angleDelta().y()
        else:
            delta = event.delta()

        if delta > 0:
            zoom_factor = 2
        else:
            zoom_factor = 0.5
        self._display.Repaint()
        self._display.ZoomFactor(zoom_factor)

    def mousePressEvent(self, event):
        print ("mouse press")
        self.setFocus()
        self.dragStartPos = point(event.pos())
        self._display.StartRotation(self.dragStartPos.x, self.dragStartPos.y)

        self.window().update()

    # @pyqtSlot(int, int)
    # def mousePressEvent(self, x, y):
    #     # self.setFocus()
    #     self.dragStartPos.x = x
    #     self.dragStartPos.y = y
    #     self._display.StartRotation(self.dragStartPos.x, self.dragStartPos.y)

    @pyqtSlot(int, int, int)
    def mouseReleaseEvent(self, mouse_button, x, y):

        print ("mouse release event")

        if mouse_button == Qt.LeftButton:
            pt = point()
            pt.x = x
            pt.y = y

            if self._select_area:
                [Xmin, Ymin, dx, dy] = self._drawbox
                self._display.SelectArea(Xmin, Ymin, Xmin + dx, Ymin + dy)
                self._select_area = False
            # else:
            #     # multiple select if shift is pressed
            #     if modifiers == Qt.ShiftModifier:
            #         self._display.ShiftSelect(pt.x, pt.y)
            #     else:
            #         # single select otherwise
            #         self._display.Select(pt.x, pt.y)
        elif mouse_button == Qt.RightButton:
            if self._zoom_area:
                [Xmin, Ymin, dx, dy] = self._drawbox
                self._display.ZoomArea(Xmin, Ymin, Xmin + dx, Ymin + dy)
                self._zoom_area = False

        self.window().update()


    def DrawBox(self, event):
        tolerance = 2
        pt = point(event.pos())
        dx = pt.x - self.dragStartPos.x
        dy = pt.y - self.dragStartPos.y
        if abs(dx) <= tolerance and abs(dy) <= tolerance:
            return
        self._drawbox = [self.dragStartPos.x, self.dragStartPos.y, dx, dy]
        self.window().update()

    @pyqtSlot(int, int, int)
    def mouseMoveEvent(self, mouse_button, x, y):
        pt = point()
        pt.x = x
        pt.y = y
        # ROTATE
        if mouse_button == Qt.LeftButton:
            # and not modifiers == Qt.ShiftModifier):
            dx = pt.x - self.dragStartPos.x
            dy = pt.y - self.dragStartPos.y
            self._display.Rotation(pt.x, pt.y)
            self._drawbox = False
        # DYNAMIC ZOOM
        elif mouse_button == Qt.RightButton:
            # and not modifiers == Qt.ShiftModifier):
            self._display.Repaint()
            self._display.DynamicZoom(abs(self.dragStartPos.x),
                                      abs(self.dragStartPos.y), abs(pt.x),
                                      abs(pt.y))
            self.dragStartPos.x = pt.x
            self.dragStartPos.y = pt.y
            self._drawbox = False
        # PAN
        elif mouse_button == Qt.MidButton:
            dx = pt.x - self.dragStartPos.x
            dy = pt.y - self.dragStartPos.y
            self.dragStartPos.x = pt.x
            self.dragStartPos.y = pt.y
            self._display.Pan(dx, -dy)
            self._drawbox = False
        # DRAW BOX
        # ZOOM WINDOW
        elif mouse_button == Qt.RightButton:
            # and modifiers == Qt.ShiftModifier):
            self._zoom_area = True
            # self.DrawBox(evt)
        # SELECT AREA
        elif mouse_button == Qt.LeftButton:
            # and modifiers == Qt.ShiftModifier):
            self._select_area = True
            # self.DrawBox(evt)
        else:
            self._drawbox = False
            self._display.MoveTo(pt.x, pt.y)

        self.window().update()


    # @pyqtSlot()
    def sync(self):
        print ("OMG, sync, do something....")
        if not self._renderer_bound:
            win  = self.window()
            win.beforeSynchronizing.connect(self.paint, Qt.DirectConnection)
            self._renderer_bound = True

        if self._inited:
            # print("resizing")
            self._display.OnResize()

    @pyqtSlot()
    def cleanup(self):
        print ("OMG, cleanup, do something....")
        pass

    # @pyqtSlot(QQuickWindow)
    def handleWindowChanged(self, win):
        """

        Parameters
        ----------
        win : QQuickWindow
        """
        if win:
            win.beforeSynchronizing.connect(self.sync, Qt.DirectConnection)
            # win.mousePressEvent.connect(self.mousePressEvent)
            win.setClearBeforeRendering(False)




if __name__ == '__main__':
    import os
    import sys

    app = QGuiApplication(sys.argv)

    view = QQuickView()
    qtQmlViewer3d._winId = view.winId()

    qmlRegisterType(qtQmlViewer3d, "OCC", 1, 0, "OCCView")

    view.setResizeMode(QQuickView.SizeRootObjectToView)
    view.setSource(
            QUrl.fromLocalFile(
                    os.path.join(os.path.dirname(__file__),'SimpleQml.qml')))
    view.show()

    sys.exit(app.exec_())
