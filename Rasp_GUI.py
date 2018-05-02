# GUI for Raspberry Pi

from Tkinter import *
import tkinter.font 

window = Tk()
window.title("INPUT GUI")
window.geometry("1000x680")

myFont = tkFont.Font(family="Times New Roman", size = 46, weight = "bold")


def sendInput():
	print("EINGABE GESENDET")

def closeGUI():
	window.destroy()



touchScreen = Button(window, text="TOUCH ME", font = myFont, command = sendInput, width = 28, height = 2, bg = "bisque2")


window.protocol("WM_DELETE_WINDOW", closeGUI)
window.mainloop()

