import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, window):
        self.window=window
        self.window.title("To-Do List")
        self.listbox=tk.Listbox(self.window,width=30,height=10)
        self.listbox.grid(row=0, column=0, padx=10, pady=10)
        self.add_button=tk.Button(self.window,text="Add",width=10,command=self.add_item)
        self.add_button.grid(row=1,column=0,padx=10,pady=10)
        self.delete_button=tk.Button(self.window,text="Delete",width=10,command=self.delete_item)
        self.delete_button.grid(row=2,column=0,padx=10,pady=10)
        self.update_button=tk.Button(self.window,text="Update",width=10,command=self.update_item)
        self.update_button.grid(row=3,column=0,padx=10,pady=10)
        self.entry=tk.Entry(self.window,width=30)
        self.entry.grid(row=0,column=1,padx=10,pady=10)
        self.label=tk.Label(self.window,text="Select an item to update:")
        self.label.grid(row=1,column=1,padx=10,pady=10)
      
    def add_item(self):
        if self.entry.get()!= "":
            self.listbox.insert(tk.END,self.entry.get())
            self.entry.delete(0,tk.END)
        else:
            messagebox.showwarning("Error","Please enter a task")
    def delete_item(self):
        try:
            self.listbox.delete(tk.ANCHOR)
        except tk.TclError:
            messagebox.showwarning("Error","Please select a task to delete")
    def update_item(self):
        try:
            selected_item=self.listbox.get(tk.ACTIVE)
            updated_item=self.entry.get()
            if updated_item!="":
                self.listbox.delete(tk.ACTIVE)
                self.listbox.insert(tk.END,updated_item)
                self.entry.delete(0,tk.END)
            else:
                messagebox.showwarning("Error","Please enter an updated task")
        except tk.TclError:
            messagebox.showwarning("Error","Please select a task to update")
root=tk.Tk()
todo=ToDoListApp(root)
root.mainloop()
