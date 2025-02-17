students = [
    (101, "Alice", 20),
    (102, "Bob", 21),
    (103, "Charlie", 19),
    (104, "David", 22)
]

roll_nos = []
names = []
ages = []

for student in students:
    roll_nos.append(student[0])
    names.append(student[1])
    ages.append(student[2])


    
print("Roll Numbers:", roll_nos)
print("Names:", names)
print("Ages:", ages)


