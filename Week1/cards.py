def monty(swaps):
    queen_loc = "middle"
    new_Loc = ""
    actions_lst = list(swaps)

    for swap in actions_lst:
        if swap == "L":
            if queen_loc == "left":
                queen_loc = "middle"
            elif queen_loc == "middle":
                queen_loc = "left"
        elif swap == "R":
            if queen_loc == "right":
                queen_loc = "middle"
            elif queen_loc == "middle":
                queen_loc = "right"
        elif swap == "O":
            if queen_loc == "right":
                queen_loc = "left"
            elif queen_loc == "left":
                queen_loc = "right"

    print(f"last queen loc: {queen_loc}")
    return queen_loc

print(monty("LROLL"))