import json
import random 
from utils import delay_message 

# To load json file 
with open("sage.json", 'r') as f:
    sage = json.load(f)

with open("sage_skills.json", 'r') as f:
    sage_skills = json.load(f)

# Load teaching sage text (for the 3 levels of teaching only)
with open(sage["3"]["teaching_sage"], 'r') as file:
    teaching_text = file.read()



# Skills nare
correct_response = {
    "1": ("Brilliant! I knew you had it in you—great work!\n"
          "You have learned Skill 2: {list(sage_skills[player_class][skill_lvl].keys())[0]} \n"
          "That’s all from me for now. Safe travels, brave one! \n"
          "Something tells me you’re destined for greatness. I’ll be rooting for you!\n"),
    "2": ("Hmph. I’ll admit, that was better than I expected. \n"
          "You have learned Skill 3: {list(sage_skills[player_class][skill_lvl].keys())[0]} \n"
          "That’s all the help you’ll get from me. \n"
          "Now go! The world won’t save itself, and I’ve no time for slackers.\n"),
    "3": ("Yes, that is correct. Your insight serves you well.\n"
          "Congratulations! \n" 
          "You have learned the ultimate skill: {list(sage_skills[player_class][skill_lvl].keys())[0]} \n" 
          "Go forth, hero, and fulfil your destiny. \n" 
          "The world’s hope rests with you, and you have proven yourself worthy of that burden. \n"
          "Remember, even in darkness, the light of wisdom shall guide you.\n")
}



def meet_sage (skill_lvl):
    score = 0
    print(sage[str(skill_lvl)]["art"])
    
    print(sage[str(skill_lvl)]["welcome"])
    
    delay_message()# Requires user to press enter to continue

    with open(sage[str(skill_lvl)]["teaching_sage"], 'r') as file:
        teaching_text = file.read()
    print(teaching_text)
    
    delay_message()# Requires user to press enter to continue
    
    print(sage[str(skill_lvl)]["quiz_time"])
    
    delay_message()# Requires user to press enter to continue
    
    quiz = sage[str(skill_lvl)]["quiz"]
    questions_list = list(quiz.values())
    random_questions = random.sample(questions_list, 2)
    for idx, question in enumerate(random_questions, start=1):
        print(f"Question {idx}: {question['question']}")
        user_answer = input("Your answer: ")
        if user_answer =="" or user_answer.isalpha() or not user_answer.isalnum(): # if input not numbers
            score =score
        else:
            user_answer = float(user_answer) 
            if user_answer == question['answer']:
                score += 1 
            else: 
                score = score
    
    if score >= 1: 
        print(correct_response[str(skill_lvl)])
        skill_lvl = skill_lvl + 1 
    else: 
        print(sage[str(skill_lvl)]["wrong"])
    
    return skill_lvl
        
        
    
meet_sage(1)
