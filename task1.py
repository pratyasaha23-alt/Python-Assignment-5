students = {
    "Rahul": 85,
    "Sneha": 92,
    "Amit": 78,
    "Priya": 88,
    "Ravi": 95
}

name = input("Enter student name: ")

if name in students:
    print("Marks:", students[name])
else:
    print("Student not found in the record.")
