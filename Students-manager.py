import json

students = []

# Load data from file
def load_data():
    global students
    try:
        with open("students.json", "r") as file:
            students = json.load(file)
    except:
        students = []

# Save data to file
def save_data():
    with open("students.json", "w") as file:
        json.dump(students, file)

def add_student():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    marks = int(input("Enter your marks: "))

    student = {
        "name": name,
        "age": age,
        "marks": marks
    }

    students.append(student)
    save_data()   
    print("Student added successfully!")

def view_students():
    if len(students) == 0:
        print("No students found.")
    else:
        for s in students:
            print("Name:", s["name"])
            print("Age:", s["age"])
            print("Marks:", s["marks"])

            if s["marks"] >= 50:
                print("Result: Pass")
            else:
                print("Result: Fail")

            print("-----------")

def search_student():
    name = input("Enter name to search: ")

    for s in students:
        if s["name"].lower() == name.lower():
            print("Found Student:")
            print("Name:", s["name"])
            print("Age:", s["age"])
            print("Marks:", s["marks"])
            return

    print("Student not found.")

def delete_student():
    name = input("Enter name to delete: ")

    for s in students:
        if s["name"].lower() == name.lower():
            students.remove(s)
            save_data()   
            print("Student deleted!")
            return

    print("Student not found.")

def average_marks():
    if len(students) == 0:
        print("No students to calculate.")
        return

    total = 0
    for s in students:
        total += s["marks"]

    avg = total / len(students)
    print("Average marks:", avg)



load_data()

while True:
    print("\n======== STUDENT MANAGER (PRO VERSION) ========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Average Marks")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        average_marks()
    elif choice == "6":
        print("Goodbye Ayesha 😎")
        break
    else:
        print("Invalid choice!")