from tkinter import *
import time

def times():
    current_time = time.strftime("%I:%M:%S:%p")
    clock_lbl = Label(root,font = "comic_sans_ms 80",bg  = "yellow", fg = "green", text  =current_time)
    clock_lbl.after(200,times)
    clock_lbl.grid(row=  0, column = 1)

root = Tk()
root.title("Digital Clock")
root.resizable(False, False)
times()

root.mainloop()
