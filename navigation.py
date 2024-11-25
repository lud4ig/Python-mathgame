def display_map(game_map, player_pos, visibility=1):
    """
    Display a portion of the game map centered around the player, with fog of war.
    
    Parameters:
        game_map (list of lists): The chosen maze for the game
        player_pos (tuple): Current position of the player (x, y).
        visibility (int): The radius of visibility around the player. Defaults to 1.
        
    This function does not return any values.
    """
    px, py = player_pos
    x, y = len(game_map), len(game_map[0])

    # Compute visible window bounds
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
            else:
                char = "#"
            row += char + " "
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