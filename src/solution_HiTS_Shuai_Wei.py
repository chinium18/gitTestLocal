#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This is a solution script for HiTS python programming assessment. 
Coded in python2.7 environment and tested with python3.6.

Created on Thu Mar 29 11:06:38 2018

@author: Shuai Wei
"""
import requests
from bs4 import BeautifulSoup as bs
import urllib3
import json

# A sub-function that make a request to the url and fetching the page. 
# Named make_soup: by using the BeautifulSoup lib.
def make_soup(url):
    http = urllib3.PoolManager()
    r = http.request('GET',url)
    soup = bs(r.data, "lxml")
    return soup

def solution():
    
    # Step 1: Taking a PubMed article ID (PMID) as a command line argument.
    PMID = input("PMID: ")
    
    # Step 2: Given a PMID above, calling the PubMed web service (make_soup) to 
    # retrieve the entry for the given PMID as XML.
    url = 'https://www.ncbi.nlm.nih.gov/pubmed/'+str(PMID)
    soup = make_soup(url)
    
    # Step 3: With the PubMed XML entry, extracting the abstract of the article
    # as a text string.
    abstract = soup.find("div",{"class":"abstr"}).text

    # Step 4: Having successfully extracted the abstract text, sending it to 
    # the REACH natural language processing web service. 
    # Specified the “fries” output format with the request.
    reach_url = 'http://agathon.sista.arizona.edu:8080/odinweb/api/text'
    reach_out = requests.post(reach_url,data={'text':abstract,'output':'fries'}).json()

    # Step 5: Saving the JSON result from the REACH web service into a file 
    # called <PMID>.json.
    file_name = str(PMID)+'.json'
    with open(file_name,'w') as fo:
        json.dump(reach_out,fo)

# Code testing by calling the function
solution()

#import math
# Loading the data from file
data = json.load(open('../data/28546431.json'))
# Simple counting of events
len(data['events'])
