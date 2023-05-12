import os
import random

def main():
    filename = "excuses.txt"
    print(f"Reading {filename}")

    with open(filename, "r") as file:
        raw_lines = file.readlines()

    lines = []
    for line in raw_lines:
        clean_line = line.strip()
        #print(clean_line)

        # skip empty lines
        if clean_line == '':
            continue
        # skip comments 
        if clean_line.startswith("#"):
            continue 

        lines.append(clean_line)

    first_parts = []
    second_parts = []
    third_parts = []

    current_section = 0

    for line in lines:
        if line == '<section>':
            current_section += 1
        else: 
            # regular line
            # add to the right part list
            if current_section == 1:
                first_parts.append( line )
            elif current_section == 2: 
                second_parts.append(line)
            elif current_section == 3 :
                third_parts.append(line)
        
    # print(first_parts)
    # print(second_parts)
    # print(third_parts)

    random_first_part = random.choice( first_parts)
    random_second_part = random.choice( second_parts)
    random_third_part = random.choice( third_parts)


    print(random_first_part, random_second_part, random_third_part)


if __name__ == "__main__":
    main()