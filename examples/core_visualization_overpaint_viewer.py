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

"""

demonstrates overpainting of the OCC OpenGL viewer to share its OpenGL Context
with Qt

this allows for interesting interfaces, where elements are drawn as an overlay

:ref:`Catia's structure browser` is a well known application of this idea

the example is extends Qt's :ref:`OpenGL overpainting example`

.. Catia's structure browser::
        http://goo.gl/KBh7BL

.. OpenGL overpainting example::
        https://github.com/Werkov/PyQt4/blob/master/examples/opengl/overpainting.py


"""

from __future__ import print_function
import random
import sys

from OCC.Display.qtDisplay import qtViewer3d, get_qt_modules, point

QtCore, QtGui, QtOpenGL = get_qt_modules()

try:
    from OpenGL.GL import (glViewport, glMatrixMode, glOrtho, glLoadIdentity,
                           GL_PROJECTION, GL_MODELVIEW)
except ImportError:
    msg = "for this example, the OpenGL module is required" \
          "why not run \"pip install PyOpenGL\"\?"
    sys.exit(status=1)


class Bubble(object):
    def __init__(self, position, radius, velocity):
        self.position = position
        self.vel = velocity
        self.radius = radius

        self.innerColor = self.randomColor()
        self.outerColor = self.randomColor()
        self.updateBrush()

    def updateBrush(self):
        gradient = QtGui.QRadialGradient(QtCore.QPointF(self.radius, self.radius),
                                         self.radius, QtCore.QPointF(self.radius * 0.5, self.radius * 0.5))
        gradient.setColorAt(0, QtGui.QColor(255, 255, 255, 0))
        gradient.setColorAt(0.25, self.innerColor)
        gradient.setColorAt(1, self.outerColor)
        self.brush = QtGui.QBrush(gradient)

    def drawBubble(self, painter, mouse_intersects):
        painter.save()
        painter.translate(self.position.x() - self.radius,
                          self.position.y() - self.radius)
        painter.setBrush(self.brush)

        if mouse_intersects:
            font = painter.font()
            font.setPointSize(20)
            painter.setFont(font)
            painter.setPen(QtCore.Qt.red)
            painter.drawText(0, 0, "so hovering over!!!")

        painter.drawEllipse(0, 0, int(2 * self.radius), int(2 * self.radius))
        painter.restore()

    def randomColor(self):
        red = random.randrange(205, 256)
        green = random.randrange(205, 256)
        blue = random.randrange(205, 256)
        alpha = random.randrange(91, 192)
        return QtGui.QColor(red, green, blue, alpha)

    def move(self, bbox):
        self.position += self.vel
        leftOverflow = self.position.x() - self.radius - bbox.left()
        rightOverflow = self.position.x() + self.radius - bbox.right()
        topOverflow = self.position.y() - self.radius - bbox.top()
        bottomOverflow = self.position.y() + self.radius - bbox.bottom()

        if leftOverflow < 0.0:
            self.position.setX(self.position.x() - 2 * leftOverflow)
            self.vel.setX(-self.vel.x())
        elif rightOverflow > 0.0:
            self.position.setX(self.position.x() - 2 * rightOverflow)
            self.vel.setX(-self.vel.x())

        if topOverflow < 0.0:
            self.position.setY(self.position.y() - 2 * topOverflow)
            self.vel.setY(-self.vel.y())
        elif bottomOverflow > 0.0:
            self.position.setY(self.position.y() - 2 * bottomOverflow)
            self.vel.setY(-self.vel.y())

    def rect(self):
        return QtCore.QRectF(self.position.x() - self.radius,
                             self.position.y() - self.radius, 2 * self.radius,
                             2 * self.radius)


class GLWidget(qtViewer3d):
    def __init__(self, parent=None):
        super(GLWidget, self).__init__(parent)

        #: state
        self._initialized = False

        # no effect?
        self.doubleBuffer()

        midnight = QtCore.QTime(0, 0, 0)
        random.seed(midnight.secsTo(QtCore.QTime.currentTime()))

        self.xRot = 0
        self.yRot = 0
        self.zRot = 0
        self.bubbles = []

        # -------------------------------------------------------------------------------
        # create properties for the last coordinate, such that the stupid "point" conversion
        # takes place implicitly
        # -------------------------------------------------------------------------------

        self.lastPos = QtCore.QPoint()

        self.setMinimumSize(200, 200)
        self.setWindowTitle("Overpainting a Scene")

        # parameters for overpainting
        self.setAttribute(QtCore.Qt.WA_NoSystemBackground)
        self.setAutoFillBackground(False)

        # start the background thread that performs the overpainting of
        # the OpenGL view with bubbles
        self._setupAnimation()

        # bookkeeping properties
        self._previous_event = None
        self._next_event = None
        self._delta_event_pos = None
        self._current_action = self.current_action = None

    @property
    def previous_event(self):
        return self._previous_event

    @previous_event.setter
    def previous_event(self, value):
        self._previous_event = value

    @property
    def next_event(self):
        return self._next_event

    @next_event.setter
    def next_event(self, event):
        self._next_event = event
        if event.buttons() & QtCore.Qt.LeftButton:
            self._current_action = "CurAction3d_DynamicRotation"

        elif event.buttons() & QtCore.Qt.RightButton:
            pass

        else:
            self._current_action = None

    @property
    def delta_event_pos(self):
        """delta between previous_event and next_event"""
        pos_a = self._previous_event.pos()
        pos_b = self._next_event.pos()

        dX = pos_a.x() - pos_b.x()
        dY = pos_a.y() - pos_b.y()
        return dX, dY

    # @property
    # def current_action(self):
    #     return self._current_action

    def _setupAnimation(self):
        self.animationTimer = QtCore.QTimer()
        self.animationTimer.setSingleShot(False)
        self.animationTimer.timeout.connect(self.animate)
        self.animationTimer.start(250)

    def mousePressEvent(self, event):
        self.setFocus()
        self.lastPos = event.pos()
        self.dragStartPos = point(event.pos())

    def mouseReleaseEvent(self, event):
        pass

    def mouseMoveEvent(self, event):
        if event.buttons() & QtCore.Qt.LeftButton:
            self.current_action = "CurAction3d_DynamicRotation"

        elif event.buttons() & QtCore.Qt.RightButton:
            pass

        else:
            self.current_action = None

        self.next_event = event

        self.lastPos = event.pos()
        self.update()

    def paintEvent(self, event):
        """


        """
        if self._inited:
            # actions like panning, zooming and rotating the view invoke redrawing it
            # therefore, these actions need to be performed in the paintEvent method
            # this way, redrawing the view takes place synchronous with the overpaint action
            # not respecting this order would lead to a jittering view
            self._handle_gui_actions()

            if self.context().isValid():
                # acquire the OpenGL context
                self.makeCurrent()
                painter = QtGui.QPainter(self)
                painter.setRenderHint(QtGui.QPainter.Antialiasing)
                # swap the buffer before overpainting it
                self.swapBuffers()
                # perform overpainting
                self._overpaint(event, painter)
                painter.end()
                # hand over the OpenGL context
                self.doneCurrent()
            else:
                print('invalid OpenGL context: Qt cannot overpaint viewer')

    def _handle_gui_actions(self):
        # invokes redrawing the view
        try:
            if self.current_action is None:
                pass
                self._display.View.Redraw()

            elif self.current_action == "CurAction3d_DynamicRotation":
                self._display.StartRotation(self.dragStartPos.x, self.dragStartPos.y)
                if hasattr(self, "lastPos"):
                    pt = point(self.lastPos)
                    self._display.Rotation(pt.x, pt.y)
                    self.dragStartPos.x = pt.x
                    self.dragStartPos.y = pt.y
        finally:
            self.current_action = None

    def _overpaint(self, event, painter):
        # draw selection rectangle
        if self._drawbox:
            painter.setPen(QtGui.QPen(QtGui.QColor(0, 0, 0), 1))
            rect = QtCore.QRect(*self._drawbox)
            painter.drawRect(rect)

        # draw bubbles
        for bubble in self.bubbles:
            bubble_rect = bubble.rect()
            if bubble_rect.intersects(QtCore.QRectF(event.rect())):
                over_mouse = bubble_rect.contains(self.lastPos)
                bubble.drawBubble(painter, over_mouse)

        # draw instructions in half transparent rectangle on top of the viewport
        self.drawInstructions(painter)

    def showEvent(self, event):
        self.createBubbles(20 - len(self.bubbles))

    def sizeHint(self):
        return QtCore.QSize(800, 600)

    def createBubbles(self, number):
        for _ in range(number):
            position = QtCore.QPointF(self.width() * (0.1 + 0.8 * random.random()),
                                      self.height() * (0.1 + 0.8 * random.random()))
            radius = min(self.width(), self.height()) * (0.0125 + 0.0875 * random.random())
            velocity = QtCore.QPointF(self.width() * 0.0125 * (-0.5 + random.random()),
                                      self.height() * 0.0125 * (-0.5 + random.random()))

            self.bubbles.append(Bubble(position, radius, velocity))

    def animate(self):
        for bubble in self.bubbles:
            bubble.move(self.rect())
        self.update()

    def drawInstructions(self, painter):
        text = """
        Click and drag with the left mouse button to rotate the box
        Shift + Right Mouse Button for multiple selection area
        """
        transparency = 80
        metrics = QtGui.QFontMetrics(self.font())
        border = max(4, metrics.leading())

        rect = metrics.boundingRect(0, 0, self.width() - 2 * border,
                                    int(self.height() * 0.125),
                                    QtCore.Qt.AlignCenter | QtCore.Qt.TextWordWrap, text)

        painter.setRenderHint(QtGui.QPainter.TextAntialiasing)

        painter.fillRect(QtCore.QRect(0, 0, self.width(), rect.height() + 2 * border),
                         QtGui.QColor(0, 0, 0, transparency))

        painter.setPen(QtCore.Qt.white)

        painter.fillRect(QtCore.QRect(0, 0, self.width(), rect.height() + 2 * border),
                         QtGui.QColor(0, 0, 0, transparency))

        painter.drawText((self.width() - rect.width()) / 2, border, rect.width(),
                         rect.height(), QtCore.Qt.AlignCenter | QtCore.Qt.TextWordWrap,
                         text)


if __name__ == '__main__':
    def TestOverPainting():
        class AppFrame(QtGui.QWidget):
            def __init__(self, parent=None):
                QtGui.QWidget.__init__(self, parent)
                self.setWindowTitle(self.tr("qtDisplay3d overpainting example"))
                self.resize(1280, 1024)
                self.canva = GLWidget(self)
                mainLayout = QtGui.QHBoxLayout()
                mainLayout.addWidget(self.canva)
                mainLayout.setContentsMargins(0, 0, 0, 0)
                self.setLayout(mainLayout)

            def runTests(self):
                self.canva._display.Test()

        app = QtGui.QApplication(sys.argv)
        frame = AppFrame()
        frame.show()
        frame.canva.InitDriver()
        frame.runTests()
        app.exec_()


    TestOverPainting()
