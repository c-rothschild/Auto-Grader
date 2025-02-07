import subprocess
from subprocess import Popen, PIPE, STDOUT
import os
import io
import glob

"""
This is the code I use for automating the grading process as a Computer Science grader at colorado college
"""

def run_file(file_path, user_input):
    """
    Run a file with a list of user inputs.
    """
    try:
        print(f"{os.path.basename(file_path)} is running")
        proc = Popen(
            ["python", file_path], stdout=PIPE, stdin=PIPE, stderr=STDOUT, text=True
        )
        
        output, _ = proc.communicate(input=user_input)
        for line in output.splitlines():
            print(line)
    except Exception as e:
        print(f"An error occurred while running the file: {e}")
    finally:
        rerun_file(file_path)

def rerun_file(file_path):
    while True:
        user_input = input("Type 'rerun' to rerun code without inputs or 'exit' to quit: ").strip().lower()
        if user_input == 'rerun':
            os.system('clear')
            try:
                print(f"{os.path.basename(file_path)} is running")
                subprocess.run(["python", file_path])
            except Exception as e:
                print(f"An error occurred while rerunning the file: {e}")
        elif user_input == 'exit':
            break
        else:
            print("Invalid input. Please type 'rerun' or 'exit'.")

def custom_run(directory, command_map):
    """
    run all the python codes in a directory if the name of the code contains a key in the command map
    codes will run once for each item in the list associated with the code's matching key
    """
    def run_code_type(f):
        """
        find a code's matching key and
        run that code with simulated user input determined by key's value
        """
        for key in command_map.keys():
            #iterate through each key(code type) in command list dictionary
            if key in f.lower():
                #check if key exists in name of file
                list(map(lambda x: run_file(f, x), command_map[key])) #run file with each user input in dictionary
    for filename in sorted(glob.iglob(f'{directory}/*.py')):
        #iterate through all python files in directory
        run_code_type(filename)

def main():
    """
    get user input (directory, code types, input for each code)
    """
    directory = input("Write directory path here: ")
    if not os.path.isdir(directory):
        #check if directory path exists
        print("Invalid directory")
        main()
        return
    codes = input("Write code names here (code1,code2,code3): ").split(',')
    command_map = {}
    for code in codes:
        command_list = []
        while True:
            command = input(f"Type command for {code} (\\n to simulate enter key, q to quit): ")
            command = command.replace('\\n', '\n')
            if command == 'q':
                break
            else:
                command_list.append(command)
        command_map[code] = command_list
    print()
    custom_run(directory, command_map)

main()
