# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 21:24:42 2021

@author: jmver
"""

import arxiv

def search(query_terms):
  search = arxiv.Search(
    query = query_terms,
    max_results = 10,
    sort_by = arxiv.SortCriterion.Relevance
  )

  for result in search.results():
    print(result.title)

search('python machine learning')