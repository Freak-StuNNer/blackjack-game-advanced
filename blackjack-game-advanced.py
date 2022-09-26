"""
blackjack_game_advanced.py

This program runs a version of black jack where the user needs to get a higher
card compination then the dealer. The highest you can go is 21, any higher and you bust.
Any ties go to the dealer.
"""

import random
import time
import os
import sys

def main():
    """
    Main function for the blackjack Program.
    """

#Clears the screen when the game starts and displays a welcome message.
    os.system('cls')
    print("\nWelcome to Blackjack.")
    print(f'\n{"":-^50}')

#Looking for user input to start the game.
    while True:
        while True:
            start_game = input("\nDo you want to sit down and start a new game?(y/n):")
            if start_game in ('n','no'):
                print('\nExiting the game.\n')
                sys.exit()
            elif start_game in ('y'):
                break
            else:
                print('\nInvalid entry.')

#Setting up the variable for the game to start.
        user_hand = []
        dealer_hand = []
        user_total = 0
        dealer_total = 0
        user_card_count = -1
        dealer_card_count = -1
        user_bust = False
        user_ace_spent = False
        dealer_ace_spent = False


#Initial card draw and storage into a list for the user and dealer.
        card_drew = card_draw()
        is_face_card, card_value = convert_card(card_drew, user_total)
        user_hand.append(is_face_card)
        user_card_count += 1
        user_total += int(card_value)
#Adjusting total if user has ace and hand and busts, one time only.
        if 'A' in user_hand and user_total > 21 and user_ace_spent is False:
            user_total -= 10
            user_ace_spent = True

        card_drew = card_draw()
        is_face_card, card_value = convert_card(card_drew, user_total)
        user_hand.append(is_face_card)
        user_card_count += 1
        user_total += int(card_value)
        if 'A' in user_hand and user_total > 21 and user_ace_spent is False:
            user_total -= 10
            user_ace_spent = True


#Initial card draw and storage into a list for the user and dealer.
        card_drew = card_draw()
        is_face_card, card_value = convert_card(card_drew, dealer_total)
        dealer_hand.append(is_face_card)
        dealer_card_count += 1
        dealer_total += int(card_value)
#Adjusting total if dealer has ace and hand and busts, one time only.
        if 'A' in dealer_hand and dealer_total > 21 and dealer_ace_spent is False:
            dealer_total -= 10
            dealer_ace_spent = True

        card_drew = card_draw()
        is_face_card, card_value = convert_card(card_drew, dealer_total)
        dealer_hand.append(is_face_card)
        dealer_card_count += 1
        dealer_total += int(card_value)
        if 'A' in dealer_hand and dealer_total > 21 and dealer_ace_spent is False:
            dealer_total -= 10
            dealer_ace_spent = True

#Message to show user what cards where drawn for user and dealer.
        print(f'\nUser drew a {user_hand[0]} and a {user_hand[1]}. User total is {user_total}')
        print(f'\nThe dealer drew a {dealer_hand[0]} and a hidden card.')


        while True:
#Checks for when the user busts or reaches 21.
            if user_total > 21:
                print('\nBust!\n\nDealer Wins!')
                user_bust = True
                break
            if user_total == 21:
                print('\nUser stands.')
                break
#Controls when the user hits or stands.
            hit_or_stand = input('\nHit or Stand? (h/s):')
            if hit_or_stand in ('h','hit'):
                card_drew = card_draw()
                is_face_card, card_value = convert_card(card_drew, user_total)
                user_hand.append(is_face_card)
                user_card_count += 1
                user_total += int(card_value)
                if 'A' in user_hand and user_total > 21 and user_ace_spent is False:
                    user_total -= 10
                    user_ace_spent = True
                print (f'\nHit! User drew a {user_hand[user_card_count]}.',end="")
                print (f' User total is {user_total}')
            elif hit_or_stand in ('s', 'stand'):
                print ('\nUser stands.')
                break
            else:
                print('\nInvalid entry.')
            continue

#If user not bust, then reveal the dealers hand and compare.
        if user_bust is False:
            time.sleep(1.5)
            print(f'\nThe dealers reveals the hidden card: {dealer_hand[1]}',end="")
            print(f' and has a total of {dealer_total}')
            time.sleep(1.5)

#Checks for if dealer is bust or over 16 total card draws.
            while True:
                if dealer_total > 21:
                    print("\nDealer busts!\n\nUser wins!!!")
                    break
                if dealer_total > 16:
                    if user_total < dealer_total:
                        print('\nDealer wins.')
                    elif user_total == dealer_total:
                        print('\nTie!\n\nDealer wins.')
                        break
                    else:
                        print('\nUser wins!!!')
                    break

#Draw phase for the dealer.
                card_drew = card_draw()
                is_face_card, card_value = convert_card(card_drew, dealer_total)
                dealer_hand.append(is_face_card)
                dealer_card_count += 1
                dealer_total += int(card_value)
                if 'A' in dealer_hand and dealer_total > 21 and dealer_ace_spent is False:
                    dealer_total -= 10
                    dealer_ace_spent = True

#Display drawn card and calculate new total.
                print(f'\nHit! Dealer drew a {dealer_hand[dealer_card_count]}.',end="")
                print (f' Dealers total is {dealer_total}')
                time.sleep(1.5)
                continue
        print(f'\n{"":-^50}')
        continue


def card_draw():
    """
    Return a random number between 1 and 13.
    """
    card = str(random.randint(1, 13))
    return card

def convert_card(card_to_convert, total):
    """
    Converts a number value to a face card. Returns the face card and the adjusted card value.
    """
    if card_to_convert == '11':
        converted_card = 'J'
        card_value = '10'
    elif card_to_convert == '12':
        converted_card = 'Q'
        card_value = '10'
    elif card_to_convert == '13':
        converted_card = 'K'
        card_value = '10'
    elif card_to_convert == '1':
        converted_card = 'A'
        if total + 11 > 21:
            card_value = '1'
        else:
            card_value = '11'
    else:
        converted_card = card_to_convert
        card_value = card_to_convert
    return converted_card, card_value


if __name__ == '__main__':
    main()
