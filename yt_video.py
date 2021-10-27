from tkinter import *
from tkinter import messagebox
from pytube import YouTube

import os
from tkinter import filedialog 
root = Tk()
root.geometry('500x500')
root.resizable(False,False)
root.configure(bg='#80b3d1')
root.title('Illegal Video Downloader')
def selected():
    return clicked.get()

global clicked
clicked = StringVar()

def donwload():
    global link 
    link = StringVar()
    link = url_box.get()
    
    if link ==  "":
        messagebox.showerror('Status','Please enter a valid link')
        return 
    yt = YouTube(link)
    if selected() == options[0]:
        yt.streams.filter(progressive=True,file_extension='mp4').order_by('resolution').last().download('E:\pytube')
    elif selected() == options[1]:
        yt.streams.filter(progressive=True,file_extension='mp4').order_by('resolution').first().download('E:\pytube')
    elif selected() == options[2]:
        yt.streams.filter(only_audio=True).last().download('E:\pytube')
    messagebox.showinfo('Status','Download complete')
options = [
    'High Resolution',
    'Low Resolution',
    'Audio only'
]
clicked.set(options[0])
drop = OptionMenu(root,clicked,*options)
drop.grid(row=1,column=3,pady=20)
url_label = Label(root,text="Paste the link",fg='black').grid(row=10,column=1)
url_box = Entry(root)
url_box.grid(row=10,column=3)
submit = Button(root,text="Download",command=donwload)
submit.grid(row=15,column=3,pady=50)

root.mainloop()