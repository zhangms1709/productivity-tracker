from colorama import init, Fore, Style, Back
from datetime import *
from dateutil.tz import *
import calendar
import os
import time

# pip3 install opencv-python
# Rust is good for command line tools
# Automating sending reset sequences.
init(autoreset=True)

# Fetch current time.
input_date = datetime.now(tzlocal())
print("Hello! The time is", input_date)
curr_day = input_date.day
colored_day = '\033[92m' + str(curr_day) + '\033[0m'
orgcal = cal = calendar.month(input_date.year, input_date.month).replace(str(curr_day), colored_day, 1)
print(cal)

# print(Fore.RED + 'some red text')
# print(Style.DIM + 'and in dim text')
# print(Style.NORMAL + 'and in dim text')
# print(Style.BRIGHT + 'and in dim text')

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
        file_names = ['ascii/t0.txt', 'ascii/t1.txt', 'ascii/t2.txt', 'ascii/t3.txt', 'ascii/t4.txt', 'ascii/t5.txt', 'ascii/t6.txt']
      
        first_time = time.time()
        last_time = first_time
        try:
            while True:   
                for file_name in file_names:
                    new_time = time.time()
                    last_time = new_time
                    with open(file_name, 'r') as file:
                        frame = file.read()
                        print(frame, end='\r') # Carriage return
                        time.sleep(1) # Animation delay
        except KeyboardInterrupt:
            pass
        os.system("reset")
        with open(file_names[-1], 'r') as file:
            frame = file.read()
            print(frame, end='\r')
        duration = new_time - first_time
        if duration < 60:
            print("Time elapsed: ", round(duration, 2), "seconds")
        else:
            print("Time elapsed: ", round(duration, 2)/60, "minutes")
    elif command == "reset_cal" or command == "rc":
        cal = orgcal
        print(cal)
    elif command == "day" or command == "d":
        day = input("Enter day to highlight: ")
        if 0 < day <= 31:
            colored_day = '\033[92m' + str(day) + '\033[0m'
            cal = cal.replace(str(day), colored_day, 1)
            print(cal)
        else:
            print("Invalid day!")
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
