import requests
from textblob import TextBlob

API_KEY = ""
URL = "https://api.nytimes.com/svc/search/v2/articlesearch.json"

user_input = input("What topic are you interested in searching? ")

params = {"query":user_input, "api-key":API_KEY}

response = requests.get(URL, params)
number_of_articles = response.json()["response"]["meta"]["hits"]
print(f"The total number of articles on the NY Times about this topic is {number_of_articles:,}")

sentiment_dict = {"negative":0, "positive":0, 
                  "subjective":0, "objective":0}

for each_article in response.json()["response"]["docs"]:
    article_blob = TextBlob(each_article["abstract"])
    if article_blob.sentiment.polarity > 0 :
        sentiment_dict["positive"] += 1
    else:
        sentiment_dict["negative"] += 1
    if article_blob.sentiment.subjectivity > 0.5:
        sentiment_dict["subjective"] += 1
    else:
        sentiment_dict["objective"] += 1

if sentiment_dict["positive"] > sentiment_dict["negative"]:
    print(f"The NY Times discusses {user_input} in a positive light")
else:
    print(f"The NY Times discusses {user_input} in a negative light")

if sentiment_dict["subjective"] > sentiment_dict["objective"]:
    print(f"The NY Times discusses {user_input} in a subjective manner")
else:
    print(f"The NY Times discusses {user_input} in a objective manner")


