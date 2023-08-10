from tkinter import *
import pyshorteners
root = Tk()
root.title('url shortner')
root.geometry("550x300")

def shorten():
    if sh.get():
        sh.delete(0,END)
    if lg.get():
        url=pyshorteners.Shortener().tinyurl.short(lg.get())
        sh.insert(END,url)
Label(root,text="Enter the url you wanted to be shortned",font=("Helvetica 20 bold")).pack(pady=10)
lg=Entry(root,width=80)
lg.pack(pady=20)
Button(root, text="Shornen URL", font=("Helvetica 15"),command=shorten).pack(pady=20)

sh=Entry(root,width=80)
sh.pack(pady=20)

root.mainloop()