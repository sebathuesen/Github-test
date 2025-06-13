import tkinter as tk
from tkinter import messagebox
import todo

class TodoApp:
    def __init__(self, master):
        self.master = master
        master.title("To-Do List")
        self.frame = tk.Frame(master)
        self.frame.pack(padx=10, pady=10)

        self.entry = tk.Entry(self.frame, width=40)
        self.entry.pack(side=tk.TOP, fill=tk.X)
        self.entry.bind("<Return>", lambda event: self.add_task())

        self.add_button = tk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_button.pack(side=tk.TOP, pady=5)

        self.listbox = tk.Listbox(self.frame, width=50)
        self.listbox.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.listbox.bind("<Double-Button-1>", lambda event: self.mark_done())

        self.done_button = tk.Button(self.frame, text="Mark Done", command=self.mark_done)
        self.done_button.pack(side=tk.TOP, pady=5)

        self.load_tasks()

    def load_tasks(self):
        self.listbox.delete(0, tk.END)
        tasks = todo.load_tasks()
        for task in tasks:
            self.listbox.insert(tk.END, task)

    def add_task(self):
        task = self.entry.get().strip()
        if not task:
            messagebox.showinfo("No task", "Please enter a task.")
            return
        todo.add_task(task)
        self.entry.delete(0, tk.END)
        self.load_tasks()

    def mark_done(self):
        sel = self.listbox.curselection()
        if not sel:
            messagebox.showinfo("Select task", "Please select a task to mark as done.")
            return
        index = sel[0] + 1
        todo.mark_done(index)
        self.load_tasks()

if __name__ == '__main__':
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
