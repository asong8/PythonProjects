print("BMI Calculator")
gender = str( input("Enter your gender: ") )
Mass = input("Enter your weight in kilograms: ")
Height = input("Enter your height in meters: ")
height = float(Height)
height = height ** 2
mass = float(Mass)
BMI = (mass) / (height)
print("Your BMI is " + str(BMI))

#bank
def message(): "Weight gain is urgent"
def message2(): "You are likely underweight"
def message3(): "You are in normal range"
def message4(): "You are marginally overweight"
def message5(): "You are overweight"
def message6(): "You are very overweight or obese"
def message7(): "You are severely obese"
def message8(): "You are morbidly obese"
def message9(): "You are super obese"

if gender == "male" and BMI <17.5:
	message()
if gender == "male" and BMI <20.7 and BMI >=17.5:
	message2()
if gender == "male" and BMI >=20.7 and BMI <26.4:
	message3()
if gender == "male" and BMI >=26.4 and BMI <27.8:
	message4()
if gender == "male" and BMI >=27.8 and BMI <31.1:
	message5()
if gender == "male" and BMI >=31.1 and BMI <35:
	message6()
if gender == "male" and BMI >=35 and BMI < 40:
	message7()
if gender == "male" and BMI >=40 and BMI <50:
	message8()
if gender == "male" and BMI >=50 and BMI <=60:
	message9()

if gender == "female" and BMI <17.5:
	message()
if gender == "female" and BMI <19.1 and BMI >=17.5:
	message2()
if gender == "female" and BMI >=19.1 and BMI <25.8:
	message3()
if gender == "female" and BMI >=25.8 and BMI <27.3:
	message4()
if gender == "female" and BMI >=27.3 and BMI <32.3:
	message5()
if gender == "female" and BMI >=32.3 and BMI <35:
	message6()
if gender == "female" and BMI >=35 and BMI <40:
	message7()
if gender == "female" and BMI >=40 and BMI <50:
	message8()
if gender == "female" and BMI >=50 and BMI <=60:
	message9()
#http://halls.md/average-weight-percentile-statistics/
