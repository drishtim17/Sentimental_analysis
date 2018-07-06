#!/usr/bin/python3
#for stopwords
from nltk.corpus import stopwords
import nltk
#removing html tags
from bs4 import BeautifulSoup
#reading data from url
import urllib.request

#for hello website
web=urllib.request.urlopen('https://www.hellodesign.com/')

#print (web)
webdata=web.read()

#applying beautiful soup
#information in systematic manner
souped=BeautifulSoup(webdata,'html5lib')
#print(souped)

#printing text only no html tags
text_data=souped.get_text()
#print(text_data)

#tokenized process on behalf of words
#tokenized=[i for i in text_data.split()]
#print(tokenized)

#with stopwords
tokenized=[i for i in text_data.split() if i not in stopwords.words('english')]
print(tokenized)

#applying frequency counter
word_count=nltk.FreqDist(tokenized)
print(word_count)





