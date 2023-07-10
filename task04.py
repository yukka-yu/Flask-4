'''Создать программу, которая будет производить подсчет количества слов в каждом файле в указанной директории
и выводить результаты в консоль. Используйте потоки.'''

import threading
import os

PATH = 'threading/'


def count_words(file):
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
        amt = len(text.split(" "))
    print(f'{file} words {amt}')

threads = []

def main():
    for item in os.walk(PATH):
        for pos in item[2]:
            filename = os.path.join(item[0], pos)
            thread = threading.Thread(target=count_words, args=[filename])
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()

if __name__ == '__main__':
    main()