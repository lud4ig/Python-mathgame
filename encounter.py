from utils import clear_screen, delay_message, create_health_bar, format_entity_info, colors
import json
import random

with open("assets/mobs.json", 'r') as f:
    mobs = json.load(f)

with open("assets/math_problems.json", 'r') as f:
    questions = json.load(f)

def skill_screen(player_skills, player_class):
    """Takes in dictionary of dictionaries of player skills, 
    and returns chosen number by player."""
    print("====================================================================")
    print(f"       Here are the skills that you currently have for the {player_class} class.\n       ")
    for skill in player_skills:
        # skill is the number (1, 2, 3)
        power_name, damage = list(player_skills[skill].items())[0] # can only retrieve power name and damage by converting dict_items object into a list
        print(f"{skill}    {power_name}  {damage} Damage\n")
    print("====================================================================")
    chosen_skill = None
    while not chosen_skill or chosen_skill not in player_skills: #input validation
        chosen_skill = input("What skill would you like to use? Choose the number. ")
        if not chosen_skill:
            print("Invalid input. Please try again!")
        elif chosen_skill not in player_skills:
            print("You do not have this skill. Please try again!")
    return chosen_skill

def mob_encounter(player_name, player_current_health, player_skills, player_class):
    """
    Takes in player health as an integer and player_skills as a dictionary
    of the skills the current player has acquired.

    Returns True as well as the player_current_health and player_skills in a list if player has survived the mob encounter and can continue the game
    Returns False if player died
    """
    print("\033[33mYou encounter a monster!\033[0m") 
    delay_message()
    # choose random mob from mob json
    # if player only has 1 ability, don't give a mob with so much health
    if len(player_skills) == 1 or len(player_skills) == 2:
        mob_difficulty = "Low"
    else:
        mob_difficulty = "High"
    possible_mobs = []
    if mob_difficulty == "Low":
        for mob in mobs:
            # mob is a Monster name
            # print(mob)
            if mobs[mob]["Difficulty"] == "Low":
                possible_mobs.append(mob)
    else:
        for mob in mobs:
            if mobs[mob]["Difficulty"] == "High":
                possible_mobs.append(mob)
                
    mob = random.choice(possible_mobs)
    mob_name = mobs[mob]["Mob"]
    mob_max_health = mobs[mob]["Health"]
    mob_current_health = mob_max_health
    mob_art = mobs[mob]["Art"]
    
    while mob_current_health > 0 and player_current_health > 0:
        
        clear_screen()
        
        mob_information = format_entity_info(mob_name, mob_current_health, mob_max_health, "RED", mob_art)
    
        player_information = format_entity_info(player_name, player_current_health, 100, "GREEN") 
        
        print(mob_information)
        print(player_information)
        
        chosen_skill = skill_screen(player_skills, player_class)
        skill_tuple = list(player_skills[chosen_skill].items())[0] # (key, value)
        power_name, damage = skill_tuple
        
        # validate input
        # after player inputs name of skill, the mob will ask a question from math_problems.json
        # if the player uses skill level 1, question will be from easy key of math_problems
        # if player uses skill level 2, qn will be from medium etc.    
        if player_skills[chosen_skill][power_name] == 10:
            question_number = random.choice(list(questions["easy"].keys()))
            question = list(questions["easy"][question_number].keys())[0]
            correct_answer = questions["easy"][question_number][question]

        elif player_skills[chosen_skill] == 30:
            question_number = random.choice(list(questions["medium"].keys()))
            question = list(questions["medium"][question_number].keys())[0]
            correct_answer = questions["medium"][question_number][question]
            
        elif player_skills[chosen_skill] == 50:
            question_number = random.choice(list(questions["hard"].keys()))
            question = list(questions["hard"][question_number].keys())[0]
            correct_answer = questions["hard"][question_number][question]
        else:
            question_number= random.choice(list(questions["very_hard"].keys()))
            question = list(questions["very_hard"][question_number].keys())[0]
            correct_answer = questions["very_hard"][question_number][question]
        
        clear_screen()
        
        print(question)
        player_answer = None
        while not player_answer or not player_answer.isnumeric():
            player_answer = input("Enter Your Answer: ")
            if not player_answer:
                print("Invalid input. Please try again!")
            elif not player_answer.isnumeric():
                print("Enter a number! Please try again!")
        if int(player_answer) == correct_answer:
            clear_screen()
            mob_current_health -= damage
            print(f"BAM!!! You have dealt {damage} damage to {mob_name}!")
            delay_message()
        else:
            clear_screen()
            player_current_health -= damage
            print(f"WOOSH! You missed! The {mob_name} retaliates and hits you for {damage} damage!")
            delay_message()

    if player_current_health <= 0:
        return [False, player_current_health, player_skills]
    else:
        print(f"Congrats! You have beaten the mob. After the battle, you have {player_current_health} health.")
        delay_message()
        return [True, player_current_health, player_skills]

def boss_encounter(player_name, player_current_health, player_skills, player_class):
    """
    Takes in player health as an integer and player_skills as a dictionary of the skills the current player has acquired. 
    Returns True as well as the player_health and player_skills in a list if player has survived the boss encounter and can continue the game. 
    Returns False if player died.

    Parameters:
    player_health(int): Number of hp the player has
    player_skills (dict): All skills of player
    player_class (str): Chosen class by player, from main.py

    """
    print(f"{colors['RED']}You encounter the final boss!{colors['RESET']}") 
    delay_message()
    clear_screen()
    # initialise boss attributes
    boss_name = "The Division Dragon"
    boss_max_health = 300
    boss_current_health = boss_max_health
    Dragon_art = """
                                  \\  `                                       
     /)         ,   '--.           \\    `                                    
    //     , '          \\/          \\   `   `                                
   //    ,'              ./         /\\    \\>- `   ,----------.               
  ( \\  ,'    .-.-._        /      ,' /\\    \\   . `            `.             
   \\ \\'     /.--. .)       ./   ,'  /  \\     .      `           `.           
    \\     -{/    \\ .)        / /   / ,' \\       `     `-----.     \\          
    <\\      )     ).:)       ./   /,' ,' \\        `.  /\\)    `.    \\         
     >^,  //     /..:)       /   //--'    \\         `(         )    )        
      | ,'/     /. .:)      /   (/         \\          \\       /    /         
      ( |(_    (...::)     (                \\       .-.\\     /   ,'          
      (O| /     \\:.::)                      /\\    ,'   \\)   /  ,'            
       \\|/      /`.:::)                   ,/  \\  /         (  /              
               /  /`,.:)                ,'/    )/           \\ \\              
             ,' ,'.'  `:>-._._________,<;'    (/            (,'              
           ,'  /  |     `^-^--^--^-^-^-'                                      
 .--------'   /   |                                                          
(       .----'    |                                                          
 \\ <`.  \\         |                                                          
  \\ \\ `. \\        |                                            
   \\ \\  `.`.      |                                                          
    \\ \\   `.`.    |                                                          
     \\ \\    `.`.  |                                                          
      \\ \\     `.`.|                                                          
       \\ \\      `.`.                                                         
        \\ \\     ,^-'
         \\ \\    |
          `.`.  |
             .`.|
              `._>
"""
    # logic of boss and mob encounter is very similar, just that there is only one preset set 
    # of questions that can be asked by the boss
    while boss_current_health > 0 and player_current_health > 0:
        boss_information = format_entity_info(boss_name,boss_current_health, boss_max_health, "RED", Dragon_art)
    
        player_information = format_entity_info(player_name, player_current_health, 100, "GREEN") 
            
        print(boss_information)
        print(player_information)

        chosen_skill = skill_screen(player_skills, player_class)
        skill_tuple = list(player_skills[chosen_skill].items())[0] # (key, value)
        power_name, damage = skill_tuple
        clear_screen()
        question_number = random.choice(list(questions["boss"].keys()))
        question = list(questions["boss"][question_number].keys())[0]
        print(question)
        player_answer = None
        while not player_answer or not player_answer.isnumeric():
            player_answer = input("Enter Your Answer: ")
            if not player_answer:
                print("Invalid input. Please try again!")
            elif not player_answer.isnumeric():
                print("Enter a number! Please try again!")
        correct_answer = questions["boss"][question_number][question]
        if int(player_answer) == correct_answer:
            boss_current_health -= damage
            print(f"KACHUNK!!! You have dealt {damage} damage to {boss_name}!")
            delay_message()
            clear_screen()
        else:
            player_current_health -= damage
            print(f"WOOSH! {boss_name} cleanly dodged your attack!\n {boss_name} retaliates with a deadly strike for {damage} damage!")
            delay_message()
            clear_screen()
    if player_current_health <= 0:
        return False
    else:
        return True
