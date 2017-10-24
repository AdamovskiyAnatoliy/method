import tkinter as Tk
import tkinter.ttk as ttk
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as inter

import method_aproks as mp
import method_lagranz as ml
import method_newton as mn


def inserter(value):
    output.delete("0.0", "end")
    output.insert("0.0", value)


def clear(event):
    caller = event.widget
    caller.delete("0", "end")


def solve_l():
    handler(ml.construction_of_lpolinom)


def solve_n():
    handler(mn.construction_of_npolinom)


def paint_l_n():
    handler(ml.paint_l)


def handler(f):
    try:
        a_val = float(a.get())
        b_val = float(b.get())
        c_val = float(c.get())
        if b_val < c_val:
            inserter(f(a_val, b_val, c_val))
        else:
            inserter("Left limit mast be lesser right limit")
    except ValueError:
        inserter("Make sure you entered 3 numbers")

root = Tk.Tk()
root.title("Method")
root.minsize(500, 350)
root.resizable(width=False, height=False)

frame = Tk.Frame(root)
frame.grid()

a = Tk.Entry(frame, width=3)
a.grid(row=1, column=1, padx=(10, 0))
a.bind("<FocusIn>", clear)
a_lab = Tk.Label(frame, text="Nodes:").grid(row=1, column=0)

b = Tk.Entry(frame, width=3)
b.bind("<FocusIn>", clear)
b.grid(row=1, column=3)
b_lab = Tk.Label(frame, text="Left limit:").grid(row=1, column=2)

c = Tk.Entry(frame, width=3)
c.bind("<FocusIn>", clear)
c.grid(row=1, column=5)
c_lab = Tk.Label(frame, text="Right limit:").grid(row=1, column=4)

but_l = Tk.Button(frame,
                  text="Solve L",
                  command=solve_l).grid(row=1, column=6, padx=(10, 0))
but_fig = Tk.Button(frame,
                    text="Graf",
                    command=paint_l_n).grid(row=1, column=7, padx=(10, 0))

output = Tk.Text(frame, bg="lightblue")
output.grid(row=2, columnspan=8)

root.mainloop()
