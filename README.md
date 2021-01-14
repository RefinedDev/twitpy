# Setup twitpy
Let's install twitpy first.
```
pip install twitpy
```

Now we need to actually setup the module by registring our API Keys.

```python
import twitpy
Access = twitpy.accesstwitpy("access_token","access_token_secret","consumer_key","consumer_key_secret")
```
You need 4 API keys to access twitpy. You need a Twitter Developer Account for this, This is the MOST important step and without doing this you will not be able to access the API.

Learn more about Twitter Developer - https://developer.twitter.com/en

Now we have succesfully Accessed twitpy, Now we will use it's features.

# Picking user from retweet (retweet picker)
Using the `Access` variable we defined before to gain access into twitpy we will now Use it's inbuilt retweet picker.

```python
retweeted_winner = Access.pickuserfrom_retweet(131429358258)
print(retweeted_winner.username)
```
In the parenthesis of `pickuserfrom_retweet` we specify the tweet ID, if the tweet id is valid and it has more than 0 retweets it will pick a user, `pickuserfrom_retweet` returns the following attributes you can use.

```
username
name
userid
followers
following
```

# Getting tweets from a user
```python
gettweets = Access.get_tweetsfromuser("OHrefineddev",10)
for i in gettweets:
    print(i.full_text)
```
In the parenthesis of `get_tweetsfromuser` we write the Username first then we write the amount of tweets we want from the user, the number of tweets should be under 10,because `gettweets` was a list due to having 10 tweets it has to be looped through, `get_tweetsfromuser` returns the following attributes.

```
full_text
id
favorite_count : Likes
retweet_count : Retweets
created_at
source
```

# Finding a user on twitter
```python
user = Access.find_user("OHrefineddev")
print(user.userid)
```
In the parenthesis of `find_user` we write the user's username, `find_user` returns the following attributes.

```
username
name
userid
created_at
description
followers
following
location
tweets_count : Total tweets from the user.
isVerified
avatar_url
```
# Retweeting A Tweet
```python
Access.retweet_tweet(258296982689)
```
In the parenthesis of `retweet_tweet` we write the tweet Id.

# Following a user.
```python
Access.follow_user("OHrefineddev")
```
In the parenthesis of `follow_user` we write the User's username.

# Sending direct messages.
```python
Access.send_dm("OHrefineddev","Hello, i love your twitpy Module."})
```
In the parenthesis of `send_dm` we write the user's username and the text we want to send to the user.

Note: There is a chance of this function to error most probably of the user you are trying to send the message is not following you, or the user has their DMs off.

# Liking a status (tweet)
```python
Access.like_tweet(138924958259208) 
```
In the parenthesis of `like_tweet` we write the Status (tweet) id.

# Unliking a status (tweet)
```python
Access.unlike_tweet(138924958259208)
```
In the parenthesis of `unlike_tweet` we write the Status (tweet) id.

# More Features Coming Soon.
