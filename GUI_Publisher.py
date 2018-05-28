# -*- coding: utf-8 -*-
# GUI for Raspberry Pi

from Tkinter import *
import tkFont
import paho.mqtt.publish as publish

window = Tk()
window.title("INPUT GUI")
fullScreenState = True
#window.attributes("-fullscreen", fullScreenState)
window.configure(cursor="none")


container = Frame(window)
container.pack()

myFont = tkFont.Font (family="Times", size = 46, weight = "bold")


def sendInput():
        print("EINGABE GESENDET")
        # Publish test string touch to topic topic/display1
        publish.single("topic/display1", "touch", hostname="test.mosquitto.org")
        # Publish test string swipe to topic topic/display2
        #publish.single("topic/display2", "swipe", hostname="test.mosquitto.org")
        
def closeGUI():

        window.destroy()
        

def toggleFullscreen(self):
        global fullScreenState
        
        if fullScreenState == True:
                
                fullScreenState = False
                window.attributes("-fullscreen", False)
                return
        elif fullScreenState == False:
 
                fullScreenState = True
                window.attributes("-fullscreen", True)
                return


touchScreen = Button(container,
                     font=myFont,
                     command=sendInput,
                     text="TOUCH ME",
                     background="grey",
                     width=1000,
                     height=680,
                     activebackground="blue"
                     )
touchScreen.pack()

window.bind("<Escape>", toggleFullscreen)

window.protocol("WM_DELETE_WINDOW", closeGUI)
window.mainloop()

