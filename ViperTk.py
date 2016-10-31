import Tkinter, tkMessageBox
top = Tkinter.Tk()
def HelloBox():
    tkMessageBox.showinfo(title="Titular Title", message="Hello Python, Goodbye spam!")
# Code to add widgets will go here...
B = Tkinter.Button( top, text = "Hello World", command = HelloBox )
#B.pack() #What does this even do?
top.mainloop()
