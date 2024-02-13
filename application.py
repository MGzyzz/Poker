from deck import Deck
from hand import Hand
from checker import Checker


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
