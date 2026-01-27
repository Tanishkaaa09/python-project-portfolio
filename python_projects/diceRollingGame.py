#ask:Roll the dice?
'''
if user enters y,
    generate random number between 1 to 6
    print the number
if user enters n,
    print("Thank you for playing")
    Terminate the program
else
    print("Game Over")
'''
import random
while True:
    choice=input("Roll the dice? (y/n): ").lower()
    if choice=='y':
        die1=random.randint(1,6)
        die2=random.randint(1,6)
        print(f'({die1},{die2})')
    elif choice=='n':
        print('Thank you for playing')
        break
    else:
        print('Game Over,please enter y or n only')
