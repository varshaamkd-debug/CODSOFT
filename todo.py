# The task list stores dictionaries like: {"task": "Buy milk", "status": "Pending"}
todo_list = []

while True:
    print("\n==============================")
    print("      MY TASK MANAGER         ")
    print("==============================")
    print("1. View All Tasks")
    print("2. Add a New Task")
    print("3. Mark a Task as Completed")
    print("4. Delete a Task")
    print("5. Exit Application")
    print("==============================")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == "1":
        if not todo_list:
            print("\n Your to-do list is completely empty!")
        else:
            print("\n--- YOUR CURRENT TASKS ---")
            for index, item in enumerate(todo_list, 1):
                # Displays task index, name, and status neatly
                print(f"{index}. [{item['status']}] {item['task']}")
                
    elif choice == "2":
        new_task = input("\nWhat task do you want to add? ")
        if new_task.strip():
            todo_list.append({"task": new_task, "status": "Pending"})
            print(f" Success: '{new_task}' added!")
        else:
            print(" Error: Task name cannot be empty.")
            
    elif choice == "3":
        if not todo_list:
            print("\n No tasks available to update.")
        else:
            print("\nSelect the task number to mark as Completed:")
            for index, item in enumerate(todo_list, 1):
                print(f"{index}. [{item['status']}] {item['task']}")
            try:
                task_num = int(input("Enter number: "))
                if 1 <= task_num <= len(todo_list):
                    todo_list[task_num - 1]["status"] = "Completed"
                    print(" Progress updated successfully!")
                else:
                    print(" Invalid task number.")
            except ValueError:
                print(" Please enter a valid number.")
                
    elif choice == "4":
        if not todo_list:
            print("\n No tasks available to delete.")
        else:
            print("\nSelect the task number to delete:")
            for index, item in enumerate(todo_list, 1):
                print(f"{index}. {item['task']}")
            try:
                task_num = int(input("Enter number: "))
                if 1 <= task_num <= len(todo_list):
                    removed = todo_list.pop(task_num - 1)
                    print(f" Deleted: '{removed['task']}'")
                else:
                    print(" Invalid task number.")
            except ValueError:
                print(" Please enter a valid number.")
                
    elif choice == "5":
        print("\nThank you for using My Task Manager. Goodbye!")
        break
    else:
        print(" Invalid option. Please choose between 1 and 5.")