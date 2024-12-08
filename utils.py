import os

colors = {
    "RED": '\033[91m',
    "RESET": '\033[0m',
    "GREEN": '\033[92m',
    "T": "\033[90m",  # Greyish
    "P": "\033[97m",  # White
    "S": "\033[96m",  # Cyan ish?
    "H": "\033[92m",  # Green
    "B": "\033[91m",  # Red
    "@": "\033[93m"  # Yellow
}

def clear_screen():
    """
    Clears the terminal screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    
def delay_message():
    """
    Pause the game to allow players to read a message.
    """
    input("\nPress Enter to continue...")
    
def create_health_bar(current_health, max_health, color):
    health_bar = f"[{('|' * current_health).ljust(max_health)}]"
    return f"{colors[color]}{health_bar}{colors['RESET']}"
    
def format_entity_info(name, current_health, max_health, bar_color, art=None):
    colored_health_bar = create_health_bar(current_health, max_health, bar_color)
    
    art_display = f"{art}\n" if art else ""
    
    return (
        f"\n{colors[bar_color]}{name}{colors['RESET']}\n"
        f"{art_display}"
        f"{name}'s Health: {current_health}/{max_health} {colored_health_bar}"
    )