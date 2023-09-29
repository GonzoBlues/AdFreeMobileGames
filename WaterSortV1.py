import random
from collections import Counter

# Define the tubes as lists where each element represents a color.
tubes = [[] for _ in range(4)]

# Define the available colors.
colors = ['Red', 'Blue', 'Green', 'Yellow', 'Purple', 'Orange', 'Pink', 'Cyan']

def create_tubes(colors, total_appearances):
    # Calculate the number of times each color should appear in total.
    num_colors = len(colors)
    appearances_per_color = total_appearances // num_colors
    
    # Create a list with each color repeated the specified number of times.
    color_pool = colors * appearances_per_color
    
    # Shuffle the color pool to randomize the order.
    random.shuffle(color_pool)
    
    # Distribute colors to the tubes.
    for i, tube in enumerate(tubes):
        # Use random.sample to ensure each tube has a random selection of colors.
        if i == 0:
            # Fill the first tube with no colors (empty).
            continue
        tube.extend(random.sample(color_pool, len(color_pool)))
    
    return tube

def pick_colors(num_colors=4, color_list=[]):
    # Shuffle the list of available colors.
    random.shuffle(color_list)
    
    # Pick the first 'num_colors' colors from the shuffled list.
    selected_colors = color_list[:num_colors]
    
    return selected_colors

def display_colors_ascii(colors):
    color_ascii = {
        'Red': 'Rd',
        'Blue': 'Bl',
        'Green': 'Gr',
        'Yellow': 'Yl',
        'Purple': 'Pu',
        'Orange': 'Or',
        'Pink': 'Pk',
        'Cyan': 'Cn'
    }

    for color in colors:
        print(color_ascii.get(color, '??'), end=' ')
    print()  # Add a newline after displaying the colors

def display_tubes():
    for i, tube in enumerate(tubes):
        print(f'Tube {i + 1}:', end=' ')
        display_colors_ascii(tube)

def move_color():
    source_tube = int(input("Enter the source tube (1-4): ")) - 1
    if source_tube < 0 or source_tube >= len(tubes):
        print("Invalid source tube.")
        return

    if not tubes[source_tube]:
        print("Source tube is empty.")
        return

    source_color = tubes[source_tube][-1]

    dest_tube = int(input("Enter the destination tube (1-4): ")) - 1
    if dest_tube < 0 or dest_tube >= len(tubes):
        print("Invalid destination tube.")
        return

    if not tubes[dest_tube] or tubes[dest_tube][-1] == source_color:
        color = tubes[source_tube].pop()
        tubes[dest_tube].append(color)
        print(f"Moved {color} from Tube {source_tube + 1} to Tube {dest_tube + 1}.")
    else:
        print("Destination tube is not empty and doesn't match the color of the source tube's top color.")

def get_difficulty():
    return int(input("How many Tubes do you want there to be?\n"))

# Create and display the tubes with colors distributed evenly.
TubeHight = 4



difficulty = get_difficulty()
chosen_colors = pick_colors(difficulty, colors)
create_tubes(chosen_colors,TubeHight)

while True:
    display_tubes()
    move_color()
    quit_game = input("Do you want to quit (yes/no)? ").lower()
    if quit_game == 'yes':
        break

