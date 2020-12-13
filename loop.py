import random
people = []

for x in range(0,4):
    person = input("type the name of a person:")
    people.append(person)

index=random.randint(0,3)
random_person= people[index]
print("Picking a random person:",random_person)
