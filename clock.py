from tkinter import *


from time import strftime
root=Tk()
root.title("Mb Clock")

def time():
    string=strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)
label=Label(root, font=("Arial" , 80), background="black" , foreground="cyan" )
label.pack(anchor='center')
time()

mainloop()