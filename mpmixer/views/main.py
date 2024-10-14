import tkinter as tk

from ..models import Part


class MainFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, padx=10, pady=10)
        self.master.title("Music Part Mixer")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.action_frame = tk.LabelFrame(self, text="操作", padx=5, pady=5)
        self.action_frame.pack()

        self.add_part_button = tk.Button(self.action_frame, text="パートを追加")
        self.add_part_button.pack(side="left")

        self.mix_button = tk.Button(self.action_frame, text="出力")
        self.mix_button.pack(side="left")

        self.parts_frame = tk.LabelFrame(self, text="パート一覧", padx=5, pady=5)
        self.parts_frame.pack()

    def update_parts(self, parts):
        for widget in self.parts_frame.winfo_children():
            widget.destroy()

        id_heading = tk.Label(self.parts_frame, text="ID")
        id_heading.grid(row=0, column=0)
        name_heading = tk.Label(self.parts_frame, text="名前")
        name_heading.grid(row=0, column=1)
        edit_heading = tk.Label(self.parts_frame, text="編集")
        edit_heading.grid(row=0, column=2)

        self.parts_list = list()

        for part in parts:
            self.parts_list.append(
                {
                    "id_entry": tk.Entry(self.parts_frame),
                    "name_entry": tk.Entry(self.parts_frame),
                    "edit_button": OpenEditButton(self.parts_frame, part),
                }
            )

            part_widgets = self.parts_list[-1]

            id_entry = part_widgets["id_entry"]
            id_entry.insert(0, part.id)
            id_entry.config(state="readonly")
            id_entry.grid(row=len(self.parts_list), column=0)
            name_entry = part_widgets["name_entry"]
            name_entry.insert(0, part.name)
            name_entry.config(state="readonly")
            name_entry.grid(row=len(self.parts_list), column=1)
            edit_button = part_widgets["edit_button"]
            edit_button.grid(row=len(self.parts_list), column=2)


class OpenEditButton(tk.Button):
    def __init__(self, master, part):
        super().__init__(master, text="編集")
        self.part = part
