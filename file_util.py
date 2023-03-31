
import os

script_dir = os.path.dirname(os.path.realpath(__file__))

def read_file(filename):
    with open(filename) as file:
        return file.read()

def write_file(filename, content):
    with open(filename, 'w') as file:
        return file.write(content)
    
def read_root_file(filename):
    file_full_path = os.path.join(script_dir, filename)
    return read_file(file_full_path)
    
def write_root_file(filename, content):
    file_full_path = os.path.join(script_dir, filename)
    return write_file(file_full_path, content)