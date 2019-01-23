# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 17:41:17 2017

@author: akank
"""

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity 


data = [
 'Life’s true gift is to discover that it  lies in your freedom to design it beautiful',
  ' waste one hour of time has not discovered how beautiful life is',
'if life were predictable it would cease to be time and in  design in a beautiful way'
]
 
v = CountVectorizer()

print(v)
v1 = v.fit_transform(data).todense() 
#split into words and create a list of vocabulary
print( v.vocabulary_ )
 
print("Euclidian Distances:")

print( euclidean_distances(v1) )

vec = TfidfVectorizer()
trans_data = vec.fit_transform(data)
cos_dist=cosine_similarity(trans_data)   
print('Cosine Similarity')
print(cos_dist)      

