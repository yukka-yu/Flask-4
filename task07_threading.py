'''Напишите программу на Python, которая будет находить
сумму элементов массива из 1000000 целых чисел.
� Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
� Массив должен быть заполнен случайными целыми числами
от 1 до 100.
� При решении задачи использовать многопоточность
В каждом решении нужно вывести время выполнения
вычислений.'''

import threading
import random
import time

SIZE = 1_000_000
summa = 0

massive = [random.randint(1, 100) for i in range(SIZE)]

def sum_(arr):
    global summa
    summa += sum(arr)

def main():
    threads = []
    start_time = time.time()
    num = 0

    for _ in range(10):
        global summa
        thread = threading.Thread(target=sum_, args=[massive[num: num+100000]])
        num += 100000
        threads.append(thread)
        thread.start()
    count_time = time.time() - start_time
    print(f'Summ = {summa}; Threading time: {count_time:0.3f}')

    for thread in threads:
        thread.join()

    

if __name__ == '__main__':
    main()
