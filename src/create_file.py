import json


def create_file(file_path):
    try:
        data_file = {"Task_List": []}
        with open(file_path, "w") as file:
            json.dump(data_file, file, indent=4)
        print(f"File created at {file_path}")

    except Exception as e:
        print(f"An error occurred while creating the file: {e}")
        raise SystemExit

    return data_file
