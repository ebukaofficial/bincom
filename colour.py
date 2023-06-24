# Colors for each day
colors = {
    "Monday": [
        "GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "BLUE", "YELLOW", "ORANGE",
        "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN"
    ],
    "Tuesday": [
        "ARSH", "BROWN", "GREEN", "BROWN", "BLUE", "BLUE", "BLEW", "PINK", "PINK", "ORANGE",
        "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "WHITE", "BLUE", "BLUE", "BLUE"
    ],
    "Wednesday": [
        "GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "RED", "YELLOW", "ORANGE", "RED",
        "ORANGE", "RED", "BLUE", "BLUE", "WHITE", "BLUE", "BLUE", "WHITE", "WHITE"
    ],
    "Thursday": [
        "BLUE", "BLUE", "GREEN", "WHITE", "BLUE", "BROWN", "PINK", "YELLOW", "ORANGE", "CREAM",
        "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN"
    ],
    "Friday": [
        "GREEN", "WHITE", "GREEN", "BROWN", "BLUE", "BLUE", "BLACK", "WHITE", "ORANGE", "RED",
        "RED", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "WHITE"
    ]
}

# Flatten the color lists for each day
all_colors = [color for day_colors in colors.values() for color in day_colors]

# Calculate the total number of colors
total_colors = len(all_colors)

# Count the occurrences of the color red
red_count = all_colors.count("RED")

# Calculate the probability of choosing red
red_probability = red_count / total_colors

print("Probability of choosing red:", red_probability)