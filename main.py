import calendar
from colorama import init, Fore, Style, Back
from datetime import *
from dateutil.tz import *
import os
from random import randint
import rich
from rich.highlighter import Highlighter
from rich.tree import Tree
import time
import re

class RainbowHighlighter(Highlighter):
    def highlight(self, text):
        for index in range(len(text)):
            text.stylize(f"color({randint(16, 255)})", index, index + 1)
rainbow = RainbowHighlighter()
# rich.print(rainbow("I must not fear. Fear is the mind-killer."))

tree = Tree("Task Tracker", guide_style="bright_blue")
tree.add("foo")
tree.add("bar")
# rich.print(tree)

# Rust is good for command line tools
# Automating sending reset sequences.
init(autoreset=True)
points = 0
# Fetch current time.
input_date = datetime.now(tzlocal())
print("Hello! The time is", input_date)
print("points: ", points)
curr_day = input_date.day
colored_day = '\033[92m' + str(curr_day) + '\033[0m'
orgcal = cal = calendar.month(input_date.year, input_date.month)
date_new  = input_date.day.__str__().rjust(2)
rday  = ('\\b' + date_new + '\\b').replace('\\b ', '\\s')
rdayc = "\033[7m" + date_new + "\033[0m"
reg = re.sub(rday,rdayc,cal)
print(reg)

# print(Fore.RED + 'some red text')
# print(Style.DIM + 'and in dim text')
# print(Style.NORMAL + 'and in dim text')
# print(Style.BRIGHT + 'and in dim text')

tasks = []
archive = []

def create_task(title, description, priority):
    tasks.append({
        'title': title,
        'description': description,
        'priority': priority,
        'status': 'In Progress',
        'date-created': str(input_date.month) + "-" + str(input_date.day) + "-" + str(input_date.year)
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
    if command[:2] == 'ct':
        if len(command) > 2:
            parts = command.split(" ")
            if len(parts) == 3:
                create_task(parts[1], None, parts[2])
            else:
                create_task(parts[1], parts[2], parts[3])
        else:
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
    elif command == "archive" or command == "a":
        task_index = int(input("Enter task index to remove: "))
        archive.append(tasks[task_index])
        tasks.pop(task_index)
        print(archive)
    elif command == 'print' or command == "p":
        print("points: ", points)
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
                        print(frame.center(os.get_terminal_size().columns), end='\r') # Carriage return
                        time.sleep(1) # Animation delay
        except KeyboardInterrupt:
            pass
        os.system("reset")
        with open(file_name, 'r') as file:
            frame = file.read()
            print(frame, end='\r')
        duration = new_time - first_time
        if duration < 60:
            print("Time elapsed: ", round(duration, 2), "seconds")
        else:
            print("Time elapsed: ", round(duration, 2)/60, "minutes")
        points += round((duration/10),2)
    elif command == "rank" or command == "r":
        rank = "study peasant"
        if points > 2:
            rank = "study squire"
        if points > 4:
            rank = "study knight"
        if points > 8:
            rank = "study baron"
        if points > 16:
            rank = "study viscount"
        if points > 32:
            rank = "study marquis"
        if points > 64:
            rank = 'study duke'
        if points > 128:
            rank = "study prince"
        if points > 256:
            rank = "study KING"
        print("Your current rank is:", rank)
    elif command == "reset_cal" or command == "rc":
        cal = orgcal
        reg = cal
        print(cal)
    elif command == "day" or command == "d":
        day = input("Enter day to highlight: ")
        if 0 < int(day) <= 31:
            date_new  = day.rjust(2)
            rday  = ('\\b' + date_new + '\\b').replace('\\b ', '\\s')
            rdayc = "\033[7m" + date_new + "\033[0m"
            print(re.sub(rday,rdayc,reg))
            reg = re.sub(rday,rdayc,reg)
        else:
            print("Invalid day!")
    elif command == 'exit' or command == 'e':
        break
    elif command == 'save' or command == 's': # save calendar and points too
        if len(tasks) == 0:
            print("No tasks have be created!")
        else:
            print(tasks)
            filename = input("Enter save file name: ")
            file = open(filename+".txt", "w+")
            content = str(tasks) + "|" + str(points)
            file.write(content)
            file.close()
    elif command == 'load' or command == 'l':
        name = input("Enter file to open (i.e. txt): ")
        file = open(name, "r")
        f = file.read()
        new = f.split("|")
        points = new[1]
        tasks = eval(new[0])
        # archive = list(set(archive + tasks))
        print(new)
        print(points)
    elif command == 'help' or command == 'h':
        print(""" 
        List of commands:
        ct - create task.
            positional arguments:
            title - title of task
            description (optional) - task details
            priority - rank indicating task urgency
            notes:
            There are two ways to use this command.
            Typing 'ct' will prompt for all 3 fields,
            alternatively one line is possible: 'ct cook 1'.
        ft - mark task as finished.
        cp - change priority of task.
        rc - reset calendar/remove highlights.
        r - check points ranking (magnitudes of 2)
        a - archive a task.
        p - print task list.
        f - focus mode.
            notes:
            CTRL+C to exit focus mode, gain points
            at a rate of 1 point per 10 seconds.
        d - highlight a specific day.
        e - exit.
        s - save current task list.
        l - load task list from text file, stores old task list in archive.
        h - open help manual.
        """)
        # rich.print(rainbow("View README for detailled usage instructions!"))
    else:
        print("Invalid command")
