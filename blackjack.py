import random

# deck of cards / player dealer hand
ah

#VERSION 1
deck = []
cardValues = {
    '2':2, '3':3, '4':4, '5':5, '6':6,'7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11
}

deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace'] * 4

random.shuffle(deck)

def dealCard(deck):
    return deck.pop()


def calculate_hand(hand):
    total = sum(cardValues[card] for card in hand)
    for card in  hand:
        if card == 'A'  and total >= 21:
            total -= 10
    return total



def player_turn(deck, player_hand):
    while True:
        player_choice = input("Hit or Stand? ").lower()
        if player_choice == 'hit':
            player_hand.append(dealCard(deck))
            total = calculate_hand(player_hand)
            print("Your hand:", player_hand, "Total:",total)
            if total > 21:
                print("That's a Bust! You lose.")
                return False
        elif player_choice == "stand":
            return True



def dealer_turn (deck, dealer_hand):
    while calculate_hand(dealer_hand) < 17:
        dealer_hand.append(dealCard(deck))
    return dealer_hand


while True:
    player_hand = [dealCard(deck), dealCard(deck)]
    dealer_hand = [dealCard(deck), dealCard(deck)]

    print("Your hand:", player_hand, "Total:", calculate_hand(player_hand))
    print("Dealer's hand:", dealer_hand[0])

    if player_turn(deck, player_hand):
        dealer_hand = dealer_turn(deck, dealer_hand)
        print("dealer's hand:", dealer_hand, "Total:", calculate_hand(dealer_hand))
        player_total = calculate_hand(player_hand)
        dealer_total = calculate_hand(dealer_hand)
        if dealer_total > 21 or player_total > dealer_total:
            print("You win!")

        elif dealer_total > player_total:
            print("Dealer wins!")
        else:
            print("It's a tie")

    play_again = input("Would you like to play again? ").lower()
    if play_again == 'no':
         break

    if len(deck) < 10:
        deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q','K','A']*4
        random.shuffle(deck)

    print("Thanks for playing!")



