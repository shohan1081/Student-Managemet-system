import json

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def display_person_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")

class Student(Person):
    def __init__(self, name, age, address, student_id):
        super().__init__(name, age, address)
        self.student_id = student_id
        self.grades = {}
        self.courses = []

    def add_grade(self, subject, grade):
        self.grades[subject] = grade
        print(f"Grade {grade} added for {self.name} in {subject}.")

    def enroll_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
            print(f"Student {self.name} (ID: {self.student_id}) enrolled in {course}.")
        else:
            print(f"Student {self.name} is already enrolled in {course}.")

    def display_student_info(self):
        self.display_person_info()
        print(f"ID: {self.student_id}")
        print("Enrolled Courses:", ", ".join(self.courses))
        print("Grades:", self.grades)

class Course:
    def __init__(self, name, code, instructor):
        self.name = name
        self.code = code
        self.instructor = instructor
        self.enrolled_students = []

    def enroll_student(self, student):
        if student not in self.enrolled_students:
            self.enrolled_students.append(student)
            student.enroll_course(self.name)
        else:
            print(f"Student {student.name} is already enrolled in {self.name}.")

    def display_course_info(self):
        print(f"Course Name: {self.name}")
        print(f"Code: {self.code}")
        print(f"Instructor: {self.instructor}")
        print("Enrolled Students:", ", ".join([student.name for student in self.enrolled_students]))


def save_data(students, courses, filename="student_management_data.json"):
    data = {
        "students": [
            {"name": s.name, "age": s.age, "address": s.address, "student_id": s.student_id,
             "grades": s.grades, "courses": s.courses} for s in students
        ],
        "courses": [
            {"name": c.name, "code": c.code, "instructor": c.instructor,
             "enrolled_students": [s.student_id for s in c.enrolled_students]} for c in courses
        ]
    }
    with open(filename, "w") as file:
        json.dump(data, file)
    print("All student and course data saved successfully.")

def load_data(filename="student_management_data.json"):
    with open(filename, "r") as file:
        data = json.load(file)
    print("Data loaded successfully.")
    return data


def main():
    students = []
    courses = []

    while True:
        print("\nSelect Option:")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Enroll Student in Course")
        print("4. Add Grade for Student")
        print("5. Display Student Details")
        print("6. Display Course Details")
        print("7. Save Data to File")
        print("8. Load Data from File")
        print("0. Exit")
        
        option = int(input("Enter option: "))

        if option == 1:
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            address = input("Enter Address: ")
            student_id = input("Enter Student ID: ")
            student = Student(name, age, address, student_id)
            students.append(student)

        elif option == 2:
            name = input("Enter Course Name: ")
            code = input("Enter Course Code: ")
            instructor = input("Enter Instructor Name: ")
            course = Course(name, code, instructor)
            courses.append(course)

        elif option == 3:
            student_id = input("Enter Student ID: ")
            course_code = input("Enter Course Code: ")
            student = next((s for s in students if s.student_id == student_id), None)
            course = next((c for c in courses if c.code == course_code), None)
            if student and course:
                course.enroll_student(student)
            else:
                print("Student or course not found.")

        elif option == 4:
            student_id = input("Enter Student ID: ")
            subject = input("Enter Course Code: ")
            grade = input("Enter Grade: ")
            student = next((s for s in students if s.student_id == student_id), None)
            if student:
                student.add_grade(subject, grade)
            else:
                print("Student not found.")

        elif option == 5:
            student_id = input("Enter Student ID: ")
            student = next((s for s in students if s.student_id == student_id), None)
            if student:
                student.display_student_info()
            else:
                print("Student not found.")

        elif option == 6:
            course_code = input("Enter Course Code: ")
            course = next((c for c in courses if c.code == course_code), None)
            if course:
                course.display_course_info()
            else:
                print("Course not found.")

        elif option == 7:
            save_data(students, courses)

        elif option == 8:
            data = load_data()

        elif option == 0:
            print("Exiting Student Management System.")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
