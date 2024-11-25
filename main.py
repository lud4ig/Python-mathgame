import json
# import curses
from generate_maze import maze, generate_maze, ensure_connected, place_start_and_end, place_s_and_h, place_perimeter
from navigation import display_map, find_player_start, is_walkable

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

def play_game(maps):
    """
    Main logic for the game
    
    Parameters:
        maps (json): list of premade maps
        
    This function does not return any values.
    """
    print("Select a map: " + ", ".join(maps.keys()) + ", or 'random' for a randomly generated map.")
    difficulty = input("Enter your choice: ").strip().lower()

    if difficulty not in maps and difficulty != "random":
        print("Invalid choice! Exiting the game.")
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

    player_pos = find_player_start(game_map)
    first_move = True

    # Main loop for the game
    while True:
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
            return
        else:
            print("Invalid input! Use WASD to move or Q to quit.")
            continue

        if is_walkable(game_map, new_pos):
            if first_move:
                game_map[x][y] = "P"
                first_move = False

            player_pos = new_pos

            # Trigger boss event when player touches the B tile
            if game_map[player_pos[0]][player_pos[1]] == "B":
                display_map(game_map, player_pos)
                print("Begin boss encounter.")
                print("Congratulations! You beat the stage!")
                break

def main():
    maps = load_maps("assets/premade_maps.json")
    play_game(maps)

if __name__ == "__main__":
    main()