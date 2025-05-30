import tkinter as tk
from tkinter import ttk
from db import get_all_games


def show_games():
    games = get_all_games()
    for row in games:
        tree.insert("", tk.END, values=row)


root = tk.Tk()
root.title("Game Backlog Manager")
root.geometry("800x400")

columns = ("ID", "Title", "Platform", "Genre", "Status", "Hours", "Completion")
tree = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)

tree.pack(expand=True, fill="both")

show_games()

root.mainloop()
