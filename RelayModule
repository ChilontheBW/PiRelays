###
#   Author:     Chris Otey for KUOW
#   Descrption: Module for activating relays as defined by usr/bin/python/RelayModule/Config.ini
#   Path:       !/usr/bin/python
###



class RelayModule:
    import RPi.GPIO as GPIO
    import time
    __pinList = []
    __boolRest = False

    def __getInt(strList):
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


    def Relay(intNum):
        self.__FireRelay(self, GPIO, intNum, self.__boolReset)
        
    def __FireRelay(self, gpio, intRelay, boolReset):
        try :
            function_call = inspect.stack()[1][4][0].strip()

            # See if the function_call has "self." in the begining
            matched = re.match( '^self\.', function_call )
            if not matched :
                raise Exception('Access Error')
                return 1
            else:
                
                if(boolReset):
                    for i in pinList:
                        gpio.output(__pinList[i], gpio.HIGH)
                try:
                    for i in len(intRelay):
                        pins[i] = __pinList[intRelay[i]]
                    gpio.output(pins, gpio.LOW)
                except:
                    print()

        except :
            raise Exception('Access Error')
            return 1
        
        return 0

    def relayTest():
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
                    intInp = __getInt(strInt)
                    __fireRelay(self, GPIO, intInp, boolCont)
                except:
                    print()

        return 0
                    
            
    def __setup(self):
        GPIO.setmode(GPIO.BCM)
        try:
            fConfig = open('config.ini', 'r')
            for i in fConfig:
                print(i)
            #self.__pinList[i] = []
            print(fConfig.readline())
            for i in pinList:
                GPIO.setup(i, GPIO.OUT)
                GPIO.output(i, GPIO.HIGH)
        except:
            print('Error in setup')
            return 1

        return 0
            
    def __init__(self):
        __setup(self)

    def __init__(self, boolReset):
        self.__boolReset = boolReset
        __setup(self)

    def __del__(self):
        GPIO.cleanup()
