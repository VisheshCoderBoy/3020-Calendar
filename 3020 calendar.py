import tkinter
from tkinter import *
import calendar
 
root=Tk()
root.state('zoomed')

def year():
    chosen_year=3020
    clnder=calendar.calendar((chosen_year))
    lbl=Label(root,text=clnder,font='Arial 12')
    lbl.grid(row=0,column=0 , padx=20)
year()

root.title("3020 Calendar")
root.mainloop()