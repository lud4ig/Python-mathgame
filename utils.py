import os

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