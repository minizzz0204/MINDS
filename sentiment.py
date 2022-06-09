import pandas as pd
import numpy as np
import nltk
import re

# nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk import word_tokenize
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt


file = pd.read_csv('news.csv')
sentimentslist = []
subjectlist = []
titles = []
for index, row in file.iterrows():
    title, text = row['titles'], row['texts']
    titles.append(title)
    
    # words = word_tokenize(text)
    # filtered_words = [word for word in words if word not in stopwords.words('english')] 
    # interpunctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%', '“', '”']   #定义标点符号列表
    # filtered_words = [word for word in filtered_words if word not in interpunctuations] 
    wordcloud = WordCloud(background_color='white',scale=1.5).generate(text)

    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()
    plt.savefig("cloudpics/picture%d.jpg" %(index + 1))
    

    blob = TextBlob(text)
    print(blob.sentiment)
    sentimentslist.append(blob.sentiment.polarity)
    subjectlist.append(blob.sentiment.subjectivity)

x = np.array(sentimentslist)
y = np.array(subjectlist)
plt.scatter(x, y)
for i in range(len(x)):
    plt.annotate(titles[i], xy = (x[i], y[i]), xytext = (x[i], y[i]))
plt.xlabel('polarity')             
plt.ylabel('subjectivity')
plt.savefig("sen_picture.jpg")
plt.show()
