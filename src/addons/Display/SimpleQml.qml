
/****************************************************************************
**
** Copyright (C) 2013 Digia Plc and/or its subsidiary(-ies).
** Contact: http://www.qt-project.org/legal
**
** This file is part of the examples of the Qt Toolkit.
**
** $QT_BEGIN_LICENSE:BSD$
** You may use this file under the terms of the BSD license as follows:
**
** "Redistribution and use in source and binary forms, with or without
** modification, are permitted provided that the following conditions are
** met:
**   * Redistributions of source code must retain the above copyright
**     notice, this list of conditions and the following disclaimer.
**   * Redistributions in binary form must reproduce the above copyright
**     notice, this list of conditions and the following disclaimer in
**     the documentation and/or other materials provided with the
**     distribution.
**   * Neither the name of Digia Plc and its Subsidiary(-ies) nor the names
**     of its contributors may be used to endorse or promote products derived
**     from this software without specific prior written permission.
**
**
** THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
** "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
** LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
** A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
** OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
** SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
** LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
** DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
** THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
** (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
** OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
**
** $QT_END_LICENSE$
**
****************************************************************************/
import QtQuick 2.5
import OCC 1.0

import QtQuick.Window 2.0
// Screen
import QtQuick.Dialogs 1.2

// FileDialog
import QtQuick.Controls 1.2

//import QtQuick.Controls.Styles 1.2

//Window{

//    minimumHeight: 800
//    minimumWidth: 800
Item {
    id: omg
    width: 600
    height: 900

    OCCView {
        id: occView
        anchors.centerIn: parent
        width: parent.width
        height: parent.height

        MouseArea {
            id: occMouseArea
//            width: parent.width
//            height: parent.height
            anchors.fill: parent
            hoverEnabled: true
            acceptedButtons: Qt.LeftButton | Qt.RightButton | Qt.MidButton

            onClicked: {
                occView.mousePressEvent(pressedButtons, mouseX, mouseY)
            }

            onPositionChanged: {
                if (occMouseArea.pressed === true) {
                    occView.mouseMoveEvent(pressedButtons, mouseX, mouseY)
                }
            }

            onReleased: {
                occView.mouseReleaseEvent(pressedButtons, mouseX, mouseY)
            }

            onEntered: {
                console.log("entering red zone")
            }

            onExited: {
                console.log("leaving red zone")
            }

            Component.onCompleted: {
                console.log("completed OCCView")
                occView.InitDriver()
            }
        }
    }

    // open button
    Rectangle {
        id: open_button

        // align
        anchors.top: parent.top
        anchors.left: parent.left

        opacity: 0.5

        // size
        width: 200
        height: 200

        color: "white"

        // image
        Image {
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter

            //source: "qrc:///icons/res/icons/ic_action_collection.png"
            source: "/Users/jelleferinga/GIT/oce/samples/qt/AndroidQt/res/icons/ic_action_collection.png"
        }

        MouseArea {
            anchors.fill: parent
            onClicked: file_dialog.open()
        }
    }

    FileDialog {
        id: file_dialog
        title: "Please choose a file"
        selectMultiple: false
        nameFilters: ["BRep files (*.brep)", "All files (*)"]
        //onAccepted: viewer.ReadShapeFromFile(file_dialog.fileUrl)
    }
}

