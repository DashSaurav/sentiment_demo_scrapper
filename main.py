import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import re
from wordcloud import WordCloud, STOPWORDS
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import snscrape.modules.twitter as sntwitter
import nltk
import streamlit as st 

# nltk.download('vader_lexicon') #required for Sentiment Analysis

#Get user input
query = st.text_area('Input the Query') #input("Query: ")
tweet_number = st.number_input('Enter the number of tweets',min_value=1, value=100)
days_number = st.number_input('Enter the number of days you want to Scrape Twitter', min_value=1, value=5)
#As long as the query is valid (not empty or equal to '#')...
if st.button("Scrape Data"):
    if query != '':
        noOfTweet = tweet_number #input("Enter the number of tweets you want to Analyze: ")
        if noOfTweet != '' :
            noOfDays = days_number #input("Enter the number of days you want to Scrape Twitter for: ")
            if noOfDays != '':
                    #Creating list to append tweet data
                    tweets_list = []
                    now = dt.date.today()
                    now = now.strftime('%Y-%m-%d')
                    yesterday = dt.date.today() - dt.timedelta(days = int(noOfDays))
                    yesterday = yesterday.strftime('%Y-%m-%d')
                    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(query + ' lang:en since:' +  yesterday + ' until:' + now + ' -filter:links -filter:replies').get_items()):
                        if i > int(noOfTweet):
                            break
                        tweets_list.append([tweet.date, tweet.id, tweet.content, tweet.username])

                    #Creating a dataframe from the tweets list above 
                    df = pd.DataFrame(tweets_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])

                    #print(df)
                    st.write(df)
