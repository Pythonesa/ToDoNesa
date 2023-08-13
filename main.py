import tkinter as tk
from tkinter import ttk, simpledialog, messagebox

task_list = None

def main():
    #Main window:
    root = tk.Tk()
    root.title("ToDoNesa")
    root.geometry("800x600")
    
    #List of tasks:
    global task_list
    task_frame = ttk.Frame(root)
    task_frame.pack(pady=20, padx=20, fill="both", expand=True)
    scrollbar = ttk.Scrollbar(task_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
    task_list = tk.Listbox(task_frame, yscrollcommand=scrollbar.set, selectmode=tk.SINGLE)
    task_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.config(command=task_list.yview)
    
    #Add task:
    add_task_button = ttk.Button(root, text="Añadir tarea", command=add_task)
    add_task_button.pack(pady=20)
    
    #Main loop:
    root.mainloop()


def add_task():
    task = simpledialog.askstring("Nueva Tarea", "¿Qué tarea quieres agregar?")
    if task:
        task_list.insert(tk.END, task)
    else:
        messagebox.showinfo("Error", "La tarea no puede estar vacía")


if __name__ == "__main__":
    main()