import os
import pickle

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

clear_terminal()

version = 1.1
account_data = []


def startup():
    global account_data

    # Attempt to load account data from the file
    try:
        with open("account_data.pkl", "rb") as f:
            account_data = pickle.load(f)
    except FileNotFoundError:
        # If the file doesn't exist, create a new account
        print(f'''Welcome. My name is VSC {version} . I am a python-coded robot that helps you in
        everyday tasks. If you ever want any support, I'm here.

        Let's Start with the basics. What is you're name?''')
        print()
        print()

        Name = input("Name > ").lower()
        print('''I see. Now, what is your age. This will tell how we can
        personalize your experience''')
        print()
        age = int(input("age > "))
        print('''This is your age? You sure?
        Double check the Data and say yes or no.''')
        print()
        account_data = [Name, age]

        print(f"Your name is {Name}, and your age is {age}. Is that right?")
        print("type 'y' for yes")
        print()
        config = input("Is this right? > ").lower()
        if config == "y":
            print("Okay")
        else:
            print("Then try again")
            clear_terminal()
            startup()

        # Save the new account data
        with open("account_data.pkl", "wb") as f:
            pickle.dump(account_data, f)

    if age in [9,10,11,12]:
        print()
        print("Welcome To VSC")
        print("Some features will be limited for your account")
    elif age in [13,14,15,16,17,18]:
        print()
        print("3/4 of the features in the application will be limited")
    else:
        print()
        print('''Welcome to VSC.
        Let's start your journey''')

def resume():
    clear_terminal()
    print("What would your first question like to be?")
    print(f"Version {version} have specified questions. This is not Chat GPT or Google Gemini.")
    questions = ["1. Math","2. Updates Log","3. Feedback"]


clear_terminal()
startup()
