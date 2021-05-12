import sys
import os

from subprocess import Popen, PIPE

try:
    import tkinter as tk
    from tkinter import filedialog
except ImportError:
    import Tkinter as tk
    from Tkinter import filedialog
from PIL import Image, ImageTk

git_path = os.getcwd()
window = tk.Tk()

def execute_console_command(command):
    execute = Popen(command.split(" "), stdout=PIPE)
    return execute.communicate()[0]

def browse_button():
    window.destroy()
    git_path = filedialog.askdirectory()
    window.__init__()
    display_ui(f"Directory changed to: {git_path}")

def refresh(message):
    window.destroy()
    window.__init__()
    display_ui(message)

def status():
    message = execute_console_command("git status")
    refresh(message)

def add_all():
    execute_console_command("git add .")
    refresh("Added all changes to the commit!")

def commit(commit_message):
    cmd = Popen(["git", "commit", "-m", f"\"{commit_message}\""], stdout=PIPE)
    refresh(cmd.communicate()[0])

def push():
    execute_console_command("git push")
    refresh("Pushed all commits to remote repository!")

def display_ui(message):
    window.title("Git GUI+")
    window.geometry("300x300")
    window.resizable(False, True)
    window.iconbitmap(f"{os.path.abspath(os.path.dirname(__file__))}/resources/icon-128.ico")

    frame1 = tk.Frame(window)
    #img  = Image.open(f"{os.path.abspath(os.path.dirname(__file__))}/resources/icon-512.ico")
    #img = img.resize((30, 30), Image.ANTIALIAS)
    #logo = ImageTk.PhotoImage(img)
    #logo_label = tk.Label(frame1, image=logo)
    #logo_label.pack(side=tk.LEFT) 
    path_label = tk.Label(frame1, text=git_path, width=33)
    path_label.pack(side=tk.LEFT, expand=True)
    btn_browse = tk.Button(frame1, text="Browse", command=browse_button)
    btn_browse.pack(side=tk.RIGHT)
    frame1.pack(fill=tk.X)

    btn_status = tk.Button(window, text="Status", command=status)
    btn_status.pack(fill=tk.X)

    btn_add_all = tk.Button(window, text="Add all", command=add_all)
    btn_add_all.pack(fill=tk.X)

    frame2 = tk.Frame(window)
    commit_message_entry = tk.Entry(frame2, width=40)
    commit_message_entry.insert(0, "Update✨")
    commit_message_entry.pack(side=tk.LEFT, expand=True)
    btn_commit = tk.Button(frame2, text="Commit", command=lambda:commit(commit_message_entry.get()))
    btn_commit.pack(side=tk.RIGHT)
    frame2.pack(fill=tk.X)

    btn_push = tk.Button(window, text="Push", command=push)
    btn_push.pack(fill=tk.X)

    console_text = tk.Label(bg="#fff", text=message, justify=tk.LEFT, font="Consolas 8", anchor="nw")
    console_text.pack(fill=tk.BOTH, expand=True)

    window.mainloop()


if __name__ == '__main__':
    display_ui("Welcome to Git GUI+!")