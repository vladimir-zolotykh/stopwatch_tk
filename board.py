#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
import tkinter as tk
from tkinter_stopwatch import Stopwatch


class Board(tk.Tk):
    def __init__(self, stopwatches):
        super().__init__()
        self.geometry("300x200")
        self.title(f"Stopwatches({stopwatches})")
        self.stopwatches = stopwatches
        self.frame = tk.Frame(self)
        self.frame.grid(column=0, row=0, sticky=tk.NSEW)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.create_widgets()

    def create_widgets(self):
        cols = 2
        rows = self.stopwatches // cols
        for row in range(rows):
            col = 0
            stopwatch = Stopwatch(self.frame, title=f"Stopwatch{str(row * cols + col)}")
            stopwatch.grid(column=col, row=row, sticky=tk.NW)
            col += 1
            stopwatch = Stopwatch(self.frame, title=f"Stopwatch{str(row * cols + col)}")
            stopwatch.grid(column=col, row=row, sticky=tk.NW)
            col += 1


if __name__ == "__main__":
    board = Board(10)
    board.mainloop()
