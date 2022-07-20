# IMPORTS
from xmlrpc import client
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import os.path
import time 
import requests
import config
import tweepy
import config
import schedule


# LOGIN #####################################################################                                 
api_key      = config.API_KEY                                             
api_secret   = config.API_KEY_SECRET                                         
token        = config.ACCESS_TOKEN                                            
token_secret = config.ACCESS_TOKEN_SECRET    
bearer       = config.BEARER_TOKEN  
bot_name     = 'Dolar50cent'  #Example. My Twitter: @KerbsOctavio. bot_name = 'KerbsOctavio'                          


# Tweepy v2.0 
client = tweepy.Client(bearer, api_key, api_secret, token, token_secret)  

# Tweepy v1.1
auth = tweepy.OAuth1UserHandler(api_key, api_secret, token, token_secret) 
api  = tweepy.API(auth)

#############################################################################


# OPEN DIRECTORIES (The only solution for heroku to find my folders)
dir = os.path.dirname(os.path.abspath(__file__))


# VARIABLES
ID_FILE      = os.path.join(dir, 'Resources', 'last.txt')
IMAGEN_PATH  = os.path.join(dir, 'Resources', 'image.jpg')
MEME_PATH    = os.path.join(dir, 'Resources', 'meme.jpg')
FONT_PATH    = os.path.join(dir, 'Resources', 'impact.ttf')


# PRICE
def price(): 
    
    # Get price
    data  = requests.get("https://api.bluelytics.com.ar/v2/latest").json()
    price = data['blue']['value_sell']
    
    # Set 50cent prop
    dollar = price / 2
    
    # Return value
    return dollar
    

# IMAGE
def imagen():
    
    # Open base image
    imagen = Image.open(IMAGEN_PATH)
    
    # Config Text
    pos    = (180,840)
    text   = str(price()) + ' pesos'
    font   = ImageFont.truetype(FONT_PATH, 80)
    fill   = (255, 255, 255)
    stroke = (0, 0, 0)
    
    # Add text
    add_text = ImageDraw.Draw(imagen)
    add_text.text(xy=pos, text=text, font=font, fill=fill, stroke_fill=stroke, stroke_width=3)
    
    # Save
    imagen.save(MEME_PATH)


# POST
def post():
    
    # Updates the image (because we are useing real-time dollar price)
    imagen()
    
    # Uploads the image
    media = api.media_upload(MEME_PATH)
    tweet = client.create_tweet(media_ids=[media.media_id])
    
    return tweet


# REPLY POST
def reply(mention_id):
    
    # Updates the image (because we are using real-time dollar price)
    imagen()
    
    # Reply post
    media = api.media_upload(filename=MEME_PATH)
    reply = client.create_tweet(in_reply_to_tweet_id = mention_id, media_ids=[media.media_id])
    
    return reply


# READ STORED ID 
def read(file):
    
    read = open(file, 'r')
    
    # Save data
    last_seen_id = int(read.read().strip())
    read.close()
    
    # Return data
    return last_seen_id


# STORE NEW ID
def store(file, new_id):
    
    write = open(file, 'w')
    
    # Write new data
    write.write(str(new_id))
    write.close()
    

# GET USER ID KNOWING USERNAME
def user_id(username): 
    
    user = api.get_user(screen_name = str(username))
    return user


# GET USERNAME KNOWING USER ID
def get_username(id):
    
    name = api.get_user(user_id=id)
    return name.screen_name
   
   
# GET BOT ID  
def my_id(): 
    
    bot_data = user_id(bot_name)
    return bot_data.id
    
    
# GET MENTIONS
def get_mentions():
    
    # Request mentions 
    mentions = client.get_users_mentions(id = my_id(), since_id = read(ID_FILE), tweet_fields = ['created_at'], 
    expansions = ['author_id'])
    
    # Return list
    return mentions


# CLEARER VERSION OF TIME
def CTime(created_at):
    value = datetime.fromisoformat(str(created_at))
    value = value.strftime("%d/%m/%Y %H:%M:%S")
    return value
    
    
# REPLY TO "#DOLAR" MENTION
def answer():
    
    # Get mentions
    mentions = get_mentions()
    
    # Loop through every mention from older to newer
    if mentions.data != None: 
        
        for mention in reversed(mentions.data):
 
            if "dolar" in mention.text.lower():
            
                # Reply Mention
                print("Price requested from @" + get_username(str(mention.author_id)) + ' ------ '+ str(CTime(mention.created_at)))
                reply(mention.id)
                
            # Like Mention
            client.like(mention.id)
        
            # Store mention id
            store(ID_FILE, mention.id) 
            

# POST AT MARKET CLOSE
def Daily():
    schedule.every().monday.    at("17:00").do(post)
    schedule.every().tuesday.   at("17:00").do(post)
    schedule.every().wednesday. at("17:00").do(post)
    schedule.every().thursday.  at("17:00").do(post)
    schedule.every().friday.    at("17:00").do(post)
    
    
# Yeah, uh-huh
# So seductive

# I'll take you to the dollar shop
# I'll let you lick the lollipop
# Go 'head, girl, don't you stop
# Keep goin' until you hit the spot, woah
# I'll take you to the dollar shop (Yeah)
# Want one taste of what I got? (Uh-huh)
# I'll have you spendin' all you got (Come on)
# Keep goin' until you hit the spot, woah

# You could have it your way, how do you want it?
# You gon' back that thing up or should I push up on it?
# Temperature risin', okay, let's go to the next level
# Dance floor jam-packed, hot as a tea kettle
# I'll break it down for you now, baby, it's simple
# If you be a nympho, I be a nympho
# In the hotel or in the back of the rental
# On the beach or in the park, it's whatever you into
# Got the magic stick, I'm the love doctor
# Have your friends teasin' you 'bout how sprung I got you
# Wanna show me you could work it, baby? No problem
# Get on top, then get to bounce around like a low rider
# I'm a seasoned vet when it come to this shit
# After you work up a sweat, you could play with the stick
# I'm tryin' to explain, baby, the best way I can
# I'll melt in your mouth, girl, not in your hand, ha-ha


# I'll take you to the dollar shop
# I'll let you lick the lollipop
# Go 'head, girl, don't you stop
# Keep goin' until you hit the spot, woah
# I'll take you to the dollar shop
# Want one taste of what I got?
# I'll have you spendin' all you got
# Keep goin' until you hit the spot, woah

# Girl, what we do (What we do)
# And where we do (And where we do)
# The things we do (Things we do)
# Are just between me and you, yeah (Oh yeah)

# Give it to me, baby, nice and slow
# Climb on top, ride like you in a rodeo
# You ain't never heard a sound like this before
# 'Cause I ain't never put it down like this
# Soon as I come through the door, she get to pullin' on my zipper
# It's like it's a race, who could get undressed quicker
# Isn't it ironic, how erotic it is to watch her in thongs?
# Had me thinkin' 'bout that ass after I'm gone
# I touched the right spot at the right time
# Lights on or lights off, she like it from behind
# So seductive, you should see the way she whine
# Her hips in slow-mo on the floor when we grind
# Long as she ain't stoppin', homie, I ain't stoppin'
# Drippin' wet with sweat, man, it's on and poppin'
# All my champagne campaign, bottle after bottle, it's on
# And we gon' sip 'til every bubble in every bottle is gone

# I'll take you to the dollar shop
# I'll let you lick the lollipop
# Go 'head, girl, don't you stop
# Keep goin' until you hit the spot, woah
# I'll take you to the dollar shop
# Want one taste of what I got?
# I'll have you spendin' all you got
# Keep goin' until you hit the spot, woah
# I'll take you to the dollar shop
# I'll let you lick the lollipop
# Go 'head, girl, don't you stop
# Keep goin' until you hit the spot, woah
# I'll take you to the dollar shop
# Want one taste of what I got?
# I'll have you spendin' all you got
# Keep goin' until you hit the spot, woah