# -*- coding: utf-8 -*-
"""
Created on Sun May  8 16:56:47 2022

@author: hp
"""
from tkinter import *
from tkinter import messagebox

tasks_list = []

counter = 1

# Function for checking input error when empty input is given in task field
def inputError() :
	
	if enterTaskField.get() == "" :
		
		messagebox.showerror("Input Error")
		
		return 0
	
	return 1

# Function for clearing the contents of task number text field
def clear_taskNumberField() :
	
	taskNumberField.delete(0.0, END)

# Function for clearing the contents of task entry field
def clear_taskField() :

	enterTaskField.delete(0, END)
	
# Function for inserting the contents from the task entry field to the text area
def insertTask():

	global counter
	
	value = inputError()
	if value == 0 :
		return

	content = enterTaskField.get() + "\n"

	tasks_list.append(content)

	# insert content of task entry field to the text area add task one by one in below one by one
	TextArea.insert('end -1 chars', "[ " + str(counter) + " ] " + content)
	counter += 1

	clear_taskField()

# function for deleting the specified task
def delete() :
	
	global counter
	
	if len(tasks_list) == 0 :
		messagebox.showerror("No task")
		return

	# get the task number, which is required to delete
	number = taskNumberField.get(1.0, END)

	if number == "\n" :
		messagebox.showerror("input error")
		return
	
	else :
		task_no = int(number)

	# function calling for deleting the content of task number field
	clear_taskNumberField()
	
	tasks_list.pop(task_no - 1)
	counter -= 1
	
	TextArea.delete(1.0, END)

	for i in range(len(tasks_list)) :
		TextArea.insert('end -1 chars', "[ " + str(i + 1) + " ] " + tasks_list[i])
	


if __name__ == "__main__" :

	gui = Tk()

	gui.configure(background = "light gray")

	gui.title("ToDo List")

	gui.geometry("280x330")

	enterTask = Label(gui, text = "Enter Your Task", bg = "light gray")

	enterTaskField = Entry(gui)

	Submit = Button(gui, text = "Submit", fg = "white", bg = "gray", command = insertTask)

	TextArea = Text(gui, height = 5, width = 25, font = "lucida 13")

	taskNumber = Label(gui, text = "Delete Task Number", bg = "light gray")
	taskNumberField = Text(gui, height = 1, width = 2, font = "lucida 13")

	delete = Button(gui, text = "Delete", fg = "white", bg = "gray", command = delete)

	Exit = Button(gui, text = "Exit", fg = "Black", bg = "Red", command = exit)

	enterTask.grid(row = 0, column = 2)

	enterTaskField.grid(row = 1, column = 2, ipadx = 50)		
	Submit.grid(row = 2, column = 2)
		
	TextArea.grid(row = 3, column = 2, padx = 10, sticky = W)			
	taskNumber.grid(row = 4, column = 2, pady = 5)
	taskNumberField.grid(row = 5, column = 2)

	delete.grid(row = 6, column = 2, pady = 5)					
	Exit.grid(row = 7, column = 2)

	gui.mainloop()