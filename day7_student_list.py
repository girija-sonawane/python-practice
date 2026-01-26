students = []

count = int(input("How many students? "))

for i in range(count):
    name = input("Enter student name: ")
    students.append(name)

print("\nStudent List:")
for student in students:
    print(student)