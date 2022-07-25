# functions go here
import random
# welcome user to the game
print()
print()
print("Welcome to cargans math quiz")
print()
print()
#list of valid responses for yes no
yes_no_list = ["yes", "no"]
# ask user if they have played b4 and if not show instructions
error = "Please awnser yes / no"
def choice_checker(question, valid_list, error):
    valid = False
    while not valid:
        #ask user for choice (and put in lowercase)
        response = input(question).lower()
        # iterates through list and if response is an item
        # in the list (or the first letter of an item), the 
        # full item name is returned
        for item in valid_list:
            if response == item[0] or response == item:
                return item
            # output error if item not in list 
        print(error)
        print()
# displays instructions / rules
def instructions():
     print()
     print()
     print()
     print("              ***** How to Play *****")
     print()
     print("****Youll be asked how many questions you want****")
     print()
     print("****Youll be asked basic maths addition questions.****")
     print()
    
     print()
     print("               ****goodluck!!****")
     print()
     return""
# ******** Main routine goes here ... **********
# list of valid responses
awnsers = ["int between 0 and 40 "]

#what to do based on played before response 
question = "Have you played the quiz before? "
played_before = choice_checker(question, yes_no_list, error)
if played_before == "no":
    instructions()
# Checks for integers, optionally includes min / max values
def intcheck(question, low=None, high=None, exit_code = None):
    while True:
        # sets up error messages
        if low is not None and high is not None:
            error = "Please enter an integer between {} and {} (inclusive)".format(low, high)
        elif low is not None and high is None:
            error = "Please enter an integer that is more than or equal to {}".format(low)
        elif low is None and high is not None:
            error = "Please enter an integer that is less than or equal to {}".format(high)
        else:
            error = "Please enter an integer"
        try:
            response = input(question)
            # check to see if response is the exit code and return it
            if response == exit_code:
                return response
            # elif response == "xxx":
            #     print("Thanks for playing")
            #     break
            # change the response into an integer
            else:
                response = int(response)
            # Checks response is not too low, not use of 'is not' keywords
            if low is not None and response < low:
                print(error)
                continue
            # Checks response is not too high
            if high is not None and response > high:
                print(error)
                continue
            return response
        # checks input is a integer
        except ValueError:
            print(error)
            continue
# intialsing variables and game summary list goes here
rounds_played = 0
rounds_won = 0
questions_correct = 0
questions_wrong = 0
mode = "regular"
rounds = intcheck("How many questions <enter> for infintite: ", 1, exit_code = "")
if rounds == "":
    # print("you chose infinite mode")
    mode = "infinte"
    rounds = 5
def num_check(question, low, high):
    error = "Please enter a whole number between {} and {}".format(low, high)
    valid = False
    while not valid:
        try:
            # Ask the question
            response = int(input(question))
            # if the amount is too low / too high give
            if low < response <= high:
                return response

            # output and error
            else:
                print(error)

        except ValueError:
            print(error)
low_num = 0
high_num = 20
#  Rounds loop starts here
end_game = "no"
while end_game == "no" and rounds_played < rounds:
    # print round number
    print()
    if mode == "infinte":
        print("*** Rounds #{} ***".format(rounds_played + 1))
        rounds_played += 1
        rounds += 1
    else:
        print("*** Round #{} of {} ***".format(rounds_played + 1, rounds))
        rounds_played += 1
    #generate 2 numbers for the question
    num = random.randint(low_num, high_num)
    second_num = random.randint(low_num, high_num)
    #generate awnser
    awnser = num + second_num
    #generate question
    question = ("What does {} + {} =".format(num , second_num))
    print()
    #get users awnser
    response = intcheck(question, exit_code="xxx") # replace with function call when integrating!!
    #tells user if they got it right or wrong
    if response == awnser:
        print()
        feedback ="Well done thats correct"
        print(feedback)
        result = "correct"
        questions_correct += 1
        print()
    elif response == "xxx":
        print()
        print("Thanks for playing")
        print()
        break
    else:
        print()
        feedback ="Sorry thats incorrect, the right awnser is {}".format(awnser)
        print(feedback)
        result = "incorrect"
        questions_wrong += 1
        print()
    if response == "":
        print("Please enter your awnser", question)
if response == "xxx" or rounds == rounds_played:
    print()
    print("All done, you got {} questions wrong and {} questions right".format(questions_wrong, questions_correct))
    print()