#import json

def flatten_tweets(tweets_in):
    """ Flattens out tweet dictionaries so relevant JSON
        is in a top-level dictionary."""
    tweets_list = []
    
    # Iterate through each tweet
    for tweet in tweets_in:
        #tweet_obj = json.loads(tweet)
    
        # Store the user screen name in 'user-screen_name'
        tweet['user-screen_name'] = tweet['user']['screen_name']
    
        # Check if this is a 140+ character tweet
        if 'extended_tweet' in tweet:
            # Store the extended tweet text in 'extended_tweet-full_text'
            tweet['extended_tweet-full_text'] = tweet['extended_tweet']['full_text']
    
        if 'retweeted_status' in tweet:
            # Store the retweet user screen name in 'retweeted_status-user-screen_name'
            tweet['retweeted_status-user-screen_name'] = tweet['retweeted_status']['user']['screen_name']

            # Store the retweet text in 'retweeted_status-text'
            tweet['retweeted_status-text'] = tweet['retweeted_status']['text']
            
            if 'extended_tweet' in tweet['retweeted_status']:
                tweet['retweeted_status-extended_tweet-full_text'] = tweet['retweeted_status']['extended_tweet']['full_text']
        
        if 'quoted_status' in tweet:
            # Store the quoted user screen name in 'retweeted_status-user-screen_name'
            tweet['quoted_status-user-screen_name'] = tweet['quoted_status']['user']['screen_name']

            # Store the retweet text in 'retweeted_status-text'
            tweet['quoted_status-text'] = tweet['quoted_status']['text']
            
            if 'extended_tweet' in tweet['quoted_status']:
                tweet['quoted_status-extended_tweet-full_text'] = tweet['quoted_status']['extended_tweet']['full_text']
            
        tweets_list.append(tweet)
    return tweets_list

def check_word_in_tweet(word, data):
    """Checks if a word is in a Twitter dataset's text. 
    Checks text and extended tweet (140+ character tweets) for tweets,
    retweets and quoted tweets.
    Returns a logical pandas Series.
    """
    contains_column = data['text'].str.contains(word, case = False)
    contains_column |= data['extended_tweet-full_text'].str.contains(word, case = False)
    contains_column |= data['quoted_status-text'].str.contains(word, case = False)
    contains_column |= data['quoted_status-extended_tweet-full_text'].str.contains(word, case = False)
    contains_column |= data['retweeted_status-text'].str.contains(word, case = False)
    contains_column |= data['retweeted_status-extended_tweet-full_text'].str.contains(word, case = False)
    return contains_column