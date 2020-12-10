person= {"name":"Bushra Sarim","gender":"Female","age":"27", "address": "Erlangen", "phone number": "012345"}
key= input("What information do you want to know about the person? ").lower()
result = person.get(key,"That information is unavailable")
print(result)





