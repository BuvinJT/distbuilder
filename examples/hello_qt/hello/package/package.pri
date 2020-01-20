#==============================================================================
# PACKAGE.PRI
#==============================================================================

# Global constants

# Get the python interpreter path from an environmental variable, if possible.
# Note, that may be assigned in a .pro.user. If that is not defined, fallback to
# a hardcoded value which assumes you want to use "python" from the system path.
PY_PATH=$$getenv( PYTHON_PATH )
isEmpty(PY_PATH){ PY_PATH=python }

#------------------------------------------------------------------------------
# Function: pyOut
#
# Pass python commands, and receive the results put on the stdout stream.
#
# Note: whatever you "print" will be returned.
# Note: to execute multiple lines, just delimit them with semi-colons.
#
defineReplace( pyOut ){
    return( $$system( $${PY_PATH} -c \"$${1}\" ) )
}
#------------------------------------------------------------------------------
# Function: quot
#
# This replaces the built-in QMake `quote` function,
# because that doesn't seem to work!
#
defineReplace( quot ){ return( \"$$1\" ) }
#------------------------------------------------------------------------------
# Function: globalStrDef
#
# This creates a global qmake string variable, and returns a value to be
# appended to the C++ DEFINES **which may contain spaces**.
#
# Note: In QMake, it is excessively tricky to create defines with spaces in
# them because the language treats white space as an implicit delimiter, and
# the string manipulation functions (e.g. replace) will not modify spaces!
#
# arguments: variable/define name, value as space delimited list (do not quote!)
#
# Example use:
#
# DEFINES += $$globalStrDef( MY_DEFINE, Hello there world! )
#
defineReplace( globalStrDef ){
    varName   = $$1
    valueList = $$list( $$2 )
    # create a string variable by joining the list items with spaces
    # and then export the variable to the global space
    # (join is one of the only qmake functions that respects white space args)
    eval( $${varName}=$$join($${valueList}, " ") )
    eval( export( $${varName} ) )
    # create another string variable by joining the list items with
    # \040 (the octal code for space), having escaped it multiple times
    # (for the various layers it must pass through), and wrap it in quotes,
    # to create a C++ string literal
    win32 {
        win32-msvc*: space=\\040
        else:        space=\\\040
    }
    else: space=\\\\\040
    defineValue=$$join($${valueList}, $${space}, \\\", \\\")
    # escape some other specific chars...
    defineValue=$$replace( defineValue, &, \& ) # escape ampersands
    # return this STATEMENT to be appended to DEFINES in the global scope
    return( $${varName}=$${defineValue} )
}

# PREPARE FOR DEPLOYMENT
#==============================================================================

# Assert Python is available
pyVerDetails=$$pyOut( "import sys; print( sys.version );" )
isEmpty(pyVerDetails){ error( Python cannot be accessed! ) }
message( Python: $${pyVerDetails} )

# Get the current year (for the copyright)
currentYear=$$pyOut( from datetime import datetime; print( datetime.now().year ); )

# Global application info shared across the C++ layer,
# the binary branding, and the Python installation builder!
DEFINES += $$globalStrDef( APP_VERSION, 1.0.0.0 )
DEFINES += $$globalStrDef( COMPANY_TRADE_NAME, Some Company )
DEFINES += $$globalStrDef( COMPANY_LEGAL_NAME, Some Company Inc. )
DEFINES += $$globalStrDef( COPYRIGHT_YEAR, $${currentYear} )
DEFINES += $$globalStrDef( PRODUCT_TITLE, Hello World Qt Example )
DEFINES += $$globalStrDef( PRODUCT_DESCRIPTION, A Distribution Builder Example )

SETUP_NAME=HelloQtSetup

win32: ICON_PATH=$${_PRO_FILE_PWD_}/icons/demo.ico
macx:  ICON_PATH=$${_PRO_FILE_PWD_}/icons/demo.icns
linux: ICON_PATH=$${_PRO_FILE_PWD_}/icons/demo.png

# Binary branding
VERSION=$${APP_VERSION}
QMAKE_TARGET_COMPANY=$${COMPANY_NAME}
QMAKE_TARGET_COPYRIGHT=Copyright (c) $${COPYRIGHT_YEAR}. $${COMPANY_LEGAL_NAME}
QMAKE_TARGET_PRODUCT=$${PRODUCT_TITLE}
QMAKE_TARGET_DESCRIPTION=$${PRODUCT_DESCRIPTION}
win32: RC_ICONS=$${ICON_PATH}
macx:      ICON=$${ICON_PATH}

#------------------------------------------------------------------------------
# Build an installer when the project is rebuilt via the "Package" build config

packageScriptPath=$${PWD}/package.py
OTHER_FILES += $${packageScriptPath}

CONFIG(package){  # detect the "package" build configuration

    # Assert Distribtion Builder is available
    distBuilderVersion=$$pyOut( "exec('try: import distbuilder; print(distbuilder.__version__);\nexcept: pass')" )
    isEmpty(distBuilderVersion){ error( Distribution Builder cannot be accessed! ) }
    message( Distribution Builder: $${distBuilderVersion} )

    # Build a shell command to run to the package script

    win32: exePath=$$OUT_PWD/release/$${TARGET}.exe
    macx:  exePath=$$OUT_PWD/$${TARGET}.app
    linux: exePath=$$OUT_PWD/$${TARGET}

    qtBinDirPath=$$dirname(QMAKE_QMAKE)
    projectRootPath=$${_PRO_FILE_PWD_}

    packageCmd=$${PY_PATH} \
        $$quot( $$clean_path( $${packageScriptPath} ) ) \
        $$quot( $$clean_path( $${exePath} ) ) \
        $$quot( $$clean_path( $${qtBinDirPath} ) ) \
        -s $$quot( $$clean_path( $${projectRootPath} ) ) \
        -i $$quot( $$clean_path( $${ICON_PATH} ) ) \
        -n $$quot( $${SETUP_NAME} ) \
        -t $$quot( $${PRODUCT_TITLE} ) \
        -d $$quot( $${PRODUCT_DESCRIPTION} ) \
        -v $$quot( $${APP_VERSION} ) \
        -c $$quot( $${COMPANY_TRADE_NAME} ) \
        -l $$quot( $${COMPANY_LEGAL_NAME} )
        
    # Detect and pass pertinent compiler details
    win32-msvc*: packageCmd += -b msvc
    win32-g++:   packageCmd += -b mingw

    # On Linux, you may optionally provide a custom "AskPass" program to handle
    # password input for root/sudo privileges if required
    #linux: packageCmd += --askPass $$quot( $$clean_path( /usr/share/git-cola/bin/ssh-askpass ) )

    # Append the command to those to be executed after exe linking
    QMAKE_POST_LINK += $${packageCmd}
}
