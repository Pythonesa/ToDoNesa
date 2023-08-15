import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
from dialogs.task_dialog import TaskDialog

task_list = None
tasks = {}

def main():
    global task_list
    
    #Main window:
    root = tk.Tk()
    root.title("ToDoNesa")
    root.geometry("800x600")
    main_frame = ttk.Frame(root)
    main_frame.pack(pady=20, padx=20, fill="both", expand=True)
    main_frame.grid_rowconfigure(0, weight=1)
    main_frame.grid_columnconfigure(0, weight=1)

    #List of tasks:
    task_frame = ttk.Frame(main_frame)
    task_frame.grid(row=0, column=0, sticky="nsew")
    scrollbar = ttk.Scrollbar(task_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
    task_list = tk.Listbox(task_frame, yscrollcommand=scrollbar.set, selectmode=tk.SINGLE)
    task_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.config(command=task_list.yview)
    #Frame for buttons:
    buttons_frame = ttk.Frame(main_frame)
    buttons_frame.grid(row=1, column=0, pady=10, sticky="ew")
    
    #Add task:
    add_task_button = ttk.Button(buttons_frame, text="Añadir tarea", command=lambda:add_task(root))
    add_task_button.pack(side=tk.LEFT, padx=20)
    #Edit task:
    edit_task_button = ttk.Button(buttons_frame, text="Editar tarea", command=lambda:edit_task(root))
    edit_task_button.pack(side=tk.LEFT, padx=20)
    #Delete task:
    delete_task_button = ttk.Button(buttons_frame, text="Eliminar tarea", command=delete_task)
    delete_task_button.pack(side=tk.LEFT, padx=20)
    
    #Main loop:
    root.mainloop()


def add_task(parent):
    dialog = TaskDialog(parent, "Crear nueva tarea")
    if dialog.result:
        task_name, task_priority, task_description, task_creation_date, task_due_date = dialog.result
        if task_name:
            task_list.insert(tk.END, f"{task_priority} - {task_name}")
            tasks[task_name] = {
                "priority": task_priority,
                "description": task_description,
                "creation_date": task_creation_date,
                "due_date": task_due_date
            }
        else:
            messagebox.showinfo("Error", "El nombre de la tarea no puede estar vacío!")

def edit_task(parent):
    try:
        selected_task_index = task_list.curselection()
        if not selected_task_index:
            messagebox.showinfo("Error", "No hay ninguna tarea seleccionada!")
            return
        task_entry = task_list.get(selected_task_index[0])
        task_name = task_entry.split(" - ", 1)[1]
        task_data = tasks[task_name]  # <-- Aquí está el cambio
        task_priority = task_data['priority']
        task_description = task_data['description']
        task_creation_date = task_data['creation_date']
        task_due_date = task_data['due_date']
        dialog = TaskDialog(parent, "Editar tarea", task_name, task_priority, task_description, task_creation_date, task_due_date)
        if dialog.result:
            updated_task_name, updated_task_priority, updated_task_description, updated_task_creation_date, updated_task_due_date = dialog.result
            if updated_task_name != task_name:
                del tasks[task_name]
            tasks[updated_task_name] = {
                'priority': updated_task_priority,
                'description': updated_task_description,
                'creation_date': task_creation_date,
                'due_date': updated_task_due_date
            }
            task_list.delete(selected_task_index[0])
            task_list.insert(selected_task_index[0], f"{updated_task_priority} - {updated_task_name}")
    except KeyError:
        messagebox.showerror("Error", "La tarea seleccionada no fue encontrada!")
        

def delete_task():
    try:
        selected_task_index = task_list.curselection()
        if not selected_task_index:
            messagebox.showinfo("Error", "No hay ninguna tarea seleccionada!")
            return
        task_name = task_list.get(selected_task_index[0]).split(" - ", 1)[1]
        confirm = messagebox.askyesno("Confirmar", f"¿Estás seguro de que vas a eliminar la tarea '{task_name}'?")
        if confirm:
            del tasks[task_name]
            task_list.delete(selected_task_index[0])
    except KeyError:
        messagebox.showerror("Error", "La tarea seleccionada no fue encontrada!")


if __name__ == "__main__":
    main()