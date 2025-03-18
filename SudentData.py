students = {
    "std1": {"name": "Ali", "age": 18},
    "std2": {"name": "Sara", "age": 19},
    "std3": {"name": "Ahmed", "age": 18},
    "std4": {"name": "Aisha", "age": 17},
    "std5": {"name": "Bilal", "age": 18},
    "std6": {"name": "Farah", "age": 20},
    "std7": {"name": "Zain", "age": 18},
    "std8": {"name": "Hina", "age": 18},
    "std9": {"name": "Usman", "age": 16},
    "std10": {"name": "Kashif", "age": 18},
    "std11": {"name": "Fatima", "age": 19},
    "std12": {"name": "Asad", "age": 18},
    "std13": {"name": "Mariam", "age": 17},
    "std14": {"name": "Junaid", "age": 18},
    "std15": {"name": "Zara", "age": 20},
    "std16": {"name": "Tariq", "age": 18},
    "std17": {"name": "Saima", "age": 15},
    "std18": {"name": "Rizwan", "age": 18},
    "std19": {"name": "Haris", "age": 21},
    "std20": {"name": "Imran", "age": 18}
}


student_key = input("Enter student key (std1, std2, etc.): ")


if student_key in students:
    print(f"{student_key} Details: {students[student_key]}")
else:
    print("Student not found!")