import random

types_dices = ["D3", "D4", "D6", "D8", "D10", "D12", "D20", "D100"]


def dice(dice_code):
    dice_code = dice_code
    for dice in types_dices:
        if dice in dice_code:
            try:
                multiply, modifier = dice_code.split(dice)
                actual_dice = dice
            except ValueError:
                return "Wrong input"
            break
    else:
        return "Wrong input"

    throws = int(list_dice_code[0])
    extra_value = list_dice_code[1]



print(dice("2D10+8"))

