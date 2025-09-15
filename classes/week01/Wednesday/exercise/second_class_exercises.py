#%%
# print 'hello' 5 times using an arithmetic operator
print('hello' * 5)

#%%
# print 'hello' 5 times using a loop

for i in range(5):
    print('hello')
#%%
# print 'hello' 5 times on the same line using a loop
word = ''
for i in range(5):
    word += 'hello'
print (word)
#%%
''' using nested loops print the following:

00 01 02
10 11 12
20 21 22

'''
for i in range(3):
    for j in range(3):
        print(str(i) + str(j), end = " ")
    print(" ")

#%%
# define txt and input some text from the keyboard into it
txt = 'my name is Dom'
#%%
# print each letter in txt 
for i in range(len(txt)):
    print(txt[i])
#%%
# assign the variable letter to the first letter in txt

'''
say txt = 'the cat in the hat was read today'
't' is the first letter

result: tttt
'''
letter = txt[0]
#%%
# print out all the letters in txt that are equal to the first letter
for i in range(len(txt)):
    new_letter = txt[i]
    if new_letter == letter:
        print(new_letter)
#%%
'''
# suppose we had a list of n elements. create a new list that
  shifts the elements by 3

    myList = ['apple', 'orange', 'pear', 'blueberry', 'peach']
      shifted_list = ['pear', 'blueberry', 'peach', 'apple', 'orange']

        Hints:
             1) use len(), %, enumerate
                  2) also assign shifted_list = [None] * length  (you'll need to determine 
                          the length variable)
                               3) shift inside the for loop
                                    4) print out the printed list outside the for loop
                                    '''



                                    # %%
names_list = ["Tommy", "Dom", "Ambre", "Tom", "Phil"]
shifted_names = []
for i in range(len(names_list)):
    new_index = (i + 3) % len(names_list)
    shifted_names.append(names_list[new_index])
print(shifted_names)
    