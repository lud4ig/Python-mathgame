import json
import random 
from utils import delay_message, clear_screen, colors

# To load json file 
with open("assets/sage.json", 'r') as f:
    sage_data = json.load(f)

with open("assets/skills.json", 'r') as f:
    skills = json.load(f)

def meet_sage (skill_lvl, player_class, first_encounter):

    correct_response = {
    "1": ("Brilliant! I knew you had it in you—great work!\n"
          f"\nYou have learned a new skill: {colors["@"]}{list(skills[player_class][str(skill_lvl+1)].keys())[0]}{colors['RESET']} \n\n"
          "That’s all from me for now. Safe travels, brave one! \n"
          "Something tells me you’re destined for greatness. I’ll be rooting for you!\n"),
    "2": ("Hmph. I’ll admit, that was better than I expected. \n"
          f"\nYou have learned an even more powerful: {list(skills[player_class][str(skill_lvl+1)].keys())[0]} \n\m"
          "That’s all the help you’ll get from me. \n"
          "Now go! The world won’t save itself, and I’ve no time for slackers.\n"),
    "3": ("Yes, that is correct. Your insight serves you well.\n"
          "Congratulations! \n" 
          f"\nYou have learned the ultimate skill: {list(skills[player_class][str(skill_lvl+1)].keys())[0]} \n" 
          "Go forth, hero, and fulfil your destiny. \n" 
          "The world’s hope rests with you, and you have proven yourself worthy of that burden. \n"
          "Remember, even in darkness, the light of wisdom shall guide you.\n")
        }   
    
    if first_encounter: # if it is the first time meeting this sage
        print(sage_data[str(skill_lvl)]["art"])
        print(sage_data[str(skill_lvl)]["welcome"])
        delay_message()
        clear_screen()
    else:
        print("Oh hey there... you again.")
        delay_message()
        clear_screen()

    if skill_lvl == 1:
        with open('assets/teach1.txt', 'r') as file:
            teaching_text = file.read()
    elif skill_lvl == 2:
        with open('assets/teach2.txt', 'r') as file:
            teaching_text = file.read()
    else:
        with open('assets/teach3.txt', 'r') as file:
            teaching_text = file.read()

    print(teaching_text)

    delay_message()# Requires user to press enter to continue
    clear_screen()

    print(sage_data[str(skill_lvl)]["quiz_time"])
    
    delay_message()# Requires user to press enter to continue
    clear_screen()
    
    score = 0
    quiz = sage_data[str(skill_lvl)]["quiz"]
    questions_list = list(quiz.values())
    random_questions = random.sample(questions_list, 2)
    for idx, question in enumerate(random_questions, start=1):
        print(sage_data[str(skill_lvl)]["art"])
        print(f"\nQuestion {idx}: {question['question']}")
        user_answer = input("Your answer: ")
        if user_answer == "" or not user_answer.isdigit(): # if input not numbers
            print("Invalid input! Moving to the next question.")
            delay_message()
            clear_screen()
        else:
            user_answer = float(user_answer) 
            if user_answer == question['answer']:
                print("Correct!")
                score += 1
                delay_message()
                clear_screen() 
            else: 
                print("Wrong answer.")
                delay_message()
                clear_screen()
    
    if score >= 1: 
        print(correct_response[str(skill_lvl)])
        skill_lvl = skill_lvl + 1 
        first_encounter = True
    else: 
        print(sage_data[str(skill_lvl)]["wrong"])
        first_encounter = False

    delay_message()
    clear_screen()

    return skill_lvl, first_encounter
