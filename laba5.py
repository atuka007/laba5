import math
import time

def recur_f(n):  # Рекурсивная реализация
    if n == 1:
        return 1
    sign = -1 if n % 2 == 0 else 1
    return sign * (recur_f(n - 1) + math.factorial(n - 1) / math.factorial(2 * n))

def iter_f(n):  # Итерационная реализация
    if n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        sign = -1 if i % 2 == 0 else 1
        result = sign * (result + math.factorial(i - 1) / math.factorial(2 * i))
    return result

def optimized_iter_f(n):  # Оптимизированная итерационная реализация с минимизацией вычислений факториалов
    if n == 1:
        return 1
    result = 1
    prev_fact = 1  # (1-1)! = 0! = 1
    current_2n_fact = 2  # (2*1)! = 2! = 2

    for i in range(2, n + 1):
        sign = -1 if i % 2 == 0 else 1  # Вычисляем текущий факториал (i-1)!
        if i > 2:
            prev_fact *= (i - 2)
        for j in range(2 * (i - 1) + 1, 2 * i + 1):  # Вычисляем (2i)! используя предыдущее значение (2(i-1))!
            current_2n_fact *= j

        term = prev_fact / current_2n_fact
        result = sign * (result + term)
    return result

def measure_time(func, n, repetitions=100):  # Функция для измерения времени выполнения
    start_time = time.perf_counter()
    for _ in range(repetitions):
        func(n)
    end_time = time.perf_counter()
    return (end_time - start_time) / repetitions

def compare_approaches(max_n):  # Сравнительный анализ
    print("n\tРекурсивно (мс)\tИтерационно (мс)\tОптимизировано (мс)")
    for n in range(1, max_n + 1):
        if n <= 20:
            rec_time = measure_time(recur_f, n) * 1000
        else:
            rec_time = float('inf')

        it_time = measure_time(iter_f, n) * 1000
        opt_time = measure_time(optimized_iter_f, n) * 1000

        print(f"{n}\t{rec_time:.6f}\t\t{it_time:.6f}\t\t{opt_time:.6f}")

compare_approaches(20)  # Выполняем сравнение для n от 1 до 20
