tasks = []


def add_task(title, priority="medium"):
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "completed": False,
        "priority": priority
    }

    tasks.append(task)
    return task


def list_tasks():
    return tasks


def get_tasks():
    return tasks


def complete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            return task

    return None


def delete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return True

    return False


def display_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\n===== TASKS =====")

    for task in tasks:
        status = "✓" if task["completed"] else " "

        print(
            f'{task["id"]}. [{status}] '
            f'{task["title"]} - Priority: {task["priority"]}'
        )


def main():
    while True:
        print("\n===== DEVOPS TASK MANAGER =====")
        print("1. Add task")
        print("2. List tasks")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter task: ")

            print("\nChoose priority:")
            print("1. High")
            print("2. Medium")
            print("3. Low")

            priority_choice = input("Choose priority: ")

            if priority_choice == "1":
                priority = "high"
            elif priority_choice == "2":
                priority = "medium"
            elif priority_choice == "3":
                priority = "low"
            else:
                print("Invalid priority.")
                continue

            add_task(title, priority)
            print("Task added successfully.")

        elif choice == "2":
            display_tasks()

        elif choice == "3":
            task_id = int(input("Enter task ID: "))
            task = complete_task(task_id)

            if task:
                print("Task completed.")
            else:
                print("Task not found.")

        elif choice == "4":
            task_id = int(input("Enter task ID: "))

            if delete_task(task_id):
                print("Task deleted.")
            else:
                print("Task not found.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
