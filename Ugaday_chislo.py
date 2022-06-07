'''
1) Комп загадывает число.
2) Игрок вводит с клавитуры число.
3) Компьютер даёт наводку(больше либо меньше).
4) Возвращаемся к шагу 2.
5) Повторять пока не кончатся попытки.
'''

import random

comp_number = random.randint(0, 10)
hearts = 3
player_number = 10

while hearts > 0 and not comp_number == player_number:
    player_number = int(input("Ваше число: "))
    if comp_number > player_number:
        print("Моё число больше")
    elif comp_number < player_number:
        print("Моё число меньше")
    else:
        print(f"Вы угадали за {3 - hearts + 1} попытки")
    hearts -= 1



