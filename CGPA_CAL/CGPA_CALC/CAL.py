# writing a program to calculate gpa of student
Grade = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1, 'F': 0}
total_points = 0
total_unit = 0
iterate = 0
course_offered = int(input('Enter the number of courses you offered this semester: '))
while course_offered > iterate:
    unit = int(input("Enter the course unit: "))
    score = int(input("Enter your score; e.g 40 or 75: "))
    if (score >= 40) and score < 45:
        point = unit * Grade['E']
    elif (score >= 60) and score < 70:
        point = unit * Grade['B']
    elif score >= 70:
        point = unit * Grade['A']
    elif (score >= 50) and score < 60:
        point = unit * Grade['C']
    elif (score >= 45) and score < 50:
        point = unit * Grade['D']
    else:
        point = unit * Grade['F']
    total_points += point
    print(f'total_points : {total_points}')
    total_unit += unit
    print(f'total_unit : {total_unit}')
    iterate += 1

CGPA = total_points / total_unit

print(f'\nyour total point for the semester is {total_points} and your total unit is {total_unit} \n\tTherefore:\n')
print(f'Your CGPA is {CGPA}\n')
print(f'Thanks for using this app')
