###
#   Author:     Chris Otey for KUOW
#   Descrption: Module for activating relays as defined by usr/bin/python/RelayModule/Config.ini
#   Path:       !/usr/bin/python
###


#import in GPIO and time
import RPi.GPIO as GPIO
import time

#Defining class for relaymodule
class RelayModule:

    # sets up private variables with defaults
    __pinList = []
    __boolReset = False
    __debug = False
    __gpioDefault = GPIO.HIGH
    __gpioAlt = GPIO.LOW

    # Method to get an int from a string input, can be one to one or many to many
    def __getInt(self, strList):
        ## debug tool
        if self.__debug: print("__getInt")

        strList = strList.split("")
        intList = []
        try:
            for i in strList:
                ## debug tool
                if self.__debug: print(i)
                
                try:
                    intI = int(strList[i])
                    intList.append(intI)
                except:
                    continue
        except TypeError:
            try:
                intList = int(strList)
            except:
                raise ValueError("not a number")

        ## debug tool
        if self.__debug: print("Return __getInt:", intList)

        return intList

            
    # private method for fireing relays on or off
    def __FireRelay(self, intRelay, boolReset):
        ## debug tool
        if self.__debug: print("__FireRelay")
                
        # checks if there if reset is every call is on
        if(boolReset):
            ## debug tool
            if self.__debug: print("Resetting Relays")

            # goes through the pinlist and resets them to default state
            for i in self.__pinList:
                GPIO.output(i, self.__gpioDefault)
                
        # tries to fire the relays that have been sent along
        try:
            ## debug tool
            if self.__debug: print(intRelay)
        
            # switches the state of the pin in the intRelay array
            for i in intRelay:
                if self.__debug: print(i)
                ## debug tool                
                if self.__debug: print("Firing Relay:", self.__pintList[i-1])

                ## Check if relay is on or not and swaps state
                if GPIO.input(self.__pinList[i-1]):
                    GPIO.output(self.__pinList[i-1], GPIO.LOW)

                    ## debug tool
                    if self.__debug: print(self.__pintList[i-1], "on")

                else:
                    GPIO.output(self.__pinList[i-1], GPIO.HIGH)

                    ## debug tool
                    if self.__debug: print(self.__pintList[i-1], "off")
                    
        except:
            raise Exception('some error')


    def relayTest(self):
        print("You can enter 'Q' at any time to quit")
        boolReset = input('Reset relays (Y/n): ')
        boolCont = True
        if(boolReset == 'q' or boolReset == 'Q'):
            boolCont = Falsee
        while(boolCont):
            strInp = input('Enter a number from 1-4: ')

            if(strInp == 'q' or strInp == 'Q'):
                boolCont = False
            else:
                try:
                    intInp = self.__getInt(strInt)
                    self.__fireRelay(intInp, boolCont)
                except:
                    print()

        return 0
                    
            
    def __setup(self):
        ## debug tool
        if self.__debug: print("__setup")

        GPIO.setmode(GPIO.BCM)
        boolPins = False
        self.__pinList = []
        self.__boolReset = False
        self.__gpioDefault = GPIO.HIGH
        self.__gpioAlt = GPIO.LOW
        
        try:
            fConfig = open('config.ini', 'r')
            for strLine in fConfig.readlines():
                strLine = strLine.lower()
                
                if 'pinlist' in strLine:
                    for i in [',','=','[',']']:
                        strLine = strLine.replace(i, ' ')
                        

                    strLine = strLine.split()

                    for i in strLine:
                        try:
                            intPin = int(i)
                            self.__pinList.append(intPin)
                        except:
                            continue
                    boolPins = True
                    ## debug tool
                    if self.__debug: print(self.__pinList)
                    
                elif 'reset' in strLine:
                    if 'true' in strLine:
                        __boolReset = True
                
                    ## debug tool
                    if self.__debug: print(self.__boolReset)
            
                elif 'default' in strLine:
                    strLine = strLine.split('default=')
                    if 'on' in strLine:
                        __gpioDefault = GPIO.LOW
                        __gpioAlt = GPIO.HIGH    
                
            if(not self.__pinList): raise ValueError("No valid pins listed")
            fConfig.close()
            GPIO.setup(self.__pinList, GPIO.OUT)
            GPIO.output(self.__pinList, self.__gpioDefault)
 
        except:
            print('Error in setup')
            return 1

        return 0


    # method for outside to fire a relay, doesnt mattter if it on or off
    def relay(self, intNum):
        intList = []
        if(len(intNum) > 2):
            intList.append(intNum)
        else:
            intList = intNum
        
        self.__FireRelay(intList, self.__boolReset)

    # method for reseting all the relays to default state
    def clearAll(self):
        GPIO.output(self.__pinList, self.__gpioDefault)

    # default constructor   
    def __init__(self, boolReset = False, debug = False):
        try:
            self.__debug == debug
            self.__boolReset = boolReset
            self.__setup()
        except Exception as e:
            print("Error in startup:", str(e))
            
    # deconstructor
    def __del__(self):
        print("del")
        GPIO.output(self.__pinList, GPIO.HIGH)
        GPIO.cleanup()

    def debug(self):
        self.__debug = not self.__debug
        print("debug set:", self.__debug)
