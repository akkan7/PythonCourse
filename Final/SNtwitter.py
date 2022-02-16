import snscrape.modules.twitter as sntwitter
import pandas as pd
from datetime import timedelta

# Creating list to append tweet data to
#tweets_list = []
fr=[]

td= timedelta(hours=1)

#I am trying a new way to calculate the total number of tweets in any hour
#i counts itself, I check if the pre-defined hour changes
#in the last tweet scraped, if it is I count it and update the hours
a2=23
b=0


# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('#NEAR OR $NEAR since:2021-11-10 until:2021-12-10').get_items()):

    if i>1000000:
        break
    a= tweet.date.hour
    if a != a2:
        a3=tweet.date.replace(microsecond=0, second=0, minute=0)+td
        fr.append([a3.strftime("%Y-%m-%d %H:%M:%S"), i-b])
        b=i
        a2=a

#last hour
a3=tweet.date.replace(hour=a2, microsecond=0, second=0, minute=0)
fr.append([a3.strftime("%Y-%m-%d %H:%M:%S"), i-b])

fbyday= pd.DataFrame(fr, columns = ['Date', 'Total'])
fbyday.to_csv('fnear.csv')

