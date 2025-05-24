import tkinter as tk
from tkinter import *
from tkinter import filedialog
import yt_dlp
import os

def download(URL,folder):
    try:
        url=URL
        option={
        "format":"best",
        "outtmpl":os.path.join(folder,"%(title)s.%(ext)s")
        }
        with yt_dlp.YoutubeDL(option) as ydl:
            ydl.download([url])
        root.destroy()
    except Exception as e:
        print("error: ",e)
        return
   
def app():
    folder=filedialog.askdirectory()
    url=Url.get()
    if folder and url:
        print(f"Selected folder to store video: {folder} & {url}")
        download(url,folder)
    
root=tk.Tk()
root.title("YouTube Video Downloader")
label=Label(root,text="Enter Youtube Url link: ",font=("Arial",20)).pack()
Url=Entry(root,width=50)
Url.pack()
button=Button(root,text="Download",command=app).pack(pady=20)

root.mainloop()

