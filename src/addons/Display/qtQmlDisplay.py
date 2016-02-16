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

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
log = logging.getLogger(__name__)

from OCC.Display import OCCViewer
# from OCC.Display.backend import get_qt_modules
#
# QtCore, QtGui, QtWidgets, QtOpenGL = get_qt_modules()


from PyQt5.QtCore import Qt, pyqtProperty, QRectF, QUrl, QRect, pyqtSlot
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


class qtQmlBaseViewer(QQuickPaintedItem):
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

        if not self._have_backend:
            raise ValueError("no backend has been loaded yet... use "
                             "``get_backend`` first")

        if self._have_pyside:
            ### with PySide, self.winId() does not return an integer
            if sys.platform == "win32":
                ## Be careful, this hack is py27 specific
                ## does not work with python31 or higher
                ## since the PyCObject api was changed
                import ctypes
                ctypes.pythonapi.PyCObject_AsVoidPtr.restype = ctypes.c_void_p
                ctypes.pythonapi.PyCObject_AsVoidPtr.argtypes = [
                    ctypes.py_object]
                win_id = ctypes.pythonapi.PyCObject_AsVoidPtr(win_id)

        elif self._have_pyqt4 or self._have_pyqt5:
            ## below integer cast may be required because self.winId() can
            ## returns a sip.voitptr according to the PyQt version used
            ## as well as the python version
            if type(win_id) is not int:  # cast to int using the int() funtion
                win_id = int(win_id)
        return win_id

    # TODO: remove
    def resizeEvent(self, event):
        if self._inited:
            self._display.OnResize()


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

    def Test(self):
        if self._inited:
            self._display.Test()

    def focusInEvent(self, event):
        if self._inited:
            self._display.Repaint()

    def focusOutEvent(self, event):
        if self._inited:
            self._display.Repaint()

    @pyqtSlot(QPainter)
    def paint(self, painter):

        print ("sender painter: ", self.sender())


        if self._inited:
            print("repainting....")
            self._display.Context.UpdateCurrentViewer()

        if painter is None:
            print("fuck painter is none...")
            return

        if self._drawbox:
            self.makeCurrent()
            painter.setPen(QPen(QColor(0, 0, 0), 1))
            rect = QRect(*self._drawbox)
            painter.drawRect(rect)
            painter.end()
            self.doneCurrent()

    def ZoomAll(self, evt):
        self._display.FitAll()

    def wheelEvent(self, event):
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

    def dragMoveEvent(self, event):
        pass

    def mousePressEvent(self, event):
        self.setFocus()
        self.dragStartPos = point(event.pos())
        self._display.StartRotation(self.dragStartPos.x, self.dragStartPos.y)

    def mouseReleaseEvent(self, event):

        print ("mouse release event")

        pt = point(event.pos())
        modifiers = event.modifiers()

        if event.button() == Qt.LeftButton:
            pt = point(event.pos())
            if self._select_area:
                [Xmin, Ymin, dx, dy] = self._drawbox
                self._display.SelectArea(Xmin, Ymin, Xmin + dx, Ymin + dy)
                self._select_area = False
            else:
                # multiple select if shift is pressed
                if modifiers == Qt.ShiftModifier:
                    self._display.ShiftSelect(pt.x, pt.y)
                else:
                    # single select otherwise
                    self._display.Select(pt.x, pt.y)
        elif event.button() == Qt.RightButton:
            if self._zoom_area:
                [Xmin, Ymin, dx, dy] = self._drawbox
                self._display.ZoomArea(Xmin, Ymin, Xmin + dx, Ymin + dy)
                self._zoom_area = False

    def DrawBox(self, event):
        tolerance = 2
        pt = point(event.pos())
        dx = pt.x - self.dragStartPos.x
        dy = pt.y - self.dragStartPos.y
        if abs(dx) <= tolerance and abs(dy) <= tolerance:
            return
        self._drawbox = [self.dragStartPos.x, self.dragStartPos.y, dx, dy]
        self.update()

    def mouseMoveEvent(self, evt):
        pt = point(evt.pos())
        buttons = int(evt.buttons())
        modifiers = evt.modifiers()
        # ROTATE
        if (buttons == Qt.LeftButton and
                not modifiers == Qt.ShiftModifier):
            dx = pt.x - self.dragStartPos.x
            dy = pt.y - self.dragStartPos.y
            self._display.Rotation(pt.x, pt.y)
            self._drawbox = False
        # DYNAMIC ZOOM
        elif (buttons == Qt.RightButton and
              not modifiers == Qt.ShiftModifier):
            self._display.Repaint()
            self._display.DynamicZoom(abs(self.dragStartPos.x),
                                      abs(self.dragStartPos.y), abs(pt.x),
                                      abs(pt.y))
            self.dragStartPos.x = pt.x
            self.dragStartPos.y = pt.y
            self._drawbox = False
        # PAN
        elif buttons == Qt.MidButton:
            dx = pt.x - self.dragStartPos.x
            dy = pt.y - self.dragStartPos.y
            self.dragStartPos.x = pt.x
            self.dragStartPos.y = pt.y
            self._display.Pan(dx, -dy)
            self._drawbox = False
        # DRAW BOX
        # ZOOM WINDOW
        elif (buttons == Qt.RightButton and
              modifiers == Qt.ShiftModifier):
            self._zoom_area = True
            self.DrawBox(evt)
        # SELECT AREA
        elif (buttons == Qt.LeftButton and
              modifiers == Qt.ShiftModifier):
            self._select_area = True
            self.DrawBox(evt)
        else:
            self._drawbox = False
            self._display.MoveTo(pt.x, pt.y)


    @pyqtSlot()
    def sync(self):
        print ("OMG, sync, do something....")
        if not self._renderer_bound:
            win  = self.window()
            painter = QPainter()
            win.beforeSynchronizing.connect(lambda: self.paint(painter), Qt.DirectConnection)
            self._renderer_bound = True

        if self._inited:
            print("resizing")
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
            #win.sceneGraphInvalidated.connect(self.cleanup, Qt.DirectConnection)
            win.setClearBeforeRendering(False)

            # win.mouseReleaseEvent.connect(self.mouseReleaseEvent)



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
