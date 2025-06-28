"""
Mini Project 1: Student Grade Tracker
Objective: Build a program to track and manage student grades for a course.
Project Components:
• Variables: Dictionary for student names and their grades.
• Conditionals: Actions based on user input (e.g., add grade, view grades).
• Loops: Loop for displaying menu and handling user input.
• Lists: Not necessary for this project.
• Dictionaries: Dictionary to store student names and grades.
• Functions: Functions for adding grades, calculating average, and displaying grades.
Description: The program allows users to add student names and their grades, calculate the
average grade, and view all grades entered.
Tasks for Participants:
1. Create a dictionary to store student names and their grades.
2. Write functions to add grades for students, calculate the average grade, and display all
student names and grades.
3. Implement a loop for displaying the menu and handling user input.
4. Use conditionals to execute different actions based on user's choices.
"""
import csv

# Initialize an empty dictionary to store student names and grades
student_list = {}

with open('MOCK_DATA.csv', mode ='r')as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        _, last, grades = lines
        student_list[last] = grades

def add_change_student_grade(student_list, name, grade):
    """Add or change the grade of a student."""
    student_list[name] = grade
    print(f"Grade for {name} updated to {grade}.")
    
def view_all_grades(student_list):
    """Display all student names and their grades."""
    for keys, values in student_list.items():
        print(f"Student: {keys}, Grade: {values}")
        
def calculate_average_grade(student_list):
    """Calculate and return the average grade of all students."""
    if not student_list:
        print("No grades available to calculate average.")
        return 0
    total = sum(float(grade) for grade in student_list.values())
    average = total / len(student_list)
    return average

while True:
    # Display the menu
    view_all_grades(student_list)
    print("Student Grade Tracker")
    print("1. Add/Change Student Grade")
    print("2. View All Grades")
    print("3. Calculate Average Grade")
    print("4. Exit")

    # Get user input
    choice = input("Enter your choice: ")

    if choice == '1':
        # Add/Change student grade
        print("Do you want to add or change a student grade?")
        print("1. Add")
        print("2. Change")
        action = input("Enter your choice: ")
        if action == '1':
            name = input("Enter student name: ")
            grade = float(input("Enter student grade: "))
            add_change_student_grade(student_list, name, grade)
            print(f"Grade added for {name}: {grade}")
        elif action == '2':
            name = input("Enter student name: ")
            for keys in list(student_list.keys()):
                if keys == name:
                    grade = float(input("Enter new grade: "))
                    add_change_student_grade(student_list, name, grade)
                    break
        else:
            print("Invalid choice. Please try again.")
            continue

    elif choice == '2':
        view_all_grades(student_list)

    elif choice == '3':
        calculate_average_grade(student_list)

    elif choice == '4':
        # Exit the program
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")