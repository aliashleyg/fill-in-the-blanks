blanks = ['_______1________', '_______2________', '_______3________', '_______4________', '_______5________', '_______6________']
easy_string = "The programming language, " + blanks[0] + ", was named after a television show called Monty Python's Flying Circus. In Python, a " + blanks[1] + " loop makes the program run while a condition is true." + blanks[2] + " is a valuable skill to learn to find errors (or bugs) in code." + blanks[3] + " is a command that ends the program and returns the value.Python allows you to store a value in a " + blanks[4] + ".This paragraph of code inside quotation marks is called a " + blanks[5] + "."
easy_answers = ['Python', 'while', 'Debugging', 'Return', 'variable','string']
medium_string = "this is the medium string"
medium_answers = ['medium','answers','will','go','here','.']
tough_string = "this is the tough string"
tough_answers = ['tough','answers','will','go','here','.']      

    
###assigns the quiz string based on what level the user chose: easy, medium, or tough
def assign_string():
    count = 0
    while count < 3:
        difficulty = raw_input("Do you want your quiz 'easy', 'medium' or 'tough'?")
        global difficulty
        if difficulty == 'easy':
            return easy_string
        elif difficulty == 'medium':
            return medium_string
        elif difficulty == 'tough':
            return tough_string
        else:
            if count < 2:
                print "Let's try that again"
                count += 1
            else:
                return False

#####checks to confirm that input is a number
def strikes():
    count = 0
    while count < 3:
        number_of_strikes = raw_input("How many strikes do you want until your game is over?")
        if number_of_strikes.isdigit():
            confirmed_number = int(number_of_strikes)
            if confirmed_number > 2 and confirmed_number < 99:
                return confirmed_number
            else:
                if count < 2:
                    print "Please choose a number between 2 and 99 to continue. Now let's try that again."
                    count += 1
                else:
                    return False
        else:
            print "Well, that was not a number. Let's try that again."
            count += 1
    return False

###assigns the correct set of answers that pair with the chosen string
def assign_answers():
    if difficulty == 'easy':
        return easy_answers
    elif difficulty == 'medium':
        return medium_answers
    else:
        return tough_answers

###question part of the quiz
def quiz(chosen_string):
    print "Here is your quiz:"
    print chosen_string
    check_answer()
                
##def correct_answer():
    

###function to check answer as correct or incorrect

###i need to rethink the logic on this loop...still not right
def check_answer():
    count = 1
    i = 0
    answer_number = 1
    local_misses_entered = misses_entered
    while i < len(chosen_answers):
        user_answer = raw_input("What is the answer for #" + str(answer_number) + "?")
        while i < local_misses_entered:
            user_answer = raw_input("What is the answer for #" + str(answer_number) + "?")
            if user_answer == chosen_answers[i]:
                print "That's correct! Great job!"
                answer_number += 1
                i += 1
            else:
                i += 1
                print "Whoops! Try again."
        print "I'm sorry that you have reached your number of strikes. Please try again soon. Goodbye."
        break
    return "Congratulations! You won the game! Thanks for playing!"
        
difficulty = None
chosen_string = assign_string()
chosen_answers = assign_answers()    
misses_entered = strikes()
quiz(chosen_string)


        
        
        
##    while index < len(chosen_answers) + no_misses_entered:
##        answer_number = 1
##        updated_strike_count = no_misses_entered - 1
##        while count < no_misses_entered:
##            user_answer = raw_input("What is the answer for #" + str(answer_number) + "?")
##            if user_answer == chosen_answers[index]:
##                print "Great job!"
##                answer_number = answer_number + 1
##                index = index + 1
##            else:
##                print "Whoops! That answer was incorrect. But don't worry. You still have " + str(updated_strike_count) + " chance(s) left to try."
##                updated_strike_count = updated_strike_count - 1
##                count = count + 1
##                index = index + 1
##    return "I'm sorry. You are out of strikes. Please come back and try again soon."

###function to check answer as correct or incorrect
##def check_answer():
##    count = 1
##    index = 0
##    while index < len(chosen_answers) + no_misses_entered:
##        answer_number = 1
##        updated_strike_count = no_misses_entered - 1
##        while count < no_misses_entered:
##            user_answer = raw_input("What is the answer for #" + str(answer_number) + "?")
##            if user_answer == chosen_answers[index]:
##                print "Great job!"
##                answer_number = answer_number + 1
##                index = index + 1
##            else:
##                print "Whoops! That answer was incorrect. But don't worry. You still have " + str(updated_strike_count) + " chance(s) left to try."
##                updated_strike_count = updated_strike_count - 1
##                count = count + 1
##                index = index + 1
##    return "I'm sorry. You are out of strikes. Please come back and try again soon."





















##
####
####def find_blank(blanks, chosen_string, chosen_answers):
####    new_list = chosen_string.split()
####    for blanks[0] in chosen_string:
####        print chosen_answers[0]
####        return chosen_answers[0]
