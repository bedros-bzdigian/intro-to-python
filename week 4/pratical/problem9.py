correct_num = 5
guess = int (input ("please enter a number: "))
for x in range (0,10):
    if guess == correct_num:
        print ("That was a great guess!")
        break
    else:
        guess= int (input("please enter another number: "))     