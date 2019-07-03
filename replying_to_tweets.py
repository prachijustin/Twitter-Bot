from credentials import *

FILE_NAME = 'last_seen_id.txt'

def get_last_seen_id(FILE_NAME):
    mentions = api.mentions_timeline()
    f_write = open(FILE_NAME, 'w')

    #using id of last 20th tweet for testing
    f_write.write(str(mentions[-1].id))
    f_write.close()


def retreive_last_seen_id(FILE_NAME):
    f_read = open(FILE_NAME, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, FILE_NAME):
    f_write = open(FILE_NAME, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return


def reply_to_tweets():
    print('retrieving and replying to tweets....')
 
    get_last_seen_id(FILE_NAME)
    last_seen_id = retreive_last_seen_id(FILE_NAME)

    mentions = api.mentions_timeline(last_seen_id, tweet_mode='extended')

    for mention in reversed(mentions):
        print(str(mention.id) + '---' + mention.full_text)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '#hello' in mention.full_text:
            print('found #helloo')
            print('responding back...')
            try:
                api.update_status('@' + mention.user.screen_name + ' #hey nice to see u ', mention.id)
            except:
                print('Duplicate status.........')
         
while True:
    reply_to_tweets()
    time.sleep(15)

