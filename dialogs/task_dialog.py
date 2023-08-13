from tkinter import simpledialog, messagebox, ttk
import tkinter as tk
from datetime import datetime
from tkcalendar import DateEntry

class TaskDialog(simpledialog.Dialog):
    def __init__(self, parent, title, task_name="", task_description="", task_creation_date="", task_due_date=""):
        self.default_task_name = task_name
        self.default_task_description = task_description
        self.default_task_creation_date = task_creation_date
        self.default_task_due_date = task_due_date
        super().__init__(parent, title)

    def body(self, parent):
        ttk.Label(parent, text="Tarea:").pack(anchor="w")
        self.e1 = ttk.Entry(parent)
        self.e1.pack(fill="both", padx=5, pady=2)
        
        ttk.Label(parent, text="Descripción:").pack(anchor="w")
        self.e2 = ttk.Entry(parent)
        self.e2.pack(fill="both", padx=5, pady=2)
        
        ttk.Label(parent, text="Fecha de creación:").pack(anchor="w")
        self.e3 = ttk.Entry(parent)
        self.e3.pack(fill="both", padx=5, pady=2)
        
        self.due_date_var = tk.BooleanVar(value=bool(self.default_task_due_date))
        self.due_date_checkbox = ttk.Checkbutton(parent, text="Establecer fecha límite", variable=self.due_date_var, command=self.toggle_due_date)
        self.due_date_checkbox.pack(anchor="w", padx=5, pady=2)

        if self.due_date_var.get():
            self.e4 = DateEntry(parent, date_pattern="dd/mm/Y")
            self.e4.pack(fill="both", padx=5, pady=2)
            self.e4.insert(0, self.default_task_due_date)
        else:
            self.e4 = None
        
        self.e1.insert(0, self.default_task_name)
        self.e2.insert(0, self.default_task_description)
        self.e3.insert(0, self.default_task_creation_date or datetime.today().strftime("%d/%m/%Y"))
        return self.e1

    def toggle_due_date(self):
        if self.due_date_var.get():
            if not hasattr(self, "e4") or self.e4 is None:
                self.e4 = DateEntry(self, date_pattern="dd/mm/Y")
                self.e4.pack(fill="both", padx=5, pady=2)
        else:
            if hasattr(self, "e4") and self.e4:
                self.e4.pack_forget()
                self.e4 = None

    def apply(self):
        task_name = self.e1.get()
        task_description = self.e2.get()
        task_creation_date = self.e3.get()
        task_due_date = self.e4.get() if self.due_date_var.get() else None
        self.result = (task_name, task_description, task_creation_date, task_due_date)
