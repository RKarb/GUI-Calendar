import calendar
from tkinter import *

def dispalyCalendar():
    ui = Tk()
    ui.config(background='blue')
    ui.title("Calendar for ")
    ui.geometry("510x510")
    year = int(yearField.get())
    uiContent = calendar.calendar(year) #Last few dates of most month are not in line with the month, visaully. Not a fun formatting issue
    calYear = Label(ui,text=uiContent,font="Consolas 10 bold")
    #calYear.grid(row=5,column=1,padx=50)
    calYear.place(x=255,y=255,anchor="center")
    ui.mainloop()

if __name__=='__main__':
    new = Tk()
    new.config(background='dark blue')
    new.title("Calendar")
    new.geometry("500x400")
    cal = Label(new, text="Calendar",bg='dark blue',font=("times",28,"bold"))
    year = Label(new,text="Enter year",bg="dark blue")
    yearField=Entry(new)
    button = Button(new,text="Show calendar",fg='black',bg='grey',command=dispalyCalendar)
    cal.place(x=250,y=170,anchor="center")
    year.place(x=250,y=200,anchor="center")
    yearField.place(x=250,y=220,anchor="center")
    button.place(x=250,y=250,anchor="center")
    new.mainloop()