import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
from dialogs.task_dialog import TaskDialog

task_list = None
tasks = {}

def main():
    global tree
    
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
    tree = ttk.Treeview(task_frame, columns=('Priority', 'Task'), show='headings')
    tree.heading('Priority', text='Prioridad')
    tree.column('Priority', width=100, stretch=tk.NO)
    tree.heading('Task', text='Tarea')
    tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar = ttk.Scrollbar(task_frame, command=tree.yview)
    tree.config(yscrollcommand=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
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
        task_name, task_status, task_priority, task_description, task_creation_date, task_due_date, task_completion_date = dialog.result
        if task_name:
            tree.insert("", "end", text=f'{task_priority} - {task_name}', values=(task_priority, task_name))
            tasks[task_name] = {
                "status": task_status,
                "priority": task_priority,
                "description": task_description,
                "creation_date": task_creation_date,
                "due_date": task_due_date,
                "completion_date": task_completion_date
            }
        else:
            messagebox.showinfo("Error", "El nombre de la tarea no puede estar vacío!")

def edit_task(parent):
    try:
        selected_task = tree.selection()
        if not selected_task:
            messagebox.showinfo("Error", "No hay ninguna tarea seleccionada!")
            return
        
        task_priority, task_name = tree.item(selected_task, "values")
        task_data = tasks[task_name]
        task_status = task_data['status']
        task_description = task_data['description']
        task_creation_date = task_data['creation_date']
        task_due_date = task_data['due_date']
        task_completion_date = task_data['completion_date']
        
        dialog = TaskDialog(parent, "Editar tarea", task_name, task_status, task_priority, task_description, task_creation_date, task_due_date, task_completion_date)
        
        if dialog.result:
            updated_task_name, updated_task_status, updated_task_priority, updated_task_description, updated_task_creation_date, updated_task_due_date, updated_task_completion_date = dialog.result
            if updated_task_name != task_name:
                del tasks[task_name]
            tasks[updated_task_name] = {
                'status': updated_task_status,
                'priority': updated_task_priority,
                'description': updated_task_description,
                'creation_date': task_creation_date,
                'due_date': updated_task_due_date,
                'completion_date': updated_task_completion_date
            }
            
            tree.delete(selected_task)
            tree.insert("", "end", values=(updated_task_priority, updated_task_name))
            
    except KeyError:
        messagebox.showerror("Error", "La tarea seleccionada no fue encontrada!")
        

def delete_task():
    try:
        selected_task = tree.selection()
        if not selected_task:
            messagebox.showinfo("Error", "No hay ninguna tarea seleccionada!")
            return
        task_priority, task_name = tree.item(selected_task, "values")
        confirm = messagebox.askyesno("Confirmar", f"¿Estás seguro de que vas a eliminar la tarea '{task_name}'?")
        if confirm:
            del tasks[task_name]
            tree.delete(selected_task)
    except KeyError:
        messagebox.showerror("Error", "La tarea seleccionada no fue encontrada!")


if __name__ == "__main__":
    main()