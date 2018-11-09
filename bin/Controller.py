#import in GPIO and time
import RPi.GPIO as GPIO
import RelayModule
import ButtonModule
import time
import os


def main():
    rc = RelayController()
    rc.run()
    

class RelayController:
    # sets up private variables
    __debug = 0
    __relayList = 0
    __buttonList = 0
    __buttonEventHandler = 0
    __boolReset = 0
    __warnings = 0
    __gpioDefault = 0
    __gpioAlt = 0
    __serverSock = 0
    __runnable = 0
        
    
    def __setup(self):
        ## debug tool
        if self.__debug: print("__setup")

        GPIO.setmode(GPIO.BCM)

        # sets the defaults of all the private variables
        boolRPins = False
        boolBPins = True
        self.__relayList = []
        self.__buttonList = []
        self.__buttonEventHandler = []
        self.__boolReset = False
        self.__warnings = False
        self.__debug = False
        self.__gpioDefault = GPIO.HIGH
        self.__gpioAlt = GPIO.LOW
        self.__relay = 0
        self.__runnable = True
        
        try:
            #  Gets the file path and creates the path to the config file
            path = os.path.realpath(__file__)
            path = path.split('\\')
            jointer = '\\'
            file = jointer.join(path[0:-1])+'\\config.ini'

            # tries to open the file on the found path
            fConfig = open(file, 'r')
            try:
                for strLine in fConfig.readlines():
                    strLine = strLine.lower()
                    if not(strLine[0] == '#'):

                        if 'relays' in strLine:
                            for i in [',','=','[',']', ':']:
                                strLine = strLine.replace(i, ' ')


                            strLine = strLine.split()

                            for i in strLine:
                                try:
                                    intPin = int(i)
                                    self.__relayList.append(intPin)
                                except:
                                    continue
                            boolRPins = True


                        elif 'buttons' in strLine:
                            for i in [',','=','[',']',':']:
                                strLine = strLine.replace(i, ' ')


                            strLine = strLine.split()

                            for i in strLine:
                                try:
                                    intPin = int(i)
                                    self.__buttonList.append(intPin)
                                except:
                                    continue
                            boolBPins = True

                            ## debug tool
                            if self.__debug: print(self.__pinList)

                        elif 'reset' in strLine:
                            if 'true' in strLine:
                                self.__boolReset = True

                            ## debug tool
                            if self.__debug: print(self.__boolReset)

                        elif 'default' in strLine:
                            if 'on' in strLine:
                                self.__gpioDefault = GPIO.LOW
                                self.__gpioAlt = GPIO.HIGH

                        elif 'debug' in strLine:
                            if 'on' in strLine:
                                self.__debug = True

                            ## debug tool
                            if self.__debug: print(self.__boolReset)

                        elif 'warning' in strLine:
                            if 'on' in strLine:
                                self.__warnings = True


                if not(boolRPins): raise ValueError("No valid pins listed")
                if not(boolBPins): raise Warning("No input pins selected")
                fConfig.close()
            except:
                print('Error in setup')
                return 1
        except:
            print('Error: Config file not found.')
            return 1

        return 0


    def run(self):
        if(self.__runnable):
            try:
                cont = True
                while cont:
                    c, addr = serverSock.accpet()
                    interface = c.getHostname()
                    cmd = c.recv(128)
                    if('quit' in cmd):
                        cont = False
                    else:

            except:
                print("unexcepted closure")
            count = 0 
            while(count < 5):
                for i in self.__buttons:
                    if(i.getStatus()):
                        time.sleep(5)
                        relayList = []
                        for i in range(i.getStatus):
                            relayList.append(i)
                        if(relayList):
                            self.__relay.relay(relayList)
        else:
            print("Not runnable please try reinitializing.")

        

    def __init__(self):
        if(not self.__setup()):
            for i in self.__buttonList:
                x = ButtonModule(i, self.__debug)
                self.__buttonEventHandler.append(x)
            self.__relay = RelayModule(self.__relayList, self.__boolReset, self.__gpioDefault, self.__debug)
        else:
            self.__runnable = False
