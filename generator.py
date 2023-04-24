import os

def main():
    filename = "excuses.txt"
    print(f"Reading {filename}")

    with open(filename, "r") as file:
        raw_lines = file.readlines()

    lines = []
    count = 0
    for line in raw_lines:
        clean = str.strip( line )
        lines.append( clean  )
        print(f"line {count}: " + line)
        count = count + 1

        # if line is blank, skip it
        # if line starts with a #, skip it
        # remove \n from each line



if __name__ == "__main__":
    main()