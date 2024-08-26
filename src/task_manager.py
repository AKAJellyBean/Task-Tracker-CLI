import json
from task import Task
from create_file import create_file
from get_date import get_date


class TaskManager:
    def __init__(self, file_path) -> None:
        self.tasks = []
        self.file_path = file_path

    def load_task(self) -> list:
        try:
            with open(self.file_path, "r") as file:
                data_file = json.load(file)
                self.tasks = data_file["Task_List"]

        except FileNotFoundError:
            print(f"File not found at {self.file_path}. Creating a new file.")
            create_file(self.file_path)

        except json.JSONDecodeError:
            print("Error decoding JSON. Please check the file format.")
            raise SystemExit
        
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            raise SystemExit

        return self.tasks
    
    def add_task(self, description):
        task_list = self.load_task()

        new_id = task_list[-1]["Id"] + 1 if task_list else 0

        task = Task(new_id, description)
        created_task = task.create_task()
        task_list.append(created_task)

        with open(self.file_path, "w") as file:
            data_file = {"Task_List": task_list}
            json.dump(data_file, file, indent=4)
            print(f"Task added successfully (ID: {new_id})")
        
        task_list.clear()

    def update_task(self, id, description):
        id = int(id)
        task_list = self.load_task()

        selected_task = None

        for task in task_list:
            if task["Id"] == id:
                selected_task = task
                break

        if selected_task:
            selected_task["description"] = description
            selected_task["updated_at"] = get_date()

            with open(self.file_path, "w") as file:
                data_file = {"Task_List": task_list}
                json.dump(data_file, file, indent=4)
                print(f"Task updated successfully (ID: {id})")

        else:
            print(f"Task with ID {id} not found.")
            raise SystemExit
        
        task_list.clear()

    def delete_task(self, id):
        id = int(id)
        task_list = self.load_task()

        task_index = None

        for index, task in enumerate(task_list):
            if task["Id"] == id:
                task_index = index
                break

        if task_index is not None:
            task_list.pop(task_index)

            with open(self.file_path, "w") as file:
                data_file = {"Task_List": task_list}
                json.dump(data_file, file, indent=4)
                print(f"Task deleted successfully (ID: {id})")

        else:
            print(f"Task with ID {id} not found.")
            raise SystemExit
        
        task_list.clear()

    def mark_task(self, id, mark):
        id = int(id)
        task_list = self.load_task()

        selected_task = None

        for task in task_list:
            if task["Id"] == id:
                selected_task = task
                break

        if selected_task:
            selected_task["status"] = mark
            selected_task["updated_at"] = get_date()

            with open(self.file_path, "w") as file:
                data_file = {"Task_List": task_list}
                json.dump(data_file, file, indent=4)
                print(f"Task (ID: {id}) marked as {mark}.")

        else:
            print(f"Task with ID {id} not found.")
            raise SystemExit
        
        task_list.clear()
