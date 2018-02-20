#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 15:59:45 2017

@author: oem
"""

import urllib3
import re
#import cookielib
#from cookielib import CookieJar

from cookiejar import jar

# If the web site expects cookies
cookie = jar.Jar()
opener = urllib3.build_opener(urllib3.HTTPCookieProcessor(cookie))

# Get Scrapper pose as Browser
opener.addHeaders = [('User-agent', 'Mozilla/5.0')]
page = 'http://feeds.reuters.com/reuters/worldNews'

def main():
    try:
        # Open the page and retrieve contents
        pageData = opener.open(page).read()

        #Filter for news headlines
        titles = re.findall(r'<title>(.*?)</title>', pageData)
        
        for title in titles:
            print (title)
    
    except Exception as e:
            print (str(e))

main()