#! /usr/bin/python
#
#import in GPIO and time
import RPi.GPIO as GPIO
import RelayModule
import ButtonModule
import time
import tkinter as tk

def main():
    rc = RelayController()
    rc.run()
    

class RelayController:
    # sets up private variables
    __root__ = 0
    __relayList__ = 0
    __buttonList__ = 0
    __Debug__ = 0
    __buttonEventHandler__ = 0
    __boolReset__ = 0
    __warnings__ = 0
    __gpioDefault__ = 0
    __gpioAlt__ = 0
    __serverPort__ = 0
    __serverType__ = 0
        
    
    def __setup__(self):
        ## debug tool
        if self.__Debug__: print("__setup__")

        GPIO.setmode(GPIO.BCM)

        # sets the defaults of all the private variables
        boolRPins = False
        boolBPins = True
        self.__root__ = tk.Tk()
        self.__relayList__ = []
        self.__buttonList__ = []
        self.__buttonEventHandler__ = []
        self.__boolReset__ = False
        self.__warnings__ = False
        self.__Debug__ = False
        self.__gpioDefault__ = GPIO.HIGH
        self.__gpioAlt__ = GPIO.LOW
        self.__relay__ = 0
        
        try:
            fConfig = open('config.ini', 'r')
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
                                self.__relayList__.append(intPin)
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
                                self.__buttonList__.append(intPin)
                            except:
                                continue
                        boolBPins = True
                        
                        ## debug tool
                        if self.__Debug__: print(self.__pinList__)
                        
                    elif 'reset' in strLine:
                        if 'true' in strLine:
                            self.__boolReset__ = True
                    
                        ## debug tool
                        if self.__Debug__: print(self.__boolReset__)
                
                    elif 'default' in strLine:
                        if 'on' in strLine:
                            self.__gpioDefault__ = GPIO.LOW
                            self.__gpioAlt__ = GPIO.HIGH

                    elif 'debug' in strLine:
                        if 'on' in strLine:
                            self.__Debug__ = True
                    
                        ## debug tool
                        if self.__Debug__: print(self.__boolReset__)

                    elif 'warning' in strLine:
                        if 'on' in strLine:
                            self.__warnings__ = True
                            
                    
            if not(boolRPins): raise ValueError("No valid pins listed")
            if not(boolBPins): raise Warning("No input pins selected")
            fConfig.close()

        except:
            print('Error in setup')
            return 1

        return 0
    
    def __close__(self):
               
        window = tk.Toplevel()
        window.wm_title("WARNING")
        
        message = "WARNING: Closing this window will exit the program. \n Only close this program if it neededs to be \n restarted."
        width = len(message)/2
        label0 = tk.Label(window, text='{m: <{w}}'.format(m=' ', w =width), font=("Liberation Mono", 12))
        label0.grid(row=0, column=0)
        label1 = tk.Label(window, text=message, font=("Liberation Mono", 12))
        label1.grid(row=1, column=0)
        label2 = tk.Label(window, text='{m: <{w}}'.format(m='', w= width), font=("Liberation Mono", 12))
        label2.grid(row=3, column=0)
        frame = tk.Frame(window)
        frame.grid(row = 2, column = 0)
        button = tk.Button(frame, text="Close", command=self.__exit__, font=("Liberation Mono", 10))
        button.grid(row=0, column=0)
        label0 = tk.Label(frame, text='  ', font=("Liberation Mono", 12))
        label0.grid(row=0, column=1)
        button = tk.Button(frame, text="Cancel", command=window.destroy, font=("Liberation Mono", 10))
        button.grid(row=0, column=2)

        winw = width*10
        winh = 8*14
        rootx = self.__root__.winfo_x()
        rooty = self.__root__.winfo_y()
        dx = (self.__root__.winfo_width()-winw)/2
        dy = (self.__root__.winfo_height()-winh)/2

        window.geometry("%dx%d+%d+%d" % (winw,winh,rootx+dx, rooty+dy))
        
    def __exit__(self):
        self.__root__.destroy()
        
    def __changeConfig__(self):
        frame = self.__root__.winfo_children()[1]
        frame.lift()

    def __howTo__(self):
        frame = self.__root__.winfo_children()[2]
        frame.lift()
        
    def __showStatus__(self):
        frame = self.__root__.winfo_children()[3]
        frame.lift()
        
    def __about__(self):
               
        window = tk.Toplevel()
        window.wm_title("About")
        
        message = "Version: 0.5 alpha \n Build Date: 11/30/18\n"
        width = len(message)/2
        label0 = tk.Label(window, text='{m: <{w}}'.format(m=' ', w =width), font=("Liberation Mono", 12))
        label0.grid(row=0, column=0)
        label1 = tk.Label(window, text=message, font=("Liberation Mono", 12))
        label1.grid(row=1, column=0)
        label2 = tk.Label(window, text='{m: <{w}}'.format(m='', w= width), font=("Liberation Mono", 12))
        label2.grid(row=3, column=0)
        
        button = tk.Button(window, text="Close", command=window.destroy, font=("Liberation Mono", 10))
        button.grid(row=2, column=0)

        winw = 5.5*len(message)
        winh = 8*14
        rootx = self.__root__.winfo_x()
        rooty = self.__root__.winfo_y()
        dx = (self.__root__.winfo_width()-winw)/2
        dy = (self.__root__.winfo_height()-winh)/2

        window.geometry("%dx%d+%d+%d" % (winw,winh,rootx+dx, rooty+dy))

        
    def __guiSetup__(self):
        self.__root__.protocol('WM_DELETE_WINDOW', self.__close__)
        self.__root__.wm_title("Emergency Relays")

        screenx = self.__root__.winfo_screenwidth()
        screeny = self.__root__.winfo_screenheight()
        ratio = 3/5
        mainwidth = int(screenx*ratio)
        mainheight = int(screeny*ratio)
        
        self.__root__.geometry("%dx%d+%d+%d" % (mainwidth, mainheight, int((screenx-mainwidth)/2)+1,int((screeny-mainheight)/2)+1))

        
        frame0 = tk.Frame(self.__root__, bg='white',width = mainwidth, height=mainheight)
        frame0.grid(row=0, column=0)
        label0 = tk.Label(frame0, text="You should not see this message", font=("Liberation Mono", 10))
        label0.grid(row=0, column=0)
        frame1 = tk.Frame(self.__root__, bg='white',width = mainwidth, height=mainheight)
        frame1.grid(row=0, column=0)
        frame2 = tk.Frame(self.__root__, bg='white',width = mainwidth, height=mainheight)
        frame2.grid(row=0, column=0)

        inFile = open('README.md', 'r')
        message2 = ''

        for x in inFile.readlines():
            message2 = message2 + x
            
        label2 = tk.Label(frame0, text=message2, font=("Liberation Mono", 10), justify="left", wraplength=mainwidth, bg = "white"
                          )
        label2.grid(row=0, column=0)
        frame3 = tk.Frame(self.__root__, bg='white',width = mainwidth, height=mainheight)
        frame3.grid(row=0, column=0)
        

        menu = tk.Menu(self.__root__)
        self.__root__.config(menu = menu)
        viewMenu = tk.Menu(menu)
        menu.add_cascade(label="Settings", menu=viewMenu)
        viewMenu.add_command(label="Status", command=self.__showStatus__)
        viewMenu.add_command(label="Configuration", command=self.__changeConfig__)
        viewMenu.add_separator()
        viewMenu.add_command(label="Exit", command=self.__close__)

        helpMenu = tk.Menu(menu)
        menu.add_cascade(label="Help", menu=helpMenu)
        helpMenu.add_command(label="How to Use", command=self.__howTo__)
        helpMenu.add_separator()
        helpMenu.add_command(label="About", command=self.__about__)

        frame3.lift()
        
        print(self.__root__.children.values()
              )
                    
    def run(self):
        print("running")

        self.__root__.mainloop()            
            
        

    def __init__(self):
        self.__setup__()
        self.__guiSetup__()
        for i in self.__buttonList__:
            x = ButtonModule(i, self.__Debug__)
            self.__buttonEventHandler__.append(x)
        self.__relay__ = RelayModule(self.__relayList__, self.__boolReset__, self.__gpioDefault__, self.__Debug__)

if __name__ == "__main__":
    rc = RelayController()
    rc.run()
