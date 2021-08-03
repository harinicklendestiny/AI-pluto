#imports
from tkinter import *
import tkinter as Tkinter
import tkinter as tk
from PIL import Image, ImageTk
from itertools import count
from tkinter import filedialog
import os
from tkinter.filedialog import askopenfilename 
import googlesearch
import webbrowser
from PIL import ImageTk, Image

#widgets

class ImageLabel(tk.Label):
    """a label that displays images, and plays them if they are gifs"""
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()

    def unload(self):
        self.config(image="")
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)

root = tk.Tk()
lbl = ImageLabel(root)
lbl.pack()
lbl.load('C:\\Users\\Hari\\Destny the ai\\pluto.gif')

#Def
def open_file(): 
    os.startfile('C:\\Users\\Hari\\Destny the ai\\pluto.py')

def callback(url):
        webbrowser.open(url)

def search_query():
        
        query = text.get("1.0","end-1c")
        s = googlesearch.search(query, tld="co.in", num=10, stop=5, pause=2)
        # print(s)
        for j in s:
                # print(j)
                webbrowser.open(j)

#other google things

#search button
search = Button(root, text="Google Search",relief=RIDGE,font=('arial',10),bg="#F3F3F3",fg="#222222",cursor="hand2",command=search_query)
search.place(x=270,y=360)

#search box
text = Text(root,width=90,height=2,relief=RIDGE,font=('roboto',10,'bold'),borderwidth=2)
text.place(x=120,y=300)

#button
Button(root, text ='Start', 
       command = open_file).pack(side = TOP, 
                                 pady = 10)

#Window
root.title('Pluto')
root.geometry("300x200+10+20")
root.geometry("800x500")

root.mainloop()
