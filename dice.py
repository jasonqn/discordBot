from random import randint


def roll_dice(select_dice: int, die_face_selection: int):
    # how many faces each die will have
    die_face = {
        4: 4,
        6: 6,
        8: 8,
        10: 10,
        12: 12,
        20: 20,
        100: 100
    }

    # amount of dice users can select, max 10
    dice_amount = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    # roll logic
    dice_rolls = [randint(1, die_face[die_face_selection]) for _ in range(select_dice)]

    # total rolls
    total_roll: int = sum(dice_rolls)

    # Format individual rolls
    individual_rolls = ', '.join(str(roll) for roll in dice_rolls)

    # error handling
    if select_dice not in dice_amount:
        return 'You can only roll up to 10 dice, your first input is the number of die you wish to roll'

    if die_face_selection not in die_face:
        return 'Invalid dice selection, only 4, 6, 8, 10, 12, 20, 100 sided die can be selected'

    return total_roll


def stat_roll_logic():
    stat = [roll_dice(1, 6) for _ in range(4)]
    stat.sort()
    while stat[0] & stat[1] == 1:
        stat.pop(0)
        new_roll = roll_dice(1, 6)
        stat.insert(0, new_roll)
    lowest_roll = min(stat)
    stat_total = sum(stat) - lowest_roll
    return (f"{stat_total}, you rolled {stat} taking the lowest roll away "
            f"of : {lowest_roll}\n ")


def random_stat_roll():
    stat = [roll_dice(1, 6) for _ in range(4)]
    stat.sort()
    stat_total = sum(stat)
    return f"{stat_total}, you rolled {stat}"


