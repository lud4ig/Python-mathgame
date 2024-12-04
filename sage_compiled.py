import random
import json
from utils import delay_message, clear_screen

with open("sage_data.json", "r") as file:
    sage_data = json.load(file)

def meet_sage(skill_lvl, count, player_class=""): 
    print(sage_data["INDEX_FOR_SAGE_ASCII"])
    
    if count == 0:
        print(sage_data["INDEX_FOR_FIRST_ENCOUNTER"]["INDEX_FOR_WELCOME"])
        delay_message()
        clear_screen()

    print(sage_data["INDEX_FOR_SAGE_ASCII"])
    print(sage_data["INDEX_FOR_SAGE_WELCOME"][str(skill_lvl)][0])
    delay_message()
    clear_screen()
    
    print(sage_data["INDEX_FOR_SAGE_ASCII"])    
    print(sage_data["INDEX_FOR_SAGE_TEACHINGS"][str(skill_lvl)])
    delay_message()
    clear_screen()
    
    print(sage_data["INDEX_FOR_SAGE_ASCII"]) 
    questions = random.sample(list(saga_data["INDEX_FOR_SAGE_QUIZ"][str(skill_lvl)].keys()), 2)
    
    score = 0
    for i in questions: 
        question_text = saga_data["INDEX_FOR_SAGE_QUIZ"][str(skill_lvl)][i]["INDEX_FOR_QUESTION"]
        correct_answer = sage_data["INDEX_FOR_SAGE_QUIZ"][str(skill_lvl)][i]["INDEX_FOR_CORRECT_ANSWER"]
        
        print(question_text)
        user_answer = input("Your answer: ")
        if user_answer == "" or not user_answer.isdigit():
                print("Invalid input! Moving to the next question.")
                delay_message()
                clear_screen()
        else:
            if int(user_answer) == correct_answer:
                print("Correct!")
                score += 1
                delay_message()
                clear_screen()
            else:
                print("Wrong answer.")
                delay_message()
                clear_screen()
                
    print(sage_data["INDEX_FOR_SAGE_ASCII"]) 
        
    if score >= 1:
        skill_lvl += 1
        print(f"{sage_data[INDEX_FOR_SAGE_CONGRATULATIONS][str(skill_lvl)]} Your skill level is now {skill_lvl}. You have learned a new skill.")
        delay_message()
        
 
    else:
        print(f"{sage_data[INDEX_FOR_SAGE_BOO][str(skill_lvl)]} Your skill level is now {skill_lvl}. You have learned a new skill.")
        delay_message()
    
    count += 1
    return (skill_lvl, count)