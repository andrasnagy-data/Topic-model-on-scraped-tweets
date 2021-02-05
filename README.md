**Twitter Scraping and Topic Modelling**

I used tweepy to download tweets based on a specific key word. I ran the "scrape_tweets.py" 4 times using 4 different keywords. The idea was that the keywords I chose, would create 4 distinct types of texts, however that turned out not quite to be the case. Nonetheless, the matrix factorization produced "abstract topics" that kind of resemble the initially choosen themes.

I decided to use randomized (to speed the process up) Singular Value Decomposition as the algortihm of choice, as I wanted the topics to be orthogonal (most different) to each other. Another algorithm that could be used is called the Non-Negative Matrix factorization.

Topics are essentially clusters of words and they emerge from statistical regularitiesin the Document-term matrix.

The outcome of this process is the following:

- 'rating putin vladimir navalny alexey zyuganov record communist reached nationalist',
- 'regret biographyone chapter writing prisoner marking survivor tuesday new vladimir',
- 'pseudo sinking farce absurd titanic style worthy changed poisoning case',
- 'learning machine machinelearning ai datascience 100daysofcode analytics python artificialintelligence devcommunity',
- 'aly rubinadilaik doing game stop gony strategy jasminbasin clever contestant',
- 'crackdown risks turning kremlin martyr navalny alexey amartyr rubinadilaik aly',
- 'cheese party burger wine blue beer jeans longer republican eat',
- 'cheese burger ajstarthere sandragathmann protests explain russias man elite big'

The first 2 topics clearly correspond to Alexey's current affairs, the 3rd one seems too ambiguous, the 4th one is clearly about Machine Learning. The 5th one seems to be about Game Stop and the strategy the strategy that was used. The 6th one again is about Alexey, while the 7th one is about cheese and a bit of politics. The last one seems to be a mixture of cheese and Alexey.