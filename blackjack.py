
# Imports the random module provided
from p1_random import P1Random
rng = P1Random()

# Creates function to get value of user's card, generated by a random number from 1 to 13
def get_user_card():
    user_card = rng.next_int(13) + 1
    return user_card

# Creates function to get value of dealer's card, generated by a random number from 16 to 26
def get_dealer_hand():
    dealer_hand = rng.next_int(11) + 16
    return dealer_hand

'''
Title: Python Functions - How to Define and Call a Function
Author: Kolade Chris
Date: March 16, 2022
Code Version: Python
Availability: https://www.freecodecamp.org/news/python-functions-define-and-call-a-function
'''

# Creates a function involving to assign string/terms for certain values
def get_value_card(user_card):
    if user_card == 1:
        value_card = "ACE"
    elif user_card == 11:
        value_card = "JACK"
    elif user_card == 12:
        value_card = "QUEEN"
    elif user_card == 13:
        value_card = "KING"
    else:
        value_card = user_card
    return value_card

# Creates a function for tracking the user's hand, a sum of the card values the user has received
def get_user_hand(current_hand, value_card):

# Assigns King, Queen, and Jack to a value of 10
    if (value_card > 10):
        value_card = 10
    user_hand = (current_hand + value_card)
    return user_hand

# Defines each variable so that they can be used in the while loop
player_wins = 0
dealer_wins = 0
tie_games = 0
percent_wins = 0
game_count = 1
user_selection = 1
user_hand = 0
new_game = 1

'''
Title: Chapter 3: Program Control
Author: Yasaman Adibi, et al.
Date: n.d.
Code Version: Python
Availability: https://learn.zybooks.com/zybook/UFLCOP3502CFall2022/chapter/3/section/1
'''

# Creates a loop to allow the user to play until they choose to exit
while user_selection != 4:

# Keeps track of the number of games played so each game starts with a new game number counting up
    if new_game == 1:
        user_hand = 0
        dealer_hand = 0
        print("START GAME #" + str(game_count))
        user_card = get_user_card()
        value_card = get_value_card(user_card)
        print("\nYour card is a " + str(value_card) + "!")
        current_hand = user_hand
        user_hand = get_user_hand(current_hand, user_card)
        print("Your hand is: " + str(user_hand))

# Prints the menu for the user to choose from
    print("\n1. Get another card")
    print("2. Hold hand")
    print("3. Print statistics")
    print("4. Exit")

# Assigns user's input to variable user_selection and expects user's input to be an integer
    user_selection = int(input("\nChoose an option: "))

# Calls designated functions for getting a card then prints its value when user inputs 1
    if user_selection == 1:
        user_card = get_user_card()
        value_card = get_value_card(user_card)
        print("Your card is a " + str(value_card) + "!")

# Calls function for user's hand in the current game then prints it
        current_hand = user_hand
        user_hand = get_user_hand(current_hand, user_card)
        print("Your hand is: " + str(user_hand))

# Determines that user loses when their hand is greater than 21, but wins when their hand is equal to 21
        if user_hand > 21:
            print("\nYou exceeded 21! You lose.\n")
            user_hand = 0
            new_game = 1
            dealer_wins = (dealer_wins + 1)
            game_count = (game_count + 1)
        elif user_hand == 21:
            print("\nBLACKJACK! You win!\n")
            new_game = 1
            player_wins = (player_wins + 1)
            game_count = (game_count + 1)
        else:
            new_game = 0

# Calls designated functions for getting the dealer hand then prints its value when user inputs 2
    elif user_selection == 2:
        dealer_hand = get_dealer_hand()
        print("Dealer's hand: " + str(dealer_hand))
        print("Your hand is: " + str(user_hand))

# Determines that dealer loses when their hand is greater than 21, but wins when their hand is equal to 21
        if dealer_hand > 21:
            print("\nYou win!\n")
            new_game = 1
            player_wins = (player_wins + 1)
            game_count = (game_count + 1)
            user_hand = 0
        elif dealer_hand == 21:
            print("Dealer wins!\n")
            dealer_wins = (dealer_wins + 1)
            game_count = (game_count + 1)
            new_game = 1

# Determines when user or dealer wins, loses, or ties by comparing hands
        elif dealer_hand == user_hand:
            print("It's a tie! No one wins!\n")
            tie_games = (tie_games + 1)
            game_count = (game_count + 1)
            new_game = 1

# Determines that the winner has hand value under and closer to or equal to 21
        elif dealer_hand > user_hand:
            print("\nDealer wins!\n")
            dealer_wins = (dealer_wins + 1)
            game_count = (game_count + 1)
            new_game = 1

# Creates new game each time someone wins, loses, or ties
# Keeps track of number of games played with variable game_count
        elif user_hand > dealer_hand:
            print("\nYou win!\n")
            player_wins = (player_wins + 1)
            game_count = (game_count + 1)
            new_game = 1
        else:
            new_game = 1

# Displays statistics by adding designated variables to print statements when user inputs 3
    elif user_selection == 3:
        print("\nNumber of Player wins: " + str(player_wins))
        print("Number of Dealer wins: " + str(dealer_wins))
        print("Number of tie games: " + str(tie_games))
        print("Total # of games played is: " + str(game_count - 1))

# Calculates percent of user wins by dividing player_wins by game_count and multiplying quotient by 100
        percent_wins = float((player_wins / (game_count - 1)) * 100)

# Formats the float percentage to print only one decimal place out
        print("Percentage of Player wins: " + "{:.1f}".format(percent_wins) + "%")
        new_game = 0

# Exits and terminates the program when user inputs 4
    elif user_selection == 4:
        exit()

# Displays error message when user inputs anything other than integer values 1 to 4
    else:
        print("Invalid input!")
        print("Please enter an integer value between 1 and 4.")
        new_game = 0