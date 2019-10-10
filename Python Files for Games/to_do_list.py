import tkinter  # Used to create GUI elements in python
import random
import tkinter.messagebox  # Used for displaying messages in tkinter module

# Create root window
root = tkinter.Tk()

# Create root window background color
root.configure(bg="white")

# Change the title
root.title("My Super to do list")

# Change the window size
root.geometry("410x310")  # Note to use "x" instead of "*" for multiplication (Its col*row)

# Create an empty list
tasks = []

# For testing purposes use a default list
tasks = ["Call mom", "Buy a guitar", "Eat sushi"]


# Create functions

def update_listbox():
    # Clear the current list
    clear_listbox()  # It will clear the list before adding the items
    # Populate the listbox
    for task in tasks:
        lb_tasks.insert("end", task)  # It will add the task at the end of the list

def clear_listbox():
    lb_tasks.delete(0, "end")  # It will delete all the tasks starting from 0 till the "end"

def add_task():
    # Get the task to add
    task = txt_input.get()  # It will get anything that is there in "txt_input" and store it in "task"
    # pass # Creates an empty function

    # Make sure the task is not empty
    if task != "":

        #Append to the list
        tasks.append(task)  # This will take the value stored in "task" and append it to the "tasks"

        # Update the listbox
        update_listbox()

    else:
        tkinter.messagebox.showwarning("Warning", "You need to enter a task")
        # lbl_display["text"] = "Please enter a task" (Use this to display message in lbl_display)
    txt_input.delete(0, "end")  # This will delete the input field after assigning the input

def del_all():
    confirmed = tkinter.messagebox.askyesno("Please Confirm", "Do you really want to delete")  # It returns a boolean value
    if confirmed == True:  # It runs the loop only when the user clicks on "yes"
        # We are actually deleting the elements from the list and then updating it on the screen
        # Since we are changing the list, it needs to be global
        global tasks
        # Clear the tasks list
        tasks = []
        # Update the list box
        update_listbox()

def del_one():
    # Get the text of the currently selected item
    task = lb_tasks.get("active")  # It stores the currently selected item in the task

    # Confirm it is in the list
    if task in tasks:
        tasks.remove(task)  # It removes the "task" from the list of "tasks"

    # Update the listbox
    update_listbox()

def sort_asc():
    # To sort a list
    tasks.sort()
    # Update the listbox
    update_listbox()

def sort_desc():
    # Sort the list
    tasks.sort()
    # Reverse the list
    tasks.reverse()
    # Update the listbox
    update_listbox()

def choose_random():
    # Choose a random task
    task = random.choice(tasks)
    # Update the display label
    lbl_display["text"] = task  # Whatever task is chosen by the random label is assigned to display function

def show_number_of_tasks():
    # Get the numbers of tasks
    number_of_tasks = len(tasks)  # Storing the length of tasks in number_of_tasks
    # Create and format the message
    msg = "Number of tasks: %s" %number_of_tasks  # It displays the number of tasks stored in the list
    # Display the message
    lbl_display["text"] = msg


lbl_title = tkinter.Label(root, text="To-Do-List", bg="white",width=15)  # Label is going to go into "root" window (used for creating labels.)
# lbl_title.pack()  # Pack gives you a list one after the other (Here you cannot decide where to place the label)
lbl_title.grid(row=0, column=0)  # Grid helps us make the labels as we want them to look inside the GUI

lbl_display = tkinter.Label(root, text="", bg="white")  # Label is going to go into "root" window
# lbl_display.pack()  # Pack gives you a list one after the other
lbl_display.grid(row=0, column=1)  # It displays the items of the list one at a time

txt_input = tkinter.Entry(root, width=15)  # It takes in an entry, parent is "root" and specify the width of characters
# txt_input.pack()
txt_input.grid(row=1, column=1)

btn_add_task = tkinter.Button(root, text="Add task", fg="green", bg="white", width=11,command=add_task)  # For creating a button
# "fg" sets the value of text in button to green and "bg" sets the background color to white
# Here "command" assigns the button to a particular function and "text" adds the text to button
# btn_add_task.pack()
btn_add_task.grid(row=1, column=0)

btn_del_all = tkinter.Button(root, text="Delete All", fg="green", bg="white", width=11,command=del_all)  # For creating a button
# fg sets the value of text in button to green and bg sets the background color to white
# btn_del_all.pack()
btn_del_all.grid(row=2, column=0)

btn_del_one = tkinter.Button(root, text="Delete One", fg="green", bg="white", width=11,command=del_one)
# btn_del_one.pack()
btn_del_one.grid(row=3, column=0)

btn_sort_asc = tkinter.Button(root, text="Sort (ASC)", fg="green", bg="white", width=11,command=sort_asc)  # For creating a button
# btn_sort_asc.pack()
btn_sort_asc.grid(row=4, column=0)

btn_sort_desc = tkinter.Button(root, text="Sort (DESC)", fg="green", bg="white", width=11,command=sort_desc)  # For creating a button
# btn_sort_desc.pack()
btn_sort_desc.grid(row=5, column=0)

btn_choose_random = tkinter.Button(root, text="Choose Random" , fg="green", bg="white", width=11,command=choose_random)  # For creating a button
# btn_choose_random.pack()
btn_choose_random.grid(row=6, column=0)

btn_number_of_tasks = tkinter.Button(root, text="No. of Tasks", fg="green", bg="white",width=11, command=show_number_of_tasks)  # For creating a button
# btn_number_of_tasks.pack()
btn_number_of_tasks.grid(row=7, column=0)

btn_exit = tkinter.Button(root, text="Exit", fg="green", bg="white", width=11,command=exit)
# We don't need to create exit its built-in
# btn_exit.pack()
btn_exit.grid(row=8, column=0)

lb_tasks = tkinter.Listbox(root)  # For creating a list (passing root inside the listbox)
# lb_tasks.pack()  # The name of the list is lb_tasks
lb_tasks.grid(row=2, column=1, rowspan=7)  # It displays the list of items entered by the user
# Here the "rowspan" property helps the computer to understand the size of lb_tasks we want to set


# Start the main events loop
root.mainloop()