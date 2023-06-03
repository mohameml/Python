# START CORRECTION
def joue_coup(cases, symbole):
    """Joue la première case libre."""
    for idx, case in enumerate(cases):
        if case == str(idx):
            return idx
    return None


# END CORRECTION
