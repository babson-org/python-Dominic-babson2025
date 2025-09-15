
from classes.week00.second_class.utils import clear_screen
'''
#13 - Conditional Logic
Ask the user for a number and print whether it is positive, negative, or zero.
'''
# enter code here
while True:
     try: 
        input_number = int(input("Enter a number:"))
        break
     except: 
        ValueError
if input_number > 0:
    print("Your number is positive")
elif input_number < 0:
    print("Your number is negative")
else:
    print("Your number is 0")


pause=input('pause')
clear_screen()

'''
#14 - Even/Odd Check
Ask the user for a number and print if it is even or odd.
'''
# enter code here
while True:
     try: 
        ur_number = int(input("Enter a number:"))
        break
     except: 
        ValueError
if (ur_number % 2 == 0):
     print("Ur number is even")
else:
     print("Ur number id odd")



pause=input('pause')
clear_screen()

'''
#15 - Boolean Operators
Ask the user for two numbers and check if both are positive, either is positive, or none is positive.
'''
# enter code here
while True:
     try: 
        my_int = int(input("Enter a number:"))
        break
     except: 
        ValueError
while True:
     try: 
        my_int2 = int(input("Enter a number:"))
        break
     except: 
        ValueError 
if (my_int > 0) & (my_int2 > 0):
    print("Both of your numbers are positive")
elif (my_int < 0) & (my_int2 < 0):
        print("Both of your numbers are negative")
else:
    print("One of your numbers is positive and one is negatve")

pause=input('pause')
clear_screen()

'''
#16 - For Loop
Print all numbers from 1 to 20, skipping multiples of 3.
'''
# enter code here
for i in range(21):
     if i % 3 == 0:
          pass
     else:
          print(i)

pause=input('pause')
clear_screen()

'''
#17 - While Loop
Ask the user to guess a secret number (hardcoded) until they get it right.
'''
# enter code here
secret = 3
number = int(input("put in number"))


'''
#18 - Break / Continue
Print numbers 1-10 but stop printing when you reach 7 and skip 3.
'''
# enter code here
i = 1
while i < 10:
     if i == 3:
        i += 1
     elif i == 7:
          print(i)
          break
     else:
          print(i)
          i += 1


pause=input('pause')
clear_screen()

'''
#19 - Function Definition
Write a function square(x) that returns the square of a number and test it.
'''
# enter code here
def square(x):
     return x ** 2 
print(square(3))


pause=input('pause')
clear_screen()

'''
#20 - Function with Mutable Argument
Write a function add_item(lst, item) that appends item to lst and observe the effect on the original list.
'''
# enter code here
lst = []
def add_item(lst, item):
     lst.append(item)
     print(lst)
add_item(lst, "hello")
add_item(lst, "poop")
add_item(lst, "skibidi")


pause=input('pause')
clear_screen()

'''
#21 - Comments / Documentation
Write a function greet(name) with single-line and multi-line comments explaining each step.
'''
# enter code here
def greet(name):
     print(f"Hello {name} how are you")
greet("dom")

pause=input('pause')
clear_screen()

'''
#22 - Combining Tools
Ask the user to enter 5 names. Store them in a list, capitalize each name, sort the list, and print it.
'''
# enter code here
names_list = []
for i in range(5):
    user_input = input("Enter a name: ")
    user_input = user_input.capitalize()
    names_list.append(user_input) 
print(names_list)



pause=input('pause')
clear_screen()

