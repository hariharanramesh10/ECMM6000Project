import tweepy
import time
import csv
import os

# consumer_key = "xHxN9CmFsFcH4kME9LVUh2v6l"
# consumer_secret = "bvMG55mYtHCpdok174GDflEzKirsOpnGtem3YetmbGqLyzlZAE"
# access_key = "1375777406-1lo4y9pq1sH5XLjqQSBHKYezwBBWOhXUPuH9OC3"
# access_secret = "SGWe4TFIWTKVJjdOhDfLlADEXWm8xIPU4TFRlHkKMIPGC"


consumer_key = "EoZiw1Po4vykdZgMjo2zIVgoH"
consumer_secret = "imHVLRZAl6Xu71KfpG8OFU6px5vHBIM4EqzF4ijBJr4fL8VHc9"
access_key = "915591987738312705-DBeC5LQnBepkH9XQqTwrZfxW35ZjEsR"
access_secret = "kNr9QUJrN3MryJ4klz7XxWC4zpQfk6dEXd8cj2nLPTfbw"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
def get_uniqueId(screen_name):
    try:
        user_profile = api.get_user(screen_name)
        id = user_profile.id_str
    except:
        id = "broken"
    
    return id

# id=str(get_uniqueId("PMOIndia"))

def get_tweets(screen_name):
    alltweets = []
    try:
        # for tweets in tweepy.Cursor(api.user_timeline, id=screen_name).items():
        #     alltweets.extend(tweets)
        # alltweets = tweepy.Cursor(api.user_timeline, id=screen_name).items()
        #https://developer.twitter.com/en/docs/tweets/timelines/overview describes user_timeline

        tweets = api.user_timeline(screen_name, count=200)
        # print "tweets"
        alltweets.extend(tweets)
        oldest = alltweets[-1].id - 1
        # print oldest
        # print len(tweets)
        while len(tweets) > 0:
            tweets = api.user_timeline(screen_name, count=200, max_id=oldest)
            alltweets.extend(tweets)
            oldest = alltweets[-1].id - 1
    except:
        user_profile = "broken"
    return alltweets

def save_csv(tweets, filename):
    count = 0
    with open (filename, 'wb') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["id","user","created_at","text"])
        for tweet in tweets:
            count+=1
            writer.writerow([tweet.id_str,tweet.user.screen_name,tweet.created_at,tweet.text.encode('unicode-escape')])
    return count

def search_tweets(query):
    alltweets = []
    try:
        # for tweets in tweepy.Cursor(api.user_timeline, id=screen_name).items():
        #     alltweets.extend(tweets)
        # alltweets = tweepy.Cursor(api.user_timeline, id=screen_name).items()
        #https://developer.twitter.com/en/docs/tweets/timelines/overview describes user_timeline
                # for tweets in tweepy.Cursor(api.search, q= "#demonetization", count=100,result_type="popular",include_entities=True ).items():
        # print tweets.text.encode('utf-8')

        tweets = api.search(q=query, count=200)
        # print "tweets"
        alltweets.extend(tweets)
        oldest = alltweets[-1].id - 1
        print oldest
        print len(tweets)
        while len(tweets) > 0:
            tweets = api.search(q=query, count=200, max_id=oldest)
            alltweets.extend(tweets)
            oldest = alltweets[-1].id - 1
            print "...%s tweets downloaded so far" % (len(alltweets))
    except:
        user_profile = "broken"
    return alltweets
username = raw_input("\nEnter the Twitter hashtag\n")
# t = get_tweets(username)
t2 = search_tweets(username)
outputfilename = raw_input("\nEnter the outputfilename\n")
# no_of_tweets= save_csv(t,'sebi.csv')
no_of_tweets= save_csv(t2,outputfilename)
print no_of_tweets