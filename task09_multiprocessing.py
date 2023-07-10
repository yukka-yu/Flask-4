import sys
import requests
from multiprocessing import Process, Pool
import time

'''urls = ['https://sibirds.ru/taxons/1486/fronpic1.jpg', 'https://images.vfl.ru/ii/1674314341/afc224c7/38705380_m.jpg',
         'https://birds.kg/taxons/163/fronpic2.jpg', 'https://ic.pics.livejournal.com/pantv/14908973/7538068/7538068_900.jpg', 
         'https://ic.pics.livejournal.com/pantv/14908973/7042833/7042833_800.jpg', 'https://images.vfl.ru/ii/1674314341/62849390/38705379_m.jpg'
        ]'''

def download_img(img_url): 
    img_name = img_url[img_url.rfind('/') + 1 : ] 
    p = requests.get(img_url)
    out = open('multiprocessing/' + img_name, "wb")
    out.write(p.content)
    out.close()

processes = []
start_time = time.time()

def main(urls):
    for url in urls:
        process = Process(target=download_img, args=(url,))
        processes.append(process)
        process.start()
    count_time = time.time() - start_time
    print(f'{len(urls)} images downloaded; MP time: {count_time:0.3f}')

for process in processes:
    process.join()

if __name__ == '__main__':
    main(sys.argv[1:])



