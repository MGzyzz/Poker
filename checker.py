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


checker = Checker(['K♣', 'K♣', 'A♠', '2♥', '♣'])
checker.check_win()