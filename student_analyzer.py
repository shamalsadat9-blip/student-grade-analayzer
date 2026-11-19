# Student Grade Analyzer

students = []

def add_student():
    name = input("Enter student name: ")
    grade = float(input("Enter student grade: "))

    if grade < 0 or grade > 100:
        print("Invalid grade!")
        return

    students.append({
        "name": name,
        "grade": grade
    })

    print("Student added successfully!")


def show_students():
    if not students:
        print("No students found.")
        return

    for student in students:
        print(student["name"], ":", student["grade"])


def calculate_average():
    if not students:
        print("No grades available.")
        return

    average = sum(s["grade"] for s in students) / len(students)
    print("Average grade:", round(average, 2))


def show_highest_and_lowest():
    if not students:
        print("No grades available.")
        return

    highest = max(students, key=lambda s: s["grade"])
    lowest = min(students, key=lambda s: s["grade"])

    print("Highest:", highest["name"], highest["grade"])
    print("Lowest:", lowest["name"], lowest["grade"])


def main():
    while True:
        print("\n===== Student Grade Analyzer =====")
        print("1. Add student")
        print("2. Show students")
        print("3. Calculate average")
        print("4. Show highest and lowest")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            show_students()
        elif choice == "3":
            calculate_average()
        elif choice == "4":
            show_highest_and_lowest()
        elif choice == "5":
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
