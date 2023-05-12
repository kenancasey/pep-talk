import os
import random 

def main():
    filename = "pep-talk.txt"
    print(f"Reading {filename}")

    with open(filename, "r") as file:
        raw_lines = file.readlines()

    #print(raw_lines)
    lines = []
    for line in raw_lines:
        clean_line = line.strip()

        #skipping empty lines
        if clean_line == '':
            continue

        #skipping coments
        if clean_line.startswith("#"):
            continue

        lines.append(clean_line)
    #print(lines)

    first_part = []
    second_part = []
    third_part = []
    final_part = []
    
    current_section = 0

    for line in lines:
        if line == '<section>':
            current_section += 1
        
        else:
            #regular line
            #add to correct section
            if current_section == 1:
                first_part.append(line)
            elif current_section == 2:
                second_part.append(line)
            elif current_section == 3:
                third_part.append(line)
            elif current_section == 4:
                final_part.append(line)

    random_first_part = random.choice(first_part)
    random_second_part = random.choice(second_part)
    random_third_part = random.choice(third_part)
    random_final_part = random.choice(final_part)

    print(random_first_part + " " + random_second_part + " " + random_third_part + " " + random_final_part)

if __name__ == "__main__":
    main()