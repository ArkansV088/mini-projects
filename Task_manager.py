#simple task manager
#import datetime

Tasks = ["eat", "sleep", "drink", "code"]

def create_task():
    New_Task = input("Add new task: ")
    if  New_Task not in Tasks:
        Tasks.append(New_Task)
        return view_tasks()
    else:
        print("Task already exists!")
        view_tasks()
        return select_option(option)

def view_tasks():
    if Tasks == None:
        return print(f"No tasks at the moment")
    else:
        for index, task in enumerate(Tasks, start=1):
            print(f"{index}: {task}")

def delete_task():
    if Tasks == None:
        return print("No tasks to delete")
    else:
        view_tasks()
        selection = int(input("Select task to delete by number: "))
        print(f"deleting; {Tasks[selection-1]}")
        Tasks.pop(selection-1)
        return view_tasks()

def show_menu():
    return print('''
___MENU___
1. Create task
2. View tasks
3. Delete task
4. Exit
''')
def select_option(option):
    if option == 1:
        create_task()
    
    elif option == 2:
        view_tasks()

    elif option == 3:
        delete_task()

    elif option == 4:
        global running_program
        running_program = False
        return print("Program Terminated")

    else:
        return print("Try again")

print('''


------------------------------------------------------TASK MANAGER-------------------------------------------------------------


''')
running_program = True

while running_program:
    show_menu()
    option = int(input("Select option number: "))
    select_option(option)

