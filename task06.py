'''Создать программу, которая будет производить подсчет
количества слов в каждом файле в указанной директории и
выводить результаты в консоль.
Используйте асинхронный подход.'''

import asyncio
import os

PATH = 'threading/'

async def count_words(file):
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
        amt = len(text.split(" "))
    print(f'{file} words {amt}')

async def main():
    tasks = []
    for item in os.walk(PATH):
        for pos in item[2]:
            filename = os.path.join(item[0], pos)
            task = asyncio.ensure_future(count_words(filename))
            tasks.append(task)
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())