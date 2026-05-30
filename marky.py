# MODULES USED
import json
import argparse
import os
import datetime
from tabulate import tabulate

# CHECKS WHETHER THE 'data.json' FILE ALREADY EXISTS? IF YES, THEN LOADS THE LIST OF DICTIONARIES,
# OTHERWISE CREATES AN EMPTY LIST
if os.path.exists('data.json'):
    with open('data.json','r') as file:
        try:
            tasks = json.load(file)
        except json.JSONDecodeError:
            tasks = []


# CREATES A PARSER TO INITIATE THE PROGRAM IN THE COMMAND-LINE
parser = argparse.ArgumentParser(
    prog='CLI-TASK-TRACKER',
)

# NOTE: WE USE SUBPARSERS INSTEAD OF STANDARD PARSERS TO CREATE MULTI-LEVEL, COMMAND-DRIVEN CLIS. EX: git commit
# SUBPARSERS LET YOU BREAK A SCRIPT INTO DISCRETE SUB-COMMANDS, GIVING EACH ITS OWN UNIQUE SET OF ARGUMENTS, REQUIRED FLAGS
# AND HELP MENUS

# COMMAND ARGUMENTS: add, delete, update, mark-in-progress, mark-done, list
subparsers = parser.add_subparsers(dest='command', required=True, help='All available commands')

parser_add = subparsers.add_parser('add', help='Creates a new task')
parser_add.add_argument('task', type=str)

parser_update = subparsers.add_parser('update', help='Updates an existing task')
parser_update.add_argument('id', type=int)
parser_update.add_argument('updated_task', type=str)

parser_delete = subparsers.add_parser('delete', help='Deletes a task')
parser_delete.add_argument('id', type=int)

parser_mark_in_progress = subparsers.add_parser('mark-in-progress', help='Marks the task as in-progress')
parser_mark_in_progress.add_argument('id', type=int)

parser_mark_done = subparsers.add_parser('mark-done', help='Marks the task as done')
parser_mark_done.add_argument('id', type=int)

parser_list = subparsers.add_parser('list', help="Lists all the tasks")
parser_list.add_argument('status', type=str, nargs='?',default=None)

args = parser.parse_args()

# THIS IF-ELSE STATEMENT CHECKS FOR THE LARGEST ID THAT ALREADY EXISTS IN 'data.json', AND ASSIGNS IT WHILE INCREMENTING BY 1
# IF ID DOES NOT EXIST, THEN ID = 1 (starting)
if tasks:
    id_int = max(task['id'] for task in tasks)+1
else:
    id_int = 1

# THE FOLLOWING IF-ELSE STATEMENTS CHECK FOR THE COMMAND ARGUMENT AND PERFORM ACTIONS
if args.command == 'add':
    task = {
        'id': id_int,
        'description': args.task,
        'status': 'todo',
        'createdAt': f"{datetime.datetime.now()}",
    }
    tasks.append(task)
    print(f"Added {args.task} with ID: {id_int}, successfully....")

elif args.command == 'delete':
    tasks = [task for task in tasks if task.get('id') != args.id]
    print(f"Deleted task with ID: {args.id}, successfully....")

elif args.command == 'update':
    for task in tasks:
        if task['id'] == args.id:
            task['description'] = args.updated_task
            task['updatedAt'] = f"{datetime.datetime.now()}"
    print(f"Updated task with ID: {args.id} to {args.updated_task}, successfully....")

elif args.command == 'mark-in-progress':
    for task in tasks:
        if task['id'] == args.id:
            task['status'] = 'in-progress'
    print(f"Marked task with ID: {args.id} as in-progress, successfully....")

elif args.command == 'mark-done':
    for task in tasks:
        if task['id'] == args.id:
            task['status'] = 'done'
    print(f"Marked task with ID: {args.id} as done, successfully....")

elif args.command == 'list':
    if args.status == 'todo':
        todo_tasks = []
        for task in tasks:
            if task['status'] == 'todo':
                todo_tasks.append(task)
        print(tabulate(todo_tasks, headers="keys", tablefmt="grid"))

    elif args.status == 'done':
        done_tasks = []
        for task in tasks:
            if task['status'] == 'done':
                done_tasks.append(task)
        print(tabulate(done_tasks, headers="keys", tablefmt="grid"))

    elif args.status == "in-progress":
        in_progress_tasks = []
        for task in tasks:
            if task['status'] == "in-progress":
                in_progress_tasks.append(task)
        print(tabulate(in_progress_tasks, headers="keys", tablefmt="grid"))

    else:
       print(tabulate(tasks, headers="keys", tablefmt="grid"))


# WRITES THE LIST OF DICTIONARIES INTO THE FILE 'data.json'
with open('data.json', 'w') as f:
    json.dump(tasks, f, indent=4)