# Comment on/off to switch modes
#IS_ANALYZING=True
IS_ANALYZING=False

from distbuilder import OpyConfig
opyConfig = OpyConfig( "HelloOpy", entryPointPy="hello.py" ) 

if IS_ANALYZING :
    from distbuilder import opyAnalyze
    opyResult = opyAnalyze( opyConfig )
else :
    from distbuilder import obfuscatePy, runPy
    obDir, obPath = obfuscatePy( opyConfig )
    runPy( obPath )