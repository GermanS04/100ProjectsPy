#Random password generator
#German Salas Martinez
import random
import string

#defining options by using a list and getting randoms out of it
def optionOnly1(list1, Q):
    passw = ''
    passw = ''.join(random.choices(list1, k = Q))
    return passw

def optionOnly2(list1, list2, Q):
    passw = ''
    final_l = list1 + list2
    passw = ''.join(random.choices(final_l, k = Q))
    return passw

def optionAll(list1, list2, list3, Q):
    passw = ''
    final_l = list1 + list2 + list3
    passw = ''.join(random.choices(final_l, k = Q))
    return passw

quantity = int(input("Length of the password: "))
print("Options: \n1. Only numbers\n2. Only letters\n3. Only symbols\n4. Numbers and Letters\n5. Letters and Symbols\n6. Numbers and Symbols\n7. All")

#let the user only choose a one digit number from 1 to 7
while True:
    option = input()
    if len(option) != 1 or int(option) > 7 or int(option) < 1:
        print("Select a valid option")
    else:
        option = int(option)
        break

#list of the alphabet in upper and lower cases
letters = list(string.ascii_letters)

#list of numbers from 0 to 9
numbers = list(string.digits)

#list of special characters
symbols = list(string.punctuation)

#variable with all type of characters
classes = [numbers,letters,symbols]

#execute optionOnly1 based on the index of the option
only1 = [1,2,3]
if option in only1:
    for i in range(len(only1)):
        if i == option-1:
            print(optionOnly1(classes[i], quantity))

#execute optionOnly2 based on the index of the option until the last one of classes that it will execute with the first one of classes
only2 = [4,5,6]
if option in only2:
    for i in range(len(only2)):
        if i == option - 4:
            try:
                print(optionOnly2(classes[i],classes[i+1],quantity))
            except:
                print(optionOnly2(classes[0],classes[-1],quantity))

#execute optionAll if user choose all
if option == 7:
    print(optionAll(numbers,letters,symbols,quantity))