
import os, sys, inspect

def read_input(file_path):
    abs_path = os.path.abspath((inspect.stack()[1])[1])
    day_dir = os.path.dirname(abs_path)

    try:
        with open(os.path.join(day_dir, file_path), 'r') as file:
            return file.read().strip()

    except FileNotFoundError:
        print(f"Input file at {file_path} not found.")
        return None