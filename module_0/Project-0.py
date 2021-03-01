import numpy as np


def game_core_v4(number):
    count = 1
    diapason = list(range(1, 101))  # заданный диапазон
    mid_index = int(len(diapason) / 2)  # индекс угадываемого числа
    predict = diapason[mid_index]  # угадываемое число

    while number != predict:
        count += 1

        if number > predict:
            diapason = diapason[mid_index:]  # берем большую половину от заданного диапазона
        elif number < predict:
            diapason = diapason[:mid_index]  # берем меньшую половину от заданного диапазона

        mid_index = int(len(diapason) / 2)
        predict = diapason[mid_index]

    return count  # выход из цикла, если угадал


def score_game(game_core):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


if __name__ == '__main__':
    score_game(game_core_v4)