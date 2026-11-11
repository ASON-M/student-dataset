# Fictional student dataset
# Name: Asiah Nosa
# Matric No: 23/13410
# Department: Computer Science

import csv
import random

departments = ["Computer Science", "Cyber Security", "Software Engineering"]
levels = [100, 200, 300, 400]

students = []
for i in range(1, 31):
    student_id = "STU" + str(i).zfill(3)
    dept = random.choice(departments)
    level = random.choice(levels)
    attendance = random.randint(50, 100)
    score = round(random.uniform(35, 95), 1)
    students.append([student_id, dept, level, attendance, score])

with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Student ID", "Department", "Level",
                     "Attendance Percentage", "Average Exam Score"])
    writer.writerows(students)

print("Dataset created: students.csv")