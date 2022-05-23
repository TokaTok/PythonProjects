from tkinter import *
from datetime import datetime

temp = 0
after_id = ""


def tick():
    global temp, after_id
    after_id = window.after(1000, tick)
    f_temp = datetime.fromtimestamp(temp).strftime("%M:%S")
    label1.config(text=str(f_temp))
    temp += 1


def start():
    btnStart.grid_forget()
    btnStop.grid(row=1, columnspan=2, sticky="ew")
    tick()


def stop():
    btnStop.grid_forget()
    btnCont.grid(row=1, column=0, sticky="ew")
    btnReset.grid(row=1, column=1, sticky="ew")

    window.after_cancel(after_id)


def cont():
    btnCont.grid_forget()
    btnReset.grid_forget()
    btnStop.grid(row=1, columnspan=2, sticky="ew")

    tick()


def reset():
    global temp
    temp = 0
    btnCont.grid_forget()
    btnReset.grid_forget()
    btnStart.grid(row=1, columnspan=2, sticky="ew")
    label1.config(text="00:00")


window = Tk()

window.title("stopwatch")

label1 = Label(window, width=5, font=("Verdana", 100), text="00:00")
label1.grid(row=0, columnspan=2)

btnStart = Button(window, text="Start", font=("Verdana", 30), command=start)
btnStop = Button(window, text="Stop", font=("Verdana", 30), command=stop)
btnCont = Button(window, text="Continue", font=("Verdana", 30), command=cont)
btnReset = Button(window, text="Reset", font=("Verdana", 30), command=reset)

btnStart.grid(row=1, columnspan=2, sticky="ew")

window.mainloop()
