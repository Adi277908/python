Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#create a program that has a set of 10 elements with mutiple of 5, now try to remove it's 5th element, get the highest value and smallest value of that set and also add 33 to that set.

multiples_of_5 = {5 * i for i in range(1, 11)}
multiples_list = list(multiples_of_5)

if len(multiples_list) >= 5:
    removed_element = multiples_list.pop(4)

    
multiples_of_5 = set(multiples_list)

highest_value = max(multiples_of_5)
smallest_value = min(multiples_of_5)

multiples_of_5.add(33)

print("Updated set after removing the 5th element and adding 33:", multiples_of_5)
Updated set after removing the 5th element and adding 33: {33, 35, 5, 40, 10, 15, 50, 20, 25, 30}
print("Highest value in the set:", highest_value)
Highest value in the set: 50
print("Smallest value in the set:", smallest_value)
Smallest value in the set: 5
