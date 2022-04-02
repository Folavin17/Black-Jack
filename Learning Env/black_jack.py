from random import randint

cards = ["J", "Q", "K", 2, 3, 4, 5, 6, 7, 8, 9, 10]  # 12


def draw_card():
    return cards[randint(0, 11)]


computer_cards = ""
player_cards = ""
computer_cards = computer_cards + draw_card() + draw_card()
player_cards = player_cards + draw_card() + draw_card()
print(computer_cards)
print(player_cards)