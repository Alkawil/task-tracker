import json
import os
import argparse
from datetime import datetime

FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(description):
    tasks = load_tasks()
    task_id = len(tasks) + 1
    task= {
        "id": task_id,
        "description" : description,
        "status" : "todo",
        "createdAt" : datetime.now().isoformat(),
        "updatedAt" : datetime.now().isoformat()
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added successfully (ID:{task_id})")


def update_task(task_id,new_description):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] =  new_description
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} upated successfully.")
            return 
    print(f'Task with ID {task_id} not found')


def delete_task(task_id):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print(f"Task {task_id} deleted successfully")
            return 
    print(f'Task with ID {task_id} not found')

def mark_progress(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "in-progress"
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} marked as in-progress.")
            return
    print(f"Task with ID {task_id} not found.")


def mark_done(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "done"
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} marked as done.")
            return
    print(f"Task with ID {task_id} not found.")

def list_tasks():
    tasks = load_tasks()
    for task in tasks:
        print(f'ID: {task["id"]}, Description: {task["description"]}, Status: {task["status"]}')


def list_tasks_by_status(status):
    tasks = load_tasks()
    filtered_tasks = []
    for task in tasks:
        if task["status"] == status:
            filtered_tasks.append(task)
    
    if not filtered_tasks:
        print(f"Task not found.")
    
    for task in filtered_tasks:
        print(f'ID: {task["id"]}, Description: {task["description"]}, Status: {task["status"]}')



def parse_arguments():
    parser = argparse.ArgumentParser(prog="task-cli",description= "Task Tracker CLI")
    sub_parser = parser.add_subparsers(dest="command")


    add_parser = sub_parser.add_parser("add",help="Add a new task")
    add_parser.add_argument("description",type=str,help="Task description")

    update_parser = sub_parser.add_parser("update",help="Update a task")
    update_parser.add_argument("id",type=int,help="Task id")
    update_parser.add_argument("description",type=str,help="New task description")

    delete_parser = sub_parser.add_parser("delete",help="Delete a task")
    delete_parser.add_argument("id",type=int,help="Task id")

    mark_progress_parser = sub_parser.add_parser("mark-in-progress",help="Marking a task in-progress")
    mark_progress_parser.add_argument("id",type=int,help="Task id")

    mark_done_parser = sub_parser.add_parser("mark-done",help="Marking a task done")
    mark_done_parser.add_argument("id",type=int,help="Task id")

    list_parser = sub_parser.add_parser("list", help="List all tasks or list tasks by status")
    list_parser.add_argument(
        "status", 
        nargs="?",  # Make status optional
        type=str, 
        choices=["todo", "in-progress", "done"], 
        help="Filter tasks by status")


    return parser.parse_args()


if __name__== "__main__":
    args = parse_arguments()

    if args.command == "add":
        add_task(args.description)
    
    elif args.command == "update":
        update_task(args.id,args.description)
    
    elif args.command == "delete":
        delete_task(args.id)

    elif args.command == "mark-in-progress":
        mark_progress(args.id)

    elif args.command == "mark-done":
        mark_done(args.id)

    # elif args.command == "list":
    #     list_tasks()
    
    elif args.command == "list":
        if args.status:
            list_tasks_by_status(args.status)
        else:
            list_tasks()