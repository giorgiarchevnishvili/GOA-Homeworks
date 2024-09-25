#Classwork 1: Basic List Operations
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print(fruits)

print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

fruits.append("fig")

fruits.remove("banana")

fruits[1] = "blueberry"

print("Length of fruits list:", len(fruits))


#Classwork 2: List Functions and Methods
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]

numbers.append(100)

numbers.insert(0, 5)

numbers.remove(30)

numbers.sort()

numbers.reverse()

index_of_50 = numbers.index(50)
print("Index of 50:", index_of_50)

count_of_20 = numbers.count(20)
print("Count of 20:", count_of_20)

#Classwork 3: Slicing and List Comprehensions
numbers = list(range(1, 11))

first_half = numbers[:5]

second_half = numbers[5:]

squares = [x**2 for x in numbers]

print("First half:", first_half)
print("Second half:", second_half)
print("Squares:", squares)
 
#Classwork 4: List Manipulation and Aggregation
temperatures = [72, 68, 75, 70, 78, 74, 71]

highest_temperature = max(temperatures)
print("Highest temperature:", highest_temperature)

lowest_temperature = min(temperatures)
print("Lowest temperature:", lowest_temperature)

average_temperature = sum(temperatures) / len(temperatures)
print("Average temperature:", average_temperature)

above_70 = [temp for temp in temperatures if temp > 70]

print("Temperatures above 70 degrees:", above_70)

