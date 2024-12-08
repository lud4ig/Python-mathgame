import random
from utils import clear_screen, delay_message, colors

def display_map(game_map, player_pos, visibility=1):
    """
    Display a portion of the game map centered around the player, with fog of war.
    
    Parameters:
        game_map (list of lists): The chosen maze for the game
        player_pos (tuple): Current position of the player (x, y).
        visibility (int, default=1): Visibility around the player.
        
    This function does not return any values.
    """

    # I ChatGPT'd these colors cause I don't know the ANSI color codes by heart

    px, py = player_pos
    x, y = len(game_map), len(game_map[0])

    start_x = max(0, px - visibility)
    end_x = min(x, px + visibility + 1)
    start_y = max(0, py - visibility)
    end_y = min(y, py + visibility + 1)

    # Render only the visible portion of the map, aka fog of war
    output = []
    for x_idx in range(start_x, end_x):
        row = ""
        for y_idx in range(start_y, end_y):
            if abs(x_idx - px) <= visibility and abs(y_idx - py) <= visibility:
                char = "@" if (x_idx, y_idx) == player_pos else game_map[x_idx][y_idx]
                colored_char = f"{colors.get(char)}{char}{colors['RESET']}"
            row += colored_char + " "
        output.append(row)
    print("\n".join(output))

def find_player_start(game_map):
    """
    Locate the starting position for the player where the @ is.
    
    Parameters:
        game_map (list of lists): The chosen maze for the game
    
    Returns:
        tuple: Starting coordinates of player
    """
    for x_idx, x in enumerate(game_map):
        for y_idx, cell in enumerate(x):
            if cell == "@":
                return (x_idx, y_idx)

def is_walkable(game_map, pos):
    """
    Collision detection
    
    Parameters:
        game_map (list of lists): The chosen maze for the game
        pos (tuple): Desired position to be moved to
        
    Returns:
        bool: True if desired position is navigable, False if not.
    """
    x, y = pos
    if 0 <= x < len(game_map) and 0 <= y < len(game_map[0]):
        return game_map[x][y] in {"P", "S", "H", "B"}  # "P" = path, "S" = start, "H" = hidden, "B" = boss
    return False
    
def check_random_encounter(step_count):
    """
    Check if a random encounter occurs based on the number of steps taken.
    
    Parameters:
        step_count (int): Number of steps taken since the last encounter.
        
    Returns:
        bool: True if an encounter occurs, False otherwise.
    """
    encounter_chance = min(50, step_count * 5)
    if random.randint(1, 100) <= encounter_chance:
        return True
    return False