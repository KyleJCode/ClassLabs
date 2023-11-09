import p1_random as p1

"""
Kyle Jeter
COP3502C
Blackjack Game
"""

# Use continue statement for the print statistics option (3)
user_choice = 1
game_number = 0
user_hand = 0
dealer_hand = 0
# ACE = 1
# JACK = 11
# QUEEN = 12
# KING = 13
# Face cards (King, Queen, Jack) are worth a value of 10. If the player is dealt a King (generated as 13), the
# value 10 should be added to the player’s hand value rather than a 13. Aces have a value of 1. Every other
# card will be worth its face value.

rng = p1.P1Random()
while user_choice != 4:
    game_number += 1

    print(f"START GAME # {game_number}\n")
    card_num = rng.next_int(13)+1

    print(f"Your card is a: ")
    print(f"Your hand is a: ")

    if user_choice == 1:
        print("")
    elif user_choice == 2:
        print("")
    if user_choice == 3:
        print("")
    elif user_choice == 4:
        exit()
    else:
        print("Invalid input!")
        print("Please enter an integer value between 1 and 6")






