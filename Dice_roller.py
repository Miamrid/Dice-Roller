import random

def roll_dice(dice_sides):
    return random.randint(1, dice_sides)


def main():
    print("Welcome to the world of dice roller")
    while True:
        dice_sides = int(input("Enter the number of sides of dice: "))
        if dice_sides<0:
            print("Enter a positive number")
        else:
            input("Press Enter to roll the dice...")
        result = roll_dice(dice_sides)
        print("You rolled:",result)

        play_again = input("Roll again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing! see you again later...")
            break

if __name__ == "__main__":
    main()



