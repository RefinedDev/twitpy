from __future__ import unicode_literals
from tweepy import Cursor
from tweepy import API
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import os
import random

class _TwitterAuthenticator():
    class Login():
        def __init__(self,ac_tok = None, ac_tok_sec = None,con_tok = None,con_tok_sec = None):
            self.actok = ac_tok
            self.actoksec = ac_tok_sec
            self.contok = con_tok
            self.contoksec = con_tok_sec    

        def authenticate_twitter_app(self):
            auth = OAuthHandler(self.contok,self.contoksec)
            auth.set_access_token(self.actok,self.actoksec)
            self.twitter_client = API(auth)
            return self.twitter_client

class accesstwitpy():
    def __init__(self,__access_token,__access_token_secret,__consumer_key,__consumer_key_secret):
        self.__a = __access_token
        self.__b = __access_token_secret
        self.__c = __consumer_key
        self.__d = __consumer_key_secret
        self.__api = _TwitterAuthenticator().Login(self.__a,self.__b,self.__c,self.__d).authenticate_twitter_app()

    def pickuserfrom_retweet(self,id):
            try:
                res = self.__api.retweeters(id)
                choose = random.choice(res)
                res2 = self.__api.get_user(choose)
                self.username = res2.screen_name
                self.name = res2.name 
                self.userid = res2.id
                self.followers = res2.followers_count
                self.following = res2.friends_count
                return self
            except:
                print('HTTP Error 404: Not Found - Not Results Found Or Invalid API Keys') 
        
    def get_tweetsfromuser(self,name,count):
        try:
            if count < 11:
                tweets = self.__api.user_timeline(screen_name=name,count= count, tweet_mode = 'extended')  
                return tweets
            else:
                print("You cannot fetch more than 10 tweets from a user.")
        except Exception as e:
            print(f"An error occured while trying to find the user: {e} Or Invalid API Keys")

    def find_user(self,name):
        try:
            api = self.__api
            result = api.get_user(name)
            self.username = result.screen_name
            self.name = result.name 
            self.userid = result.id
            self.created_at = result.created_at
            self.description = result.description
            self.followers = result.followers_count
            self.following = result.friends_count
            self.location = result.location
            self.tweets_count = result.statuses_count
            self.isVerified = result.verified 
            self.avatar_url = result.profile_image_url
            return self
        except:
            print("HTTP Error 404: Not Found - Not Results Found Or Invalid API Keys")

access = accesstwitpy("1204782674663002113-Q9j4sXuZaE6UCp5x7H8fTfJRoxv81p","531AQWa3VtVtXdTGfeTAlwKPTIB7wD83sOR7FgwZtsj7C","TpspAUJsIrzeMTvSgt4aL86WY","5VnP1o1YIjI9fN9iAYRaZcm4hkcAUDWhqteExNo9cn5Z1W25dI")
b =  access.get_tweetsfromuser("FortniteGame",1)
print(dir(b[0]))