students = {
    "Ivan": [3, 4, 3],
    "Daniel": [ 5, 6, 4],
    "Maria": [6, 6, 5]
}

def add_grade(name, grade):
    if name in students:
        students[name].append(grade)
    else: 
        students[name] = [grade]

def average_grade(name):
    if name in students and len(students[name]) > 0:
        total = 0 

        for grade in students[name]:
            total += grade

        return total / len(students[name])
    return 0

def show_report():
    for name in students:
        average = average_grade(name)
        print(f" {name}: average grade {average:.2f}")

add_grade("Maria", 6)
print("data for all students: ")
show_report()