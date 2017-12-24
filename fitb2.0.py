blanks = ['_______1________', '_______2________', '_______3________', '_______4________', '_______5________', '_______6________']
easy_string = "The programming language, " + blanks[0] + ", was named after a television show called Monty Python's Flying Circus. In Python, a " + blanks[1] + " loop makes the program run while a condition is true." + blanks[2] + " is a valuable skill to learn to find errors (or bugs) in code." + blanks[3] + " is a command that ends the program and returns the value.Python allows you to store a value in a " + blanks[4] + ".This paragraph of code inside quotation marks is called a " + blanks[5] + "."
easy_answers = ['Python', 'while', 'Debugging', 'Return', 'variable','string']
medium_string = "this is the medium string"
medium_answers = ['medium','answers','will','go','here','.']
tough_string = "this is the tough string"
tough_answers = ['tough','answers','will','go','here','.']         


#assigns the quiz string based on what level the user chose: easy, medium, or tough
def assign_string(difficulty):
    count = 0
    while count < 3:
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
                difficulty = raw_input("Do you want your quiz 'easy', 'medium' or 'tough'?")
            else:
                print "Sorry you are having such a difficult time. Come back and try again soon. Goodbye."
                return
           
#assigns the correct set of answers that pair with the chosen string
def assign_answers(difficulty):
    if difficulty == 'easy':
        return easy_answers
    elif difficulty == 'medium':
        return medium_answers
    else:
        return tough_answers

def total_strikes(number_of_strikes):
    count = 0
    while count < 3:
        if number_of_strikes == int:
            if number_of_strikes > 2 and number_of_strikes < 99:
                return number_of_strikes
            else:
                if count < 2:
                    print "Please choose a number between 2 and 99 to continue."
                    count += 1
                else:
                    print "Sorry you are having so much trouble. Please come back soon and try again."
                    return

print 'Welcome to my "fill-in-the-blanks" challenge!'
difficulty = raw_input("Do you want your quiz 'easy', 'medium' or 'tough'?")    
chosen_string = assign_string(difficulty)
chosen_answers = assign_answers(difficulty)
number_of_strikes = input("How many strikes do you want until your game is over?")
chosen_strike_number = total_strikes(number_of_strikes)
quiz(chosen_string,chosen_answers)















##def check_answer(user_answer, number_of_strikes):
##    count = 1
##    index = 0
##    while count <= number_of_strikes:
##        if user_answer == chosen_answers[index]:
##            print "Great job!"
##            find_blank(blanks, chosen_string,chosen_answers)
##            break
##        else:
##            new_nos = int(number_of_strikes) - 1
##            print "Whoops! That answer was incorrect. But don't worry. You still have " + str(new_nos) + " chances left to try"
##            count = count + 1
##            user_answer = raw_input("What is the answer for #" + str(answer_number) + "?")
##
##def find_blank(blanks, chosen_string, chosen_answers):
##    new_list = chosen_string.split()
##    for blanks[0] in chosen_string:
##        print chosen_answers[0]
##        return chosen_answers[0]
##        
    

## 
##def check_answer(user_answer, chosen_answers, number_of_strikes):
##    counter = 0
##    index = 0
##    while counter < number_of_strikes:
##        if user_answer == chosen_answers[index]:
##            print "Great job!"
##            return
##        else:
##            print "Whoops! Let's try that again."
##            number_of_strikes = input("How many strikes do you want until your game is over?")
##            counter += 1
##
##
##
##    
##
##def quiz(chosen_string,chosen_answers):
##    print chosen_string
##    answer_number = 1
##    index = 0
##    while index < len(chosen_answers):
##        user_answer = raw_input("What is the answer for #" + str(answer_number) + "?")
##        check_answer(user_answer, chosen_answers, number_of_strikes)
##        index = index + 1
##        answer_number = answer_number + 1
##
##
##
##
