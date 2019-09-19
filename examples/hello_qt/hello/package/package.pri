currentYear=$$pyOut( from datetime import datetime; print( datetime.now().year ); )

# Global application info
# Shared across the C++, the binary branding, and the installer!
DEFINES += $$globalStrDef( APP_VERSION, 1.0.0.0 )
DEFINES += $$globalStrDef( COMPANY_NAME, Some Company )
DEFINES += $$globalStrDef( COMPANY_LEGAL_NAME, Some Company Inc. )
DEFINES += $$globalStrDef( COPYRIGHT_YEAR, $${currentYear} )
DEFINES += $$globalStrDef( PRODUCT_TITLE, Hello Qt World Example )
DEFINES += $$globalStrDef( PRODUCT_DESCRIPTION, A Distribution Builder Example )
DEFINES += $$globalStrDef( ICON_RESOURCE_PATH, :/icons/demo.png ) # must align with .qrc

SETUP_NAME=HelloQtSetup

win32: ICON_PATH=$${_PRO_FILE_PWD_}/icons/demo.ico
win64: ICON_PATH=$${_PRO_FILE_PWD_}/icons/demo.ico
macx:  ICON_PATH=$${_PRO_FILE_PWD_}/icons/demo.icns
linux: ICON_PATH=$${_PRO_FILE_PWD_}/icons/demo.png

# Binary branding
VERSION=$${APP_VERSION}
QMAKE_TARGET_COMPANY=$${COMPANY_NAME}
QMAKE_TARGET_COPYRIGHT=Copyright (c) $${COPYRIGHT_YEAR}. $${COMPANY_NAME}
QMAKE_TARGET_PRODUCT=$${PRODUCT_TITLE}
QMAKE_TARGET_DESCRIPTION=$${PRODUCT_DESCRIPTION}
RC_ICONS=$${ICON_PATH}

#------------------------------------------------------------------------------
# Build an installer (via the distbuilder Python library)
# when the "Package" build config is used

packageScriptPath=$${PWD}/package.py
OTHER_FILES += $${packageScriptPath}

CONFIG(package){  # if running the "package" build configuration...

    win32: binaryPath=$$OUT_PWD/release/$${TARGET}.exe
    else:  binaryPath=$$OUT_PWD/$${TARGET}

    qtBinDirPath = $$dirname(QMAKE_QMAKE)

    packageCmd=$${PY_PATH} \
        $$quot( $$clean_path( $${packageScriptPath} ) ) \
        $$quot( $$clean_path( $${binaryPath} ) ) \
        $$quot( $$clean_path( $${qtBinDirPath} ) ) \
        -t $$quot( $${PRODUCT_TITLE} ) \
        -d $$quot( $${PRODUCT_DESCRIPTION} ) \
        -v $$quot( $${APP_VERSION} ) \
        -c $$quot( $${COMPANY_NAME} ) \
        -l $$quot( $${COMPANY_LEGAL_NAME} ) \
        -s $$quot( $${SETUP_NAME} ) \
        -i $$quot( $$clean_path( $${ICON_PATH} ) )

    # detect and pass the compiler used
    win32-msvc*: packageCmd += -b msvc
    win32-g++:   packageCmd += -b mingw

    # These shell commands are executed upon rebuilding the project
    QMAKE_POST_LINK += $${packageCmd}
}
