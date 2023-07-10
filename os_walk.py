import os
import requests

'''a = os.walk('/home/sasha/Documents/Developing/Flask/project4/async')
for i in a:
    print(i)
    print('\n')'''


img_url = 'https://sibirds.ru/taxons/1486/fronpic1.jpg'
img_name = img_url[img_url.rfind('/') + 1 : ]
p = requests.get(img_url)
out = open(img_name, "wb")
out.write(p.content)
out.close()