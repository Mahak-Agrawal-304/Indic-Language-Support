#PROGRAM TO CREATE LANGUAGE TRANSLATOR 

#import GUI library tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#import googletrans library
from googletrans import Translator,LANGUAGES

#import libraries for voice translation
import speech_recognition as sr
from langdetect import detect
from gtts import gTTS
import os


#creating object window 
root = Tk()
root.geometry("500x650")#Geometry
root.title("Translator")#Title
root.config(bg='#fefbfa')#config color 
    

#Function for clearing all values       
def clearall():
    sou_txt.delete(1.0,tk.END)
    des_txt.delete(1.0,tk.END)

#Function for recording speech
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        text="Speak something..."
        sou_txt.insert(tk.END,text)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        t=f"{text}"
        sou_txt.delete(1.0,tk.END)
        sou_txt.insert(tk.END,t)
        comb_sou_option=comb_sou.get()
        comb_des_option=comb_des.get()
        txt = sou_txt.get(1.0,tk.END)
        trans = Translator()
        trans1 = trans.translate(text=txt,src=comb_sou_option,dest=comb_des_option)
    
        des_txt.delete(1.0, tk.END)
        des_txt.insert(tk.END,trans1.text)
      
    except sr.UnknownValueError:
        messagebox.showinfo("Error","Speech recognition could not understand the audio.")
        return ""
    except sr.RequestError as e:
        messagebox.error("Error",f"Could not request results from Google Speech Recognition service; {e}")
        return ""


#Function for playing translated text
def text_to_speech():
    text=des_txt.get(1.0,tk.END)
    comb_des_option=comb_des.get()
    lang_code=detect(comb_des_option)
    tts = gTTS(text=text, lang=lang_code, slow=False)
    tts.save("output.mp3")
    os.system("start output.mp3")


#Creating a label text and placing it in object window
lbl_txt = Label(root,text="Translator",font=("Times New Roman",30),bg='#fefbfa')
lbl_txt.place(x=100,y=15,height=40,width=300)


#Creating label Source text
lbl_txt = Label(root,text="Source Text",font=("Times New Roman",16),bg='#fefbfa' )
lbl_txt.place(x=0,y=80,height=30,width=130)
sou_txt = Text(root,font=("Times New Roman",14))
sou_txt.place(x=10,y=120,height=200,width=480)


#creating list for languages
list_txt = list(LANGUAGES.values()) 


#Creating combobox for from language
comb_sou= ttk.Combobox(root,values = list_txt)
comb_sou.place(x=200,y =80,height = 30,width= 100)
comb_sou.set("English")


#Creating combobox for to language
comb_des= ttk.Combobox(root,values = list_txt)
comb_des.place(x=200,y =400,height = 30,width= 100)
comb_des.set("Hindi")


#Creating label for output 
lbl_txt = Label(root,text="Translated Text",font=("Times New Roman",16),bg='#fefbfa' )
lbl_txt.place(x=0,y=400,height=30,width=155)
des_txt = Text(root,font=("Times New Roman",14),wrap=WORD)
des_txt.place(x=10,y=440,height=200,width=480)


#Button for translation
Btn1=Button(root,text='Translate',relief=RAISED,command=get_data, bg="white")
Btn1.place(x=120,y=340,height = 30,width = 100)


#Button for voice translation
img1_path="C:/Users/HP/HackAI/voice.png"
img1=PhotoImage(file=img1_path)
voicebtn= Button(root,image=img1,command=recognize_speech)
voicebtn.place(x=450,y=80,height=30,width=30)


#Button for playing translated text
img2_path="C:/Users/HP/HackAI/play.png"
img2=PhotoImage(file=img2_path)
playbtn= Button(root,image=img2,command=text_to_speech)
playbtn.place(x=450,y=400,height=30,width=30)


#Button for Clear all
Btn2=Button(root,text='Clear all',relief=RAISED,command=clearall,bg="white")
Btn2.place(x=280,y=340,height = 30,width = 100)

root.mainloop()
