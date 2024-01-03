tasks = []

def create_task(title, description, priority):
    tasks.append({
        'title': title,
        'description': description,
        'priority': priority,
        'status': 'In Progress'
    })

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
        task_index = int(input("Enter task index to mark as finished: "))
        mark_task_as_finished(task_index)
    elif command == 'cp':
        task_index = int(input("Enter task index to change priority: "))
        new_priority = input("Enter new priority: ")
        change_priority(task_index, new_priority)
    elif command == 'exit':
        break
    elif command == 'save':
        print(tasks)
        filename = input("Enter save file name: ")
        file = open(filename+".txt", "w+")
        content = str(tasks)
        file.write(content)
        file.close()
    elif command == 'help':
        print("View README for detailled usage instructions!")
    else:
        print("Invalid command")
