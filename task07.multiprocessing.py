import multiprocessing 
import random
import time

SIZE = 1_000_000
summa = multiprocessing.Value('i', 0)

massive = [random.randint(1, 100) for i in range(SIZE)]

def sum_(arr):
    with summa.get_lock():
        summa.value += sum(arr)

def main():
    processes = []
    start_time = time.time()
    num = 0

    for _ in range(10):
        process = multiprocessing.Process(target=sum_, args=[massive[num: num+100000]])
        num += 100000
        processes.append(process)
        process.start()
    count_time = time.time() - start_time
    print(f'sum = {summa.value}; MP time: {count_time:0.3f}')

    for process in processes:
        process.join()

if __name__ == '__main__':
    main()

