import os

def run_command(command):
    try:
        result = os.popen(command).read()
        return result if result else "No output"
    except Exception as e:
        return str(e)