# TH 2nd Average Grade Practice

gradeList = []

classes = int(input("How many classes do you have? "))
start_index = 0
end_index = classes+1
 

for i in range(classes):
    print("--------------------------------------------------")
    grade = float(input("Give me the number grade of a class\n(Don't reuse the class used this time):"))
    print("--------------------------------------------------")
    gradeList.append(grade)
selected_range = gradeList[start_index:end_index]
grade_sum = sum(selected_range)
print("--------------------------------------------------")
print(f"Your grade average is {round(grade_sum/classes, 2)}")
print("--------------------------------------------------")