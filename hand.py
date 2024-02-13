class Hand:
    def __init__(self, deck, hand):
        self.deck = deck
        self.hand = hand

    def take_card(self):
        self.hand.append(self.deck.give_card())

    def card_replacement(self):
        print(self.__str__())
        choose_user = input("Какуе карты вы хотите изменить? ").replace(" ", "")
        while not (choose_user.isdigit()) or any(int(j) > 5 for j in choose_user):
            if len(choose_user) == 0:
                return
            choose_user = input(f"Неверный символ! Символ не должен содержать букв или знаков. Повторите запрос снова:").replace(" ", "")

        for check in choose_user:
            for j in range(len(self.hand)):
                if j + 1 == int(check):
                    self.hand[j] = self.deck.give_card()
                    break
        print(f"\nКарты изменены\n{self.__str__()}")




    def print_header(self):
        result = ' '

        for i in range(5):
            result += f'| {i+1:<4}'

        return result + "|"

    def print_body(self):
        result = ' '
        for i in self.hand:
            result += f'| {i:<4}'
        return result + "|"

    def __str__(self):
        header = self.print_header()
        body = self.print_body()
        print(f"Вашы карты:")
        return f'\n{header}\n{body}\n'