import os
import time
import tweepy
import schedule
from dotenv import load_dotenv
from datetime import datetime
import random

# Load credentials from .env
load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

# Authenticate
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Your AI-generated or static tweet ideas
TWEETS = [
    "Hello, world! This is my first automated tweet.",
    "AI bots are fun to build. #Python #BotLife",
    f"The current time is: {datetime.now().strftime('%H:%M:%S')}"
]

# Function to post tweet
def post_tweet():
    tweet = random.choice(TWEETS)
    try:
        api.update_status(tweet)
        print(f"Tweet posted: {tweet}")
    except Exception as e:
        print(f"Failed to post tweet: {e}")
        
        
# Post immediately
post_tweet()  #This runs the first tweet instantly

# Schedule tweet every 30 minutes
schedule.every(30).minutes.do(post_tweet)

print("AI Twitter agent started. Posting every 30 minutes...")

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
