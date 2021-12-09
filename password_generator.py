letters = list("abcdefjhijklmnopqrstuvwxyzABCDEFJHIJKLMINOPQRSTUVWXYZ")
numbers =list("0123456789")
symbols = list("!#$%&()*+")

l = [letters, numbers, symbols]

letters_number = int(input("Enter the number of letters: "))
numbers_number = int(input("Enter the number of numbers: "))
symbols_number = int(input("Enter the number of symbols: "))

last_index = 2
letters_done = 0
numbers_done = 0
symbols_done = 0

import random

password = []

for i in range(letters_number+numbers_number+symbols_number):
    choose_type = random.randint(0, last_index)
    
    element = random.randint(0, len(l[choose_type])-1)
    password.append(l[choose_type][element])
    a = str(l[choose_type].pop(element))
    if a.isdigit():
        numbers_done += 1
        if numbers_number == numbers_done:
            l.pop(choose_type)
            last_index -= 1
    elif a.isalpha():
        letters_done += 1
        if letters_done == letters_number:
            l.pop(choose_type)
            last_index -= 1
    else:
        symbols_done += 1
        if symbols_done == symbols_number:
            l.pop(choose_type)
            last_index -= 1

password = ''.join(password)
print(password)
