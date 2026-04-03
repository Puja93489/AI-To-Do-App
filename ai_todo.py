import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("AI To-Do App")
root.geometry("400x550")

root.attributes("-fullscreen", True)

def toggle_fullscreen(event=None):
    current = root.attributes("-fullscreen")
    root.attributes("-fullscreen", not current)

root.bind("<Escape>", lambda e: root.attributes("-fullscreen", False))

root.bind("<F11>", toggle_fullscreen)

def create_gradient(canvas, width, height, color1, color2):
    r1, g1, b1 = root.winfo_rgb(color1)
    r2, g2, b2 = root.winfo_rgb(color2)

    r_ratio = (r2 - r1) / height
    g_ratio = (g2 - g1) / height
    b_ratio = (b2 - b1) / height

    for i in range(height):
        nr = int(r1 + (r_ratio * i))
        ng = int(g1 + (g_ratio * i))
        nb = int(b1 + (b_ratio * i))

        color = f'#{nr//256:02x}{ng//256:02x}{nb//256:02x}'
        canvas.create_line(0, i, width, i, fill=color)

canvas = tk.Canvas(root, highlightthickness=0)
canvas.pack(fill="both", expand=True)

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
create_gradient(canvas, width, height, "#ffc0cb", "#ffffff")


welcome_label = tk.Label(root, text="Welcome to AI To-Do List",
                         font=("Arial", 22), bg="#ffffff")

enter_button = tk.Button(root, text="Click Here",
                         bg="purple", fg="white", command=lambda: open_todo())

canvas.create_window(width//2, height//3, window=welcome_label)
canvas.create_window(width//2, height//3 + 80, window=enter_button)


title_label = tk.Label(root, text="AI To-Do List",
                       font=("Arial", 20), bg="#ffffff")

task_entry = tk.Entry(root, width=30, font=("Arial", 12))

task_listbox = tk.Listbox(root, width=40, height=15, font=("Arial", 11))


def suggest_priority(task):
    task = task.lower()
    if "exam" in task or "urgent" in task or "project" in task:
        return "High Priority 🔴"
    elif "study" in task or "assignment" in task:
        return "Medium Priority 🟠"
    else:
        return "Low Priority 🟢"

def add_task():
    task = task_entry.get()
    if task == "":
        messagebox.showwarning("Warning", "Please enter a task!")
        return

    priority = suggest_priority(task)
    task_listbox.insert(tk.END, f"{task} ({priority})")

    index = task_listbox.size() - 1

    if "High" in priority:
        task_listbox.itemconfig(index, {'fg': 'red'})
    elif "Medium" in priority:
        task_listbox.itemconfig(index, {'fg': 'orange'})
    else:
        task_listbox.itemconfig(index, {'fg': 'green'})

    task_entry.delete(0, tk.END)

def delete_task():
    try:
        selected = task_listbox.curselection()[0]
        task_listbox.delete(selected)
    except:
        messagebox.showwarning("Warning", "Select a task to delete!")

add_btn = tk.Button(root, text="Add Task",
                    bg="purple", fg="white", command=add_task)

delete_btn = tk.Button(root, text="Delete Task",
                       bg="purple", fg="white", command=delete_task)

def open_todo():
    canvas.delete("all")
    create_gradient(canvas, width, height, "#ffc0cb", "#ffffff")

    canvas.create_window(width//2, 80, window=title_label)
    canvas.create_window(width//2, 140, window=task_entry)
    canvas.create_window(width//2, 190, window=add_btn)
    canvas.create_window(width//2, 240, window=delete_btn)
    canvas.create_window(width//2, height//2 + 50, window=task_listbox)



root.mainloop()