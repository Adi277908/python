names_set = set()

names_set.add("Alice")
names_set.add("Bob")
names_set.add("Charlie")
names_set.add("David")
names_set.add("Eve")

print("Set after adding names:", names_set)

names_set.remove("Bob")
names_set.add("Robert")

print("Set after modifying a name:", names_set)

names_set.remove("Charlie")
names_set.remove("Eve")

print("Final set after deleting names:", names_set)
