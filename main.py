import numpy as np

number = np.random.randint(1, 101)  # задаём число, которое требуется угадать

def game_core(number):  # функция подсчёта количества попыток
    count = 0  # задём счётчик
    first = 1  # задаём начало интервала
    last = 100  # задаём конец интервала
    predict = (first + last) // 2  # задаём предполагаемое число
    # для запуска цикла while
    while number != predict:  # цикл, выполняющийся пока не будет угадано число
        count += 1  # плюсуем попытку
        if number == predict:
            break  # выход из цикла, если угадали
        elif number > predict:
            # меняем начало интервала, если
            # загаданное число больше предполагаемого
            first = predict + 1
        elif number < predict:
            # меняем конец интервала, если
            # загаданное число меньше предполагаемого
            last = predict - 1
        predict = (first + last) // 2  # задаём новое предполагаемое число
    return(count)  # возвращаем количество попыток


# дальнейший код взят из задания
def score_game():
    # Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED,
    # чтобы ваш эксперимент был воспроизводим
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = round(np.mean(count_ls))  # единственное изменение,
    # для честности решил округлять, а не просто отбрасывать цифры после точки
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


score_game()
