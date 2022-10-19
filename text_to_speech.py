
import tkinter as tk
from  tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter.ttk import Combobox
import pyttsx3
import os

root=Tk()
root.title("Text To Speech Converter")
root.geometry("900x500+250+100")
root.resizable(height=False,width=False)
root.config(bg="orange")




engine=pyttsx3.init()

def speaknow():
    text = text_area.get(1.0,END) 
    gender=gender_clobox.get()
    speed=speed_clobox.get()
    voices=engine.getProperty('voices')

    def setvoice():
        if (gender=='Male'):
            engine.setProperty('voice', voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            engine.say(text)
            engine.runAndWait()

    if(text):
        if speed=="Fast":
            engine.setProperty('rate',250)
            setvoice()
        elif(speed=="Normal"):
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate',100)
            setvoice()


def download():
    text = text_area.get(1.0,END) 
    gender=gender_clobox.get()
    speed=speed_clobox.get()
    voices=engine.getProperty('voices')

    def setvoice():
        if (gender=='Male'):
            engine.setProperty('voice', voices[0].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()

    if(text):
        if speed=="Fast":
            engine.setProperty('rate',250)
            setvoice()
        elif(speed=="Normal"):
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate',100)
            setvoice()







#icones
title_icone=PhotoImage(file="icons8-speaker-50.png")
root.iconphoto(False,title_icone)

#Top heading
top_header=Frame(root,bg="white",width=900,height=100)
top_header.place(x=0,y=0)

top_icon=PhotoImage(file="icons8-speaker-50.png")
Label(top_header,image=top_icon,bg="white").place(x=20,y=10)

Label(top_header,text="Text To Speech",bg="white",font="arial 20 bold",fg="black").place(x=100,y=20)




text_area=Text(root,font="Robote 20",bg="white",relief=GROOVE,wrap=WORD)
text_area.place(x=10,y=150,height=300,width=550)


Label(root, text="VOICE",font="arial 15 bold",bg="blue",fg="white").place(x=599,y=140)
Label( text="SPEED",font="arial 15 bold",bg="blue",fg="white").place(x=785,y=140)

gender_clobox=Combobox(root,values=['Male','Female'],font="arial 15",state='r',width=10)
gender_clobox.place(x=580,y=180)
gender_clobox.set("Male")


speed_clobox=Combobox(root,values=['Slow','Normal','Fast'],font="arial 15",state='r',width=10)
speed_clobox.place(x=750,y=180)
speed_clobox.set("Normal")

imageicon1=PhotoImage(file="speak.png")
btn=Button(root,text="Speak",compound=LEFT,image=imageicon1,font="arial 14 bold" ,command=speaknow)
btn.place(x=580,y=270)

#imageicon2=PhotoImage(file="icons8-speaker-50.png")
imageicon2=PhotoImage(file="save.Png")
save=Button(root,text="Save",compound=LEFT,font="arial 14 bold",image=imageicon2,bg="green",command=download)
save.place(x=750,y=270)

root.mainloop()
