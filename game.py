import random

types_dices = ["D3", "D4", "D6", "D8", "D10", "D12", "D20", "D100"]


def dice(dice_code):
    dice_code = dice_code
    for dice in types_dices:
        if dice in dice_code:
            try:
                multiply, modifier = dice_code.split(dice)
                actual_dice = int(dice[1:])
            except ValueError:
                return "Wrong input"

            break
    else:
        return "Wrong input"

    try:
        multiply = int(multiply) if multiply else 1
    except:
        return "Wrong input"
    try:
        modifier = int(modifier) if modifier else 0
    except:
        return "Wrong input"
    sum_throws = 0
    for i in range(multiply):
        throw = random.randint(1, actual_dice+1)
        print(throw)
        sum_throws += throw
    sum_dices = sum_throws + modifier
    return sum_dices

if __name__ == "__main__":
    print(dice("3D6+2"))

