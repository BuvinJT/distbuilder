#------------------------------------------------------------------------------
# Global constants

# Hardcode the path to your Python interpreter here.
# Or, alternatively, use the (commented out) environmental varibale method
PY_PATH=python
#PY_PATH=$$getenv( PYTHON_PATH )

UNCONDITIONAL_CMD_SEP=;
CONDITIONAL_CMD_SEP=" && "

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

# Confirm Python is available as expected, if not terminate the build!
pyVerDetails=$$pyOut( import sys; print( sys.version ); )
isEmpty(pyVerDetails){ error( Python cannot be accessed! ) }
message( Python: $${pyVerDetails} )

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
    win32:space=\\\040
    else: space=\\\\\040
    defineValue=$$join($${valueList}, $${space}, \\\", \\\")
    # escape some other specific chars...
    defineValue=$$replace( defineValue, &, \& ) # escape ampersands
    # return this STATEMENT to be appended to DEFINES in the global scope
    return( $${varName}=$${defineValue} )
}
#------------------------------------------------------------------------------
