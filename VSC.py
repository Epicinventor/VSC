### clr screen function ###
import os

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

clear_terminal()


### startup for the robot ###
def startup():
    print('''Welcome. My name is VSC. I am a python-coded robot that helps you in
        everyday tasks. If you ever want any support, I'm here.
        
        Let's Start with the basics. What is you're name?''')

    Name = input("Name > ").lower()
    print('''I see. Now, what is your age. This will tell how we can
        personalize your experience''')
    age = int(input("age > "))
    print('''This is your age? You sure?
        Double check the Data and say yes or no.''')

    print(f"Your name is {Name}, and your age is {age}. Is that right?")
    print("type 'y' for yes")
    config = input("Is this right? > ").lower()
    if config == "y":
        print("Okay")
    else:
        print("Then try again")
        clear_terminal()
        startup()

    if age == [9,10,11,12]:
        print("Some features will be limited for your account")
    elif age == [13,14,15,16,17,18]:
        print("3/4 of the features in the application will be limited")
    else:
        print('''Welcome to VSC.
              Let's start your journey''')

def resume():
    print("What would your first question like to be?")

clear_terminal()
startup()
