#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
import time


class Stopwatch(ttk.Frame):
    def __init__(self, master, title: str = "Stopwatch"):
        super().__init__(master, padding=10)

        self.running = False
        self.start_time = 0.0
        self.elapsed = 0.0
        self.after_id = None
        self._title_text = title
        self._title_history: list[str] = [title]
        self.create_widgets()

    def create_widgets(self):
        self.title_var = tk.StringVar(value=self._title_text)
        self.title_entry = ttk.Combobox(
            self,
            textvariable=self.title_var,
            values=self._title_history,
            justify="center",
        )
        self.title_entry.grid(row=0, column=0, columnspan=3, pady=(0, 10), sticky="ew")
        self.title_entry.bind("<Return>", self._save_title)
        self.title_entry.bind("<FocusOut>", self._save_title)

        self.time_var = tk.StringVar(value="00:00:00")

        self.label = ttk.Label(
            self,
            textvariable=self.time_var,
            font=("TkDefaultFont", 28),
            anchor="center",
        )
        self.label.grid(row=1, column=0, columnspan=3, pady=(0, 10))

        self.start_button = ttk.Button(
            self,
            text="Start",
            command=self.start,
        )
        self.start_button.grid(row=2, column=0, padx=5)

        self.stop_button = ttk.Button(
            self,
            text="Stop",
            command=self.stop,
        )
        self.stop_button.grid(row=2, column=1, padx=5)

        self.reset_button = ttk.Button(
            self,
            text="Reset",
            command=self.reset,
        )
        self.reset_button.grid(row=2, column=2, padx=5)

    def _save_title(self, event=None):
        """Add the current entry text to the history (if non-empty & new)."""
        text = self.title_var.get().strip()
        if text and text not in self._title_history:
            self._title_history.insert(0, text)  # most-recent first
            self.title_entry["values"] = self._title_history

    def start(self):
        if not self.running:
            self.running = True
            self.start_time = time.perf_counter() - self.elapsed
            self.update_clock()

    def stop(self):
        if self.running:
            self.running = False

            if self.after_id is not None:
                self.after_cancel(self.after_id)
                self.after_id = None

            self.elapsed = time.perf_counter() - self.start_time

    def reset(self):
        self.stop()

        self.elapsed = 0.0
        self.time_var.set("00:00:00")

    def update_clock(self):
        if self.running:
            self.elapsed = time.perf_counter() - self.start_time

            total_seconds = int(self.elapsed)

            hours = total_seconds // 3600
            minutes = (total_seconds % 3600) // 60
            seconds = total_seconds % 60

            self.time_var.set(f"{hours:02}:{minutes:02}:{seconds:02}")

            self.after_id = self.after(100, self.update_clock)


def main():
    root = tk.Tk()
    root.title("Stopwatch")

    stopwatch = Stopwatch(root)
    stopwatch.pack(padx=20, pady=20)

    root.mainloop()


if __name__ == "__main__":
    main()
