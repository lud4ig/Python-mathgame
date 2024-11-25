import json
import curses
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

def play_game(stdscr, maps):
    """
    Main logic for the game
    
    Parameters:
        stdscr: curses window object
        maps (json): list of premade maps
        
    This function does not return any values.
    """
    stdscr.clear()
    stdscr.addstr(0, 0, "Select a map: " + ", ".join(maps.keys()) + ", or 'random' for a randomly generated map.")
    stdscr.refresh()
    
    stdscr.addstr(1, 0, "Enter your choice: ")
    curses.echo()
    difficulty = stdscr.getstr(1, len("Enter your choice: ")).decode().lower()
    curses.noecho()

    if difficulty not in maps and difficulty != "random":
        stdscr.addstr(3, 0, "Invalid choice! Press any key to exit.")
        stdscr.getch()
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
        display_map(stdscr, game_map, player_pos)

        stdscr.addstr(len(game_map) + 1, 0, "(WASD) Move | (P)layer Information | (Q)uit")
        key = stdscr.getch()

        # Player options, add or remove as needed
        x, y = player_pos
        if key == ord('w'):  # Up
            new_pos = (x - 1, y)
        elif key == ord('a'):  # Left
            new_pos = (x, y - 1)
        elif key == ord('s'):  # Down
            new_pos = (x + 1, y)
        elif key == ord('d'):  # Right
            new_pos = (x, y + 1)
        elif key == ord('q'):  # Quit
            stdscr.addstr(len(game_map) + 2, 0, "Goodbye! Press any key to exit.")
            stdscr.getch()
            return
        else:
            continue

        if is_walkable(game_map, new_pos):
            if first_move:
                game_map[x][y] = "P"
                first_move = False

            player_pos = new_pos

            # Trigger boss event when player touches the B tile
            if game_map[player_pos[0]][player_pos[1]] == "B":
                display_map(stdscr, game_map, player_pos)
                stdscr.addstr(len(game_map) + 2, 0, "Begin boss encounter.")
                stdscr.addstr(len(game_map) + 3, 0, "Congratulations! You beat the stage!")
                stdscr.getch()
                break

def main(stdscr):
    maps = load_maps("assets/premade_maps.json")
    play_game(stdscr, maps)

if __name__ == "__main__":
    curses.wrapper(main)