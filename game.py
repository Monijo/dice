import random

types_dices = ["D3", "D4", "D6", "D8", "D10", "D12", "D20", "D100"]


def dice(dice_code):
    dice_code = dice_code
    for dice in types_dices:
        if dice in dice_code:
            print(dice)

print(dice("2D10+8"))

