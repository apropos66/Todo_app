import json
from pathlib import Path

json_path = Path(__file__).parent / "tasks.json"
tasks = []

try:
    with open(json_path, "r") as f:
        tasks = json.load(f)
except FileNotFoundError:
    tasks = []


def show_menu():
    print()
    print("1.Add task")
    print("2.Show all tasks")
    print("3.Mark done")
    print("4.Delete task")
    print("5.Quit")
    print()


def add_task() -> None:
    task: str = input("Enter the task: ")
    tasks.append({"task": task, "done": False})
    print("Task added!")
    print()


def show_tasks(verbose: bool = True) -> None:
    if not tasks:
        print("No tasks yet!")
        return
    print()
    print("Todo list:")
    for i, task in enumerate(tasks, start=1):
        if task["done"]:
            mark = "x"
        else:
            mark = ""
        if verbose:
            print(f"[{mark}] {task['task']}")
        else:
            print(f"[{mark}] {task['task']} -> {i}")


def mark_done(num: int) -> None:
    tasks[num - 1]["done"] = True


def delete_task(num: int) -> bool:
    if 1 <= num <= len(tasks):
        del tasks[num - 1]
        return True

    return False


def show_all_task_menu() -> None:
    show_tasks() if tasks else print("No tasks yet!")


def mark_done_menu() -> None:
    if not tasks:
        print("No tasks yet!")
        return
    show_tasks(verbose=False)
    try:
        num = int(input("Enter the task to mark done: "))
        mark_done(num)
    except ValueError:
        print("Enter only numbers!")

    else:
        print()
        print(f"Marked task {num} as done")


def delete_task_menu() -> None:

    if not tasks:
        print("No tasks to delete.")
        return

    show_tasks(verbose=False)
    try:
        num = int(input("Enter the task to delete: "))
    except ValueError:
        print("Enter a valid number.")
        print()
        return
    if delete_task(num):
        print("Task deleted!")

    else:
        print(f"No task #{num}")
    print()


def quit_app() -> bool:
    with open(json_path, "w") as f:
        json.dump(tasks, f, indent=2)

    return False


def main() -> None:
    actions = {
        1: add_task,
        2: show_all_task_menu,
        3: mark_done_menu,
        4: delete_task_menu,
        5: quit_app,
    }
    while True:
        show_menu()
        try:
            choice = int(input("Choose: "))
        except ValueError:
            print("Enter a valid choice.")
            print()
            continue

        action = actions.get(choice)
        if action is None:
            print("Enter a valid number!")
            continue
        if action() is False:
            break


if __name__ == "__main__":
    main()
