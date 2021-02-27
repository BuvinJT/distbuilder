import sys, os
import datetime
import atexit
import traceback

class Logger:

    __EXTENSION                = "log"
    __UNIQUE_FILENAME_TMPLT    = "%s-%s"
    __DTSTAMP_FORMAT           = "%y%m%d%H%M%S%f"
    
    __instance = None
    @staticmethod    
    def singleton( name=None, isUniqueFile=False ):
        if not Logger.__instance: 
            Logger.__instance = Logger( name, isUniqueFile )
            Logger.__instance._isPrimary = True
        return Logger.__instance        

    @staticmethod    
    def isSingletonOpen():
        return Logger.__instance is not None and Logger.__instance.isOpen()
    
    def __init__( self, name=None, isUniqueFile=False ) :
        from distbuilder.util import rootFileName
        self.name          = name if None else rootFileName( sys.argv[0] )
        self.isUniqueFile  = isUniqueFile
        self._isPrimary    = False
        self.__path        = None
        self.__file        = None        
        self.__stderr      = None
        self.__stdout      = None
        self.__isException = False
        atexit.register( self.__onExit )

    def open( self ): self._getFile()

    def close( self ):
        if self.isOpen():
            self.pause()
            self.toStdoutLn( "Log closed: %s" % (self.__path,) )
            self.__path = None

    def pause( self ):
        if self.isOpen():
            self._flush()
            self.__file.close()
            self.__file = None     
            if self._isPrimary: 
                self.__restoreStd()
                self.__stopCatchall()

    def resume( self ):
        if self.isPaused(): self._getFile( isAppend=True )
                        
    def write( self, msg ):
        self._getFile().write( str(msg) )
        self._flush()

    def toStdout( self, msg ):
        stream = self.__stdout if self.__stdout else sys.stdout
        stream.write( str(msg) )
        stream.flush()

    def toStderr( self, msg ):
        stream = self.__stderr if self.__stderr else sys.stderr
        stream.write( str(msg) )
        stream.flush()

    def writeLn(    self, msg ): self.write(    self.__formatLn( msg ) )
    def toStdoutLn( self, msg ): self.toStdout( self.__formatLn( msg ) )
    def toStderrLn( self, msg ): self.toStderr( self.__formatLn( msg ) )   
    def __formatLn( self, msg ): return str(msg) + "\n"

    def isOpen( self ): return self.__file is not None

    def isPaused( self ): 
        return self.__file is None and self.__path is not None 

    def filePath( self ): return self.__path

    def _getFile( self, isAppend=False ):
        if not self.__file:
            if not self.__path and not isAppend:
                from distbuilder.util import joinExt, absPath
                rootLogName =( Logger.__UNIQUE_FILENAME_TMPLT % ( 
                    self.name, datetime.datetime.now().__format__( 
                        Logger.__DTSTAMP_FORMAT ) ) 
                    if self.isUniqueFile else self.name )                                 
                self.__path = absPath( joinExt( 
                    rootLogName, Logger.__EXTENSION ) )         
            self.__file = open( self.__path, "a+" if isAppend else "w" )        
            if self._isPrimary: 
                self.__redirectStd()
                self.__startCatchall()
            if not isAppend: self.toStdoutLn( "Logging to: %s" % (self.__path,) )    
        return self.__file
                                        
    def _flush( self ):
        if self._isPrimary:         
            sys.stderr.flush()
            sys.stdout.flush()                
        if self.__file:
            self.__file.flush()
            os.fsync( self.__file.fileno() )
    
    def __redirectStd( self ):
        self._flush()        
        self.__stderr = sys.stderr  
        self.__stdout = sys.stdout  
        sys.stderr = self.__file
        sys.stdout = self.__file

    def __restoreStd( self ):
        sys.stderr = self.__stderr
        sys.stdout = self.__stdout
        self.__stderr = None
        self.__stdout = None
    
    def __startCatchall( self ): sys.excepthook = self.__onUncaughtException
    
    def __stopCatchall( self ): sys.excepthook = None

    def __onUncaughtException( self, *exc_info ):
        self.__isException = True
        if self._isPrimary:        
            self.toStderr( "".join( traceback.format_exception( *exc_info ) ) )
        sys.__excepthook__( *exc_info )

    def __onExit( self ):
        if self.isOpen():
            self.close()
            if self._isPrimary and not self.__isException: 
                self.toStdout( "Done!" )
            
def startLogging( name=None, isUniqueFile=False ): 
    Logger.singleton( name, isUniqueFile ).open()

def stopLogging(): Logger.singleton().close()
        
def isLogging(): return Logger.isSingletonOpen()
        
def log( msg ): 
    if Logger.isSingletonOpen(): Logger.singleton().writeLn( msg )
        