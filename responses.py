import random


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    if lowered == '':
        return 'Say something dzaddy!'
    elif 'hello' in lowered:
        return 'Hello there!'


def roll_dice(select_dice: int, dice_amount: int):
    dices = [4, 6, 8, 10, 12, 20, 100]
    dice_range = range(1, 10, 1)
    dice_roll = select_dice * dice_amount

    if select_dice not in dices:
        return ''

    if dice_amount not in dice_range:
        return ''

    return f'You chose a {select_dice} sided dice and you roll {dice_amount} dices giving you {dice_roll}'
