test = bool
test = True
while test:
    try:
        grade1 = float(input("Type the grade of the first test : "))
    except:
        print("Invalid number! ")
        continue
    if grade1 > 20 or grade1 < 0:
        print("Grade should be between 20 and 0")
    else:
        test = False


test = True
while test:
    try:
        grade2 = float(input("Type the grade of the first test : "))
    except:
        print("Invalid number! ")
        continue
    if grade2 > 20 or grade2 < 0:
        print("Grade should be between 20 and 0")
    else:
        test = False


avg_grade = (grade1 + grade2) / 2
print("The average grade : ", avg_grade)