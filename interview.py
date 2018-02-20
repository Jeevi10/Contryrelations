#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 22:28:50 2017

@author: oem
"""

import re


def numberer(number):
    u=number;
    reverse =0
    total=0
    
    if number > 1000:
        print("more than 1000")
        
    else:
        
        while (100>number >0):
            reminder =number%10
            reverse =(reverse *10)+reminder
            number =number //10
            total =reverse+u
            
    print(numberer(total))
    
       
       
    
    
        


