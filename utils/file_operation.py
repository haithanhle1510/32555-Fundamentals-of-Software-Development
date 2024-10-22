import json
import os


def read_file_and_convert_to_list(file_path):
    if os.path.exists(file_path):
        # Read the file and return the data as a list
        with open(file_path, 'r') as file:
            try:
                data = json.load(file)
                if isinstance(data, list):
                    return data
                else:
                    # If the data isn't a list, convert it to a list
                    return [data]
            except json.JSONDecodeError:
                return []  # If the file is empty or invalid, return an empty list
    else:
        return []


def write_new_data_to_file(file_path, content):
    # First, read the existing data as a list
    data = read_file_and_convert_to_list(file_path)

    # Append new data to the list
    data.append(content)

    # Write the updated data back to the file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def update_data_to_file(file_path, content):
    # Write the updated data back to the file
    with open(file_path, 'w') as file:
        json.dump(content, file, indent=4)


def clear_file(file_path):
    try:
        with open(file_path, 'w') as file:
            pass
        print(f"File '{file_path}' has been cleared.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
