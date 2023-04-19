"""
Horner Bible Reading Plan
"""

import yaml

# Load Configuration File:
with open("config.yml", "r", encoding="utf-8") as config:

    # Read yaml:
    config = yaml.safe_load(config)

    # Configuration variables:
    readings_start = config["readings_start"]
    readings_end = config["readings_end"]

    # Load each list:
    list_1 = config["list_1"]
    list_2 = config["list_2"]
    list_3 = config["list_3"]
    list_4 = config["list_4"]
    list_5 = config["list_5"]
    list_6 = config["list_6"]
    list_7 = config["list_7"]
    list_8 = config["list_8"]
    list_9 = config["list_9"]
    list_10 = config["list_10"]


def get_readings_list(items):
    """
    Returns a list of all readings for a given list of books.
    """

    readings_list = []

    # Loop through list:
    for item in items:

        # Split into book and total chapters:
        book, total_chapters = item.split(", ")

        # Make chapters an integer:
        total_chapters = int(total_chapters)

        # Keep looping through available chapters from books in list:
        for chapter in range(1, total_chapters + 1):

            # Append book and chapter (as string) to list,
            # giving us the full list of readings for this list:
            readings_list.append(book + " " + str(chapter))

    return readings_list


# Create empty lists to populate with readings:
readings_list_1 = get_readings_list(list_1)
readings_list_2 = get_readings_list(list_2)
readings_list_3 = get_readings_list(list_3)
readings_list_4 = get_readings_list(list_4)
readings_list_5 = get_readings_list(list_5)
readings_list_6 = get_readings_list(list_6)
readings_list_7 = get_readings_list(list_7)
readings_list_8 = get_readings_list(list_8)
readings_list_9 = get_readings_list(list_9)
readings_list_10 = get_readings_list(list_10)

# Combine each list:
combined_lists = (
    readings_list_1,
    readings_list_2,
    readings_list_3,
    readings_list_4,
    readings_list_5,
    readings_list_6,
    readings_list_7,
    readings_list_8,
    readings_list_9,
    readings_list_10,
)


# Loop through readings:
for i in range(readings_start, readings_end):

    # Count the day number we are on:
    day = i + 1

    # Print the readings:
    print(
        day,
        readings_list_1[i % len(readings_list_1)],
        readings_list_2[i % len(readings_list_2)],
        readings_list_3[i % len(readings_list_3)],
        readings_list_4[i % len(readings_list_4)],
        readings_list_5[i % len(readings_list_5)],
        readings_list_6[i % len(readings_list_6)],
        readings_list_7[i % len(readings_list_7)],
        readings_list_8[i % len(readings_list_8)],
        readings_list_9[i % len(readings_list_9)],
        readings_list_10[i % len(readings_list_10)],
        sep=", ",
    )
