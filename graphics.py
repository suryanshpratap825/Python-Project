from tkinter import *
root=Tk()
# root.geometry("500x400") #it is take only string in this form
root.state('zoomed')
root.resizable(width=False,height=False)
root.configure(bg="#BFFFF0")
b1=Button(root,text="submit")
b2=Button(root,text="ok")
b1.pack(side="top",anchor="w")
root.mainloop()