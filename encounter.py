from utils import clear_screen, delay_message
import json
import random

with open("assets/mobs.json", 'r') as f:
    mobs = json.load(f)

with open("assets/math_problems.json", 'r') as f:
    questions = json.load(f)

def mob_encounter(player_health, player_skills):
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
    print("Mob Name:", mob_name, "\nMob Health:", mob_health) # print mob name and health
    while mob_health > 0 and player_health > 0:
        # print the list of skills that the player can use against the mob, from 1 to 4 (that is, if the player has it)
        print("You have", player_health, "health.")
        print(f"You have {list(player_skills.items())[0]}")
        chosen_skill = input("What skill would you like to use? Choose the number. ")
        skill_tuple = list(player_skills[chosen_skill].items())[0]
        power_name, damage = skill_tuple
        # validate input
        while chosen_skill not in list(player_skills.keys()):
            print("Do you sure you have this skill? Try again!")
            delay_message()
            chosen_skill = input("What skill would you like to use?")
        # after player inputs name of skill, the mob will ask a question from math_problems.json
        # if the player uses skill level 1, question will be from easy key of math_problems
        # if player uses skill level 2, qn will be from medium etc.
        # show question
        clear_screen()
        if player_skills[chosen_skill][power_name] == 10:
            question_number = random.choice(list(questions["easy"].keys()))
            question = list(questions["easy"][question_number].keys())[0]
            print(question)
            player_answer = int(input("Enter Your Answer: "))
            correct_answer = questions["easy"][question_number][question]
            if player_answer == correct_answer:
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