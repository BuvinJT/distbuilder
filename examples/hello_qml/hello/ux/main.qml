import QtQuick 2.4
import QtCanvas3D 1.1
import QtQuick.Window 2.2
import QtMultimedia 5.8

import "glcode.js" as GLCode

Window {
    width: 400
    height: 300
    visible: true

    Canvas3D {
        id: canvas3d
        anchors.fill: parent
        focus: true

        onInitializeGL: {
            GLCode.initializeGL(canvas3d);
        }

        onPaintGL: {
            GLCode.paintGL(canvas3d);
        }

        onResizeGL: {
            GLCode.resizeGL(canvas3d);
        }

        Column {
            y: 20
            width: parent.width
            Text {
                objectName: "product_title"
                width: parent.width                
                font.family: "Arial Black"
                font.pointSize: 20
                horizontalAlignment: Text.AlignHCenter
                color: "white"
            }
            Text {
                objectName: "app_version"
                width: parent.width
                font.family: "Arial Black"
                font.pointSize: 14
                horizontalAlignment: Text.AlignHCenter
                color: "white"
            }
        }
    }

    Timer {
        id: rotateTimer
        interval: 10; running: true; repeat: true
        onTriggered: GLCode.rotateGL(canvas3d);
    }

    SoundEffect {
        id: drumroll
        source: "drumroll.wav"
    }

    Component.onCompleted: drumroll.play()
}
