import sys
import argparse
import requests
import threading
import time


'''urls = ['https://sibirds.ru/taxons/1486/fronpic1.jpg', 'https://images.vfl.ru/ii/1674314341/afc224c7/38705380_m.jpg',
         'https://birds.kg/taxons/163/fronpic2.jpg', 'https://ic.pics.livejournal.com/pantv/14908973/7538068/7538068_900.jpg', 
         'https://ic.pics.livejournal.com/pantv/14908973/7042833/7042833_800.jpg', 'https://images.vfl.ru/ii/1674314341/62849390/38705379_m.jpg'
        ]'''

def download_img(img_url):
    img_name = img_url[img_url.rfind('/') + 1 : ]
    p = requests.get(img_url)
    out = open('threading/' + img_name, "wb")
    out.write(p.content)
    out.close()

threads = []
start_time = time.time()

def main(urls):
    for url in urls:
        thread = threading.Thread(target=download_img, args=[url])
        threads.append(thread)
        thread.start()
    count_time = time.time() - start_time
    print(f'{len(urls)} images downloaded; Threading time: {count_time:0.3f}')

    for thread in threads:
        thread.join()

if __name__ == '__main__':
    main(sys.argv[1:])    

