blanks = ['_______1________', '_______2________', '_______3________', '_______4________', '_______5________', '_______6________']
easy_string = "The programming language, " + blanks[0] + ", was named after a television show called Monty Python's Flying Circus. In Python, a " + blanks[1] + " loop makes the program run while a condition is true." + blanks[2] + " is a valuable skill to learn to find errors (or bugs) in code." + blanks[3] + " is a command that ends the program and returns the value.Python allows you to store a value in a " + blanks[4] + ".This paragraph of code inside quotation marks is called a " + blanks[5] + "."
easy_answers = ['Python', 'while', 'Debugging', 'Return', 'variable','string']
medium_string = "this is the medium string"
medium_answers = ['medium','answers','will','go','here','.']
hard_string = "this is the hard string"
hard_answers = ['hard','answers','will','go','here','.']         

#confirms user input is valid and returns appropriate value for quiz assignment
def choose_level(user_difficulty_choice):
    valid_difficulty_choice = ['easy','medium','hard']
    if user_difficulty_choice in valid_difficulty_choice:
        return user_difficulty_choice
    else:
        while user_difficulty_choice not in valid_difficulty_choice:
            user_difficulty_choice = raw_input("Please select the level of difficulty for your quiz: 'easy', 'medium', or 'hard'")
    return user_difficulty_choice          

#assigns appropriate quiz from user input
def assign_quiz(user_difficulty_assignment):
    if user_difficulty_assignment == 'easy':
        return easy_string
    elif user_difficulty_assignment == 'medium':
        return medium_string
    else:
        return hard_string

#assigns appropriate answers from user input
def assign_answers(user_difficulty_assignment):
    if user_difficulty_assignment == 'easy':
        return easy_answers
    elif user_difficulty_assignment == 'medium':
        return medium_answers
    else:
        return hard_answers

def find_blank_in_string (blank_to_fill, blanks):
    for str in blanks:
        if str in blank_to_fill:
            return str
        else:
            return None

def update_list (user_answer,chosen_quiz, blanks):
    updated_quiz_string = []
    chosen_quiz_as_list = chosen_quiz.split()
    for i in chosen_quiz_as_list:
        if find_blank_in_string(i, blanks):
            if find_blank_in_string(i,blanks) < i:
                updated_quiz_string.append(user_answer + ',')
            else:
                updated_quiz_string.append(user_answer)
        else:
            updated_quiz_string.append(i)
    return ' '.join(updated_quiz_string)
    
           
#checks user answer against chosen string
def check_answer(chosen_quiz,chosen_answers):
    question_number  = 0
    while question_number < len(blanks):
        user_answer = raw_input("What is the answer to " + blanks[question_number] + "?")
        print update_list(user_answer, chosen_quiz, blanks)
        while user_answer != chosen_answers[question_number]:
            user_answer = raw_input("What is the answer to " + blanks[question_number] + "?")
        question_number += 1
    print "Congratulations! You completed the quiz! Thanks for playing. Goodbye."


user_difficulty_choice = raw_input("Please select the level of difficulty for your quiz: 'easy', 'medium', or 'hard'")
user_difficulty_assignment = choose_level(user_difficulty_choice)
chosen_quiz = assign_quiz(user_difficulty_assignment)
print chosen_quiz
chosen_answers = assign_answers(user_difficulty_assignment)
fill_blank_with_answer = check_answer(chosen_quiz,chosen_answers)

           
