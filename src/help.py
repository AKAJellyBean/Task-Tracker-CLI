def print_help():
    help_text = """
Available Commands:
--------------------
1. add <description>
   Adds a new task with the specified description.

2. update <id> <description>
   Updates the task with the specified ID.

3. delete <id>
   Deletes the task with the specified ID.

4. mark <id> <status>
   Marks the task with the specified ID with the given status (e.g., 'done', 'todo', 'in-progress').

5. list [<status>]
   Lists all tasks or filters tasks based on the specified status ('done', 'todo', 'in-progress').

6. help
   Displays this help message.

7. quit
   Exits the application.
    """
    print(help_text)