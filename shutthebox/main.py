import dice

die1 = dice.roll_dice()
die2 = dice.roll_dice()

# a python list that's mutable
pips = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f"Your selections are {pips}")
print(f"Your dice are {str(die1)} and {str(die2)}")


def remove_pips():
    remove_pip = int(input("Enter the pips to remove: "))
    if remove_pip in pips:
        pips.remove(remove_pip)
    else: 
        print(f"The item you selected {remove_pip} is not found")
    return pips

remove_pips()

print(pips)
