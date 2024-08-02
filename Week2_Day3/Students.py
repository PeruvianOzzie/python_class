students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
grades = [
    [85, 92, 78],
    [79, 85, 88],
    [91, 89, 95],
    [70, 65, 80],
    [88, 90, 92]
]


student_avg = {}

for indx, student in enumerate(students):
    grade_avg = 0
    grade_total = 0
    number_of_grades = 0
    
    grade_total = sum(grades[indx])
    number_of_grades = len(grades[indx])
    grade_avg = grade_total / number_of_grades
    student_avg[student] = grade_avg
    continue

print(f"List of student grades: {student_avg} \n")

student_avg_sorted = dict(sorted(student_avg.items(), key=lambda item: item[1]))

print(f"sorted roster with grades {student_avg_sorted}\n")

student_keys = list(student_avg_sorted.keys())

print(f"Student with the lowest average: {student_keys[0]} with a grade of: {student_avg_sorted[student_keys[0]]}")
print(f"Student with the highest average: {student_keys[-1]} with a grade of: {student_avg_sorted[student_keys[-1]]}")