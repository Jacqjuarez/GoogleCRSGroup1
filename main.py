import time
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("650x200")
root.title("Pomodoro Timer")
root.config(bg='blue')

hour = StringVar()
minute = StringVar()
second = StringVar()

# setting the default value as 0
hour.set("00")
minute.set("00")
second.set("00")

# Using Entry class to take input from the user
hour_box = Entry(
    root,
    width=3,
    font=("Arial", 35, ""),
    textvariable=hour
)

hour_box.place(x=175, y=30)

mins_box = Entry(
    root,
    width=3,
    font=("Arial", 35, ""),
    textvariable=minute)

mins_box.place(x=275, y=30)

sec_box = Entry(
    root,
    width=3,
    font=("Arial", 35, ""),
    textvariable=second)

sec_box.place(x=375, y=30)


def countdowntimer():
    try:
        # store the user input
        user_input = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
    except:
        messagebox.showwarning('', 'Invalid Input!')
    while user_input > -1:

        # divmod(firstvalue = user_input//60, secondvalue = user_input%60)
        mins, secs = divmod(user_input, 60)

        # Converting the input entered in mins or secs to hours,
        hours = 0
        if mins > 60:
            hours, mins = divmod(mins, 60)

        # store the value up to two decimal places
        # using the format() method
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))

        # updating the GUI window
        root.update()
        time.sleep(1)

        # if user_input value = 0, then a messagebox pop's up
        # with a message
        if (user_input == 0):
            messagebox.showinfo("Time Countdown", "Time Over")


        # decresing the value of temp
        # after every one sec by one
        user_input -= 1


# button widget
btn = Button(root, text='Study'
                        '', bd='5',
             command=countdowntimer)
btn.place(x=300, y=150)

root.mainloop()
