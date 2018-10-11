
# coding: utf-8

# In[ ]:


import random

number = random.randint(1, 20)
tries = 0
win = False 


name = input("Hello, What is your username?")

print("Hello " + name + "." )

question = input("Would you like to play a game? [Y/N] ")
if question.lower() == "n": 
    print("Be gone with you then!")
    exit()
if question.lower() == "y":
    print("I'm thinking of a number between 1 & 20, you have 5 tries to guess what it is.")
    while not win:       
        guess = int(input("Have a guess: "))
        tries = tries + 1
        if tries == 5:
            print("You failed to guess the number within 5 tries, game over.")
            break
        if guess == number:
            win = True    
        elif guess < number:
            print("Guess Higher")
        elif guess > number:
            print("Guess Lower")

        
            print("Congrats, you guessed correctly. The number was indeed {}".format(number))
            print("it had taken you {} tries".format(tries))

