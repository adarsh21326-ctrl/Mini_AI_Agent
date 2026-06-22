from executor_new import run_command
from command_parser import parse_command
from commands import COMMAND_MAP
from datetime import datetime

print("=== Mini AI Agent Started ===")

while True:
    command = input("Enter command (or type exit): ")

    if command.lower() == "exit":
        print("Exiting...")
        break

    real_command = parse_command(command)
    if command.lower() == "help":
        print("\nAvailable commands:")
        for command in COMMAND_MAP:
           print("-", command)
        print("------------------------")
        continue


    if command.lower() == "history":
        print("Recent Commands:")
        with open("logs.txt", "r") as file:
            lines = file.readlines()
            for line in lines[-5:]:
               print(line.strip())
        continue


    if command.lower() == "about":
        print(
        "Mini AI Agent v1.0\n"
        "Created by Adarsh\n"
        "Features:\n"
        "- Command Translation\n"
        "- Logging\n"
        "- History"
    )
        continue

    if real_command is None:
       print("\nSorry, I don't understand that command.")
       print("------------------------")
       continue

    print(f"\nTranslated to command: {real_command}")

    output = run_command(real_command)

    current_time = datetime.now()

    with open("logs.txt", "a") as log_file:
       log_file.write(
          f"{current_time} | {command} | {real_command}\n"
    )

    print("\nOutput:")
    print(output)
    print("------------------------")