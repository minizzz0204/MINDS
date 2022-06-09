
from tkinter.font import names
from bs4 import BeautifulSoup
import requests, sys
from tqdm import tqdm
import time
import json
import csv


class downloader(object):

    def __init__(self):
        self.server = 'https://www.aljazeera.com'
        self.target = 'https://www.aljazeera.com/where/mozambique'
        self.names = []         #news title
        self.urls = []          #news url
        self.nums = 0           #news quantity
        # self.dics = []

        
    def get_download_url(self):
        headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'}
        req = requests.get(url = self.target, headers = headers)
        html = req.text
        bf = BeautifulSoup(html)
        sec_content = bf.find_all('article', class_ = 'gc u-clickable-card gc--type-post gc--list gc--with-image')
        self.nums = len(sec_content)   
        for each_content in sec_content:
            a_bf = BeautifulSoup(str(each_content))
            a = a_bf.find_all('a', class_ = 'u-clickable-card__link')
            for each in a:
                self.names.append(each.string)
                self.urls.append(self.server + each.get('href'))

    

        
    def get_contents(self, target):
        headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'}
        req = requests.get(url = target, headers = headers)
        html = req.text
        bf = BeautifulSoup(html)
        texts = bf.find_all('div', class_ = 'wysiwyg wysiwyg--all-content css-1ck9wyi')
        
        texts = texts[0].text.replace('\xa0'*8,'')
        texts = texts.replace('\n','')
        texts = texts.replace('-','')
        # texts = texts.encode('raw_unicode_escape').decode('unicode').replace('\\u', '')
        return texts

    
    # def writer(self, name, path, text):
    #     write_flag = True
    #     with open(path, 'a', encoding='utf-8') as f:
    #         f.write('************************************************\n')
    #         f.write(name + '\n')
    #         f.writelines(text + '\n')

if __name__ == "__main__":
    f = open('news.csv','wt',newline='')
    writer = csv.writer(f)
    writer.writerow(('titles', 'texts'))
    dl = downloader()
    dl.get_download_url()
    # dics = []
    for i in tqdm(iterable=range(dl.nums)):
        # dic = {"title": dl.names[i], "context": dl.get_contents(dl.urls[i])}
        # dics.append(dic)
        # dl.writer(dl.names[i], 'news.txt', dl.get_contents(dl.urls[i]))
        sys.stdout.flush()
        time.sleep(0.1) 
        writer.writerow((dl.names[i],dl.get_contents(dl.urls[i])))
    f.close()
    print('news download complete')
    # json_string = json.dumps(dics)

    # with open('json_data.json', 'w') as outfile:
    #     json.dump(eval("'{}'".format(json_string)), outfile)
    
