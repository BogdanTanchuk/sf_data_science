import numpy as np

def game_core_v3(number: int = 1, left=0, right=101, count=0) -> int:
    count += 1
    predict = (left + right) // 2

    if number == predict:
        return count
    elif number > predict:
        return game_core_v3(number, predict, right, count)
    elif number < predict:
        return game_core_v3(number, left, predict, count)
    
def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")

print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)