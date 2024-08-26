# Importing necessary files
from create_file import create_file
from validator import separate_commands
from help import print_help
from task_manager import TaskManager
from task import Task
import os


# Initializing file path
file_path = "../data/task.json"


# Initializing nessasry instances
tm = TaskManager(file_path)
task = Task(None, None)


def file_validate(directory,file_path):

    # Ensure the 'data' directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)

    # check if the file exist
    if not os.path.exists(file_path):
        print(f"File not found at {file_path}. Creating a new file.")
        create_file(file_path)
        
def get_data():
    # Taking user inputs
    command = input("task-cli: ")

    # Check if a string is enclosed within quotes
    parse_commands = separate_commands(command)

    return parse_commands

def main():

    file_validate("../data", file_path)
    while True:
        # Initialize available commands
        command = None
        task_id = None
        arg = None
        
        parse_commands = get_data()
        
        if len(parse_commands) >= 3:
            command = parse_commands[0]
            task_id = parse_commands[1]
            arg = parse_commands[2]

        elif len(parse_commands) >= 2:
            command = parse_commands[0]
            arg = parse_commands[1]
            

        elif len(parse_commands) == 1:
            command = parse_commands[0]

        if command == "add":
            tm.add_task(arg)
        elif command == "update":
            if task_id is not None:
                try:
                    task_id = int(task_id)
                    tm.update_task(task_id, arg)
                except ValueError:
                    print("Invalid task ID format. Please provide a valid integer ID.")
                    continue  
            else:
                print("Task ID is required for updating a task.")
        
        elif command == "delete":
            if arg is not None:
                try:
                    task_id = int(arg)
                    tm.delete_task(arg)
                except ValueError:
                    print("Invalid task ID format. Please provide a valid integer ID.")
                    continue  
            else:
                print("Task ID is required for deleting a task.")
        
        elif command == "mark":
            if task_id is not None:
                try:
                    task_id = int(task_id)
                    tm.mark_task(task_id, arg)
                except ValueError:
                    print("Invalid task ID format. Please provide a valid integer ID.")

        elif command == "list":
            task.list_task(arg)

        elif command == "help":
            print_help()
        elif command == "quit":
            print("Exiting")
            break  
        else:
            print("Invalid Command")


if __name__ == "__main__":
    main()
