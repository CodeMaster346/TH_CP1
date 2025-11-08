import tkinter as tk
from tkinter import ttk

tk_root = tk.Tk()
tk_root.title("Tkinter Overview")
tk_root.geometry("500x400")
tk_root.mainloop()

title_label = ttk.Label(tk_root, text = "Miles to Kilometers", align = "center", font = ("Arial", 24))
title_label.pack()