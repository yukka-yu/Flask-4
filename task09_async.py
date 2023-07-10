import sys
import asyncio
import aiohttp, aiofiles
import time

'''urls = ['https://sibirds.ru/taxons/1486/fronpic1.jpg', 'https://images.vfl.ru/ii/1674314341/afc224c7/38705380_m.jpg',
         'https://birds.kg/taxons/163/fronpic2.jpg', 'https://ic.pics.livejournal.com/pantv/14908973/7538068/7538068_900.jpg', 
         'https://ic.pics.livejournal.com/pantv/14908973/7042833/7042833_800.jpg', 'https://images.vfl.ru/ii/1674314341/62849390/38705379_m.jpg'
        ]'''

async def download_image(url):
    img_name = url[url.rfind('/') + 1 : ]
    async with aiohttp.ClientSession() as session:
        response = await session.request(method="GET", url=url)
        async with aiofiles.open('async/' + img_name, mode='wb') as file:
            await file.write(await response.read()) 



async def main(urls):
    tasks = []
    start_time = time.time()
    for url in urls:
        task = asyncio.ensure_future(download_image(url))
        tasks.append(task)
    await asyncio.gather(*tasks)
    count_time = time.time() - start_time
    print(f'{len(urls)} images downloaded; Async time: {count_time:0.3f}')



if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(sys.argv[1:]))