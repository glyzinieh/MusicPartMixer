import tkinter as tk

from ..models import Part


class EditFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, padx=10, pady=10)
        self.master.title("パート編集")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.id_frame = tk.Frame(self)
        self.id_frame.pack()
        self.id_label = tk.Label(self.id_frame, text="ID")
        self.id_label.pack(side="left")
        self.id_entry = tk.Entry(self.id_frame)
        self.id_entry.pack(side="left")

        self.name_frame = tk.Frame(self)
        self.name_frame.pack()
        self.name_label = tk.Label(self.name_frame, text="名前")
        self.name_label.pack(side="left")
        self.name_entry = tk.Entry(self.name_frame)
        self.name_entry.pack(side="left")

        self.file_name_frame = tk.Frame(self)
        self.file_name_frame.pack()
        self.file_name_label = tk.Label(self.file_name_frame, text="ファイル名")
        self.file_name_label.pack(side="left")
        self.file_name_entry = tk.Entry(self.file_name_frame)
        self.file_name_entry.pack(side="left")
        self.file_name_button = tk.Button(self.file_name_frame, text="参照")
        self.file_name_button.pack(side="left")

        self.action_frame = tk.Frame(self)
        self.action_frame.pack()

        self.update_button = tk.Button(self.action_frame, text="更新")
        self.update_button.pack(side="left")

        self.delete_button = tk.Button(self.action_frame, text="削除")
        self.delete_button.pack(side="left")
