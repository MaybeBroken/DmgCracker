import os
from tkinter import filedialog, Tk
from tkinter import *
from time import sleep

os.chdir(os.path.dirname(__file__))


class VIEWER:
    def __init__(self):
        None

    def print(self, message):
        print(message)


class Main:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("450x425")
        self.root.title("File Cracker")
        self.root.configure(bg="black")
        self.viewer = VIEWER()
        self.buildGui()
        self.root.focus_force()

    def openDmg(self, file_path=None, out_path=None):
        if not file_path:
            print("No file selected.")
            return False
        elif not out_path:
            out_path = os.path.dirname(file_path)
            print("Output directory not selected, defaulting to:", out_path)
        os.system(f".{os.path.sep}7zz x -o{out_path} -y -snl {file_path}")
        self.viewer.print("File extracted to: " + out_path)
        self.root.focus_force()

    def buildGui(self):
        self.label = Label(
            self.root, text="Add files to crack:", bg="black", fg="white"
        )
        self.label.pack(pady=20)

        self.top_frame = Frame(self.root, bg="black")
        self.top_frame.pack(pady=10)
        self.select_button = Button(
            self.top_frame,
            text="Add File",
            command=self.select_file,
            bg="black",
            fg="black",
        )
        self.select_button.pack(side=LEFT, pady=10)

        self.delete_button = Button(
            self.top_frame,
            text="Delete Selected File",
            command=lambda: self.files_list.delete(ANCHOR),
            bg="black",
            fg="black",
        )
        self.delete_button.pack(side=RIGHT, padx=10)

        self.files_list = Listbox(self.root, width=50, height=10)
        self.files_list.pack(pady=10)

        self.bottom_frame = Frame(self.root, bg="black")
        self.bottom_frame.pack(pady=10)
        self.output_button = Button(
            self.bottom_frame,
            text="Select Output Directory",
            command=self.select_output,
            bg="black",
            fg="black",
        )
        self.output_button.pack(side=LEFT, pady=10)
        self.start_button = Button(
            self.bottom_frame,
            text="Start Cracking",
            command=self.start_cracking,
            bg="black",
            fg="black",
        )
        self.start_button.pack(side=RIGHT, padx=10)

    def select_file(self):
        file_path = filedialog.askopenfilename(
            title="Select File",
            filetypes=[("All files", "*.*")],
        )
        if file_path:
            self.files_list.insert(END, file_path)
            self.viewer.print("File selected: " + file_path)
        else:
            self.viewer.print("No file selected.")
        self.root.focus_force()

    def select_output(self):
        self.out_path = filedialog.askdirectory(
            title="Select Output Directory",
        )
        if self.out_path:
            self.viewer.print("Output directory selected: " + self.out_path)
        else:
            self.viewer.print("No output directory selected.")
        self.root.focus_force()

    def start_cracking(self):
        selected_files = self.files_list.get(0, END)
        if not selected_files:
            print("No files selected.")
            return False
        for file_path in selected_files:
            self.viewer.print("Cracking file: " + file_path)
            self.openDmg(file_path, self.out_path)
        self.files_list.delete(0, END)


Main().root.mainloop()
