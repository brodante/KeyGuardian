import os

def print_centered(text):
    terminal_width = os.get_terminal_size().columns
    centered_text = "{:^{width}}".format(text, width=terminal_width)
    print(centered_text)

def logo():
    os.system("cls" if os.name == "nt" else "clear")
    print("\n\n")
    print_centered("\033[96mKeyGuardian v0.02\033[0m")
    
    # Define the ASCII logo
    logo_ascii = """
  _  __           _____                     _ _                      ___   ___  _  _     _          _        
 | |/ /          / ____|                   | (_)                    / _ \ / _ \| || |   | |        | |       
 | ' / ___ _   _| |  __ _   _  __ _ _ __ __| |_  __ _ _ __   __   _| | | | | | | || |_  | |__   ___| |_ __ _ 
 |  < / _ \ | | | | |_ | | | |/ _` | '__/ _` | |/ _` | '_ \  \ \ / / | | | | | |__   _| | '_ \ / _ \ __/ _` |
 | . \  __/ |_| | |__| | |_| | (_| | | | (_| | | (_| | | | |  \ V /| |_| | |_| |  | |   | |_) |  __/ || (_| |
 |_|\_\___|\__, |\_____|\__,_|\__,_|_|  \__,_|_|\__,_|_| |_|   \_/  \___(_)___/   |_|   |_.__/ \___|\__\__,_|
            __/ |                                                                                            
           |___/                                                                                             
"""
    
    # Resize the logo to fit the terminal width
    terminal_width = os.get_terminal_size().columns  # Define terminal width here
    logo_width = len(logo_ascii.split('\n')[1])  # Get the width of the logo
    logo_lines = logo_ascii.strip().split('\n')  # Get the logo lines without leading/trailing spaces
    
    for line in logo_lines:
        print_centered(line.center(terminal_width))  # Center each line of the logo in the terminal

# Example usage
logo()
