name = input("Name: ")
Section = input("Section: ")
prelim = float(input("Prelim Term Grade: "))
midterm= float(input("Mid Term Grade: "))
finals = float(input("Final Term Grade: "))
final_grade = round((prelim*0.3333)+(midterm* 0.3333)+(finals* 0.3333))
print("Final Grade = " + str(final_grade))

## error input by the user if they enter a grade less than 40
if prelim <= 40:
    print("Please enter  a valid grade for the Prelim Term")
if midterm <= 40:
    print("Please enter  a valid grade for the Mid Term")
if finals <= 40:
    print("Please enter  a valid grade for the Final Term")
    
## Calculation for the gpa
if final_grade >= 99 and  final_grade <= 100:
    print("Your GPA is 1.00.")
elif final_grade >= 96 and  final_grade <= 98:
    print ("Your GPA is 1.25.")
elif final_grade >= 93 and  final_grade <= 95:
    print ("Your GPA is 1.50.")
elif final_grade >= 90 and  final_grade <= 92:
    print ("Your GPA is 1.75.")
elif final_grade >= 87 and  final_grade <= 89:
    print ("Your GPA is 2.00.")
elif final_grade >= 84 and  final_grade <= 86:
    print ("Your GPA is 2.25.")
elif final_grade >= 81 and  final_grade <= 83:
    print ("Your GPA is 2.50.")
elif final_grade >= 78 and  final_grade <= 80:
    print ("Your GPA is 2.75.")
elif final_grade >= 75 and  final_grade <= 77:
    print ("Your GPA is 3.00.")
elif final_grade >= 40 and  final_grade <= 74:
    print ("Your GPA is Below 75.")
## Error if the user input a non-numeric value
else:
    print ("Invalid Grade")