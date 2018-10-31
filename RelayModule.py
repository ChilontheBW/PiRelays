###
#   Author:     Chris Otey for KUOW
#   Descrption: Module for activating relays as defined by usr/bin/python/RelayModule/Config.ini
#   Path:       !/usr/bin/python
###


#Defining class for relaymodule
class RelayModule:
    #import in GPIO and time
    import RPi.GPIO as GPIO
    import time

    # sets up private variables with defaults
    __pinList = []
    __boolReset = False
    __gpioDefault = GPIO.HIGH
    __gpioAlt = GPIO.LOW

    # Method to get an int from a string input, can be one to one or many to many
    def __getInt(self, strList):
        try :
            function_call = inspect.stack()[1][4][0].strip()

            # See if the function_call has "self." in the begining
            matched = re.match( '^self\.', function_call )
            if not matched :
                raise Exception('Access Error')
            else:
                strList = strList.split("")
                intList = []

                for i in strList:
                    try:
                        intI = int(strList[i])
                        intList.append(intI)
                    except:
                    ##Nothing
                        return intList
        except :
            raise Exception('Access Error')


    # private method for fireing relays on or off
    def __FireRelay(self, gpio, intRelay, boolReset):
        # checks to see if this is being called by itself
        try :
            function_call = inspect.stack()[1][4][0].strip()

            # See if the function_call has "self." in the begining
            matched = re.match( '^self\.', function_call )

            # if not it throws an access error
            if not matched :
                raise Exception('Access Error')
                return 1
            else:
                # checks if there if reset is every call is on
                if(boolReset):
                    # goes through the pinlist and resets them to default state
                    for i in __pinList:
                        gpio.output(i, gpioDefault)
                        
                # tries to fire the relays that have been sent along
                try:
                    # switches the state of the pin in the intRelay array
                    for i in intRelay:
                        if gpio.input(__pinList[i-1])):
                            gpio.output(__pinList[i-1], gpio.LOW)
                        else:
                            gpio.output(__pinList[i-1], gpio.HIGH)
                            
                except:
                    raise Exception('some error')

        # if not it throws an access error
        except :
            raise Exception('Access Error')
            return 1
        
        return 0

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
                    self.__fireRelay(self, GPIO, intInp, boolCont)
                except:
                    print()

        return 0
                    
            
    def __setup(self):
        GPIO.setmode(GPIO.BCM)
        boolPins = False
        
        try:
            fConfig = open('config.ini', 'r')
            for strLine in fConfig.readlines():
                strLine = strLine.lower()
                strLine = strLine.split(' ')
                if 'pinlist' in strLine:
                    strLine = strLine.split('pinlist=')
                    for i in strLine:
                        try:
                            intPin = int(i)
                            __pinList.append(intPin)
                        except:
                            continue

                    boolPins = True
                    
                elif 'reset' in strLine:
                    strLine = strLine.split('reset=')
                    if 'true' in strLine:
                        __boolReset = True
                    boolReset = True
                
            
                elif 'default' in strLine:
                    strLine = strLine.split('default=')
                    if 'on' in strLine:
                        __gpioDefault = GPIO.LOW
                        __gpioAlt = GPIO.HIGH    
                
                
            
            GPIO.setup(__pinList, GPIO.OUT)
            GPIO.output(__pinList, gpioDefault)
 
        except:
            print('Error in setup')
            return 1

        return 0


    # method for outside to fire a relay, doesnt mattter if it on or off
    def relay(self, intNum):
        self.__FireRelay(self, GPIO, intNum, self.__boolReset)

    # method for reseting all the relays to default state
    def clearAll(self):
        for i in self.__pinList:
            gpio.output(i, self.__gpioDefault)
    # default constructor   
    def __init__(self):
        __setup(self)
        
    # alt constructor
    def __init__(self, boolReset):
        self.__boolReset = boolReset
        __setup(self)

    # deconstructor
    def __del__(self):
        GPIO.cleanup()

        
    
