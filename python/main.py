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

# def greet_user(username):
#     print(f"Welcome, {username}!")

# greet_user("ayadaooo")


# def is_even(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False
# print(is_even(7))


# def multiply_list(numbers):
#     count = 1
#     for number in numbers:
#         count *= number
#     return count

# print(multiply_list([2,3,4]))

# word = ["a", "b", "c", "d", "e"]

# def first_and_last(word):
#     return [word[0], word[-1]]

# print(first_and_last(word))


# def square(number):
#     total = number * number
#     return total
# print(square(6))

# def is_positive(number):
#     if number > 0:
#         return True
#     else:
#         return False
# print(is_positive(-3))

# def count_items(items):
#     count = 0
#     for i in items:
#         count += 1
#     return count

# print(count_items(["a", "b", "c", "d"]))

# def repeat_string(word,a):
#     return word * a
# print(repeat_string("hello",3))

# def celsius_to_fahrenheit(temp):
#     return (temp * 9/5) + 32
# print(celsius_to_fahrenheit(0))

# def fizzbuzz(number):
#     if number % 3 == 0 and number % 5 == 0:
#         return ("FizzBuzz")
#     if number % 3 == 0:
#         return ("Fizz")
#     elif number %  5 == 0:
#         return ("Buzz")
#     else:
#         return (number)

# print(fizzbuzz(15))

# def get_initials(first_name,last_name):
#     initials = first_name[0] + "." + last_name[0]
#     return initials.upper()
# print(get_initials("Adrian", "Yadao"))

# def longest_word(list):
#     longest = list[0]
#     if len(list) > len(longest):
    

#     return longest
# print(longest_word(["cat", "elephant", "dog", "rhinoceros"]))