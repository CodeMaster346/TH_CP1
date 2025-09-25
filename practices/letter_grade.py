# TH 2nd What Is My Grade
gradeList = []

while True:
    percent = float(input("What is your grade percentage: "))
    user_choice = input("Type 'New' if you want to input a new grade\npercentage, or type 'Exit' if you want to exit: ").lower().strip()
    if user_choice == "New":
        if percent >= 94:
            print("Your letter grade is an A")
            gradeGpaForm = 4.0
            gradeList.append(gradeGpaForm)
        elif percent >= 90:
            print("Your letter grade is an A-")
            gradeGpaForm = 3.7
            gradeList.append(gradeGpaForm)
        elif percent >= 87:
            print("Your letter grade is a B+")
            gradeGpaForm = 3.3
            gradeList.append(gradeGpaForm)
        elif percent >= 84:
            print("Your letter grade is a B") 
            gradeGpaForm = 3.0
            gradeList.append(gradeGpaForm)
        elif percent >= 80:
            print("Your letter grade is a B-")
            gradeGpaForm = 2.7
            gradeList.append(gradeGpaForm)
        elif percent >= 77:
            print("Your letter grade is a C+")
            gradeGpaForm = 2.3
            gradeList.append(gradeGpaForm)
        elif percent >= 73:
            print("Your letter grade is a C")
            gradeGpaForm = 2.0
            gradeList.append(gradeGpaForm)
        elif percent >= 70:
            print("Your letter grade is a C-")
            gradeGpaForm = 1.7
            gradeList.append(gradeGpaForm)
        elif percent >= 67:
            print("Your letter grade is a D+")
            gradeGpaForm = 1.3
            gradeList.append(gradeGpaForm)
        elif percent >= 63:
            print("Your letter grade is a D")
            gradeGpaForm = 1.0
            gradeList.append(gradeGpaForm)
        elif percent >= 60:
            print("Your letter grade is a D-")
            gradeGpaForm = 0.7
            gradeList.append(gradeGpaForm)
        else:
            print("Your letter grade is an F")
            gradeGpaForm = 0.0
            gradeList.append(gradeGpaForm)

        if len(gradeList) > 1:
            GPA = sum(gradeList)/len(gradeList)
            if GPA >= 4.0:
                print("Your average letter grade for grades given is an A")
            elif GPA >= 3.7:
                print("Your average letter grade for grades given is an A-")
            elif GPA >= 3.3:
                print("Your average letter grade for grades given is an B+")
            elif GPA >= 3.0:
                print("Your average letter grade for grades given is an B")
            elif GPA >= 2.7:
                print("Your average letter grade for grades given is an B-")
            elif GPA >= 2.3:
                print("Your average letter grade for grades given is an C+")
            elif GPA >= 2.0:
                print("Your average letter grade for grades given is an C")
            elif GPA >= 1.7:
                print("Your average letter grade for grades given is an C-")
            elif GPA >= 1.3:
                print("Your average letter grade for grades given is an D+")
            elif GPA >= 1.0:
                print("Your average letter grade for grades given is an D")
            elif GPA >= 0.7:
                print("Your average letter grade for grades given is an D-")
            else:
                print("Your average letter grade for grades given is an F")
        elif user_choice == "exit":
            raise SystemExit