#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""
import random
import time


class Ticket:

    def __init__(self):
        self.kegs = []
        self.__generate_ticket__()

    def __str__(self):
        result = f"{'-'*26}\n"
        for line in self.kegs:
            result += ' '.join([f'{x:2}' for x in line])+'\n'
        result += f"{'-'*26}"
        return result

    def __generate_ticket__(self):
        possible = list(range(1, 91))
        values = [possible.pop(random.randint(0, len(possible)-1)) for x in range(15)]
        for i in range(3):
            line = []
            for j in range(5):
                line.append(values.pop())
            line = sorted(line)

            for k in range(4):
                index = random.randrange(len(line)+1)
                line.insert(index, ' ')
            self.kegs.append(line)

    def check_keg(self, keg):
        for line in self.kegs:
            if keg in line:
                return True
        return False

    def get_keg_count(self):
        count = 0
        for line in self.kegs:
            count += len([k for k in line if k not in [' ', '-']])
        return count

    def cross_off__keg(self, keg):
        for line in self.kegs:
            for i, k in enumerate(line):
                if k == keg:
                    line[i] = '-'
                    return True
        return False


class Player:

    def __init__(self, name, is_ai=True):
        self.name = name
        self.is_ai = is_ai
        if is_ai:
            self.name += '(AI)'
        self.ticket = Ticket()

    def __ai_step__(self, keg):
        time.sleep(0.5)
        answer = self.ticket.check_keg(keg)
        if random.randint(0, 100) == 0:
            answer = not answer
        return answer

    def step(self, keg):
        print(f'{self.name} STEP')
        print(str(self.ticket))
        print('Cross off number? [Y/N]')
        if self.is_ai:
            is_cross_off = self.__ai_step__(keg)
            print('Y' if is_cross_off else 'N')
        else:
            answer = input()
            is_cross_off = answer.upper() == 'Y'

        if is_cross_off:
            return self.ticket.cross_off__keg(keg)
        elif self.ticket.check_keg(keg):
            return False
        return True


class Loto:

    def __init__(self, **kwargs):
        self.kegs = []
        self.players = []
        if 'players' in kwargs:
            self.players = kwargs['players']
        self.round_index = -1

    def __get_random_keg__(self):
        random.shuffle(self.kegs)
        return self.kegs.pop()

    def add_player(self, player):
        self.players.append(player)

    def __step__(self):

        message = f'ROUND {self.round_index}'
        print(f'{message:=^50}')

        current_keg = self.__get_random_keg__()
        print(f'CURRENT KEG IS {current_keg} ({len(self.kegs)} left)')

        for pl in self.players:
            if not pl.step(current_keg):
                print(f'{pl.name} is lose')
                self.players.remove(pl)
            elif pl.ticket.get_keg_count() == 0:
                return True, pl
            else:
                print(f'{pl.ticket.get_keg_count()} kegs left\n')

        self.round_index += 1
        if len(self.players) == 0:
            return True, None
        return False, None

    def start_game(self):
        self.kegs = list(range(1, 91))
        self.round_index = 1
        is_end_game = False
        winner = None
        while not is_end_game:
            is_end_game, winner = self.__step__()
        if winner:
            print(f'Winner - {winner.name}')
        else:
            print(f'Winner not found')


def main():

    end_creation = False
    players = []
    while not end_creation:
        name = input('Enter player name:\n')
        ai = input('This player is AI? [Y/N]\n')
        is_ai = ai.upper() == 'Y'
        players.append(Player(name, is_ai))
        if len(players) < 2:
            end = 'Y'
        else:
            end = input('Create next player? [Y/N]\n')
        end_creation = end.upper() == 'N'
    game = Loto(players=players)
    game.start_game()


def test():
    pl = Player('TEST', True)
    pl_2 = Player('PC', True)
    pl_3 = Player('BOT', True)
    game = Loto(players=[pl, pl_2, pl_3])
    game.start_game()


if __name__ == '__main__':
    main()
