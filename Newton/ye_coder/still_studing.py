'''Building to_do_list '''

def to_do_list():
    pass


task = []

while True:
    print("1. Add a task")
    print("2. Remove tasks")
    print("3. Show tasks")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        task_name = input("Enter the task name: ")
        task.append(task_name)
    elif choice == "2":    
        task_name = input("Enter the task name to remove: ")
        if task_name in task:
            task.remove(task_name)
        else:
            print("Task not found.")
    elif choice == "3":
        print("Tasks:")
        for t in task:
            print(f"-" + {t})
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
to_do_list()        