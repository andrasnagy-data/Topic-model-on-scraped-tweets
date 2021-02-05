import tweepy
import pandas as pd
import credentials


# function for scraping
def scrape_tweets(htags, n_tweets, start_date= '2021-02-04', df_name= 'tweets.csv'):

    # create dataframe
    df = pd.DataFrame(columns= ['username', 'description', 'location', 'following', 
                                'followers', 'totaltweets', 'retweetcount', 'text', 
                                'hashtags'])

    tweets = tweepy.Cursor(api.search, q= htags, lang= 'en', since= start_date, 
        tweet_mode= 'extended').items(n_tweets)

    # unpack tweets from returned cursor object   
    tweet_list = [tweet for tweet in tweets]

    for tweet in tweet_list: 
        username = tweet.user.screen_name 
        description = tweet.user.description 
        location = tweet.user.location 
        following = tweet.user.friends_count 
        followers = tweet.user.followers_count 
        totaltweets = tweet.user.statuses_count 
        retweetcount = tweet.retweet_count 
        hashtags = tweet.entities['hashtags']

        try: 
            text = tweet.retweeted_status.full_text

        except AttributeError:
            text = tweet.full_text

        hashtext = [] 
        for i in range(0, len(hashtags)): 
            hashtext.append(hashtags[i]['text'])
        
        ith_tweet = [username, description, location, following, 
                     followers, totaltweets, retweetcount, text, hashtext]

        df.loc[len(df)] = ith_tweet

    # save data frame to CSV
    name = df_name
    df.to_csv(name, index= False)


if __name__ == '__main__':

    # handle authentication
    auth = tweepy.OAuthHandler(credentials.consumer_key, credentials.consumer_key_secret)
    auth.set_access_token(credentials.access_token, credentials.access_token_secret)
    api = tweepy.API(auth)

    # arguments
    htags = 'Game Stop'
    n_tweets = 200

    # scrape twitter
    scrape_tweets(htags, n_tweets, df_name= 'gamestop.csv')