import QtQuick 2.0
import Sailfish.Silica 1.0
import io.thp.pyotherside 1.4

Page {
    id: page

    // The effective value will be restricted by ApplicationWindow.allowedOrientations
    allowedOrientations: Orientation.All

    // To enable PullDownMenu, place our content in a SilicaFlickable
    SilicaFlickable {
        anchors.fill: parent

        // PullDownMenu and PushUpMenu must be declared in SilicaFlickable, SilicaListView or SilicaGridView
        PullDownMenu {
            MenuItem {
                text: qsTr("Show Page 2")
                onClicked: pageStack.animatorPush(Qt.resolvedUrl("SecondPage.qml"))
            }
        }

        // Tell SilicaFlickable the height of its content.
        contentHeight: column.height

        // Place our content in a Column.  The PageHeader is always placed at the top
        // of the page, followed by our content.
        Column {
            id: column

            width: page.width
            spacing: Theme.paddingLarge
            PageHeader {
                title: qsTr("Waydroid Companion")
            }
            Label {
                x: Theme.horizontalPageMargin
                text: qsTr("Settings are coming soon")
                color: Theme.secondaryHighlightColor
                font.pixelSize: Theme.fontSizeExtraLarge
                wrapMode: Text.Wrap
                width: parent.width - Theme.horizontalPageMargin*2
            }

            ButtonLayout {
                Button {
                    text: qsTr("Forward notifications")
                    onClicked: py.call('main.comm.send_notifications')
                }
            }

            SectionHeader { text: qsTr("Container") }

            IconTextSwitch {
                text: qsTr("Start container")
                icon.source: "image://theme/icon-m-" + (py.status.container.state ? "play" : "pause")
                description: py.status.container.state ? qsTr("Container is running") : qsTr("Container is stopped")
                checked: py.status.container.state || false
                automaticCheck: true
                onCheckedChanged: {
                    if (checked === py.status.container.state) return
                    busy = true
                    py.call('main.comm.toggle_container', [], function(res) {
                        console.log("Succsessfully (or not xD) toggled contanier:", res, "<output ends here>")
                        busy = false
                    })
                }
            }

            Label {
                text: py.status.display || ""
            }
        }
    }
}
