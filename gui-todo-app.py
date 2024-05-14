from tkinter import *
from tkinter import messagebox

tasks = []

task_num_count = 1

root = Tk()

root.title("GUI Todo List App")

root.geometry("600x500")

Label(root, fg="red", text="Welcome To GUI Todo List App!", font=("Arial", 25)).pack()

blank_label = Label(root, text="").pack()


def task():

    global task_num_count

    def empty_field():

        if task_entry.get() == "":

            messagebox.showinfo("Enter in the contents of the task")

            return 0
        
        return 1

    val = empty_field()

    if val == 0:

        return

    contents = f"{task_entry.get()}\n"

    tasks.append(contents)

    task_area.insert("end -1 chars", f"{str(task_num_count)}. {contents}")

    task_num_count += 1

    task_entry.delete(0, END)

    task_entry.insert(0, "Enter in the task contents")


task_entry = Entry(root, width=100, borderwidth=5)

task_entry.pack()

task_entry.insert(0, "Enter in the task contents")

task_enter = Button(root, text="Enter", command=task).pack()

blank_label2 = Label(root, text="").pack()

task_area = Text(root, width=50, height=15)

task_area.pack()

blank_label3 = Label(root, text="").pack()


def delete_task():

    global task_num_count

    if len(tasks) == 0:

        messagebox.showerror("No tasks available to clear!")

        return

    num = task_num_entry.get(1.0, END)

    if num == "\n":

        messagebox.showerror("Input not valid!")

    else:

        task_num = int(num)
    
    tasks.pop(task_num - 1)

    task_num_count -= 1

    task_area.delete(1.0, END)

    for i in range(len(tasks)):

        task_area.insert("end -1 chars", f"{str(i + 1)}. {tasks[i]}")


task_num_label = Label(root, text="Enter A Task Number Below To Delete:").pack()

task_num_entry = Text(root, width=3, height=1)

task_num_entry.pack()

task_delete = Button(root, text="Delete Task", command=delete_task)

task_delete.pack()

root.mainloop()