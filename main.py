############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from random import choice
import os
from art import logo


def deal_card():
    """Returns a random card from the list."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = choice(cards)
    return card

def calculate_score(cards):
    """Takes in a card list and returns a sum of the list."""
    # checking for 21 at start
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # checking for an 11 in hand if score is over 21
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    """Compares passed in scores to determine winner."""
    if computer_score == 0:
        return "You lose! Computer has Blackjack."
    elif user_score == 0:
        return "You win! You have Blackjack."
    elif user_score == computer_score:
        return "Draw!"
    elif user_score > 21:
        return "You lose! You busted!"
    elif computer_score > 21:
        return "You win! Computer busted!"
    elif user_score > computer_score:
        return "You win!"
    elif computer_score > user_score:
        return "You lose!"
    else:
        return

def play_game():
    """Main function of the blackjack game."""
    print(logo)

    user_hand = []
    computer_hand = []
    is_game_over = False

    for i in range(2):
        user_hand.append(deal_card())
        computer_hand.append(deal_card())
    
    while not is_game_over:
        user_current_score = calculate_score(user_hand)
        computer_current_score = calculate_score(computer_hand)
        print(f"Your cards {user_hand} ,current score: {user_current_score}")
        print(f"Computer's cards {computer_hand[0]}")

        if computer_current_score == 0 or user_current_score == 0 or user_current_score > 21:
            is_game_over = True
        else:
            user_hit = input("Type 'h' to hit for another card, type 'p' to pass: ")
            if user_hit == "h":
                user_hand.append(deal_card())
            else:
                is_game_over = True

    while computer_current_score != 0 and user_current_score != 0 and computer_current_score < 17:
        computer_hand.append(deal_card())
        computer_current_score = calculate_score(computer_hand)

    print(f"   Your final hand: {user_hand}, final score: {user_current_score}")
    print(f"   Computer's final hand: {computer_hand}, final score: {computer_current_score}")
    print(compare(user_current_score, computer_current_score))

while input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    os.system('clear')
    play_game()
