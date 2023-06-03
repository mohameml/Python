# START CORRECTION
def get_wining_threes(case):
    if case == 0:
        yield (0, 1, 2)
        yield (0, 3, 6)
        yield (0, 4, 8)
    elif case == 1:
        yield (0, 1, 2)
        yield (1, 4, 7)
    elif case == 2:
        yield (0, 1, 2)
        yield (2, 4, 6)
        yield (2, 5, 8)
    elif case == 3:
        yield (3, 4, 5)
        yield (0, 3, 6)
    elif case == 4:
        yield (1, 4, 7)
        yield (3, 4, 5)
        yield (0, 4, 8)
        yield (2, 4, 6)
    elif case == 5:
        yield (3, 4, 5)
        yield (2, 5, 8)
    elif case == 6:
        yield (6, 7, 8)
        yield (0, 3, 6)
        yield (6, 4, 2)
    elif case == 7:
        yield (6, 7, 8)
        yield (1, 4, 7)
    elif case == 8:
        yield (6, 7, 8)
        yield (0, 4, 8)
        yield (2, 5, 8)


def get_all_wining_threes():

    # 3 lines
    for line in range(3):
        first = 3 * line
        yield (first, first + 1, first + 2)

    # 3 columns
    for column in range(3):
        first = column
        yield (first, first + 3, first + 6)

    # 2 diagonals
    yield (0, 4, 8)
    yield (2, 4, 6)


def get_wining_play_in_wining_three(wining_three, cases, symbole):
    # Do I already have 2 in a row ?
    count = sum(1 for case in wining_three if cases[case] == symbole)
    # If yes, is the third position free ?
    if count == 2:
        free = next(
            (
                case
                for case in wining_three
                if cases[case] != "x" and cases[case] != "o"
            ),
            None,
        )
        if free:
            return free
    return None


def get_wining_play(cases, symbole):
    for three in get_all_wining_threes():
        play = get_wining_play_in_wining_three(three, cases, symbole)
        if play:
            return play
    return None


def get_empty_cases(cases):
    for case in cases:
        if case != "x" and case != "o":
            yield int(case)


def get_forks(cases, symbole):
    for case in get_empty_cases(cases):
        # suppose I play case
        new_cases = cases[:case] + [symbole] + cases[case + 1 :]
        # check if I now have two wining plays
        nb_wining_plays = 0
        for wining_threes in get_wining_threes(case):
            play = get_wining_play_in_wining_three(wining_threes, new_cases, symbole)
            if play:
                nb_wining_plays += 1
        if nb_wining_plays >= 2:
            yield case


def joue_coup(cases, symbole):

    # Win: if i have two in a row, I place a third
    # to get three in a row.
    free = get_wining_play(cases, symbole)
    if free:
        # print("WIN")
        return free

    # Block: if other has two in a row, block it
    oponent_symbol = "o" if symbole == "x" else "x"
    free = get_wining_play(cases, oponent_symbol)
    if free:
        # print("BLOCK")
        return free

    # Fork: create an opportunity where I have two ways
    # to win (two non-blocked lines of 2)
    free = next(get_forks(cases, symbole), None)
    if free:
        # print("FORK")
        return free

    # Blocking Fork: if there is only one possible fork for the opponent,
    # the player should block it. Otherwise, the player should block all
    # forks in any way that simultaneously allows them to create two in
    # a row. Otherwise, the player should create a two in a row to force
    # the opponent into defending, as long as it doesn't result in them
    # creating a fork. For example, if "X" has two opposite corners and
    # "O" has the center, "O" must not play a corner move in order to win.
    # (Playing a corner move in this scenario creates a fork for "X" to win.)
    oponent_forks = list(get_forks(cases, oponent_symbol))
    if len(oponent_forks) == 1:
        print(oponent_forks[0])
        return oponent_forks[0]

    # Center
    if cases[4] != "x" and cases[4] != "o":
        return 4

    # Opposite corners
    if cases[0] == oponent_symbol and cases[8] != "x" and cases[8] != "o":
        return 8
    if cases[8] == oponent_symbol and cases[0] != "x" and cases[0] != "o":
        return 0
    if cases[2] == oponent_symbol and cases[6] != "x" and cases[6] != "o":
        return 6
    if cases[6] == oponent_symbol and cases[2] != "x" and cases[2] != "o":
        return 2

    # Empty corners
    if cases[0] != "x" and cases[0] != "o":
        return 0
    if cases[2] != "x" and cases[2] != "o":
        return 2
    if cases[6] != "x" and cases[6] != "o":
        return 6
    if cases[8] != "x" and cases[8] != "o":
        return 8

    # Empty midle sides
    if cases[1] != "x" and cases[1] != "o":
        return 1
    if cases[3] != "x" and cases[3] != "o":
        return 3
    if cases[5] != "x" and cases[5] != "o":
        return 5
    if cases[7] != "x" and cases[7] != "o":
        return 7

    assert False


# END CORRECTION
