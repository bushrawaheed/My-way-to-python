months=("january","febuary","March","April","May","june","july","August","September","October","November","December")
birthday=input("Type your birthday in a form of DD-MM-YYYY:")
index= int(birthday[3:5])-1
bd_months= months[index]
print("your birthday month is:",bd_months)