students = []


def add_student():
    print("\n--- Add Student ---")

    student_id = input("Enter student ID: ").strip()

    if not student_id:
        print("Student ID cannot be empty.")
        return

    # Check for duplicate student IDs
    for student in students:
        if student["id"] == student_id:
            print("Error: This student ID already exists.")
            return

    name = input("Enter student name: ").strip()
    age_text = input("Enter student age: ").strip()
    course = input("Enter student course: ").strip()

    if not name or not course:
        print("Name and course cannot be empty.")
        return

    try:
        age = int(age_text)
        if age <= 0:
            print("Age must be a positive number.")
            return
    except ValueError:
        print("Invalid age. Please enter a whole number.")
        return

    student = {"id": student_id, "name": name, "age": age, "course": course}

    students.append(student)
    print("Student added successfully!")


def view_students():
    print("\n--- Student List ---")

    if not students:
        print("No student records found.")
        return

    print("-" * 55)
    print(f"{'ID':<12}{'Name':<20}{'Age':<8}{'Course'}")
    print("-" * 55)

    for student in students:
        print(
            f"{student['id']:<12}"
            f"{student['name']:<20}"
            f"{student['age']:<8}"
            f"{student['course']}"
        )

    print("-" * 55)


def search_student():
    print("\n--- Search Student ---")

    student_id = input("Enter student ID to search: ").strip()

    for student in students:
        if student["id"] == student_id:
            print("\nStudent found:")
            print(f"ID:     {student['id']}")
            print(f"Name:   {student['name']}")
            print(f"Age:    {student['age']}")
            print(f"Course: {student['course']}")
            return

    print("Student not found.")


def update_student():
    print("\n--- Update Student ---")

    student_id = input("Enter student ID to update: ").strip()

    for student in students:
        if student["id"] == student_id:
            print("Press Enter to keep the current value.")

            new_name = input(f"Name [{student['name']}]: ").strip()

            new_age = input(f"Age [{student['age']}]: ").strip()

            new_course = input(f"Course [{student['course']}]: ").strip()

            if new_age:
                try:
                    age = int(new_age)
                    if age <= 0:
                        print("Age must be positive. Update cancelled.")
                        return
                except ValueError:
                    print("Invalid age. Update cancelled.")
                    return

            if new_name:
                student["name"] = new_name

            if new_age:
                student["age"] = int(new_age)

            if new_course:
                student["course"] = new_course

            print("Student updated successfully!")
            return

    print("Student not found.")


def delete_student():
    print("\n--- Delete Student ---")

    student_id = input("Enter student ID to delete: ").strip()

    for student in students:
        if student["id"] == student_id:
            confirm = input(f"Delete {student['name']}? (y/n): ").strip().lower()

            if confirm == "y":
                students.remove(student)
                print("Student deleted successfully!")
            else:
                print("Deletion cancelled.")

            return

    print("Student not found.")


def main():
    while True:
        print("\n==============================")
        print("  STUDENT MANAGEMENT SYSTEM")
        print("==============================")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("0. Exit")
        print("==============================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "0":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice. Please select 0-5.")


if __name__ == "__main__":
    main()
