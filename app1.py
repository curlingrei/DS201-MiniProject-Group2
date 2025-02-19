import os

def main():
  # Restore tasks
  if os.path.isfile("tasks.txt"):
    with open('tasks.txt', 'r') as file:
      tasks_list = [line.strip() for line in file.readlines()]
  else:
    tasks_list = []

  while True:
    # Display Menu
    print("To-Do List Application")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")

    choice = int(input("Enter your choice with a number: "))
    print()

    if choice == 1:
      add_task(tasks_list)
    elif choice == 2:
      remove_task(tasks_list)
    elif choice == 3:
      view_tasks(tasks_list)
    elif choice == 4:
      ## save tasks
      with open("tasks.txt", "w") as f:
        f.write("\n".join(tasks_list))
      print("Your tasks have been saved. Exiting the application. Goodbye!")
      break
    else:
      print("You need to input 1, 2 ,3 or 4. Other values are not allowed\n")
      continue

def add_task(tasks):
    new_task = input("Enter the task title: ")
    print(f"{new_task} has been added to the list.\n")
    tasks.append(new_task)

def remove_task(tasks):
  print("You have the following tasks")
  view_tasks(tasks)
  while True:
    target_task = input("Enter the task to remove: ")
    if target_task in tasks:
      print(f"{target_task} has been removed from the list.\n")
      tasks.remove(target_task)
      break
    else:
      print("The task doesn't exist. Try again.\n")
      continue

def view_tasks(tasks):
  print("To-Do List: ")
  for i in range(len(tasks)):
    print(f"{i+1}. {tasks[i]}")
  print()

if __name__ == "__main__":
    main()