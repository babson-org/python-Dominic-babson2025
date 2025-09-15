from classes.week00.second_class.utils import clear_screen
'''
# 1

Write down the steps a program would need to make a cup of tea. Then implement a Python 
function make_tea() that prints each step.
'''
# enter your code here
'''
Steps to make a cup of tea from chat gpt:
* Boil water.
* Place a tea bag (or loose tea in an infuser) into a cup.
* Pour the hot water over the tea.
* Let it steep for 3-5 minutes (adjust based on tea type and preference).
* Remove the tea bag or infuser.
* Add milk, sugar, honey, or lemon if desired.
* Stir and enjoy!
'''
def make_tea():
    print("Boil water.")
    print('Place a tea bag (or loose tea in an infuser) into a cup.')
    print('Pour the hot water over the tea.')
    print('Let it steep for 3-5 minutes (adjust based on tea type and preference).')
    print('Remove the tea bag or infuser.')
    print('Add milk, sugar, honey, or lemon if desired.')
    print('Stir and enjoy!')

make_tea()


pause=input('pause')
clear_screen()
'''
#2

Given a list [2, 4, 6, 8, 10], write a program that prints the next three numbers in the list.  
(the ones after 10)
'''
# enter your code here
def skip_two():
    for i in range(3):
        number = 12
        print(number)
        number = number + 2

skip_two()


pause=input('pause')
clear_screen()
'''
#3

Write a program that asks the user for their first and last name, then prints a greeting:
"Hello, <first name> <last name>!"
'''
# enter your code here
def greeting():
    first_name = input("What is your first name?")
    last_name = input("What is your last name?")
    print("Hello, " + first_name + last_name)

greeting()


pause=input('pause')
clear_screen()
'''
#4

Write a program that prints your Python version and platform using the sys and platform modules.
'''
# enter your code here


pause=input('pause')
clear_screen()
'''
#5

Ask the user to input two numbers. Calculate and print their sum, difference, product, 
and division (both / and //).
'''
# enter your code here
def do_math():
    number_1 = int(input("Enter a number"))
    number_2 = int(input("Enter another number"))
    print(number_1 + number_2)
    print(number_1 - number_2)
    print(number_1 * number_2)
    print(number_1 / number_2)
    print(number_1 // number_2)
do_math()

pause=input('pause')
clear_screen()
'''
#6

Ask the user to input a sentence. Print it in uppercase, lowercase, with the first letter 
capitalized, and split it into words.
'''

# enter your code here


pause=input('pause')
clear_screen()
'''
#7

Calculate the result of the following without parentheses and then with parentheses:
10 + 2 * 5 / 2 - 3 ** 2
'''
# enter your code here


pause=input('pause')
clear_screen()
'''
#8

Create a list of your three favorite foods. Replace the second item with a new one, 
then print the list.
'''
# enter your code here
my_list = ["soup", "pasta", "pizza"]
my_list[1] = "ice cream"
print(my_list)

pause=input('pause')
clear_screen()
'''
#9

Create a tuple with four numbers. Try to change the first number (observe the error) 
and then print the tuple.
'''
# enter your code here
dom_tuple = (1, 2, 3, 4)
print(dom_tuple)

pause=input('pause')
clear_screen()
'''
#10

Create a dictionary representing a student (name, age). Update the age. Create a list of 
favorite numbers and add a new number.
'''
# enter your code here


pause=input('pause')
clear_screen()
'''
#11

Ask the user to input their favorite quote. Save it to a file quotes.txt 
and read it back to print it.
'''
# enter your code here


pause=input('pause')
clear_screen()
'''
#12
Ask the user to input 5 numbers (one at a time), store them in a list, and print the sum and average.
'''
# enter your code here


pause=input('pause')
clear_screen()