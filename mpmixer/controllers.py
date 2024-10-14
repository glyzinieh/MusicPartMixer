import tkinter as tk
from tkinter import filedialog

from .models import Music, Part
from .views.edit import EditFrame
from .views.main import MainFrame, OpenEditButton


class MainController:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.part_list = Music()
        self.main_view = MainFrame(root)

        self.main_view.add_part_button.config(command=self.open_edit)
        self.main_view.mix_button.config(command=self.mix)

        self.update_view()

    def open_edit(self, part: Part = None):
        part = part if part is not None else self.part_list.create_part()

        edit_window = tk.Toplevel()
        EditController(edit_window, self, part)

    def mix(self):
        output = self.part_list.mix()
        filename = filedialog.asksaveasfilename()
        output.export(filename)

    def update_view(self):
        parts = self.part_list
        self.main_view.update_parts(parts)

        for widgets in self.main_view.parts_list:
            button: OpenEditButton = widgets["edit_button"]
            button.config(command=lambda part=button.part: self.open_edit(part))


class EditController:
    def __init__(self, root: tk.Toplevel, main_controller: MainController, part: Part):
        self.root = root
        self.main_controller = main_controller
        self.part = part
        self.edit_view = EditFrame(root)

        part_name = part.name if part.name is not None else ""
        part_file_name = part.file_name if part.file_name is not None else ""

        self.edit_view.id_entry.insert(0, self.part.id)
        # self.edit_view.id_entry.config(state="readonly")
        self.edit_view.name_entry.insert(0, part_name)
        self.edit_view.file_name_entry.insert(0, part_file_name)
        self.edit_view.update_button.config(command=self.update_part)
        self.edit_view.delete_button.config(command=self.delete_part)

        self.edit_view.file_name_button.config(command=self.select_file)

    def select_file(self):
        file_name = filedialog.askopenfilename()
        self.edit_view.file_name_entry.delete(0, tk.END)
        self.edit_view.file_name_entry.insert(0, file_name)

    def update_part(self):
        self.part.id = int(self.edit_view.id_entry.get())
        self.part.name = self.edit_view.name_entry.get()
        self.part.file_name = self.edit_view.file_name_entry.get()
        self.main_controller.part_list.update_part(self.part)
        self.main_controller.update_view()
        self.root.destroy()

    def delete_part(self):
        self.main_controller.part_list.delete_part(self.part.id)
        self.main_controller.update_view()
        self.root.destroy()
