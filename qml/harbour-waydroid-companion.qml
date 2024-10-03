import QtQuick 2.0
import Sailfish.Silica 1.0
import "pages"
import io.thp.pyotherside 1.4
import Nemo.Notifications 1.0

ApplicationWindow {
    initialPage: Component { FirstPage { } }
    cover: Qt.resolvedUrl("cover/CoverPage.qml")
    allowedOrientations: defaultAllowedOrientations

    Notification {
        id: notification


    }

    Python {
        id: py
        property bool rooted: false

        Component.onCompleted: {
            setHandler("rooted", function(r){rooted = r})
            setHandler("notification", function(appName, title, summary, text) {
                notification.appName = appName
                notification.summary = title
                notification.subText = summary
                notification.body = text
                notification.publish()
                notification.replacesId = 0
            })

            addImportPath(Qt.resolvedUrl("../python"))
            importModule('main', function() {})
        }

        onError: console.log("python error: " + traceback)
        onReceived: console.log("got message from python: " + data)
    }
}
