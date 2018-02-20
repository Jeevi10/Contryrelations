#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 17:03:53 2017

@author: oem
"""

import feedparser
import pycountry
import re
import requests
import json
import time
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import matplotlib.pyplot as plt
import numpy as np

 
# Function to fetch the rss feed and return the parsed RSS
def parseRSS( rss_url ):
    return feedparser.parse( rss_url ) 
    
# Function grabs the rss feed headlines (titles) and returns them as a list
def getHeadlines( rss_url ):
    headlines = []
    
    feed = parseRSS( rss_url )
    for newsitem in feed['items']:
        #print(newsitem)
        headlines.append(newsitem['summary'])
    
    return headlines
 
# A list to hold all headlines
allheadlines = []

# List of RSS feeds that we will fetch and combine
newsurls = {
    
    'returespol':          'http://feeds.reuters.com/Reuters/PoliticsNews',
    'returesworld':         'http://feeds.reuters.com/Reuters/worldNews'
}
 
# Iterate over the feed urls
for key,url in newsurls.items():
    # Call getHeadlines() and combine the returned headlines with allheadlines
    allheadlines.extend( getHeadlines( url ) )
 
 

# Iterate over the allheadlines list and print each headline
data_all=[]
for hl in allheadlines:
    
    hl=hl.lower()
    result = re.sub('<[^>]+>', '',hl)
    #print(hl)
    data_all.append(result)
    
    
    
sia = SIA()
pos_list = []
neg_list = []
for post in data_all:
    print(post)
    res = sia.polarity_scores(post)
    print(res)
    
    if res['compound'] > 0.2:
        pos_list.append(post)
    elif res['compound'] < -0.2:
        neg_list.append(post)

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

   