'''
@Author: Nagashree C R
@Date: 2024-07-12
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-12
@Title :program to call an external command in Python.
'''

import subprocess

def external_command(command):
    
    try:
        # Execute the command in the shell
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Print the output
        print("Command output:")
        print(result.stdout.decode('utf-8'))
        
    except subprocess.CalledProcessError as e:
        # If the command returns a non-zero exit status, handle the error
        print(f"Error executing command: {e}")
        print(f"Command output (stderr):")
        print(e.stderr.decode('utf-8'))


command ='ls'  
external_command(command)
