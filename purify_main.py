import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog, messagebox
from purifier import *
import os

def browseFiles():
    filepath = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("ASS files",
                                                        "*.ass*"),
                                                       ("all files",
                                                        "*.*")))
    return filepath

class App:
    def __init__(self, root):
        #setting title
        root.title("Sub Purifier")
        #setting window size
        width=490
        height=214
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        purify_btn=tk.Button(root)
        purify_btn["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=12)
        purify_btn["font"] = ft
        purify_btn["fg"] = "#fff"
        purify_btn["bg"] = "#5cb85c"
        purify_btn["justify"] = "center"
        purify_btn["text"] = "Purify"
        purify_btn.place(x=345,y=120,width=110,height=42)
        purify_btn["command"] = self.purify_btn_command

        reset_btn = tk.Button(root)
        reset_btn["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        reset_btn["font"] = ft
        reset_btn["fg"] = "#000000"
        reset_btn["justify"] = "center"
        reset_btn["text"] = "reset"
        reset_btn.place(x=40, y=175, width=40, height=20)
        reset_btn["command"] = self.reset_btn_command

        browse_btn=tk.Button(root)
        browse_btn["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=12)
        browse_btn["font"] = ft
        browse_btn["fg"] = "#000000"
        browse_btn["justify"] = "center"
        browse_btn["text"] = "Browse"
        browse_btn.place(x=345,y=60,width=110,height=42)
        browse_btn["command"] = self.browse_btn_command

        global sub_listbox
        sub_listbox = tk.Listbox(root)
        scrollbar = tk.Scrollbar(root)
        # scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
        scrollbar.place(x=30, y=30, height=145)
        sub_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=sub_listbox.yview)
        sub_listbox["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times', size=10)
        sub_listbox["font"] = ft
        sub_listbox["fg"] = "#333333"
        sub_listbox["justify"] = "center"
        # sub_file_lbl["text"] = "No files chosen"
        sub_listbox.place(x=40, y=30, width=250, height=145)
        global sub_path
        sub_path = []

    def purify_btn_command(self):
        if sub_path:
            for sub in sub_path:
                replace_with_alt(sub)
            tk.messagebox.showinfo(title="Success!", message="Successfuly Purified")
        else:
            tk.messagebox.showerror(title="No fileSuccesspath", message="No subfile chosen")

    def browse_btn_command(self):
        newfile = browseFiles()
        if newfile and newfile not in sub_path:
            sub_path.append(newfile)
            last_part = os.path.basename(newfile)
            if len(last_part) > 40:
                last_part = last_part[-40:]
            sub_listbox.insert(tk.END, last_part)

    def reset_btn_command(self):
        sub_listbox.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
