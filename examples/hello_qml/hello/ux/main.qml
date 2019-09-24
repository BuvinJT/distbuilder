import QtQuick 2.4
import QtCanvas3D 1.1
import QtQuick.Window 2.2

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
                color: "white"
                font.pointSize: 24
                horizontalAlignment: Text.AlignHCenter
            }
            Text {
                objectName: "app_version"
                width: parent.width
                color: "white"
                font.pointSize: 18
                horizontalAlignment: Text.AlignHCenter
            }
        }
    }
}
