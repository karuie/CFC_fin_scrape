import scrapy
import pandas as pd
import re
import json
from bs4 import BeautifulSoup
import nltk
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from nltk import FreqDist
from nltk.stem import SnowballStemmer
from nltk import word_tokenize

def find_list_resources(tag, attribute, soup):
    list = []
    for x in soup.findAll(tag):
        try:
            list.append(x[attribute])
        except KeyError:
            pass
    return (list)


class CfcTestSpider(scrapy.Spider):
    name = 'cfc_test'
    allowed_domains = ['cfcunderwriting.com']
    start_urls = ['https://cfcunderwriting.com/']

    def parse(self, response):
        # 1. scrape the index home page with the response result and decode it
        html = response.body.decode('utf-8')

        # 2. list all externally loaded resources with BeautifulSoup
        soup = BeautifulSoup(html)
        # fetch the resources by tag and attribute with the find_list_resources defined above
        image_scr = find_list_resources('img', "src", soup)
        scipt_src = find_list_resources('script', "src", soup)
        css_link = find_list_resources("link", "href", soup)
        video_src = find_list_resources("video", "src", soup)
        audio_src = find_list_resources("audio", "src", soup)
        iframe_src = find_list_resources("iframe", "src", soup)
        embed_src = find_list_resources("embed", "src", soup)
        object_data = find_list_resources("object", "data", soup)
        soruce_src = find_list_resources("source", "src", soup)
        resources_d = dict()
        resources_d['img'] = image_scr
        resources_d['script'] = scipt_src
        resources_d['link'] = css_link
        resources_d['video'] = video_src
        resources_d['audio'] = audio_src
        resources_d['iframe'] = iframe_src
        resources_d['embed'] = embed_src
        resources_d['object'] = object_data
        resources_d['source'] = soruce_src
        with open('resources.json', 'w') as f:
            json.dump(resources_d, f)


        # 3. Enumerates the page's hyperlinks and identifies the location of the "Privacy Policy" page with selenium
        
        
        # add webdriver options like headless mode 
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("enable-automation")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        Chrome_url = str('https://cfcunderwriting.com/')
        driver.get(Chrome_url)

        # we can try with regular method of tagname or identify elements with tagname a
        for link in soup.findAll('a'):
            print(link.get('href'))

        lnks = driver.find_elements_by_tag_name("a")
        # traverse list
        lnk_content = []
        for lnk in lnks:
            # get_attribute() to get all href
            lnk_content.append(lnk.get_attribute("href"))
        n = len(lnk_content)
        # n = 132

        # we can find the Privacy Policy lication with the 'find_elements_by_xpath'
        Privacy_Policy_link = driver.find_elements_by_xpath("//*[contains(text(), 'Privacy Policy')]")
        pp_links = [elem.get_attribute('href') for elem in Privacy_Policy_link]
        
        # pick up the first one as it is the single link that we need
        pp_link = pp_links[0]
        pp_link_str = ''.join(map(str, pp_link))
        # Privacy_Policy_link = 'https://www.cfcunderwriting.com/en-gb/support/privacy-policy/'

        # 4. we follow the identified privacy policy URL with callback using response.follow()
        yield response.follow(url=pp_link_str, callback=self.parse_pp)


        # Word Count with nltk
    def parse_pp(self, response):
        # To count the words, we could simply count the word and we also could use FreqDist in NLP area, here we use the later

        # scrape the pages content like what we do in the step 1
        html =  response.body.decode('utf-8')
        soup = BeautifulSoup(html)
        raw_words = soup.text
        # remove the special characters like comma
        raw_words = raw_words.replace(',', '').replace('.', '').replace('|', ' ').replace('↑', ' ')
        tokens = word_tokenize(raw_words)
        text_tokens = nltk.Text(tokens)
        # .lower() to account for count's case sensitive behaviour
        lower_words = []
        lower_words_be = [word.lower() for word in text_tokens]
        lower_words.append(lower_words_be)
        # stem the word to get more robust result
        stemmer = SnowballStemmer(language='english')
        word_count_stemmed = []
        for i in range(len(lower_words)):
            stemmed_words = [stemmer.stem(word) for word in lower_words[i]]
            count_stemmed_be = FreqDist(stemmed_words)
            word_count_stemmed.append(count_stemmed_be)
        with open('word_count_stemmed.json', 'w') as f:
            json.dump(word_count_stemmed, f, indent=4)

