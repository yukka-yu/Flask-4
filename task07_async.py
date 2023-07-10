import asyncio
import time
from random import randint

SIZE = 1_000_000
summa = 0
massive = [randint(1, 100) for i in range(SIZE)]

async def sum_(arr):
    global summa
    summa += sum(arr)

async def main():
    tasks = []
    start_time = time.time()
    num = 0

    for _ in range(10):
        start_time = time.time()
        task = asyncio.ensure_future(sum_(massive[num:num+100_000]))
        tasks.append(task)
        num += 100_000
    await asyncio.gather(*tasks)
    count_time = time.time() - start_time
    print(f'summa = {summa}; Async time: {count_time:0.3f}')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())