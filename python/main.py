
# name = input("Enter your name:")
# print(name)

# name = input("Enter Your Name")
# print("Hello " + name)
# print (f"Hello {name}")

# age = int(input("Enter your age:"))
# if age >= 18:
#     print ("You're allowed to vote.")
# else:
#     print ("You're not allowed to vote.")

# for i in range(1, 6):
#     print(i)

# number = int (input ("Enter a number:"))
# while number != 0:
#     number = int (input ("Enter a number:"))
# print("done")

# def multiply(a, b):
#     return a * b
# print(multiply(4,5))
# result = multiply(4, 5)  # stored because we used return
# print(result)  # now we can use it

# def greet(name):
#     print(f"Hello {name}")

# greet("Adrian")

# my_list = ["a", "b", "c"]
# def get_length(list):
#     return len(list)
# print(get_length(my_list))

# items = ["one", "two", "three"]
# def print_items(items):
#     for i, item in enumerate(items, 1):
#         print(f'{i}: {item}')
# print_items(items)

# number1 = int (input ("Enter number 1 here:"))
# number2 = int (input ("Enter number 2 here:"))
# sum = number1 + number2
# print(sum)

# def is_positive(number):
#     if number > 0:
#         return  True
#     else:
#         return False
# print(is_positive(-5))


# items = ["Crystal Ball", "Talisman", "Cursed Mirror", "Demon Key", "Cursed Locket"]

# for item in items:
#     if item.startswith("C"):
#         print(item)


# def count_vowels(name):
#     vowels = ["a", "e", "i", "o", "u"]
#     count = 0
#     for char in name:
#         if char in vowels:
#             count += 1
#     return count

# print(count_vowels("Adrian"))


# numbers = [10,20,30,40,50]

# def get_average(numbers):
#     return sum(numbers) / len(numbers)
# print(get_average(numbers))


# numbers = [1,2,3,4,5]

# def find_max(numbers):
#     current_max = numbers[0]
#     for number in numbers:
#         if number > current_max:
#             current_max = number
#     return current_max

# print(find_max(numbers))

# numbers = [1,2,3,4,5]

# def reverse_list(numbers):
#     for number in numbers (range[5:1:-1]):
#         return numbers
# print(reverse_list(numbers))

# numbers = [1, 2, 3, 4, 5]

# def reverse_list(numbers):
#     reversed_numbers = []
#     for i in range(len(numbers) - 1, -1, -1):
#         reversed_numbers.append(numbers[i])
#     return reversed_numbers

# print(reverse_list(numbers))

# items = ["a", "b", "a", "c", "a"]

# def count_occurences(items):
#     for i, items in enumerate(items,1):
#         print(f'{i} {items}')
# print(count_occurences(items))

# items = ["a", "b", "a", "c", "a"]

# def count_occurrences(items, value):
#     count = 0
#     for item in items:
#         if item == value:
#             count += 1
#     return count


# print(count_occurrences(items,"a"))

# name = "Adrian"
# def say_hello(name):
#     print(f'Hello {name}!')
# say_hello(name)


# age = 20

# def is_adult(age):
#     if age >= 18:
#         return True
#     else: 
#         return False
    
# print(is_adult(age))


# numbers = [1,2,3,4,5]
# def sum_list(list):
#     count = 0
#     for number in numbers:
#         count += number
#     return count
    
# print(sum_list(list))

# words = "hello"
# def is_palindrome(word):
#     if word == word[::-1]:
#         return True
#     else:
#         return False

# print(is_palindrome(words))



# def celsius_to_fahrenheit(temp):
#     return (temp * 9/5) + 32

# print(celsius_to_fahrenheit(11))

    
# password = "password123"

# def validate_password(password):
#     if len(password) >= 8:
#         return True
#     else:
#         return False
    
# print(validate_password(password))


# def get_grade(score):
#     if score >= 90:
#         grade = "A"
#     elif score >= 80:
#         grade = "B"
#     elif score >= 70:
#         grade = "C"
#     elif score >= 60:
#         grade = "D"
#     else:
#         grade = "F"
#     return(grade)

# print(get_grade(85))
    


# def greet_user(username):
#     print(f"Welcome {username}!")

# greet_user("ayadaooo")


# def is_passing(grade):
#     if grade >= 50:
#         return True
#     else:
#         return False
# print(is_passing(45))

# numbers = 2,3,4
# def multiply_list(numbers):
#     count = [1]
#     multiplied *= count 
#     return multiplied

# print(multiply_list(numbers))

# def square(number):
#     square = number * number
#     return square
# print(square(9))

# def is_negative(number):
#     if number >= 0:
#         return False
#     else:
#         return True
# print(is_negative(-7))

# def sum_list(numbers):
#     count = 0
#     for number in numbers:
#         count += number
#     return count
# print(sum_list([5, 10, 15, 20]))


# def multiply_list(numbers):
#     count = 1
#     for number in numbers:
#         count *= number
#     return count
# print(multiply_list([2, 3, 4]))

# def count_vowels(word):
#     vowels = ["a","e", "i","o","u"]
#     count = 0
#     for vowel in word:
#         if vowel in vowels:
#             count += 1
#     return count

# print(count_vowels("Adrian"))

# def find_max(numbers):
#     max_n = 0
#     for n in numbers:
#         if n > max_n:
#             max_n = n
#     return max_n
# print(find_max([3, 7, 1, 9, 4]))

# def reverse_list(numbers):
#     reverse_numbers = []
#     for n in range(len(numbers) -1, -1, -1,):
#         reverse_numbers.append(numbers[n])
#     return reverse_numbers

# print(reverse_list([1, 2, 3, 4, 5]))

# colors = ["red","green","blue","yellow", "pink"]
# print(colors[2], colors[-1]colors[0])

# numbers = [1,2,3,4,5]
# count = 0
# for n in numbers:
#     count += n
# print(count)

# games = ["GW2", "PoE", "D2", "Warframe", "Hades"]
# for i in range(0,len(games),2):
#     print(games[i])

# person = {"name": "Adrian", "city": "Edmonton", "age": "21"}
# result = person.get("city", "unknown")
# print(result)

# person = {"name": "Adrian", "city": "Edmonton", "age": "21"}
# result = person.get("city", "unknown")
# for key,value in person.items():
#     print(key,value)


# def remove_duplicates(numbers):
#     return set(numbers)
# print(remove_duplicates([1, 2, 2, 3, 3, 3, 4]))

# prices = [9.99, 15.50, 7.25, 22.00]
# count = 0
# for i in prices:
#     count += i
# print(count)

# names = ["Alice", "Bob", "Charlie"]
# ages = [25, 30, 22]
# for i in range(len(names)):
#     print(f'Name: {names[i]} Age: {ages[i]}')

# scores = [85, 92, 78, 90, 88]
# highest_score = 0
# highest_position = 0
# for i, score in enumerate(scores):
#     if score > highest_score:
#         highest_score = score
#         highest_position = i
# print(highest_score, highest_position)


# def multiply_list(numbers):
#     count = 1
#     for i in numbers:
#         count *= i
#     return count
# print(multiply_list([2, 3, 4]))

# def find_max(numbers):
#     max_number = 0
#     current_number = 0
#     for current_number in numbers:
#         if current_number > max_number:
#             max_number = current_number
#     return max_number
# print(find_max([3, 7, 1, 9, 4]))

# def count_vowels(name):
#     vowels = ["a", "e", "i", "o", "u"]
#     vowel_check = 0
#     for vowel in name:
#         if vowel in vowels:
#             vowel_check += 1
#     return vowel_check
# print(count_vowels("Mississippi"))