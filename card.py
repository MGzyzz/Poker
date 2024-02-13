import random


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


class Card:
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    SUITS = ["\u2660", "\u2665", "\u2666", "\u2663"]  # ♠ ♥ ♦ ♣

    def random_choice(self):
        random_ranks = random.choice(self.RANKS)
        random_suits = random.choice(self.SUITS)
        card = random_ranks + random_suits
        return card

    def show_card(self):
        return print(f"Карта: {self.random_choice()}")


class Deck:

    def __init__(self):
        self.deck = []
        i = 0
        while i != 52:
            card = Card().random_choice()
            if not (card in self.deck):
                self.deck.append(card)
                i += 1

    def give_card(self):
        card = random.choice(self.deck)
        self.deck.remove(card)
        return card


    def shuffle(self):
        random.shuffle(self.deck)

    def __str__(self):
        return f'{self.deck}'

class Checker:
    def __init__(self, hand):
        self.hand = hand
        self.score = 0

    def check_win(self):
        checks = [
            self.kare(),
            self.full_house(),
            self.flash(),
            self.three_of_a_kind(),
            self.two_pair(),
            self.pair(),
            self.high_card()
        ]
        for check in checks:
            score = check
            if score:
                print(f"\nОБЩАЯ КОЛИЧЕСТВО ОЧКОВ ПОЛУЧЕННО = {self.score}\n")
                return self.score



    def kare(self):
        ranks = []
        for i in self.hand:
            rank = i[:-1]
            ranks.append(rank)
        pairs = set(rank for rank in ranks if ranks.count(rank) == 4)
        if len(pairs) > 0:
            print("\nВыпало Каре! Количество полученных очков 8\n")
            self.score += 8
            return True
        else:
            return False

    def full_house(self):
        ranks = []
        for i in self.hand:
            rank = i[:-1]
            ranks.append(rank)
        pairs_one = set(rank for rank in ranks if ranks.count(rank) == 3)
        pairs_two = set(rank for rank in ranks if ranks.count(rank) == 2)

        if len(pairs_one) > 0 and len(pairs_two) > 0:
            print("\nВыпал Фулл-Хаус! Количество полученных очков 7\n")
            self.score += 7
            return True
        else:
            return False

    def flash(self):
        ranks = []
        for i in self.hand:
            rank = i[-1]
            ranks.append(rank)
        pairs = set(rank for rank in ranks if ranks.count(rank) == 5)
        if len(pairs) > 0:
            print("\nВыпал Флэш! Количество полученных очков 6\n")
            self.score += 6
            return True
        else:
            return False

    def three_of_a_kind(self):
        ranks = []
        for i in self.hand:
            rank = i[:-1]
            ranks.append(rank)
        pairs = set(rank for rank in ranks if ranks.count(rank) == 5)
        if len(pairs) > 0:
            print("\nВыпала Тройка! Количество полученных очков 4\n")
            self.score += 4
            return True,
        else:
            return False

    def two_pair(self):
        ranks = []
        for i in self.hand:
            rank = i[:-1]
            ranks.append(rank)
        pairs = set(rank for rank in ranks if ranks.count(rank) == 2)
        if len(pairs) == 2:
            print("\nВыпала Две пары! Количество полученных очков 3\n")
            self.score += 3
            return True
        else:
            return False

    def pair(self):
        ranks = []
        for i in self.hand:
            rank = i[:-1]
            ranks.append(rank)
        pairs = set(rank for rank in ranks if ranks.count(rank) == 2)
        if len(pairs) > 0:
            print("\nВыпала Пара! Количество полученных очков 2\n")
            self.score += 2
            return True
        else:
            return False

    def high_card(self):
        print("\nВыпала Старшая карта! Количество полученных очков 1\n")
        self.score += 1
        return True

class Application:
    def main(self):
        while True:
            print("Добро пожаловать в игру 'Покер. Обяьснение игры:\n[1]Вам будут даны карты в количестве 5 штук\n[2]Ваша задача получить наибольшую комбинацию которая есть в покере\n[3]В конце игры вам покажит количество очков\nУДАЧИ!\n")
            deck = Deck()
            deck.shuffle()
            player_hand = Hand(deck, [])

            for i in range(5):
                player_hand.take_card()
            print(player_hand)

            choose = input("\nХотите ли вы изменить карты? y/n: ").lower()
            while choose not in ['y', 'n']:
                choose = input(f"Неверный символ! Выберите символ 'y' или 'n': ").lower()

            if choose == "y":
                player_hand.card_replacement()
            Checker(player_hand.hand).check_win()

            choose_user = input("Хотите ли вы еще сыграть? y/n: ").lower()
            while choose_user not in ['y', 'n']:
                choose_user = input(f"Неверный символ! Выберите символ 'y' или 'n': ").lower()

            if choose_user != 'y':
                return True


Application().main()