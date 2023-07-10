import requests
import threading
import time


SIZE = 200
urls = [f'http://www.radioscanner.ru/base/index.php?action=list&sortBy=0&page={i}' for i in range(SIZE)]

def download(url):
    response = requests.get(url) 
    filename = url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
    with open('threading/radioscanner/' + filename, "w", encoding='utf-8') as f:
        f.write(response.text)
        
threads = []
start_time = time.time()

def main():
    for url in urls:
        thread = threading.Thread(target=download, args=[url])
        threads.append(thread)
        thread.start()
    count_time = time.time() - start_time
    print(f'{SIZE} pages downloaded; Threading time: {count_time:0.3f}')

    for thread in threads:
        thread.join()

if __name__ == '__main__':
    main()    
