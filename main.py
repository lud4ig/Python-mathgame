import json
from generate_maze import maze, generate_maze, ensure_connected, place_start_and_end, place_s_and_h, place_perimeter
from navigation import display_map, find_player_start, is_walkable, check_random_encounter
from utils import clear_screen, delay_message
from encounter import mob_encounter, boss_encounter
from sage_compiled_w_json import meet_sage
import random

with open("assets/math_problems.json", 'r') as f:
    questions = json.load(f)

with open("assets/skills.json", 'r') as f:
    skills = json.load(f)

def show_rules():
    """
    Prints out the rules of the game to the player.
    """
    clear_screen()
    print("=== GAME RULES ===")
    print("""
    1. Navigate the maze by entering WASD.
    2. Dangerous challenges await:
        - 'P' tiles are walkable paths.
        - 'T' tiles are thickets that cannot be traversed.
        - 'H' tiles are healing zones to recover.
        - 'B' tiles are boss fights.
        - 'S' tiles contain wise sages who will guide you to success.
    3. Your objective is to reach the boss and defeat it with your newfound mathematical prowess! You can look for the boss directly,
          but let this be a gentle reminder: the questions given to you by the boss are going to be hard.
    """)
    delay_message()

def title_screen():
    clear_screen()
    print("======================================")
    print("       WELCOME, BRAVE WARRIOR!")
    print("======================================")
    print("""
    1. New Game
    2. Rules
    Q. Quit
    """)
    menu_choice = input("Enter your choice: ").strip().lower()
    return menu_choice

def load_maps(filename):
    """
    Load premade maps in the assets/ folder.
    
    Parameters:
        filename (json) : Absolute path of the .json file
        
    Returns:
        json.load(file) (list of lists) 
    """
    with open(filename, 'r') as file:
        return json.load(file)

def play_game(maps, ADD_OTHER_FILES=True):
    """
    Main logic for the game
    
    Parameters:
        maps (json): list of premade maps
        
    This function does not return any values.
    """
    player_health = 100
    skill_lvl = 1
    first_encounter = True   
    print("Select a map: " + ", ".join(maps.keys()) + ", or 'random' for a randomly generated map.")
    difficulty = input("Enter your choice: ").strip().lower()

    if difficulty not in maps and difficulty != "random":
        print("Invalid choice! Returning to main menu.")
        delay_message()
        return

    if difficulty == "random":
        generate_maze() 
        ensure_connected()
        start_x, start_y, end_x, end_y = place_start_and_end()
        place_s_and_h(start_x, start_y, end_x, end_y)
        place_perimeter()
        game_map = maze
    else:
        game_map = maps[difficulty]

    print("Select a class: " + ", ".join(skills.keys()))
    player_class = None

    while player_class not in skills or player_class is None:
        player_class = input("Enter your class choice: ").strip().lower()
        if player_class not in skills:
            print("Invalid choice! Please try again!")

    else:
        player_skills = {} # player skills will be a dictionary of dictionaries
        player_skills['1'] = skills[player_class]['1'] # dictionary with only the 1st skill from the class when player starts the game {'1': {'Mighty Strike': 10}}
        player_pos = find_player_start(game_map)
        first_move = True
        step_count = 0

    # Main loop for the game
    while True:
        clear_screen()
        display_map(game_map, player_pos)
        print("(WASD) Move | (P)layer Information | (Q)uit")
        key = input("Your move: ").lower()

        # Player options
        x, y = player_pos
        if key == 'w':  # Up
            new_pos = (x - 1, y)
        elif key == 'a':  # Left
            new_pos = (x, y - 1)
        elif key == 's':  # Down
            new_pos = (x + 1, y)
        elif key == 'd':  # Right
            new_pos = (x, y + 1)
        elif key == 'q':  # Quit
            print("Goodbye! Exiting the game.")
            delay_message()
            return
        else:
            print("Invalid input! Use WASD to move or Q to quit.")
            delay_message()
            continue

        if is_walkable(game_map, new_pos):
            if first_move:
                game_map[x][y] = "P"
                first_move = False

            player_pos = new_pos

            if game_map[player_pos[0]][player_pos[1]] == "P":
                step_count += 1
                if check_random_encounter(step_count):
                    return_object = mob_encounter(player_health, player_skills, player_class)
                    alive = return_object[0]
                    player_health = return_object[1]
                    player_skills = return_object[2]
                    if alive:
                        step_count = 0
                    else:
                        print("You died! Try again next time!")
                        delay_message()
                        break
                    
            if game_map[player_pos[0]][player_pos[1]] == "S":
                skill_lvl, first_encounter = meet_sage(skill_lvl, player_class, first_encounter)
                player_skills[f'{skill_lvl}'] = skills[player_class][f'{skill_lvl}']
                
            if game_map[player_pos[0]][player_pos[1]] == "H":
                Heal_art = """
                        _|_
                         | 
                         |
                        / \
                       //_\\
                      //(_)\\
                       |/^\|
                       ||_||
                       // \\
                      //   \\
                     // === \\
                    // =-=-= \\
                   //   ===   \\
                  //|         |\\
                    |         |
                    |  __ __  |
                    | |  |  | |
                    | | -|- | |
                    |_|__|__|_|
                  /`  =======  `\\
                /`    =======    `\\
                """
                print(Heal_art)
                print ("You found a healing point! You recovered some health!")
                delay_message()
                max_health = 100
                player_health += 30 
                if player_health > max_health:
                    player_health = max_health
                print(f"You now have {player_health} health.")
                delay_message()

            # Trigger boss event when player touches the B tile
            if game_map[player_pos[0]][player_pos[1]] == "B":
                #PLACEHOLDER, REWRITE IT WITH THE APPROPRIATE BOSS FUNCTION
                alive = boss_encounter(player_health, player_skills, player_class)
                if alive:
                    clear_screen()
                    print("Congrats! You have beaten the boss! You are now ready to tackle the upcoming challenges in the world of mathematics.")
                    delay_message()
                    break
                else:
                    clear_screen()
                    print("Sorry.. you were not able to defeat the final boss. Try harder, and eventually you can do it!")
                    delay_message()
                    break

def main():
    while True:
        menu_choice = title_screen()
        clear_screen()
        if menu_choice == "1":
            maps = load_maps("assets/premade_maps.json")
            play_game(maps)
        elif menu_choice == "2":
            show_rules()
        elif menu_choice == "Q".lower():
            print("Thanks for playing! Goodbye!")
            delay_message()
            break
        else:
            print("Invalid choice! Please try again.")
            delay_message()

if __name__ == "__main__":
    main()
