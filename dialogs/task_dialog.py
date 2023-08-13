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
        ttk.Label(parent, text="Tarea:").grid(column=0, row=0, sticky="w")
        ttk.Label(parent, text="Descripción:").grid(column=0, row=1, sticky="w")
        ttk.Label(parent, text="Fecha de creación:").grid(column=0, row=2, sticky="w")
        ttk.Label(parent, text="Fecha límite:").grid(column=0, row=3, sticky="w")
        
        self.e1 = ttk.Entry(parent)
        self.e2 = ttk.Entry(parent)
        self.e3 = ttk.Entry(parent)
        self.e4 = DateEntry(parent, date_pattern="dd/mm/Y")
        self.e4.delete(0, 'end')
        
        
        self.e1.grid(column=1, row=0, sticky="ew")
        self.e2.grid(column=1, row=1, sticky="ew")
        self.e3.grid(column=1, row=2, sticky="ew")
        self.e4.grid(column=1, row=3, sticky="ew")
        
        self.due_date_var = tk.BooleanVar(value=bool(self.default_task_due_date))
        self.due_date_checkbox = ttk.Checkbutton(parent, text="Establecer fecha límite", variable=self.due_date_var, command=self.toggle_due_date)
        self.due_date_checkbox.grid(column=0, row=4, sticky="w")
        
        self.e1.insert(0, self.default_task_name)
        self.e2.insert(0, self.default_task_description)
        self.e3.insert(0, self.default_task_creation_date or datetime.today().strftime("%d/%m/%Y"))
        self.e4.insert(0, self.default_task_due_date or "")
        
        # Si la fecha de vencimiento predeterminada no está establecida, oculta el widget DateEntry
        if not self.default_task_due_date:
            self.e4.grid_remove()
        
        return self.e1
    
    def toggle_due_date(self):
        if self.due_date_var.get():
            self.e4.grid()
        else:
            self.e4.grid_remove()
    
    def apply(self):
        task_name = self.e1.get()
        task_description = self.e2.get()
        task_creation_date = self.e3.get()
        task_due_date = self.e4.get() if self.due_date_var.get() else None
        
        self.result = (task_name, task_description, task_creation_date, task_due_date)
