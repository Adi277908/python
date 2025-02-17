names = [
    ("John",), 
    ("Mike",), 
    ("Tom",), 
    "Alice", 
    "Sophia", 
    ("David",), 
    "Emma"
]

boys_count = 0
girls_count = 0

for name in names:
    if isinstance(name, tuple):
        boys_count += 1
    else:
              girls_count += 1


print("Number of boys:", boys_count)
print



