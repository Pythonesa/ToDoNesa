import tkinter as tk
from tkinter import ttk, simpledialog, messagebox

task_list = None

def main():
    global task_list
    
    #Main window:
    root = tk.Tk()
    root.title("ToDoNesa")
    root.geometry("800x600")
    main_frame = ttk.Frame(root)
    main_frame.pack(pady=20, padx=20, fill="both", expand=True)
    main_frame.grid_rowconfigure(0, weight=1)  # Permite que task_frame se expanda
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
    add_task_button = ttk.Button(buttons_frame, text="Añadir tarea", command=add_task)
    add_task_button.pack(side=tk.LEFT, padx=20)
    #Edit task:
    edit_task_button = ttk.Button(buttons_frame, text="Editar tarea", command=edit_task)
    edit_task_button.pack(side=tk.LEFT, padx=20)
    #Delete task:
    delete_task_button = ttk.Button(buttons_frame, text="Eliminar tarea", command=delete_task)
    delete_task_button.pack(side=tk.LEFT, padx=20)
    
    #Main loop:
    root.mainloop()


def add_task():
    task = simpledialog.askstring("Nueva Tarea", "¿Qué tarea quieres agregar?")
    if task:
        task_list.insert(tk.END, task)
    else:
        messagebox.showinfo("Error", "La tarea no puede estar vacía!")

def edit_task():
    try:
        selected_task_index = task_list.curselection()[0]
        current_task = task_list.get(selected_task_index)
        new_task = simpledialog.askstring("Editar Tarea", "Edita la tarea:")
    
        if new_task:
            task_list.delete(selected_task_index)
            task_list.insert(selected_task_index, new_task)
        else:
            messagebox.showinfo("Error", "La tarea no puede quedar vacía!")
    except IndexError:
        messagebox.showinfo("Error", "No hay ninguna tarea seleccionada!")

def delete_task():
    try:
        selected_task_index = task_list.curselection()[0]
        task_list.delete(selected_task_index)
    except IndexError:
        messagebox.showinfo("Error", "No hay ninguna tarea seleccionada!")


if __name__ == "__main__":
    main()