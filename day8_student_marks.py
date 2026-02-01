students = {}

count = int(input("How many students? "))

for i in range(count):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

print("\nStudent Marks:")
for name, marks in students.items():
    print(name, ":", marks)