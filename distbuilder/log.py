import sys, os
import datetime
import atexit

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
        self.name         = name if None else rootFileName( sys.argv[0] )
        self.isUniqueFile = isUniqueFile
        self._isPrimary   = False
        self.__path       = None
        self.__file       = None        
        self.__stderr     = None
        self.__stdout     = None        
        atexit.register( self.close )

    def isOpen( self ): return self.__file is not None

    def open( self ): self._getFile()

    def close( self ):
        if self.__file:
            self._flush()
            self.__file.close()
            self.__file = None     
            if self._isPrimary: self.__restoreStd()
            self.toStdout( "Log closed: %s" % (self.__path,) )
            self.__path = None
            
    def write( self, msg ):
        self._getFile().write( self.__formatLn( msg ) )
        self._flush()

    def toStdout( self, msg ):
        stream = self.__stdout if self.__stdout else sys.stdout
        stream.write( self.__formatLn( msg ) )
        stream.flush()

    def toStderr( self, msg ):
        stream = self.__stderr if self.__stderr else sys.stderr
        stream.write( self.__formatLn( msg ) )
        stream.flush()
                                        
    def _flush( self ):
        if self._isPrimary:         
            sys.stderr.flush()
            sys.stdout.flush()                
        if self.__file:
            self.__file.flush()
            os.fsync( self.__file.fileno() )

    def _getFile( self ):
        if not self.__file:
            from distbuilder.util import joinExt, absPath
            rootLogName =( Logger.__UNIQUE_FILENAME_TMPLT % ( 
                self.name, datetime.datetime.now().__format__( 
                    Logger.__DTSTAMP_FORMAT ) ) 
                if self.isUniqueFile else self.name )                                 
            self.__path = absPath( joinExt( rootLogName, Logger.__EXTENSION ) )                 
            self.__file = open( self.__path, "w" )        
            if self._isPrimary: self.__redirectStd()            
            self.toStdout( "Logging to: %s" % (self.__path,) )    
        return self.__file
    
    def __redirectStd(self):
        self._flush()        
        self.__stderr = sys.stderr  
        self.__stdout = sys.stdout  
        sys.stderr = self.__file
        sys.stdout = self.__file

    def __restoreStd(self):
        sys.stderr = self.__stderr
        sys.stdout = self.__stdout
        self.__stderr = None
        self.__stdout = None
        
    def __formatLn( self, msg ): return str(msg) + "\n"    
        
def startLog( name=None, isUniqueFile=False ): 
    Logger.singleton( name, isUniqueFile ).open()

def stopLog(): Logger.singleton().close()
        
def isLogging(): return Logger.isSingletonOpen()
        
def log( msg ): 
    if Logger.isSingletonOpen(): Logger.singleton().write( msg )
        