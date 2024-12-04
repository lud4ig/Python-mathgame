from utils import clear_screen, delay_message
import json
import random

with open("assets/mobs.json", 'r') as f:
    mobs = json.load(f)

with open("assets/math_problems.json", 'r') as f:
    questions = json.load(f)

def skill_screen(player_skills, player_class):
    """Takes in list of dictionaries of player skills, 
    and returns chosen number by player."""
    print("====================================================================")
    print(f"       Here are the skills that you currently have for the {player_class} class.\n       ")
    for skill in player_skills:
        power_name, damage = list(player_skills[skill].items())[0]
        print(f"{skill}    {power_name}  {damage} Damage\n")
    print("====================================================================")
    chosen_skill = None
    while not chosen_skill or chosen_skill not in player_skills:
        chosen_skill = input("What skill would you like to use? Choose the number. ")
        if not chosen_skill:
            print("Invalid input. Please try again!")
        elif chosen_skill not in player_skills:
            print("You do not have this skill. Please try again!")
    return chosen_skill

def mob_encounter(player_health, player_skills, player_class):
    """
    Takes in player health as an integer and player_skills as a dictionary
    of the skills the current player has acquired.

    Returns True as well as the player_health and player_skills in a list if player has survived the mob encounter and can continue the game
    Returns False if player died
    """
    print("\033[33mYou encounter a monster!\033[0m") 
    delay_message()
    # choose random mob from mob json
    # if player only has 1 ability, don't give a mob with so much damage
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
    mob_health = mobs[mob]["Health"]
    mob_art = mobs[mob]["Art"]
    clear_screen()
    print("Mob Name:", mob_name, "\nMob Art:", mob_art, "\nMob Health:", mob_health) # print mob name and health
    while mob_health > 0 and player_health > 0:
        # print the list of skills that the player can use against the mob, from 1 to 4 (that is, if the player has it)
        print("You have", player_health, "health.")
        chosen_skill = skill_screen(player_skills, player_class)
        skill_tuple = list(player_skills[chosen_skill].items())[0] # (key, value)
        power_name, damage = skill_tuple
        # validate input
        # after player inputs name of skill, the mob will ask a question from math_problems.json
        # if the player uses skill level 1, question will be from easy key of math_problems
        # if player uses skill level 2, qn will be from medium etc.
        # show question
        clear_screen()
        if player_skills[chosen_skill][power_name] == 10:
            question_number = random.choice(list(questions["easy"].keys()))
            question = list(questions["easy"][question_number].keys())[0]
            print(question)
            player_answer = None
            while not player_answer or not player_answer.isnumeric():
                player_answer = input("Enter Your Answer: ")
                if not player_answer:
                    print("Invalid input. Please try again!")
                elif not player_answer.isnumeric():
                    print("Enter a number! Please try again!")
            correct_answer = questions["easy"][question_number][question]
            if int(player_answer) == correct_answer:
                mob_health -= damage
                print(f"Congrats! You have dealt {damage} damage to the mob. The mob now has {mob_health} health.")
            else:
                player_health -= damage*5
                print(f"That answer was incorrect. The correct answer was {correct_answer}.")
        elif player_skills[chosen_skill] == 30:
            question_number = random.choice(list(questions["medium"].keys()))
            
        elif player_skills[chosen_skill] == 50:
            question_number = random.choice(list(questions["hard"].keys()))
        else:
            question_number= random.choice(list(questions["very hard"].keys()))

    if player_health <= 0:
        return [False, player_health, player_skills]
    else:
        print(f"Congrats! You have beaten the mob. After the battle, you have {player_health} health.")
        delay_message()
        return [True, player_health, player_skills]

def boss_encounter(player_health, player_skills, player_class):
    print("\033[31mYou encounter the final boss!\033[0m") 
    delay_message()
    boss_name = "The Division Dragon"
    boss_health = 300
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
    clear_screen()
    print(f"Boss name: {boss_name} | Boss health: {boss_health}")
    print(Dragon_art)
    while boss_health > 0 and player_health > 0:
        print("You have", player_health, "health.")
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
                boss_health -= damage
                print(f"Congrats! You have dealt {damage} damage to the boss. The boss now has {boss_health} health.")
            else:
                player_health -= damage*5
                print(f"That answer was incorrect. The correct answer was {correct_answer}.")
    if player_health <= 0:
        return False
    else:
        return True
