tasks = []

while True:

    print("\n--- MENU ---")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")
    if choice == "1":
        task = input("Enter Task Name: ")
        tasks.append(task)
        print("Task Added!")

    elif choice == "2":
        print("\n--- YOUR TASKS ---")
        for task in tasks:
            print(task)
    elif choice == '3':
        task_to_delete = input("Enter task to delete: ")
        if task_to_delete in tasks:
            tasks.remove(task_to_delete)
            print("Task deleted!")
        else:
            print("Task not found!")

    elif choice == '4':
        print("Goodbye!")
        break

