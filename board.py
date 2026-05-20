#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
import tkinter as tk
from tkinter_stopwatch import Stopwatch, NoteHistory


class Board(tk.Tk):
    def __init__(self, stopwatches):
        super().__init__()
        # self.geometry("300x200")
        self.title(f"Stopwatches({stopwatches})")
        self.stopwatches = stopwatches
        self.frame = tk.Frame(self)
        self.frame.grid(column=0, row=0, sticky=tk.NSEW)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        # self.note_history = NoteHistory(["creatine&piracetam", "IMET"])

        self.create_widgets()

    def create_widgets(self):
        Stopwatch.note_history = NoteHistory(["creatine&piracetam", "IMET"])
        rows = self.stopwatches // 2
        for row in range(rows):
            stopwatch = Stopwatch(self.frame)
            stopwatch.grid(column=0, row=row, sticky=tk.NW)
            stopwatch = Stopwatch(self.frame)
            stopwatch.grid(column=1, row=row, sticky=tk.NW)


if __name__ == "__main__":
    board = Board(10)
    board.mainloop()
