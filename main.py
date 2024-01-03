from colorama import init, Fore, Style, Back

# Automating sending reset sequences
init(autoreset=True)

print(Fore.RED + 'some red text')
print('automatically back to default color again')
print(Style.DIM + 'and in dim text')
print(Style.NORMAL + 'and in dim text')
print(Style.BRIGHT + 'and in dim text')

tasks = []

def create_task(title, description, priority):
    tasks.append({
        'title': title,
        'description': description,
        'priority': priority,
        'status': 'In Progress'
    }) # create sub tasks w tree structure? Use colorama and argparse?

def mark_task_as_finished(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]['status'] = 'Finished'
    else:
        print("Task index out of range.")

def change_priority(task_index, new_priority):
    if 0 <= task_index < len(tasks):
        tasks[task_index]['priority'] = new_priority
    else:
        print("Task index out of range.")

while True:
    command = input("Enter command (ct, ft, cp): ")
    if command == 'ct':
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        priority = input("Enter task priority: ")
        create_task(title, description, priority)
    elif command == 'ft':
        if len(tasks) == 0:
            print("No tasks have be created!")
        else:
            task_index = int(input("Enter task index to mark as finished: "))
            mark_task_as_finished(task_index)
    elif command == 'cp':
        if len(tasks) == 0:
            print("No tasks have be created!")
        else:
            task_index = int(input("Enter task index to change priority: ")) # change 0 indexed to 1 indexed?
            new_priority = input("Enter new priority: ")
            change_priority(task_index, new_priority)
    elif command == 'print' or command == "p":
        if len(tasks) == 0:
            print("No tasks have be created!")
        else:
            print(tasks)
    elif command == "focus" or command == "f":
        print()
    elif command == 'exit' or command == 'e':
        break
    elif command == 'save' or command == 's':
        if len(tasks) == 0:
            print("No tasks have be created!")
        else:
            print(tasks)
            filename = input("Enter save file name: ")
            file = open(filename+".txt", "w+")
            content = str(tasks)
            file.write(content)
            file.close()
    elif command == 'help' or command == 'h':
        print("View README for detailled usage instructions!")
    else:
        print("Invalid command")
