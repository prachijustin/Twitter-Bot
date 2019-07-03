from credentials import *

user = api.user_timeline('justinbieber')    
#20 recent tweets by justin
for tweet in user:
    print( '------' + tweet.text)

id = user[0].id    #id of recent most tweet

while True:
    try:
        api.retweet(id)
        print('rted......')
        api.create_favorite(id)
        print('liked......')
    except:
        print('already retweeted')

    time.sleep(15)

