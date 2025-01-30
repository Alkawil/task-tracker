# task-tracker

A simple command-line task tracker to manage tasks with descriptions, statuses, and timestamps. The tool allows you to add, update, delete, and mark tasks with different statuses like "todo", "in-progress", and "done".

## Features
- Add a new task with a description.
- Update the description of an existing task.
- Delete a task.
- Mark a task as "in-progress" or "done".
- List all tasks or filter tasks by their status.

## Requirements
- Python 3.x
- `tasks.json` file to store task data.

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/Alkawil/task-tracker.git
   cd task-tracker
## Run the following command to build and run the project:
   ```bash 
# To add a task
./task-tracker add "Buy groceries"

# To update a task
./task-tracker update 1 "Buy groceries and cook dinner"

# To delete a task
./task-tracker delete 1

# To mark a task as in progress/done/todo
./task-tracker mark-in-progress 1
./task-tracker mark-done 1
./task-tracker mark-todo 1

# To list all tasks
./task-tracker list
./task-tracker list done
./task-tracker list todo
./task-tracker list in-progress
