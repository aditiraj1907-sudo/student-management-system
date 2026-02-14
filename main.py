def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    course = input("Enter course: ")
    marks = input("Enter marks: ")

    with open("students.txt", "a") as file:
        file.write(f"{name},{roll},{course},{marks}\n")

    print("✅ Student added successfully!")


def menu():
    print("\n====== Student Management System ======")
    print("1. Add Student")
    print("2. Exit")


while True:
    menu()
    choice = input("Enter your choice (1-2): ")

    if choice == '1':
        add_student()
    elif choice == '2':
        print("Thank you! Exiting...")
        break
    else:
        print("Invalid choice! Try again.")

