#this program is for error handling

grade = input("type your grade:")
try:
    grade = int(grade)
    print("the grade is:",grade)
except:
    print("invalid grade")
