tasks = ["do the dishes", "take out the trash", "walk the dog", "do the laundry"]

def add_task(task):
    tasks.append(task)

def remove_task(index):
    if 0 <= index < len(tasks):
        del tasks[index]
        print(f"Task at index {index} removed")
    else:
        print("Invalid task index")

def edit_task(index, new_task):
    if 0 <= index < len(tasks):
        tasks[index] = new_task
        print(f"Task at index {index} updated")
    else:
        print("Invalid task index")

def show_tasks():
    if len(tasks) == 0:
        print("No tasks available")
    else: 
        for i in range(len(tasks)):
            print(f"{i + 1}: {tasks[i]}")

add_task("buy groceries")
edit_task(1, "buy milk")
remove_task(2)
print("\nCurrent tasks:")
show_tasks()