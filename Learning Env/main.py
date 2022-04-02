from random import randint
from time import sleep


def draw_card():
    cards = ["J", "Q", "K", 2, 3, 4, 5, 6, 7, 8, 9, 10]  # 12
    return cards[randint(0, 11)]


def check_card_value(cards):
    card_value = 0
    ace_number = 0
    letters = ["K", "J", "Q"]
    for card in cards:
        if card in letters:
            card_value = card_value + 10
        elif card == "A":
            ace_number = ace_number + 1
        elif 2 <= int(card) <= 10:
            card_value = card_value + int(card)
    if ace_number != 0:
        card_value = card_value + ace_number * 1
        if card_value <= 11:
            if card_value + 10 <= 21:
                card_value = card_value + 10
    return card_value


computer_cards = [draw_card(), draw_card()]
player_cards = [draw_card(), draw_card()]

bet = int(input("State your bet: "))

print("Dealer:", computer_cards[0])
print("Your cards:", player_cards[0], player_cards[1])

while True:
    if check_card_value(player_cards) == 21 and len(player_cards) == 2:
        print("Blackjack! Victory:", str(bet * 2.5))
        exit()
    print("Decide: 1: Hit, 2: Stand")
    user_input = input()
    if user_input == "2":
        break
    if user_input == "1":
        player_cards.append(draw_card())
    print("Your cards:", *player_cards)
    if check_card_value(player_cards) > 21:
        print("Bust! You lost")
        exit()

while True:
    print("Dealer:", *computer_cards)
    if 15 <= check_card_value(computer_cards):
        if check_card_value(computer_cards) > 21:
            print("Dealer's bust. Victory! Winnings:", bet * 2)
            exit()
        if check_card_value(computer_cards) > check_card_value(player_cards):
            print("You lost!")
            exit()
        if check_card_value(computer_cards) == check_card_value(player_cards):
            print("Draw! Winnings:", bet)
            exit()
        else:
            print("Victory! Winnings:", bet * 2)
            exit()
    computer_cards.append(draw_card())
    sleep(2)
