## TwitterBot

This is a twitter bot that updates the dollar price in relation with the peso Argentino.
Everyday at 5pm, the bot will upload a 50 Cent photo with the price in half, half dollar in relation with the peso.

This is not just a Twitter image upload, the code was made so you can understand and edit it. Feel free to see how the Twitter API works with this software. Good luck!

### Example (1U$D = 291 24/10/22)
[![50cent.jpg](https://i.postimg.cc/Hxq0YcDB/50cent.jpg)](https://postimg.cc/0MCKZNNw)

### Features
- Automatic post
- Mention reply
- Mention Like


### Requirements
- __First__: You will need to install python.

  - [Python 3.10.5](https://www.python.org/downloads/)
- __Second__: Open your computer command line then run the command: __pip install__ +  
  - tweepy
  - pillow
  - schedule
  - requests
  - pymongo
  - pymongo[srv]
 
- __Third__: Complete the config.py file with your twitter keys

- __Fourth__: Complete your MongoDB data from line 44 to 46.

- __Fifth__: Execute Bot.py


### License 
* MIT
