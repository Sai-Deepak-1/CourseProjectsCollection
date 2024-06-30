import sys


def read_file(file_path):
    with open(file_path, "r") as file:
        return file.readlines()


def add_task(lines, task):
    lines.append(f"{task.capitalize()}\n")


def remove_task(lines, index):
    if 0 <= index < len(lines):
        lines.pop(index)
    else:
        print("Error: Invalid task number.")
        sys.exit(1)


def save_file(file_path, lines):
    with open(file_path, "w") as file:
        file.writelines(lines)


def print_tasks(lines):
    print("\nHere's your ToDo list:\n")
    for num, line in enumerate(lines, start=1):
        print(f"{num}. {line.strip()}")


def print_usage(script_name):
    print("\n*******************************\n")
    print(f"To view ToDos:\n{script_name}")
    print(f'\nTo add a ToDo:\n{script_name} add "Clean Room"\n')
    print(f"To remove or complete a ToDo:\n{script_name} remove 2\n")


def main():
    file_path = "todo.txt"
    lines = read_file(file_path)

    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "add":
            if len(sys.argv) < 3:
                print('Error: No task provided. Usage: py todo.py add "task"')
                sys.exit(1)
            else:
                task = " ".join(sys.argv[2:])
                add_task(lines, task)
                print_tasks(lines)
        elif command == "remove":
            if len(sys.argv) < 3:
                print(
                    "Error: No task number provided. Usage: py todo.py remove <task_number>"
                )
                sys.exit(1)
            else:
                try:
                    index = int(sys.argv[2]) - 1
                    remove_task(lines, index)
                    print_tasks(lines)
                except ValueError:
                    print(
                        "Error: Please provide a valid task number. Usage: py todo.py remove <task_number>"
                    )
        elif command == "show":
            print_tasks(lines)
        elif command == "cmd":
            print_usage(sys.argv[0])
        else:
            print(f"Unknown command: {command}")
            sys.exit(1)

    save_file(file_path, lines)
    # print_tasks(lines)
    # print_usage(sys.argv[0])


if __name__ == "__main__":
    main()
