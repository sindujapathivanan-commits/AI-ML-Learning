# 1.Add student function
students = {
    101: {
        "name": "Sinduja",
        "marks": 90
    },
    102: {
        "name": "Arjun",
        "marks": 85
    },
    103: {
        "name": "Kavya",
        "marks": 95
    },
    104: {
        "name": "Ravi",
        "marks": 88
    },
    105: {
        "name": "Ananya",
        "marks": 92
    }
}

# 2.View All Students

for student in students:
    print(f"ID: {student}, Name: {students[student]['name']}, Marks: {students[student]['marks']}")

# 3.  Search Student by ID
search_id = int(input("Enter the student ID to search: "))

for student in students:
    if student == search_id:
        print(students[student])

# 4. Update Student Marks
update_id = int(input("Enter the students ID to update marks: "))
new_marks = int(input("Enter the new marks: "))
students[update_id]['marks'] = new_marks

# 5. Delete Student
delete_id = int(input("Enter the student ID to delete: "))
if delete_id in students:
    del students[delete_id]
else:
    print("Student not found.")

#6. Display Grade Report
def calculate_grade(marks):
    if marks >= 75:
        grade = "A"
    elif marks >= 60:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    elif marks >= 40:
        grade = "S"
    else:
        grade = "Failed"
    return grade

for student in students:

    students[student]['grade'] = calculate_grade(marks)
    marks = students[student]['marks']
    
    print(students[student])

    print("grade:", grade) #Marks → Check condition → Automatically give Grade.

#7. Exit Application 
for student in students:
    choice: str = input("Enter 1 to continue or 2 to exit: ")

if choice == "2":
    print("Goodbye!")
    exit()  #exit() = close/stop the program.

#8. Validate Student ID
search_id = int(input("Enter the student ID to search: ")) # first searching the student ID 
if search_id not in students:
    print("Invalid student ID.") #If it is not present, then it will print "Invalid student ID.
else:
    for student in students:
        if student == search_id:
            print(students[student]) # It's available, it will print the student details.

# 9.Validate Marks (0–100)
marks = int(input("Enter the marks: "))
if marks < 0 or marks > 100:               #It the marks are less than 0 or greater than 100, it will print "Invalid marks. 
    print("Invalid marks. Please enter marks between 0 and 100.")
else:
    print("Valid marks entered.") #Please enter marks between 0 and 100."

# 10.  Calculate Average Marks
for student in students:
    total_marks = sum(student['marks'] for student in students.values()) # Calculate the total marks of all students

    average = total_marks / 5   # Calculate the average marks


# Show Top Performer
top_performer = max(student['marks'] for student in students.values())

print("Top Performer:", top_performer) #top performer  will be printed.
