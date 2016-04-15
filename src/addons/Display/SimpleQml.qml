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
            anchors.fill: parent
            hoverEnabled: true
            acceptedButtons: Qt.LeftButton | Qt.RightButton | Qt.MidButton

            //preventStealing: true
            onPressed: {
                occView.mousePressEvent(pressedButtons, mouseX, mouseY)
            }

            onPositionChanged: {
                //if (occMouseArea.pressed === true) {
                occView.mouseMoveEvent(pressedButtons, mouseX, mouseY)
                //}
            }

            onReleased: {
                occView.mouseReleaseEvent(mouseX, mouseY)
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

        // open button
        Rectangle {
            id: debugInfo

            // align
            anchors.top: parent.top
            anchors.right: parent.right

            opacity: 0.5
            color: "cyan"

            // size
            width: 200
            height: 200

            Column{
                Text {
                    id: xxx
                    text: "delta mouse pos: " + occView.delta_mouse_event_pos[0] + " " + occView.delta_mouse_event_pos[1]
                }
                Text{
                    id: ppp
                    text: occView.point_on_mouse_press[0]
                }
           }
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
