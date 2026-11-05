import sys
import db_helper

def display_menu():
    print("\n--- TO-DO LIST ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks():
    tasks = db_helper.get_all_tasks()
    if not tasks:
        print("\nNo tasks found!")
        return
    
    print("\nID  | Status | Title - Description")
    print("-" * 40)
    for t in tasks:
        status = "✅" if t['is_completed'] else "❌"
        print(f"{t['id']:<3} |   {status}   | {t['title']} - {t['description']}")

def main():
    while True:
        display_menu()
        choice = input("\nEnter choice (1-5): ").strip()
        
        if choice == '1':
            view_tasks()
        elif choice == '2':
            title = input("Enter task title: ")
            desc = input("Enter task description (optional): ")
            db_helper.add_task(title, desc)
            print("Task added successfully!")
        elif choice == '3':
            view_tasks()
            try:
                task_id = int(input("\nEnter task ID to mark complete: "))
                db_helper.update_task_status(task_id, True)
                print("Task marked as completed!")
            except ValueError:
                print("Invalid ID.")
        elif choice == '4':
            view_tasks()
            try:
                task_id = int(input("\nEnter task ID to delete: "))
                db_helper.delete_task(task_id)
                print("Task deleted!")
            except ValueError:
                print("Invalid ID.")
        elif choice == '5':
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid choice, please select 1-5.")

if __name__ == "__main__":
    main()
