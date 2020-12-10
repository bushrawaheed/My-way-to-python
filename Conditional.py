print("This program is to calculate your body mass index")
weight= float(input("What's your weight in kg (e.g. 73kg)?"))
height= float(input("What's your height in meters(e.g.1.7m)?"))
bmi= weight/(height*height)
print("your bmi is:",round(bmi,2))
if(bmi<=18.5):
    classification= "underweight"
elif(bmi>18.5 and bmi<=24.9):
    classification="normal"
elif(bmi > 24.9 and bmi <= 29.9):
    classification="overweight"
else:
    classification="obesity"
print("the classification of your bmi is:",classification)
