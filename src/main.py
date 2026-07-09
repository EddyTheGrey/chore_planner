import datetime
import pandas as pd
import os
import chore_create
import chore_storage

def todays_chores(chores = [], filename = "csv_files/chores.csv"):
    today = datetime.datetime.now().date()

    for chore in chores:
        if chore.next_due_date is None or chore.next_due_date.date() <= today:
            print("Was the following chore completed? (y/n):")
            print(f"Chore: {chore.name}, Description: {chore.description}, Area: {chore.area}, Last Completed: {chore.last_completed}")
            key = input("Press 'y' for yes or 'n' for no: ").lower()
            if key == 'y':
                chore.mark_completed()
                print(f"Marked '{chore.name}' as completed on {chore.last_completed}.")
                chore.last_completed = datetime.datetime.now().strftime("%Y-%m-%d")
                chore.next_due_date = chore.last_completed + pd.to_timedelta(chore.frequency, unit='D')
            elif key == 'n':
                print(f"Chore '{chore.name}' not marked as completed.")
    
    chore_storage.save_chores_to_csv(chores, filename=filename)

def add_chore(chores, filename):
    print("Adding a new chore?")
    key = input("press 'y' to add a new chore or 'n' to cancel: ").lower()
    
    if key == 'y':
        name = input("Enter chore name: ")
        description = input("Enter chore description: ")
        frequency = int(input("Enter chore frequency in number of days: "))
        length = int(input("Enter chore length in minutes: "))
        area = input("Enter chore area (e.g., Kitchen, Bathroom): ")
        due_date_input = input("Enter next due date (YYYY-MM-DD) or leave blank for no due date: ")
        next_due_date = pd.to_datetime(due_date_input) if due_date_input else None  

        new_chore = chore_create.chore(name, description, frequency, length, area, next_due_date=next_due_date )
        chores.append(new_chore)
        chore_storage.save_chores_to_csv(chores, filename=filename)

def delete_chore(chores, filename):
    print("Deleting a chore?")
    key = input("press 'y' to delete a chore or 'n' to cancel: ").lower()
    
    if key == 'y':
        name = input("Enter the name of the chore to delete: ")
        chore_to_delete = next((chore for chore in chores if chore.name == name), None)
        
        if chore_to_delete:
            chores.remove(chore_to_delete)
            chore_storage.save_chores_to_csv(chores, filename=filename)
            print(f"Chore '{name}' has been deleted.")
        else:
            print(f"No chore found with the name '{name}'.")

def main():
    # Load chores from CSV
    base = os.getcwd()
    filename = os.path.join(base, "csv_files", "chores.csv")
    if not os.path.exists(filename):
        print("No chores found. Creating a new chore list.")
        chores = []
    else:
        chores = chore_storage.load_chores_from_csv(filename)
    todays_chores(chores, filename)
    add_chore(chores, filename)
    delete_chore(chores, filename)
    # Print loaded chores
    print("\nThat completes today's chores. Here are the chore outlook for the next few days:")
    for chore in chores:
        print("------------------------------")
        print(chore)
        print("------------------------------")

if __name__ == "__main__":
    main()