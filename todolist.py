class ToDoList:
    def __init__(self):
        self.tasks = [] 

    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("Tasks:")
            for idx, task in enumerate(self.tasks):
                status = "Done" if task["done"] else "Not Done" 
                print(f"{idx + 1}. {task['task']} - {status}")

    def mark_task_as_done(self, task_idx):
        if 1 <= task_idx <= len(self.tasks):
            self.tasks[task_idx - 1]["done"] = True
            print("Task marked as done.")
        else:
            print("Invalid task index.")

    def delete_task(self, task_idx):
        if 1 <= task_idx <= len(self.tasks):
            del self.tasks[task_idx - 1]
            print("Task deleted.")
        else:
            print("Invalid task index.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.list_tasks()
        elif choice == "3":
            task_idx = int(input("Enter task index to mark as done: "))
            todo_list.mark_task_as_done(task_idx)
        elif choice == "4":
            task_idx = int(input("Enter task index to delete: "))
            todo_list.delete_task(task_idx)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
