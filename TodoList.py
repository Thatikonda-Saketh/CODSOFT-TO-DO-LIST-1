class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for index, task in enumerate(self.tasks, start=1):
                status = "Done" if task["completed"] else "Not Done"
                print(f"{index}. {task['task']} - {status}")

    def mark_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task index.")

def main():
    todo_list = TodoList()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
            print("Task added.")

        elif choice == "2":
            print("\nTasks:")
            todo_list.view_tasks()

        elif choice == "3":
            todo_list.view_tasks()
            task_index = int(input("Enter the index of the task to mark as completed: "))
            todo_list.mark_completed(task_index)

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
