#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 10:53:46 2017

@author: oem
"""

import requests
import json
import time
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import matplotlib.pyplot as plt
import math


hdr={'User-Agent': 'ubuntu:Python/politics.single.result:v1.0' +
       '(by /u/Jeevithan)'}

url = 'https://www.reddit.com/r/politics/.json'
req = requests.get(url, headers=hdr)
json_data = json.loads(req.text)

posts = json.dumps(json_data['data']['children'], indent=4, sort_keys=True)



data_all = json_data['data']['children']
num_of_posts = 0
while len(data_all) <= 1000:
    time.sleep(2)
    last = data_all[-1]['data']['name']
    url = 'https://www.reddit.com/r/politics/.json?after=' + str(last)
    req = requests.get(url, headers=hdr)
    data = json.loads(req.text)
    data_all += data['data']['children']
    if num_of_posts == len(data_all):
        break
    else:
        num_of_posts = len(data_all)
        

sia = SIA()
pos_list = []
neg_list = []
for post in data_all:
    print(post)
    res = sia.polarity_scores(post['data']['title'])
    print(res)
    
    if res['compound'] > 0.2:
        pos_list.append(post['data']['title'])
    elif res['compound'] < -0.2:
        neg_list.append(post['data']['title'])

with open("pos_news_titles.txt", "w", encoding='utf-8',
          errors='ignore') as f_pos:
    for post in pos_list:
        f_pos.write(post + "\n")

with open("neg_news_titles.txt", "w", encoding='utf-8',
          errors='ignore') as f_neg:
    for post in neg_list:
        f_neg.write(post + "\n")
        


example = "This is an example sentence! However, it " \
          "is a very informative one,"

print(nltk.word_tokenize(example, language='english'))

print(nltk.word_tokenize(example, language='english'))
tokenizer = RegexpTokenizer(r'\w+')
print(tokenizer.tokenize(example))
stop_words = set(stopwords.words('english'))


all_words_pos = []
with open("pos_news_titles.txt", "r", encoding='utf-8',
          errors='ignore') as f_pos:
    for line in f_pos.readlines():
        words = tokenizer.tokenize(line)
        for w in words:
            if w.lower() not in stop_words:
                all_words_pos.append(w.lower())
                
pos_res = nltk.FreqDist(all_words_pos)
print(pos_res.most_common(30))



all_words_neg = []
with open("neg_news_titles.txt", "r", encoding='utf-8',
          errors='ignore') as f_neg:
    for line in f_neg.readlines():
        words = tokenizer.tokenize(line)
        for w in words:
            if w.lower() not in stop_words:
                all_words_neg.append(w.lower())
                
neg_res = nltk.FreqDist(all_words_neg)
print(neg_res.most_common(30))


