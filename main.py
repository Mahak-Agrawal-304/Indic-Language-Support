#PROGRAM TO CREATE LANGUAGE TRANSLATOR 

#import GUI library tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import Tk, filedialog

#for text detection
import pandas as pd
import easyocr
import cv2

#import googletrans library
from googletrans import Translator,LANGUAGES

#import libraries for voice translation
import speech_recognition as sr
from langdetect import detect
from gtts import gTTS
import os

#creating object window 
root = Tk()
root.geometry("500x700")#Geometry
root.title("Translator")#Title
root.config(bg='#fefbfa')#config meand color and all


#Function for translation
def get_data():
    comb_sou_option=comb_sou.get()
    comb_des_option=comb_des.get()
    txt = sou_txt.get(1.0,tk.END)
    try:
        trans = Translator()
        trans1 = trans.translate(text=txt,src=comb_sou_option,dest=comb_des_option)
    
        des_txt.delete(1.0, tk.END)
        des_txt.insert(tk.END,trans1.text)
        return None
    except Exception as e:
        messagebox.showerror("Error","Please enter text to be translated")
        return None
    

#Function for clearing all values       
def clearall():
    sou_txt.delete(1.0,tk.END)
    des_txt.delete(1.0,tk.END)
    upld("")


#Functionto record audio
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        t=f"{text}"
        sou_txt.delete(1.0,tk.END)
        sou_txt.insert(tk.END,t)
        return text
    except sr.UnknownValueError:
        messagebox.showinfo("Error","Speech recognition could not understand the audio.")
        return ""
    except sr.RequestError as e:
        messagebox.error("Error",f"Could not request results from Google Speech Recognition service; {e}")
        return ""

#Function to convert text into speech
def text_to_speech():
    text=des_txt.get(1.0,tk.END)
    comb_des_option=comb_des.get()
    lang_code=detect(comb_des_option)
    tts = gTTS(text=text, lang=lang_code, slow=False)
    tts.save("output.mp3")
    os.system("start output.mp3")


#Function to upload file
def select_image_file():
    root = Tk()
    root.withdraw()  # Hide the root window

    # Prompt the user to select an image file using a file dialogue
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp")])
    image_file_path = file_path
    img1=image_file_path
    filename=os.path.basename(img1)
    upld(filename)

    img = cv2.imread(img1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #noise = cv2.medianBlur(gray,3)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4)

    #thresh = cv2.threshold(noise, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    reader = easyocr.Reader(['en'])
    result = reader.readtext(img,paragraph=False)
    text_lines = [entry[1] for entry in result[0::]]  # Exclude the last line
    text = ' '.join(text_lines)
    df = pd.DataFrame({"":text_lines})

    sou_txt.delete(1.0,tk.END)
    sou_txt.insert(tk.END,df.to_string(index=False,header=False))
    

#Creating a label text and placing it in object window
lbl_txt = Label(root,text="Translator",font=("Times New Roman",30),bg='#fefbfa')
lbl_txt.place(x=100,y=15,height=40,width=300)


#Creating label Source text
lbl_txt = Label(root,text="Source Text",font=("Times New roman",16),bg='#fefbfa' )
lbl_txt.place(x=0,y=80,height=30,width=130)
sou_txt = Text(root,font=("Times New roman",14))
sou_txt.place(x=10,y=145,height=200,width=480)


#creating list for languages
list_txt = ('Bengali',
            'English',
            'Gujarati',
            'Hindi',
            'Kannada',
            'Malayalam',
            'Marathi',
            'Nepali',
            'Odia',
            'Punjabi',
            'Sindhi',
            'Tamil',
            'Telugu',
            'Urdu')

#Creating combobox for from language
comb_sou= ttk.Combobox(root,values = list_txt)
comb_sou.place(x=200,y =80,height = 30,width= 100)
comb_sou.set("English")


#Creating combobox for to language
comb_des= ttk.Combobox(root,values = list_txt)
comb_des.place(x=200,y =430,height = 30,width= 100)
comb_des.set("Hindi")


#Creating label for output 
lbl_txt = Label(root,text="Translated Text",font=("Times New roman",16),bg='#fefbfa' )
lbl_txt.place(x=0,y=430,height=30,width=155)
des_txt = Text(root,font=("Times New roman",14),wrap=WORD)
des_txt.place(x=10,y=470,height=200,width=480)

def upld(image):
    lbl_txt = Label(root,text=f"Image Uploaded: {image}",font=("Times New roman",12),bg='#fefbfa' )
    lbl_txt.place(x=300,y=110,height=30,width=200)


#Button for translation
Btn1=Button(root,text='Translate',relief=RAISED,command=get_data, bg="white")
Btn1.place(x=120,y=370,height = 30,width = 100)


#Button for voice translation
img1_path="C:/Users/HP/HackAI/voice.png"
img1=PhotoImage(file=img1_path)
voicebtn= Button(root,image=img1,command=recognize_speech)
voicebtn.place(x=400,y=80,height=30,width=30)


#Button for playing translated text
img2_path="C:/Users/HP/HackAI/play.png"
img2=PhotoImage(file=img2_path)
playbtn= Button(root,image=img2,command=text_to_speech)
playbtn.place(x=450,y=430,height=30,width=30)


#Button for uploading image
img3_path="C:/Users/HP/HackAI/upload.png"
img3=PhotoImage(file=img3_path)
upldbtn= Button(root,image=img3, command=select_image_file)
upldbtn.place(x=450,y=80,height=30,width=30)


#Button for Clear all
Btn2=Button(root,text='Clear all',relief=RAISED,command=clearall,bg="white")
Btn2.place(x=280,y=370,height = 30,width = 100)

root.mainloop()
