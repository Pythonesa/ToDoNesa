from tkinter import simpledialog, messagebox, ttk
import tkinter as tk
from datetime import datetime
from tkcalendar import DateEntry

class TaskDialog(simpledialog.Dialog):
    def body(self, parent):
        ttk.Label(parent, text="Tarea:").grid(column=0, row=0, sticky="w")
        ttk.Label(parent, text="Descripción:").grid(column=0, row=1, sticky="w")
        ttk.Label(parent, text="Fecha de creación:").grid(column=0, row=2, sticky="w")
        ttk.Label(parent, text="Fecha límite:").grid(column=0, row=3, sticky="w")
        
        self.e1 = ttk.Entry(parent)
        self.e2 = ttk.Entry(parent)
        self.e3 = ttk.Entry(parent)
        self.e4 = DateEntry(parent, date_pattern="dd/mm/Y")
        
        self.e1.grid(column=1, row=0, sticky="ew")
        self.e2.grid(column=1, row=1, sticky="ew")
        self.e3.grid(column=1, row=2, sticky="ew")
        self.e4.grid(column=1, row=3, sticky="ew")
        
        self.e3.insert(0, datetime.today().strftime("%d/%m/%Y"))
        
        return self.e1
    def apply(self):
        task_name = self.e1.get()
        task_description = self.e2.get()
        task_creation_date = self.e3.get()
        task_due_date = self.e4.get() or None
        
        self.result = (task_name, task_description, task_creation_date, task_due_date)