# Task-Tracker-CLI

## Description
Task Tracker CLI is a command-line interface application designed to help you manage your tasks efficiently. With this tool, you can add, update, delete, mark, and list tasks directly from the command line.

## Features

- **Add Tasks**: Easily add new tasks with descriptions.
- **Update Tasks**: Modify the description or status of existing tasks.
- **Delete Tasks**: Remove tasks from your list.
- **Mark Tasks**: Mark tasks as 'done', 'in progress', etc.
- **List Tasks**: View all tasks or filter them by status.

## Installation
To set up the Task Tracker CLI application on your local machine, follow these steps:

1. Clone the repository:
```bash 
https://github.com/AKAJellyBean/Task-Tracker-CLI.git 
```
2. Navigate to the project directory
```bash
cd task-tracker-cli
```

> [!IMPORTANT]  
> Ensure you have Python installed. The application is compatible with Python 3.6 and above.

3. Run the application
```bash
python src/main.py
```

## Usage

here are some examples of hot to use the Task Tracker CLI

- **Add a new task**

When adding a task, system uses the following structure:

- **Command: `add`**
- **Argument: `task description`**

```bash
task-cli: add "Your task description here"
```
> [!NOTE]  
> When creating a task, the task Id and task creation date is automatically generated and included.

- **Update a task**

When updating a task, system use the following structure:

- **Command: ``update``**
- **Argument: ``task ID`` and ``updated task description``**

```bash
task-cli: update 1 "updated task description"
```

> [!NOTE]  
> When updating a task, the task updated date is automatically generated and included.

- **Delete a Task**

When deleting a task, the system uses the following structure:

- **Command: ``delete``**
- **Argument: ``task ID``**

```bash
task-cli: delete 1
```

- **Mark a Task**

When marking a task, the system uses the following structure:

- **Command: ``mark``**
- **Arguments: ``task ID`` and ``status``**

```bash
task-cli: mark 2 "done"
```
- **List Tasks**

When listing tasks, the system uses the following structure:

- **Command: ``list``**
- **Argument: ``filter`` (optional)**

    - If no argument is provided, all tasks will be listed.
    - Arguments can include ``done``, ``todo``, or ``in-progress`` to filter tasks by their status.

```bash
# List all tasks
task-cli: list

# List tasks that are done
task-cli: list "done"

# List tasks that are marked as todo
task-cli: list "todo"

# List tasks that are in progress
task-cli: list "in-progress"
```
> [!IMPORTANT]  
> When adding, updating, or marking tasks, ensure that the descriptions are enclosed in double or single quotes. IDs do not require quotes.

## File Structure
- `.venv/`: Contains the virtual environment for the project.
- `data/`: Directory for storing data files, including the JSON file used by the application.
- `src/`: Contains all the source code files for the application.
  - `src/main.py`: The main script that runs the CLI application.
  - `src/task_manager.py`: Manages task-related operations.
  - `src/task.py`: Defines the Task class.
  - `src/validator.py`: Contains functions for validating and parsing user input.
  - `src/create_file.py`: Handles the creation of necessary files.
  - `src/get_date.py`: Provides the current date for task creation and updates.

## Dependencies

This project requires the following Python libraries:

- **``json``** (standard library)
- **``os``** (standard library)
- **``datetime``** (standard library)

## Contributing
If you'd like to contribute to the Task Tracker CLI, please fork the repository and use a feature branch. Pull requests are welcome.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact Information
For any questions or suggestions, feel free to reach out to me at dinethekanayake@outlook.com.