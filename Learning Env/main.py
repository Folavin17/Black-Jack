player_count = int(input("Ilu będzie graczy?\n"))


def calculate_victory(cards):
    card_value = 0
    ace_number = 0
    letters = "KJTQ"
    for card in cards:
        if card in letters:
            card_value = card_value + 10
        elif card == "A":
            ace_number = ace_number + 1
        elif 2 <= int(card) <= 10:
            card_value = card_value + int(card)
    if ace_number != 0:
        card_value2 = card_value + ace_number * 1
        if 15 < card_value2 < 21:
            return True
        for ace in range(ace_number):
            card_value2 = card_value2 + 9
            if 15 < card_value2 < 21:
                return True
    if 15 < card_value < 21:
        return True
    return False


for i in range(player_count):
    print("Podaj karty", i + 1, "gracza")
    if calculate_victory(input()):
        print("Gracz", i + 1, "wygrywa")
    else:
        print("Gracz", i + 1, "przegrywa")
