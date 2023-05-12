import os
import random

def main():
    filename = "pep-talk.txt"
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

    current_section=0
    list_of_part_lists = []
    current_list = []

    for line in lines:
        if line == '<section>':
            current_section += 1
            list_of_part_lists.append( [] )
            current_list = list_of_part_lists[ -1]
        else: 
            # regular line
            current_list.append(line)

    #print(list_of_part_lists)

    sentence = ""
    for list in list_of_part_lists:
        sentence += random.choice(list) + " "

    print(sentence)

if __name__ == "__main__":
    main()