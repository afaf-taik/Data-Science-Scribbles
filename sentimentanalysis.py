import json
import math
import re
from twitterscraper import query_tweets
from afinn import Afinn


#Uncomment for storing data
#Note that you have to remove the quotes from the file manually, still looking for an alternative
#1st argument is query words, second is limit number of tweets
#data=query_tweets("Trump OR Clinton", 1000)
#with open('data.json', encoding='utf-8',mode='w') as outfile:
#    json.dump(str(data), outfile)

with open("data.json",encoding='utf-8') as json_file:
    json_data = json.load(json_file)

json_file.close()
afinn = Afinn(emoticons=True)
for item in json_data:
    tweet=item["text"]
    sentiment_value=afinn.score(tweet)
    item["sentiment"]=sentiment_value

with open('sentiments.json', encoding='utf-8',mode='w') as f:
  json.dump(json_data, f, ensure_ascii=True)
f.close()

print('All done.')
