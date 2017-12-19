#function to ask if user his or her name
def your_name(name):
    print "Nice to meet you, " + name + "!"
    print "Now " + name + ", are you ready to take the quiz?"

#function to ask if user is ready for quiz
def quiz_ready(quiz_time):
    counter = 0
    while counter < 3:
        if quiz_time == "yes" or quiz_time == "no":
            if quiz_time == "yes":
                print "Alright! Let's go!"
                break
            else:
                return "Bummer! Come back if you change your mind. :("
            
        else:
            if counter < 2:
                print "Whoops! That was an invalid response. Let's try that again."
                quiz_time  = raw_input("Would you like to try the quiz? Please type 'yes' or 'no'.")
                counter += 1
            else:
                print "Sorry you are having a difficult time! Please try again soon."
                return

#ask user how difficult they want the quiz to be
def difficulty(quiz_time):
    how_tough = raw_input("Are you thinking 'easy','medium' or 'difficult'?")
    counter = 0
    while counter < 3:
        if how_tough == 'easy' or how_tough == 'medium' or how_tough == 'difficult':
            if how_tough == 'easy':
                print "So you want your quiz easy, huh? Here we go!"
                quiz_time = 0
                return quiz_time
                break
            elif how_tough == 'medium':
                print "Feeling somewhere in the middle, are you? Here it is."
                quiz_time = 1
                return quiz_time
                break
            else:
                print "So you are feeling a little daring today, are you? Give it your best shot!"
                quiz_time = 2
                return quiz_time
            break
        else:
            if counter < 2:
                print "Now c'mon...you have to decide."
                how_tough = raw_input("Would you like an 'easy', 'medium', or 'difficult' quiz today?")
                counter += 1
            else:
                print "I understand...not in the mood to make such a tough decision. Come back when you want to test your knowledge."
                return

def quiz(quiz_time):
    if quiz_time == 0:
        blanks = ['_______1________', '_______2________', '_______3________', '_______4________', '_______5________', '_______6________']
        easy_string = "The programming language, _______1________, was named after a television show called Monty Python's Flying Circus. In python, a _______2________ loop makes the program run while a condition is true._______3________ is a valuable skill to learn to find errors (or bugs) in code._______4________ is a command that ends the program and returns the value.Python allows you to store a value in a _______5________.This paragraph of code inside quotation marks is called a _______6________."
        correct_answer =['Python', 'while', 'Debugging', 'Return', 'variable','string']
        print easy_string
        index = 0
        answer_number = 1
        mistake_counter = 0
        user_answer = raw_input("What is the answer for #" + str(answer_number) + "?") 
        while index < len(correct_answer):
            if user_answer == correct_answer[index]:
                print "good job!"
                index = index + 1
                answer_number += 1
            else:
                if mistake_counter < 3:
                    print "Whoops! Let's try that again."
                    user_answer = raw_input("What is the answer for #" + str(answer_number) + "?")
                    mistake_counter += 1
                else:
                    return "Thanks for trying. Come back and try again soon."
    elif quiz_time == 1:
        print "here is where my medium quiz will go"
    else:
        print "here is where my difficult quiz will go"
           
print "Hi! Thanks for stopping by. :)"
name = raw_input("What is your name?")
your_name(name)
quiz_time  = raw_input("'yes' or 'no'?")
quiz_ready(quiz_time)
print "You get to decide how tough you want this quiz to be."
difficulty(quiz_time)
quiz(quiz_time)



