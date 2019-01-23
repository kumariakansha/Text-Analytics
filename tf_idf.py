import math
from collections import Counter

vector_dict = {}                                       #Dict that will hold tf-idf matrix

#Just loads in all the documents
def load_docs():
 print("Loading docs...")
 doc1=('d1', 'Life’s true gift is to discover that it  lies in your freedom to design it beautiful')
 doc2=('d2', ' waste one hour of time has not discovered how beautiful life is')
 doc3=('d3','if life were predictable it would cease to be time and in  design in a beautiful way')
 var1 =('v1','if life was not predictable and it would not have time to design in beautiful way')
 var2 =('v2','if life was unpredictable and it ceased time and designed in beautiful way')
 var3 =('v3','if prediction of life  and time was easy then it could be designed beautifully')
 var4 = ('v4','life would have been designed in a beautiful way if prediction of time was easy')
 var5 =('v5','design the time in a way to make life beautiful')
 return [doc1, doc2,doc3,var1,var2,var3,var4,var5]

#Computes TF for words in each doc, DF for all features in all docs; finally whole Tf-IDF matrix
def process_docs(all_dcs):
 stop_words = [ 'of', 'and', 'on','in','to','it','be','the','with','you','your','has','if' ]
 all_words = []                                         #list to collect all unique words in each docs
 counts_dict = {}                                       #dict to collect doc data, word-counts and word-lists
 for doc in all_dcs:
    words = [x.lower() for x in doc[1].split() if x not in stop_words]
    words_counted = Counter(words)                      #counts words in a doc
    unique_words = list(words_counted.keys())           #list of the unique words in the doc
    counts_dict[doc[0]] = words_counted                 #make dict entry {'d1' : {'a': 1, 'b':6}}
    all_words = all_words + unique_words                #collect all unique words from each doc; bit hacky
 n = len(counts_dict)                                   #number of documents is no of entries in dict
 df_counts = Counter(all_words)                         #DF of all unique words from each doc, counted
 compute_vector_len(counts_dict, n, df_counts)          #computes TF-IDF for all words in all docs


#computes TF-IDF for all words in all docs
def compute_vector_len(doc_dict, no, df_counts):
  global vector_dict
  for doc_name in doc_dict:                              #for each doc
    doc_words = doc_dict[doc_name].keys()                #get all the unique words in the doc
    wd_tfidf_scores = {}
    for wd in list(set(doc_words)):                      #for each word in the doc
        wds_cts = doc_dict[doc_name]                     #get the word-counts-dict for the doc
        wd_tf_idf = wds_cts[wd] * math.log(no / df_counts[wd], 10)   #compute TF-IDF
        wd_tfidf_scores[wd] = round(wd_tf_idf, 4)        #store Tf-IDf scores with word
    vector_dict[doc_name] = wd_tfidf_scores              #store all Tf-IDf scores for words with doc_name


def get_cosine(text1, text2):
     vec1 = vector_dict[text1]
     vec2 = vector_dict[text2]
     intersection = set(vec1.keys()) & set(vec2.keys())
     #NB strictly, this is not really correct, needs vector of all features with zeros
     numerator = sum([vec1[x] * vec2[x] for x in intersection])
     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)
     if not denominator:
        return 0.0
     else:
        return round(float(numerator) / denominator, 3)



#RUN THE DEFINED FNS

all_docs = load_docs()
process_docs(all_docs)
vector_dict['q'] = {'life' : 1, 'beautiful' : 1, 'time' : 1}

for keys,values in vector_dict.items(): print(keys, values)

text1 = 'd1'
text2 = 'd2'
cosined1 = get_cosine(text1, text2)
print(' The Cosine similaity id d1 and d2:', cosined1)
text1 = 'd2'
text2d2 = 'd3'
cosined2 = get_cosine(text1, text2)
print(' The Cosine similarity of d2 and d3:', cosined2)
text1 = 'd3'
text2 = 'd1'
cosined3 = get_cosine(text1, text2)
print('The Cosine similarity of d1 and d3:', cosined3)
text1 = 'd3'
text2 = 'v1'
cosinev1 = get_cosine(text1, text2)
print('The Cosine  similarity of d3 with variant1:', cosinev1)
text1 = 'd3'
text2 = 'v2'
cosinev2 = get_cosine(text1, text2)
print(' The Cosine  similarity of d3 with variant2:', cosinev2)
text1 = 'd3'
text2 = 'v3'
cosinev3 = get_cosine(text1, text2)
print('The Cosine  similarity of d3 with variant3:', cosinev3)
text1 = 'd3'
text2 = 'v4'
cosinev4 = get_cosine(text1, text2)
print('The Cosine  similarity of d3 with variant4:', cosinev4)

text1 = 'd3'
text2 = 'v5'
cosinev5 = get_cosine(text1, text2)
print('The Cosine  similarity of d3 with variant5:', cosinev5)

#to create the bar graph of the cosine values of documents
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
 
objects = ('cosine d1/d2', 'cosine d2/d3', 'cosine d3/d1')
y_pos = np.arange(len(objects))
performance = [cosined1,cosined2,cosined3]
 
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('cosine values')
plt.title('documents')
 
plt.show()

#to create the bar graph of the cosine values of the variants

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
 
objects = ('cosine v1', 'cosine v2', 'cosine v3','cosine v4','cosine v5')
y_pos = np.arange(len(objects))
performance = [cosinev1,cosinev2,cosinev3,cosinev4,cosinev5]
 
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('cosine values')
plt.title('documents')
 
plt.show()
