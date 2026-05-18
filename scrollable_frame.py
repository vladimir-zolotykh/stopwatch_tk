#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
import tkinter as tk
from tkinter_stopwatch import Stopwatch

root = tk.Tk()
root.geometry("300x200")

# Create canvas + scrollbar
canvas = tk.Canvas(root)
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

# Layout with grid
canvas.grid(row=0, column=0, sticky="nsew")
scrollbar.grid(row=0, column=1, sticky="ns")

# Make root expandable
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Create a frame inside the canvas
scroll_frame = tk.Frame(canvas)
stopwatch1 = Stopwatch(canvas)
stopwatch2 = Stopwatch(canvas)
stopwatch3 = Stopwatch(canvas)

# Add the frame to the canvas
# window = canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
window1 = canvas.create_window((0, 0), window=stopwatch1, anchor="nw")
window2 = canvas.create_window((0, 100), window=stopwatch2, anchor="nw")
window3 = canvas.create_window((0, 200), window=stopwatch3, anchor="nw")


# Ensure canvas scrolls when frame grows
def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))


# scroll_frame.bind("<Configure>", on_configure)
stopwatch1.bind("<Configure>", on_configure)

# Populate with many widgets
# for i in range(30):
#     tk.Label(scroll_frame, text=f"Row {i}").grid(row=i, column=0, sticky="w")

root.mainloop()
