import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import *
from tkinter import filedialog
import os
import pyttsx3

window = Tk()
window.title("SpeechBoy")
window.geometry("1000x450+150+150")
window.resizable(False,False)
window.config(bg="maroon")

engine = pyttsx3.init()

def speakNow():
    text=textArea.get(1.0,END)
    gender = gender_select.get()
    speed = speed_select.get()
    volume = loud_select.get()
    voices = engine.getProperty('voices')

    def setVoice():
        if(gender=="Male"):
            engine.setProperty('voice',voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice',voices[1].id)
            engine.say(text)
            engine.runAndWait()
    if(text):
        if(speed=="Fast"):
            engine.setProperty('rate',250)
        elif(speed=="Normal"):
            engine.setProperty('rate',150)
        else:
            engine.setProperty('rate',60)
    if(text):
        if(volume=="Loud"):
            engine.setProperty('volume',1.0)
        elif(volume=="Normal"):
            engine.setProperty('volume',0.5)
        else:
            engine.setProperty('volume',0.2)

        
        setVoice()

def saveNow():
    text=textArea.get(1.0,END)
    gender = gender_select.get()
    speed = speed_select.get()
    volume = loud_select.get()
    voices = engine.getProperty('voices')

    def setVoice():
        if(gender=="Male"):
            engine.setProperty('voice',voices[0].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()
        else:
            engine.setProperty('voice',voices[1].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()
    if(text):
        if(speed=="Fast"):
            engine.setProperty('rate',250)
        elif(speed=="Normal"):
            engine.setProperty('rate',150)
        else:
            engine.setProperty('rate',60)
    
    if(text):
        if(volume=="Loud"):
            engine.setProperty('volume',1.0)
        elif(volume=="Normal"):
            engine.setProperty('volume',0.5)
        else:
            engine.setProperty('volume',0.2)
        
        setVoice()

# Icon
img = PhotoImage(file="WindowLogo.png")
window.iconphoto(False,img)

#TopFrame
TopFrame = Frame(window,bg='White',width=1000,height=100)
TopFrame.place(x=0,y=0)

Label(TopFrame,text="Text To Speech",font="arial 20 bold",bg='white',fg='maroon').place(x=90,y=30)

textArea = Text(window,font='arial 20 bold',bg='white',relief=GROOVE,wrap=WORD)
textArea.place(x=40,y=150,width=500,height=250)

Label(window,text="Voices",font="arial 20 bold",bg='maroon',fg='white').place(x=570,y=160)
Label(window,text="Speed",font="arial 20 bold",bg='maroon',fg='white').place(x=700,y=160)
Label(window,text="Volume",font="arial 20 bold",bg='maroon',fg='white').place(x=832,y=160)

gender_select = Combobox(window,values=['Male','Female'],state='r',width=13)
gender_select.place(x=570,y=200)
gender_select.set("Male")

speed_select = Combobox(window,values=['Fast','Normal','Slow'],state='r',width=13)
speed_select.place(x=700,y=200)
speed_select.set("Normal")

loud_select = Combobox(window,values=['Loud','Normal','Low'],state='r',width=13)
loud_select.place(x=832,y=200)
loud_select.set("Normal")

# Speak Btn
speakBtn = Button(window,text="Speak",font="arial 14 bold",width=7,command=speakNow) 
speakBtn.place(x=570,y=280)

# Save Btn
saveBtn = Button(window,text="Save",font="arial 14 bold",width=7,command=saveNow) 
saveBtn.place(x=700,y=280)
window.mainloop()