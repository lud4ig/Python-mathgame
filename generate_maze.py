import random

width = 20
height = 20
directions = [(0, 1), (1, 0)] # two directions for binary tree algorithm
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)] # possible moves for DFS
maze = [['T' for _ in range(width)] for _ in range(height)] # generate a w*h maze full of T's

def generate_maze():
    """
    Replace the T's with some random number of P's using a binary tree algorithm.
    
    This function does not take any parameters or return any values.
    """
    for y in range(height):
        for x in range(width):
            direction = random.choice(directions)
            dx, dy = direction
            if 0 <= x + dx < width and 0 <= y + dy < height:
                maze[y + dy][x + dx] = 'P'


def is_valid_move(x, y):
    """
    Checks if the coordinate cell (x, y) is within the boundaries of the maze and if the cell is 'P'.
    
    Parameters:
        x, y (integer): Coordinates for a cell in the maze.
        
    Returns:
        bool: True if the coordinate is within the maze, false if it's OOB.
    """
    return 0 <= x < width and 0 <= y < height and maze[y][x] == 'P'


def flood_fill(x, y, visited):
    """
    Implementation of DFS.
    
    Parameters:
        x, y (integer): Coordinates for a cell in the maze.
        visited (set[tuple[int, int]]): A set of tuples where each tuple contains two integers.
    
    This function does not return any values.
    """
    stack = [(x, y)]
    while stack:
        cx, cy = stack.pop()
        if (cx, cy) not in visited:
            visited.add((cx, cy))
            for dx, dy in moves:
                nx, ny = cx + dx, cy + dy
                if is_valid_move(nx, ny) and (nx, ny) not in visited:
                    stack.append((nx, ny))


def ensure_connected():
    """
    Uses an implementation of DFS to perform a flood fill. This marks all walkable areas "P" in the maze, and then connects any isolated "P" areas in the maze. This also has the dual-purpose of hopefully preventing any isolated "B" areas.
    
    This function does not take any parameters or return any values. 
    """
    visited = set()
    for y in range(height):
        for x in range(width):
            if maze[y][x] == 'P':
                flood_fill(x, y, visited)
                break
        else:
            continue
        break

    for y in range(1, height - 1):
        for x in range(1, width - 1):
            if maze[y][x] == 'P' and (x, y) not in visited:
                for dx, dy in moves:
                    nx, ny = x + dx, y + dy
                    if is_valid_move(nx, ny) and (nx, ny) in visited:
                        maze[y][x] = 'P'
                        break


def place_start_and_end():
    """
    Add start and boss points to the maze. Farthest point is based on the Manhattan distance.
    
    Returns:
        start_x, start_y, end_x, end_y (integer): The x-y coordinates of the start and end (boss) points.

    This function does not take any parameters.
    """
    start_x = random.randint(1, width - 2)
    start_y = random.randint(1, height - 2)
    maze[start_y][start_x] = '@'
    
    max_distance = -1
    end_x, end_y = start_x, start_y
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            if maze[y][x] == 'P':
                distance = abs(x - start_x) + abs(y - start_y)
                if distance > max_distance:
                    max_distance = distance
                    end_x, end_y = x, y
    maze[end_y][end_x] = 'B'
    
    return start_x, start_y, end_x, end_y


def place_s_and_h(start_x, start_y, end_x, end_y):
    """
    Places three Sage 'S' points and two Healing 'H' points, where one 'S' is always beside the @ and one 'H' is always beside the B.
    
    Parameters:
        start_x, start_y, end_x, end_y (integer): The x-y coordinates of the start and end (boss) points.
        
    This function does not return any values.
    """

    s_points = []
    h_points = []

    adj_start = []
    for dx, dy in moves:
        nx, ny = start_x + dx, start_y + dy # Pretty sure this will cause some issues later on
        if is_valid_move(nx, ny):
            adj_start.append((nx, ny))

    if adj_start:
        s_points.append(random.choice(adj_start))

    adj_end = []
    for dx, dy in moves:
        nx, ny = end_x + dx, end_y + dy #Pretty sure this will cause some issues later on
        if is_valid_move(nx, ny):
            adj_end.append((nx, ny))

    if adj_end:
        h_points.append(random.choice(adj_end))

    while len(s_points) < 3:
        x = random.randint(1, width - 2)
        y = random.randint(1, height - 2)
        if maze[y][x] == 'P' and (x, y) not in s_points and (x, y) not in h_points:
            s_points.append((x, y))

    while len(h_points) < 2:
        x = random.randint(1, width - 2)
        y = random.randint(1, height - 2)
        if maze[y][x] == 'P' and (x, y) not in s_points and (x, y) not in h_points:
            h_points.append((x, y))

    for (sx, sy) in s_points:
        if maze[sy][sx] != '@' and maze[sy][sx] != 'B' and maze[sy][sx] != 'T':
            maze[sy][sx] = 'S'
    
    for (hx, hy) in h_points:
        if maze[hy][hx] != '@' and maze[hy][hx] != 'B' and maze[sy][sx] != 'T':
            maze[hy][hx] = 'H'

def place_perimeter():
    """
    Creates the perimeter to prevent going OOB.
    
    This function does not take any parameters or return any values. 
    """
    for y in range(height):
        for x in range(width):
            if x == 0 or x == width - 1 or y == 0 or y == height - 1:
                maze[y][x] = 'T'

#generate_maze()
#ensure_connected()
#start_x, start_y, end_x, end_y = place_start_and_end()
#place_s_and_h(start_x, start_y, end_x, end_y)
#place_perimeter()