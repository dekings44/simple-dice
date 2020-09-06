''' First develop a random number within the specified range you want your dice. Which is conventionally 6. Import the random module '''

import random
'''n = random.random() * 6
print(n) '''  # This code by default generates a random number between 0 and 1.


''' The above expression return floats (that is numbers with decimal points) However, what we want is integers (That is only positive whole numbers) between 1 and 6. Hence we use the expression below '''


''' Having gotten all the range of whole numbers we need. It's time to loop make decision using if state '''

print("This is my dice simulator")
x = "y"


while x == "y":
    number = random.randint(1, 6)
    print(number)

    if number == 1:
        print("---------")
        print("|       |")
        print("|   0   |")
        print("|       |")
        print("---------")
    elif number == 2:
        print("---------")
        print("|     0 |")
        print("|       |")
        print("| 0     |")
        print("---------")
    elif number == 3:
        print("---------")
        print("|     0 |")
        print("|   0   |")
        print("| 0     |")
        print("---------")
    elif number == 4:
        print("---------")
        print("| 0   0 |")
        print("|       |")
        print("| 0   0 |")
        print("---------")
    elif number == 5:
        print("---------")
        print("| 0   0 |")
        print("|   0   |")
        print("| 0   0 |")
        print("---------")
    else:
        print("---------")
        print("| 0   0 |")
        print("| 0   0 |")
        print("| 0   0 |")
        print("---------")

    x = input(" Please press y to roll again ")

''' This is the end of the game. In it's simplest form. '''
