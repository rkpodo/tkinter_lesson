import tkinter as tk #import Tkinter
from tkinterweb import HtmlFrame #import the HTML browser

root = tk.Tk() #create the tkinter window
frame = HtmlFrame(root) #create HTML browser

frame.load_website("https://openlabs.edu.gh/") #load a website
frame.pack(fill="both", expand=True) #attach the HtmlFrame widget to the parent window
root.mainloop()