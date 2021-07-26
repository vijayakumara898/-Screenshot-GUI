import pyautogui
import tkinter as tk
from tkinter import *
from tkinter.filedialog import *
import PIL

window = tk.Tk()
canvas1 = tk.Canvas(window,width="300",height="300",bg="green")
canvas1.pack()

def screenshot():
    img = pyautogui.screenshot()
    save_path = asksaveasfilename()
    img.save(save_path+"_screenshot.png")

b1 =tk.Button(text="Take Screenshot", command=screenshot,font="10")
canvas1.create_window(150,150,window =b1, anchor="center")

mainloop()