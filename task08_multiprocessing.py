import requests
from multiprocessing import Process, Pool
import time

SIZE = 200
urls = [f'http://www.radioscanner.ru/base/index.php?action=list&sortBy=0&page={i}' for i in range(SIZE)]

def download(url):
    response = requests.get(url)
    filename = url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
    with open('multiprocessing/radioscanner/' + filename, "w", encoding='utf-8') as f:
        f.write(response.text)

processes = []
start_time = time.time()

def main():
    for url in urls:
        process = Process(target=download, args=(url,))
        processes.append(process)
        process.start()
    count_time = time.time() - start_time
    print(f'{SIZE} pages downloaded; MP time: {count_time:0.3f}')

for process in processes:
    process.join()

if __name__ == '__main__':
    main()