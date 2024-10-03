# NOTICE:
#
# Application name defined in TARGET has a corresponding QML filename.
# If name defined in TARGET is changed, the following needs to be done
# to match new name:
#   - corresponding QML filename must be changed
#   - desktop icon filename must be changed
#   - desktop filename must be changed
#   - icon definition filename in desktop file must be changed
#   - translation filenames have to be changed

# The name of your application
TARGET = harbour-waydroid-companion

CONFIG += sailfishapp

SOURCES += src/harbour-waydroid-companion.cpp

DISTFILES += qml/harbour-waydroid-companion.qml \
    qml/cover/CoverPage.qml \
    qml/pages/FirstPage.qml \
    qml/pages/SecondPage.qml \
    rpm/harbour-waydroid-companion.changes.in \
    rpm/harbour-waydroid-companion.changes.run.in \
    rpm/harbour-waydroid-companion.spec \
    translations/*.ts \
    harbour-waydroid-companion.desktop

SAILFISHAPP_ICONS = 86x86 108x108 128x128 172x172

# to disable building translations every time, comment out the
# following CONFIG line
CONFIG += sailfishapp_i18n

# German translation is enabled as an example. If you aren't
# planning to localize your app, remember to comment out the
# following TRANSLATIONS line. And also do not forget to
# modify the localized app name in the the .desktop file.
TRANSLATIONS += translations/harbour-waydroid-companion-de.ts

python.files = python
python.path = /usr/share/$${TARGET}

appinstall.files = waydroid.app.install.desktop
appinstall.path = /usr/share/applications

INSTALLS += python appinstall

# This is probably a security issue but i dont really know any alternatives
QMAKE_INSTALL_PROGRAM = install -m 4755 -p