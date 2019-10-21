#!/usr/bin/env python
# coding: utf-8

# In[9]:


from bs4 import BeautifulSoup  #Importing the Beautiful Soup Library
import requests                #Importing the requests library
import time                    #Importing the time library
import re                      #Importing the regular expression module

response = requests.get('http://www.imdb.com/chart/top')
soup = BeautifulSoup(response.text, 'lxml')
movies = soup.select('td.titleColumn')
links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
ratings = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]

imdb = []
for index in range(0, len(movies)):
    # Seperate movie into: 'place', 'title', 'year'
    movie_string = movies[index].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(index))+1:-7]
    year = re.search('\((.*?)\)', movie_string).group(1)
    data = {"movie_title": movie_title, "year": year, "star_cast": crew[index], "rating": ratings[index], "link": links[index]}
    imdb.append(data)
    
for item in imdb:
    print(item['movie_title'], '('+item['year']+') -', 'Starring:', item['star_cast'], '-', 'Rating:', item['rating'], ',' 'Links:', item['link'])


# In[ ]:




