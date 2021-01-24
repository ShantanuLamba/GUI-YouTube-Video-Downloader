from tkinter import *
from pytube import YouTube

def download():
    YouTube(url.get()).streams.first().download()

root = Tk()

root.minsize(600, 300)
root.maxsize(600, 300)
root.title("YouTube Video Downloader")

Title = Label(text="YouTube Video Downloader", bg="red", fg="white", font="helvetica 24 bold", borderwidth= 3, relief=RIDGE,)
Title.pack()

label2 = Label(text="Paste Link Here:", font="helvetica 13 bold")
label3 = Label(text="NOTE-The video will be saved on the same folder where this program is saved", font="10")
label3.pack(pady=10)
label2.pack(pady=10)

url = StringVar()
entry = Entry(root, textvariable = url, font="25")
entry.pack(pady=7)
button = Button(text="Download", font="helvetica 14 bold", bg="blue", fg="white", command=download).pack(pady=10)
label4 = Label(text="NOTE-The Download goes on until the download button is blue again")
label4.pack(pady=10)


root.mainloop()
