from tkinter import *
from PIL import ImageTk, Image
from recognize import record_audio, parse_audio

gui = Tk()
gui.title('Language Learner')
gui.geometry("500x200")

Label1 = Label(gui, text="Test yourself to see if you can speak Spanish!")
Label2 = Label(gui, text="After you're done, click on the button bellow to see your speach in text.")

B1 = Button(gui, text="Click to begin recording audio.", command=record_audio)
B2 = Button(gui, text="Click to see your results.", command=parse_audio)

Label1.pack()
B1.pack()
Label2.pack()
B2.pack()

gui.mainloop()
