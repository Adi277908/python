#write a program to create a set containing 10 random numbers in the range 15 to 45.Count how many of these numbers are less than 30 . Delete all numbers that are greater than 35.
import random

random_numbers = {random.randint(15, 45) for _ in range(10)}

count_less_than_30 = sum(1 for number in random_numbers if number < 30)

random_numbers = {number for number in random_numbers if number <= 35}

print("Original set of random numbers:", random_numbers)
print("Count of numbers less than 30:", count_less_than_30)
print("Updated set after removing numbers greater than 35:", random_numbers)
