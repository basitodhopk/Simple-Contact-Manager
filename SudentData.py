students = [
    {"name": "Ali", "age": 18},
    {"name": "Sara", "age": 19},
    {"name": "Ahmed", "age": 18},
    {"name": "Aisha", "age": 17},
    {"name": "Bilal", "age": 18},
    {"name": "Farah", "age": 20},
    {"name": "Zain", "age": 18},
    {"name": "Hina", "age": 18},
    {"name": "Usman", "age": 16},
    {"name": "Kashif", "age": 18},
    {"name": "Fatima", "age": 19},
    {"name": "Asad", "age": 18},
    {"name": "Mariam", "age": 17},
    {"name": "Junaid", "age": 18},
    {"name": "Zara", "age": 20},
    {"name": "Tariq", "age": 18},
    {"name": "Saima", "age": 15},
    {"name": "Rizwan", "age": 18},
    {"name": "Haris", "age": 21},
    {"name": "Imran", "age": 18}
]

selected_students = []

for student in students:
    if student['age'] == 18:
        selected_students.append(student["name"])

print("Selected Students:", selected_students)
