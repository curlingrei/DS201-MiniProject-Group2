# Common
## Requirements

1. Display messages
   1. after starting the app
   2. after adding a task
   3. after removing a task
   4. after exiting the app
2. Accept inputs from users
3. Add tasks
4. Remove tasks
5. Stop using the app by inputting "exit"
6. Display Menus repeatedly
7. A user can input the value again after inputting an unacceptable value without starting from the begining.

## Extra Requirements
1. Registered tasks should be seen after restarting the app.
2. Tasks can be registered up to 50.

## Error Handling
1. Input when a user adds a task
   1. the value shouldn't be list, touple, or dictionary, it should be string, numbers, or simbol.
   2. the input shouldn't be empty
2. Input when a user selects something in a menu
   1. accept only 1 - 4
3. Input when a user removes a task
   1. accept only existing task's name
   2. the input shouldn't be empty

# App 1
## Requirements
1. The datatype of task list should be list
2. Display tasks with numbers and its description

# App 2

## Requirements
1. The datatype of task list should be list containing dictionary for each task.
2. Suggest a tasks according to priority and deadline
3. Display tasks with numbers, its description, priority, and deadline

## Design
1. How to realize suggestion function

- sort the list in descending order by priority and then deadline and then pick up the first element.
  - https://note.nkmk.me/en/python-dict-list-sort/
-

## Extra Requirements
1. priority and deadline can be blank
2.
