tasks = []

print("=== TO-DO LIST ===\n")

while True:
    print("1. Add Task\n2. View Tasks\n3. Exit\n")

    choice = int(input("Choose (1-3): "))
    print()

    if choice == 1:
        tasks.append(input("Enter task: "))
        print("Added\n")
        
    elif choice ==2:
        if not tasks:
            print("No task available")
            
        else:
            print("Your Tasks:")
            i = 1
            for task in tasks:
                print(i, task)
                i += 1
        print()

    elif choice == 3:
        print("Goodbye!")
        break

    else:
        print("Invalid option, try again")
        print()
               