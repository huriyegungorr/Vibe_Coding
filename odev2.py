import tweepy
from textblob import TextBlob
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv

# API Bağlantısı
load_dotenv()
BEARER_TOKEN = os.getenv('BEARER_TOKEN')

if not BEARER_TOKEN:
    raise ValueError("BEARER_TOKEN bulunamadı. Lütfen API anahtarınızı .env dosyasına ekleyin!")

client = tweepy.Client(bearer_token=BEARER_TOKEN)

# Ana akış
if __name__ == "__main__": 
    hashtag = "#python"
    print(f"{hashtag} için tweetler çekiliyor...")

    try:
        query = f"{hashtag} lang:tr -is:retweet"
        tweets = client.search_recent_tweets(query=query, max_results=75)  
        
        if tweets and tweets.data:
            tweet_texts = [tweet.text for tweet in tweets.data]
            print(f"{len(tweet_texts)} tweet bulundu. Analiz başlıyor...")

            sentiments = {'positive': 0, 'neutral': 0, 'negative': 0}
            for tweet in tweet_texts:
                analysis = TextBlob(tweet)
                score = analysis.sentiment.polarity
                if score > 0:
                    sentiments['positive'] += 1
                elif score == 0:
                    sentiments['neutral'] += 1
                else:
                    sentiments['negative'] += 1

            labels, counts = sentiments.keys(), sentiments.values()
            plt.figure(figsize=(8, 6))
            plt.bar(labels, counts, color=['green', 'gray', 'red'])
            plt.title('Sentiment Analizi')
            plt.xlabel('Duygu')
            plt.ylabel('Tweet Sayısı')
            plt.show()
        else:
            print("Belirtilen hashtag için tweet bulunamadı veya API isteği başarısız oldu.")
    
    except Exception as e:
        print(f"Tweet çekme sırasında hata oluştu: {e}")
