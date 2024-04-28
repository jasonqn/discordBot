import random
from random import randint


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    if lowered == '':
        return 'Say something dzaddy!'
    elif 'hello' in lowered:
        return 'Hello there!'


def roll_dice(select_dice: int, die_face_selection: int):
    die_face = [4, 6, 8, 10, 12, 20, 100]

    dice_amount = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    dice_roll = select_dice * (randint(1, die_face_selection))

    if select_dice not in dice_amount:
        return 'You can only roll up to 10 dice, your first input is the number of die you wish to roll'

    if die_face_selection not in die_face:
        return 'Invalid dice selection, only 4, 6, 8, 10, 12, 20, 100 sided die can be selected'

    return f'You chose {select_dice}  dice with {die_face_selection} faces giving you {dice_roll}'
