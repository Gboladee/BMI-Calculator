#Calculate your body mass index today
Name = input("Hello, what is your name? ")

print("Okay", Name , " I would like to ask you some questions okay? ")

Weight = int(input("What do you weigh in kilograms?: "))

Height = float(input("How tall are you in meters?: "))

bmi = Weight/(Height*Height)
print(bmi) 
if bmi <= 18.5:
    print("you're underweight, " + Name)
elif (bmi > 18.5 and bmi < 24.9):
    print("your BMI is within range, " + Name)
elif (bmi > 25.0 and bmi < 39.9):
    print("You're Overweight, " + Name)
elif bmi > 40.0:
    print("You're Morbidly Obese, " + Name)
else:
    print("You're Obese, "+ Name)