# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 21:24:42 2021

@author: jmver
"""

import arxiv
import pandas as pd

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
    max_results = 10,
    sort_by = arxiv.SortCriterion.Relevance
  )

    for result in search.results():
            data.append({
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
    return pd.DataFrame(data)


search('python', 'machine learning')