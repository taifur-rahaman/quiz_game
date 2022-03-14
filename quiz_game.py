from tkinter import Y


print("Simple Text Quiz Game")  # game_name

print("Welcome to the Quiz Game")  # welcome message

choice = input("Do you want to Play? ")

if choice.lower() != "yes":
    choice_quit = input("you want to quit now?(y/n)\n")
    if choice_quit == "y":
        quit(0)   # built in python function which is used to exit a program
    else:
        pass

print("Thank you for choosing to Play")

score = 0  # score board


#question - 1
question = input("What is the correct abbribiation of CPU? ")
if question.lower() == "central proccesing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")

#question - 2
question = input("What is the correct abbribiation of RAM? ")
if question.lower() == "random access memory":
    print("Correct")
    score += 1
else:
    print("Incorrect")

#question - 3
question = input("What is the correct abbribiation of ROM? ")
if question.lower() == "read only memory":
    print("Correct")
    score += 1
else:
    print("Incorrect")

#question - 4
question = input("What is the correct abbribiation of PSU? ")
if question.lower() == "power supply unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")

#question - 5
question = input("What is the correct abbribiation of BIOS? ")
if question.lower() == "basic input output system":
    print("Correct")
    score += 1
else:
    print("Incorrect")


print(f"Your score is {score} and you got {(score/5)*100}% mark")
