#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
import tkinter as tk
import shelve
from tkinter import ttk
from tkinter_stopwatch import Stopwatch, NoteHistory


class Board(tk.Tk):
    def __init__(self, stopwatches, note_history_init=[]):
        super().__init__()
        style = ttk.Style()
        style.theme_use("clam")
        default_font = ("Arial", 7)
        style.configure(
            "TButton",
            font=default_font,
            padding=0,
        )

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
        # Stopwatch.note_history = NoteHistory(["creatine&piracetam", "IMET"])
        Stopwatch.note_history = NoteHistory(saved_notes["note_history"])
        rows = self.stopwatches // 2
        for row in range(rows):
            stopwatch = Stopwatch(self.frame)
            stopwatch.grid(column=0, row=row, sticky=tk.NW)
            stopwatch = Stopwatch(self.frame)
            stopwatch.grid(column=1, row=row, sticky=tk.NW)


if __name__ == "__main__":
    with shelve.open(".board_note_history") as saved_notes:
        if "note_history" not in saved_notes:
            saved_notes["note_history"] = ["creatine&piracetam", "IMET"]
        board = Board(10, saved_notes["note_history"])
        board.mainloop()
        saved_notes["note_history"] = Stopwatch.note_history.data
