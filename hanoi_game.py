import sys
from copy import copy

NUMBER_OF_DISKS = 5
FINAL_RESULT = list(range(NUMBER_OF_DISKS, 0, -1))
ALLOWED_MOVES = ["AB", "AC", "BA", "BC", "CA", "CB"]


def display_towers(towers):
    # [5, 4, 3, 0, 0] [1, 0, 0, 0, 0] [2, 0, 0, 0, 0]

    for level in range(NUMBER_OF_DISKS, -1, -1):
        for tower in towers.values():
            if level >= len(tower):
                display_disk(0)
            else:
                display_disk(tower[level])
        print()


def display_disk(disk):
    empty_space = (NUMBER_OF_DISKS - disk) * " "
    if disk < 0:
        raise ValueError("Disk value cannot be lower than 0")
    if disk == 0:
        print(f"{empty_space}||{empty_space}", end="")
    else:
        print(f'{empty_space}{disk * "*"} {disk}{disk * "*"}{empty_space}', end="")


def get_player_move(towers):
    while True:
        player_input = input("Move one disk, enter Q to quit: ").upper()
        if player_input == "Q":
            sys.exit()
        if player_input not in ALLOWED_MOVES:
            print("Enter a valid combination")
            continue

        source, destination = player_input
        if len(towers[source]) == 0:
            print("Source tower cannot be empty")
            continue
        if len(towers[destination]) == 0:
            return source, destination
        if towers[source][-1] > towers[destination][-1]:
            print("Source disk cannot be bigger than destination disk")
            continue
        return source, destination


def main():
    towers = {"A": copy(FINAL_RESULT), "B": [], "C": []}
    while True:
        display_towers(towers)
        source, destination = get_player_move(towers)
        disk_to_move = towers[source].pop()
        towers[destination].append(disk_to_move)
        if FINAL_RESULT in (towers["B"], towers["C"]):
            print("You've won!")
            break


if __name__ == "__main__":
    main()
