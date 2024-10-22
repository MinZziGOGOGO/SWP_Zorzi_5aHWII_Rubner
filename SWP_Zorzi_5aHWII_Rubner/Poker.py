from collections import Counter
import random

class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def __str__(self):
        return f"{self.number} of {self.suit}"


def create_hand():
    numbers = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
    deck = [Card(number, suit) for number in numbers for suit in suits]
    hand = random.sample(deck, 5)
    return hand


def check_hand(hand):
    card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                   'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
    #split number and suits
    numbers = [card.number for card in hand]
    suits = [card.suit for card in hand]
    #number of ...
    number_counts = Counter(numbers)
    #for straight
    values = sorted(card_values[number] for number in numbers)
    #for pair
    count_values = sorted(number_counts.values(), reverse=True)
    #bool for cases ...
    flush = len(set(suits)) == 1
    straight = (len(set(values)) == 5 and max(values) - min(values) == 4) or values == [2, 3, 4, 5, 14]
    #print("hallo")
    if flush and straight and min(values) == 10:
        return "Royal Flush"
    if flush and straight:
        return "Straight Flush"
    if count_values == [4, 1]:
        return "Four of a Kind"
    if count_values == [3, 2]:
        return "Full House"
    if flush:
        return "Flush"
    if straight:
        return "Straight"
    if count_values == [3, 1, 1]:
        return "Three of a Kind"
    if count_values == [2, 2, 1]:
        return "Two Pair"
    if count_values == [2, 1, 1, 1]:
        return "Pair"

    return "High Card"


def main():
    poker_hands = {
        "High Card": 0,
        "Pair": 0,
        "Two Pair": 0,
        "Three of a Kind": 0,
        "Straight": 0,
        "Flush": 0,
        "Full House": 0,
        "Four of a Kind": 0,
        "Straight Flush": 0,
        "Royal Flush": 0
    }
    for i in range(10000000):
        hand = create_hand()
        result = check_hand(hand)
        poker_hands[result] += 1
    print(poker_hands)
    hands = list(poker_hands.keys())
    counts = list(poker_hands.values())

    total_counts = sum(counts)
    percentages = [(count / total_counts) * 100 for count in counts]
    print("Poker Hands Percentages:")
    for hand, percentage in zip(hands, percentages):
        print(f"{hand}: {percentage:.5f}%")

if __name__ == "__main__":
    main()
