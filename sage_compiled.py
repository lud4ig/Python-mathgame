# Teaching and Quiz 

import random
from sage_dialogue import sage_dialogue
from sage_ascii_teach_quiz import sage, sage_teaching, quiz
from utils import delay_message 

#To be in main code


def meet_sage(skill_lvl, count): 
    score = 0
    print(random.choice(sage[skill_lvl-1])) # Display 1 random sage for that level
    
    if count == 0:  # For first encounter or sage, explain what sage is 
        print(sage_dialogue["first_encounter"]["welcome"])
    
    print(sage_dialogue[str(skill_lvl)]["welcome"])  # Display welcome message 
    delay_message() # Requires user to press enter to continue
    print(sage_teaching[str(skill_lvl)]) # Display teaching content 
    delay_message()
    print(sage_dialogue[str(skill_lvl)]["quiz_time"]) # Display quiz 
    questions = random.sample(list(quiz[str(skill_lvl)].keys()), 2)  # Choose 2 random question from approprate level 
    
    # For each question 
    for i in questions: 
        question, correct_answer = quiz[str(skill_lvl)][i]  # Get the question and answer 
        print(question)  # Print the question 

        user_answer = input("Your answer: ")  # Get user input 
        if user_answer =="" or user_answer.isalpha() or not user_answer.isalnum(): # if input not numbers
            score = score
        else:  # If input is numbers 
            user_answer = float(user_answer) 
            if user_answer == correct_answer: 
                score += 1 
            else: 
                score = score 
        
    if score >= 1: # If pass quiz
        print(sage_dialogue[str(skill_lvl)]["correct"])
        skill_lvl = skill_lvl + 1 
 
    else: # If fail quiz
        print(sage_dialogue[str(skill_lvl)]["wrong"])
    
    count += 1 # To record if it is the first time encountering sage 
    return (skill_lvl, count)
        
    

    
