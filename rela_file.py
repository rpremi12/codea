# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 21:24:42 2021

@author: herebcirelapsed
"""

import arxiv
import pandas as pd
from bs4 import BeautifulSoup
import requests as r
import re
import PyPDF2
import io
from math import ceil
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 150)
def list_to_string(target):
    string = ''
    for substring in target:
        new_string = '{} '.format(substring)
        string = string + new_string
    return(string)



def search(*query_terms):
    data = []
    search = arxiv.Search(
    query = list_to_string(query_terms),
    max_results = 1,
    sort_by = arxiv.SortCriterion.Relevance
  )

    for result in search.results():
        new_data = pd.Series({
        'id': result.entry_id.split('/')[-1],
        'url': result.pdf_url,
        'title': result.title,
        'image': None,
        'claps': None,
        'responses': None,
        'reading_time': None,
        'publication': result.published,
        'date': result.updated
        })
        link = new_data['url']
        #stripped_title = re.sub(r'\W+', '', new_data['title'])
        request = r.get(link)
        file = io.BytesIO(request.content)
        # creating a pdf reader object 
        pdfReader = PyPDF2.PdfFileReader(file)
        file_length = pdfReader.numPages
        full_text_length = 0
        for i in range(file_length):
            pageObj = pdfReader.getPage(i) 
            new_text = pageObj.extractText()
            new_text_length = len(new_text)
            full_text_length = full_text_length + new_text_length
        reading_time = ceil((full_text_length/5)/200)
        new_data.update({'reading_time': reading_time})
        #print("reading time is {} minutes".format(reading_time))
        data.append(new_data)
    return pd.DataFrame(data)

print(search('python', 'machine learning'))