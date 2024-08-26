import json
from get_date import get_date


class Task:
    def __init__(self, id, description, status=None, created_at=None, updated_at=None) -> None:
        self.id = id
        self.description = description
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at
        self.file_path = "./data/task.json"
    
    def create_task(self):
        # Load the existing task list
        task_list = self.get_tasks()

        # Create a new task dictionary
        self.task = {
            "Id": self.id,
            "description": self.description,
            "status": self.status,
            "created_at": get_date(),
            "updated_at": self.updated_at
        }
        
        return self.task
      
    def get_tasks(self) -> list:
        try:
            # Reading task json file and get all the tasks into a list
            with open(self.file_path, "r") as file:
                task_list = json.load(file)
                task_list = task_list["Task_List"]

        except FileNotFoundError:
            print("No task file found at data/task.json. Please create the file first.")
            raise SystemExit

        except json.JSONDecodeError:
            print("Error decoding JSON. Please check the file format.")
            raise SystemExit
                
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            raise SystemExit
        
        return task_list
    
    def list_task(self, arg=None):
        '''
        List tasks based on the provided argument.
        If no argument is provided, list all tasks.
        Arguments can be:
            - 'done' to list tasks marked as done.
            - 'todo' to list tasks marked as todo.
            - 'in-progress' to list tasks in progress.
        '''

        task_list = self.get_tasks()
        if not task_list:
            print("No task to Display")
            raise SystemExit
        
        try:
            if len(task_list) > 0:
                if arg is None:
                    for task in task_list:
                        print(f'''----------Task ID: {task["Id"]}----------
Task: {task["description"]}
Status: {task["status"]}
Created At: {task["created_at"]}
Updated At: {task["updated_at"]}
------------------------------''')

                elif arg == "done":
                    done_task = [task for task in task_list if task["status"] == "done"]
                    if done_task:
                        for task in done_task:
                            print(f'''----------Task ID: {task["Id"]}----------
Task: {task["description"]}
Status: {task["status"]}
Created At: {task["created_at"]}
Updated At: {task["updated_at"]}
------------------------------''')
                    else:
                        print("No task to Display")

                elif arg == "todo":
                    todo_task = [task for task in task_list if task["status"] == "todo"]
                    if todo_task:
                        for task in todo_task:
                            print(f'''----------Task ID: {task["Id"]}----------
Task: {task["description"]}
Status: {task["status"]}
Created At: {task["created_at"]}
Updated At: {task["updated_at"]}
------------------------------''')
                    else:
                        print("No task to Display")

                elif arg == "in-progress":
                    progress_task = [task for task in task_list if task["status"] == "in-progress"]
                    if progress_task:
                        for task in progress_task:
                            print(f'''----------Task ID: {task["Id"]}----------
Task: {task["description"]}
Status: {task["status"]}
Created At: {task["created_at"]}
Updated At: {task["updated_at"]}
------------------------------''')
                    else:
                        print("No tasks marked as In-Progress.")

                else:
                    print("Invalid argument. Please enter a valid argument ('done', 'todo', 'in-progress').")

        except IndexError:
            print("Error: Index out of range while accessing tasks.")
            raise SystemExit

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            raise SystemExit
