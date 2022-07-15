import tweepy
from Program import process
import time
import schedule




# LOGIN --------------------------------------------------------------

# Set Keys
all_keys = open('./Program/Resources/TKeys', 'r').read().splitlines()
api_key = all_keys[0]
api_key_secret = all_keys[1]
access_token = all_keys[2]
access_token_secret = all_keys[3]

# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
print("Authentication Successfully")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True)



# CONSTANTS --------------------------------------------------------------

meme_file = "./Program/Resources/meme-50.jpg"
bot_id = int(api.verify_credentials().id_str)



# ACTIONS --------------------------------------------------------------


# Regular Post
def upload_media(text, file):
    media = api.media_upload(file)
    api.update_status(text, media_ids = [media.media_id_string])

def regular_post():
   process.updateImage()
   upload_media('#Dolar #DolarBlue','./Program/Resources/meme-50.jpg')


# Response Post
FILE_NAME = './Program/Resources/last.txt'

def read(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

def reply():
    # Download last 20 mentions
    tweets = api.mentions_timeline(count=read(FILE_NAME), tweet_mode='extended')

    #Check if mention's id was replied before
    for tweet in reversed(tweets):
        if tweet.id > read(FILE_NAME):
            if '#dolar' in tweet.full_text.lower() and tweet.author.id != bot_id:
                print("Price Requested from:  @" + tweet.author.screen_name + " --- " + str(tweet.created_at))
                reply_status = "@%s %s" % (tweet.author.screen_name, '#Dolar #DolarBlue')
                api.update_status_with_media(status = reply_status,filename = meme_file ,in_reply_to_status_id = tweet.id_str)

                #Like mention        
                status = api.get_status(tweet.id)
                favorited = status.favorited
                if favorited != True:
                    api.create_favorite(tweet.id)

            # Store mention id
            store(FILE_NAME, tweet.id)
            print("test")


# Bot
def start_bot():
    print("---Initialized-------------")
    schedule.every().day.at("17:00").do(regular_post)
    while True:
        schedule.run_pending()
        time.sleep(1)
        reply()
        time.sleep(15)