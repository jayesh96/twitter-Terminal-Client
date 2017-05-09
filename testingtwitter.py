consumer_key = 'XXX'
consumer_secret = 'XXX'
access_token = 'XXX'
access_token_secret = 'XXX'

import tweepy, os

def getStatus():
    lines = []
    while True:
        line = raw_input()
        if line:
            lines.append(line)
        else:
            break
    status = '\n'.join(lines)
    return status

##auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
##auth.set_access_token(access_token, access_token_secret)
##
##api = tweepy.API(auth)
##
##public_tweets = api.home_timeline()
##for tweet in public_tweets:
##    print("--------------------------------")
##    print tweet.text
##    print("--------------------------------")
##user = api.get_user('simrankr012')
##print user.screen_name
##print user.followers_count
##for friend in user.friends():
##   print friend.screen_name
try:
    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    api = tweepy.API(auth)
    user = api.me()
except:
    print("No Internet Connection")


print(user.name)
tweet = getStatus()
try:
    api.update_status(tweet)
except Exception as e:
    print e
    

print("Done")



print(user.name)
