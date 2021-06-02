from tkinter import *
import webbrowser
import tkinter as tk
window= Tk()
thelabel=Label(window,text="Hello, welcome to Tinnitus supporter",fg="red")
thelabel.pack()
canvas1 = tk.Canvas(window, width = 400, height = 900)
canvas1.pack()
label = tk.Label(text='Enter your age')
canvas1.create_window(200, 30, window=label)
entry1 = tk.Entry (window)
canvas1.create_window(200, 50, window=entry1)
thelabel1=Label(window,text="Please select your gender")
canvas1.create_window(200, 80, window=thelabel1)
thelabel.pack()
C1 = Radiobutton(window, text="male", value=1 )
C1.pack()
canvas1.create_window(200, 100, window=C1)
C2 = Radiobutton(window, text="female",value=2)
C2.pack()
canvas1.create_window(200, 120, window=C2)



def onClick(x):
    webbrowser.open(x,new=1)


label3 = Label(text="It is gonna be alright, you're not alone")
label3.pack()
canvas1.create_window(200, 150, window=label3)

labelOne = Label(text="Watch these youtube videos for feeling relaxed")
labelOne.pack()
canvas1.create_window(200, 180, window=labelOne)


url1 = "https://www.youtube.com/watch?v=cGpJvhR9h-s&ab_channel=YellowBrickCinema-RelaxingMusic"

click = Button(text="Video 1", command=lambda: onClick(url1))
click.pack()
canvas1.create_window(200, 230, window=click)

url2 = "https://www.youtube.com/watch?v=cGpJvhR9h-s&ab_channel=YellowBrickCinema-RelaxingMusic"

click = Button(text="Video 2", command=lambda: onClick(url2))
click.pack()
canvas1.create_window(200, 260, window=click)


window.mainloop()
