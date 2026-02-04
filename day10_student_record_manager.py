def add_student():
    name = input("Enter student name: ")
    age = input("Enter age: ")
    marks = input("Enter marks: ")

    with open("students.txt", "a") as file:
        file.write(name + "," + age + "," + marks + "\n")

    print("Student record added successfully\n")


def view_students():
    print("\n--- Student Records ---")

    try:
        with open("students.txt", "r") as file:
            records = file.readlines()

            if not records:
                print("No records found")
            else:
                for record in records:
                    name, age, marks = record.strip().split(",")
                    print("Name:", name, "| Age:", age, "| Marks:", marks)

    except FileNotFoundError:
        print("No records file found")


while True:
    print("\n===== Student Record Manager =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        print("Exiting program...")
        break
    else:
        print("Invalid choice, try again")