from random import randint



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

bet = input("Podaj wartosc zakladu: ")

print("Karty dilera:", computer_cards[0])
print("Twoje karty:", player_cards[0], player_cards[1])

while True:
    if check_card_value(player_cards) == 21 and len(player_cards) == 2:
        print("Blackjack! Wygrywasz:", str(float(bet) * 2.5))
    print("Podejmij decyzje: 1: Hit, 2: Stand")
    user_input = input()
    if user_input == "2":
        break
    if user_input == "1":
        player_cards.append(draw_card())
    if check_card_value(player_cards) > 21:
        print("Bust! Przegrywasz")
        break
    print("Twoje karty:", *player_cards)

