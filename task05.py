'''Создать программу, которая будет производить подсчет
количества слов в каждом файле в указанной директории и
выводить результаты в консоль.
Используйте процессы.'''

from multiprocessing import Process, Pool
import os

PATH = 'threading/'

def count_words(file):
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
        amt = len(text.split(" "))
    print(f'{file} words {amt}')

processes = []

def main():
    for item in os.walk(PATH):
        for pos in item[2]:
            filename = os.path.join(item[0], pos)
            process = Process(target=count_words, args=[filename])
            processes.append(process)
            process.start()

for process in processes:
    process.join()

if __name__ == '__main__':
    main()