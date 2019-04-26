---
layout: post
title:  "Methodology and Data Collection"
categories: team
---

## Dataset
We are building a dataset that aims to capture information needed to learn differences between dialects of English. In doing so, we include dialects that show recognizable features in written form. We knew that American, UK, Australian, Singaporean, and Indian English would have this property. Originally, we wanted to include the standard English from each of these regions, along with small community differences.

However, we realized that the standard dialects from each region would likely be difficult to tease apart. So, we've decided to first focus on assembling tweets for Standard American English, and other English dialects in the US for comparison. We'll mostly be treating other countries as monoliths, since it may be difficult to distinguish more fine-grained differences in written form. However, we if we have enough resources to distinguish regional dialects in the UK, we will attempt that too. Our final dialect list is as follows.

US English Dialects:
- Standard American
- African American
- Chicano
- South US
- Appalachian

Non-US English:
- Standard UK
- Irish
- Scottish
- English (from England)
- French-speaking Canada
- Singapore
- India
- Australia
- New Zealand

If Irish/Scottish/English end up being too difficult to tease apart, we may consolidate them into a single UK monolith.

## Data Collection Progress
Following the issues with unavailable/irrelevant tweets in the previous gardenhose dataset, we decided to collect tweets from the Twitter Streaming API directly.  We spent the early part of the week writing and refining a script to connect to the streaming API, which is essentially a push endpoint that is sent tweets in real-time.  Unlike the previous approach, where we were rate-limited by the number of tweet requests in a 15-minute window, this approach rate-limits us by the amount of connection attempts; a robust script therefore enables us to collect as many tweets as are available.  There is also the added bonus of filtering by location, which results in only geolocated tweets, which we can classify into different potential dialects based on their location.  In the time we've run the script, we've managed to collect several hundred thousand tweets from the aggregation of the various regions; we plan to run this for another couple days to ensure that we a) eliminate noise from a particular day; and b) increase the likelihood of finding unique tweets.  Here's a sample of the raw data so far.  The output is tweet ID, date, user ID, region, country, whether Twitter classified it as English, tweet content, and exact coordinates (if available), all separated by tabs:
```
1121455557330833408     2019-04-25 16:46:55     27612193        Comber, Northern Ireland        United Kingdom  True    @WACCOE I never even thought of that...poor twat.!
1121455475944579072     2019-04-25 16:46:35     170266806       Hamilton, Scotland      United Kingdom  True    Wish a wasn’t a mad freak that eats about 2 things, am needin to grow up
1121453458828210182     2019-04-25 16:38:34     147157830       Solihull, England       United Kingdom  True    Bloody hell! I’m all passed out with excitement here.
1121457604524482561     2019-04-25 16:55:03     1621184652      Montréal, Québec        Canada  False   @PKP_Qc Great catch mon PK !! Après avoir sacré la volée à #tlmep dimanche, tu vas maintenant montrer à Taillefer c… https://t.co/zdNK5cNTcK
1121461326771965952     2019-04-25 17:09:50     2313480672      North Region, Singapore Singapore       True    Huh booboo laughing in her sleep meh? cb mimpi ape je
1121453514624868353     2019-04-25 16:38:48     813048016684785665      Jaipur, India   India   False   @nishantchat Bilkul sir!
Isiliye to priyanka vadra ne withdraw kar liya.
1121453518798446594     2019-04-25 16:38:49     962232407352135680      New Delhi, India        India   False   @Dr_Uditraj Tumko sting operation yaad hai. Vahi kaaran hai tumko ticket reject honey mein.
1121463802552184833     2019-04-25 17:19:40     814570224       Perth, Western Australia        Australia       True    @dancingfool75 Bugger. Are you feeling any better? Perhaps puppy cuddles will help?
1121489112794406912     2019-04-25 19:00:15     48945958        Christchurch City, New Zealand  New Zealand     True    chur so true
1121489116619689984     2019-04-25 19:00:16     117572800       New Orleans, LA United States   True    That’s all it’s ever gon be!
```


## Tweet Filtering Methodology
Once we have aggregated the tweets, our task is to split them into their respective dialects (from the set we chose earlier and on the basis of which we defined our bounding boxes for collection). Overall, we will manually classify a subset of tweets (hoping it's representative), and then train a model to classify the rest while evaluating 1 in every 50 tweets to see that the model is working reasonably. We think that this method has a few disadvantages such as that similar models trained on our set will just learn what our model did (which may be completely incorrect). Therefore, while this is our most likely plan, we are on the lookout for alternatives.

Before getting to that, we will be cleaning the tweets we recieve from the api by  removing hashtags, URLs, repeated punctuation (!!!), and emojis. If the tweet contains a non-Latin script, we will not consider it to be in English. We will also be using a language model trained on Standard US English (or UK for the UK region) and use it's perplexity on a given tweet as a measure of how close the tweet is to English. This will help us decide whether we want to consider it as the local ("basilect") dialect of English, as opposed to the standard ("acrolect") form. If this is ineffective, we may go a simpler route and just ensure that at least 1/3rd - half of the words can be found in a dictionary.

Another thing that might help us is that we are saving tweets from our regions in different files. We will be collecting data for smaller regions simultaneously (i.e. the Appalachian region) which we can then isolate from the broader US twitter feed. 

Once we have a cleaner set, we will begin annotating and follow the process described earlier.

## Tentative Schedule
Since our task doesn't fit the benchmarks too well, here's our proposed tentative schedule for the rest of the quarter:
4/25 (today) - Finalize tweet collection mechanism and begin collecting tweets
5/2 - For at least one region (Singapore or India) extract the English tweets and select the ones that are most vernacular, based on our methodology above
5/9 - Extract/select tweets for the rest of the regions, and begin labeling and compiling the dataset; decide on additional annotations, if feasible
5/16 - Build V1 classifier and/or make annotations
5/23 - Expand on V1 classifier
