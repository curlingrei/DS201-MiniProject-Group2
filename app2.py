import os
import csv
from datetime import datetime

def main():
  tasks_list = []
  # Restore tasks
  if os.path.isfile("tasks.csv"):
    with open("tasks.csv", newline='') as csvfile:
      reader = csv.DictReader(csvfile)
      for task in reader:
        tasks_list.append(dict(task))

  while True:
    # Display Menu
    print("Advanced To-Do List Application")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Suggest Tasks")
    print("5. Exit")

    try:
      choice = int(input("Enter your choice with a number: "))
    except ValueError:
      print("Invalid Input! Only numbers are allowed to input")
      continue

    print()

    if choice == 1:
      add_task(tasks_list)
    elif choice == 2:
      remove_task(tasks_list)
    elif choice == 3:
      view_tasks(tasks_list)
    elif choice == 4:
      suggest_task(tasks_list)
    elif choice == 5:
      ## save tasks
      with open("tasks.csv", 'w') as csvfile:
        fieldnames = ['title', 'priority', 'deadline']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in tasks_list:
          writer.writerow(row)

      print("Your tasks have been saved. Exiting the application. Goodbye!")
      break
    else:
      print("You need to input 1, 2 ,3, 4 or 5. Other numbers are not allowed\n")
      continue

def add_task(tasks):
  new_task_title = input("Enter the task title: ")
  while True:
    new_task_priority = input("Enter the task priority(high, midium, low): ")
    if new_task_priority not in ["high", "medium", "low"]:
      print("Choose one from high, medium, or low")
      continue
    else:
      break

  while True:
    new_task_deadline = input("Enter the task deadline(YYYY-MM-DD): ")
    if is_valid_yyyy_mm_dd(new_task_deadline):
      if datetime.strptime(new_task_deadline, "%Y-%m-%d").date() > datetime.today().date():
        break
      else:
        print("You need to input a future date")
        continue
    else:
      print("You need to input the deadline in YYYY-MM-DD format")
      continue

  print(f"{new_task_title} has been added to the list.\n")
  tasks.append({
      "title": new_task_title,
      "priority": new_task_priority,
      "deadline": new_task_deadline
    }
  )

def remove_task(tasks):
  print("You have the following tasks")
  view_tasks(tasks)
  while True:
    target_task = input("Enter the task title to remove: ")
    if any(target_task == task['title'] for task in tasks):
      for task in tasks:
        if target_task == task['title']:
          tasks.remove(task)
          print(f"{target_task} has been removed from the list.\n")
          break
      break
    else:
      print("The task doesn't exist. Try again.\n")
      continue

def view_tasks(tasks):
  print("Advanced To-Do List: ")
  for i in range(len(tasks)):
    print(f"{i+1}. {tasks[i]['title']} - {tasks[i]['priority']} -  {tasks[i]['deadline']}")
  print()

def suggest_task(tasks):
  print("Good afternoon! Here are some tasks you might want to work on:")
  tasks = sorted(
    tasks,
    key = lambda x: (x['priority'], x['deadline'], x['title'])
    )

  ## Show only top 3 tasks
  i = 0
  for task in tasks:
    print(f"{task['title']} - {task['priority']} -  {task['deadline']}")
    i += 1
    if i == 3:
      break

def is_valid_yyyy_mm_dd(date_str):
    try:
      datetime.strptime(date_str, "%Y-%m-%d")
      return True
    except ValueError:
      return False

if __name__ == "__main__":
    main()