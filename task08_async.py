import asyncio
import aiohttp
import time

SIZE = 200
urls = [f'http://www.radioscanner.ru/base/index.php?action=list&sortBy=0&page={i}' for i in range(SIZE)]

async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text()
            filename = url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
            with open('async/radioscanner/' + filename, "w", encoding='utf-8') as f:
                f.write(text)

async def main():
    tasks = []
    start_time = time.time()
    for url in urls:
        task = asyncio.ensure_future(download(url))
        tasks.append(task)
    await asyncio.gather(*tasks)
    count_time = time.time() - start_time
    print(f'{SIZE} pages downloaded; MP time: {count_time:0.3f}')



if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())