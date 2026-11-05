def evaluate_expression(students_dict):
    schoolarship_students = []

    for name, grades in students_dict.items():
        if len(grades) == 0:
            continue

        average = sum(grades) / len(grades)
        if average > 5.00:
            schoolarship_students.append((name, round(average, 2)))

    schoolarship_students.sort(key=lambda x: x[1], reverse=True)
    return schoolarship_students


students = {
    "Ivan": [3, 4, 3],
    "Maria": [5, 6, 6],
    "Petar": [4, 4, 4]
}

print(evaluate_expression(students))