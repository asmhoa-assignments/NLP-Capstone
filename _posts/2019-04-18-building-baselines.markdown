---
layout: post
title:  "Building Baselines"
categories: team
---
# Building Baselines

Given the nature of our project, the pre-established benchmarks/deadlines often don't correspond well.  We'll be following a different project schedule (to be finalized shortly), and for this blog post, we create a preliminary list of the dialects we intend to identify (pending data) and briefly explain how we plan to label them.  We also attempt (and fail) to begin extracting Tweets from Twitter.

## Dialects

We are still finalizing our choice of dialects, but our initial selections are given below. For our decision, we need to consider which dialects will show a learnable difference from 'Standard' English in written text. Within those languages, some may have a wider presence on Twitter, such as African-American English as opposed to Appalachian English.

We're also considering both regional dialects in the USA, and standard or combined English dialects from other countries. We will stick to approximately 10 dialects, in order to limit convolution and variance in features and be able to annotate them accurately.

Considerations:

* USA dialects: AAVE, Chicano English, Southern American English, Appalachian, Standard American English
* Other countries: Singapore, Scotland, Ireland, England (Standard and Cockney?), Canada (maybe multiple Canadian, maybe there is something interesting going on with the French-speaking parts' use of English)

This is not to say we *will* collect data for all of these dialects. They may not be distinguishable in their written form as used on Twitter, or the population which uses them may not be active on Twitter, or we may run into other problems. We are combining smaller dialects defined by their accents into larger dialect areas becuase it's unlikely the phonological features will make it into Tweets. We may readjust our boundaries depending on what features show up in Tweets that allow us to distinguish dialects.

Our first idea for distinguishing location-based dialects is just that: location. The API lets us query based on latitude and longitude, so we can get samples from specific regions known to have a dialect we're interested in. For sociolects such as AAVE, we can use census data to identify geographical areas with a high density of members of that community. Not everyone in a region will use its noted dialect, nor use it all the time, but we can filter on linguistic features if necessary (although not all written dialect will be necesssarily distinguishable, a Tweet might happen not to use any features of the dialect in a way which is impossible to do accidentally with a spoken accent).

## First Attempts at an Unfiltered Dataset
This week, we attempted to use Morstatter et al. (2013)'s "Gardenhose" list of Tweet ID's, which was cited in Blodgett et al. (2016) as a source for their data.  Using this list of IDs, we attempted to retrieve the contents of each Tweet: tweet ID, timestamp, author, latitude/longitude, and text.  However, we quickly encountered a few problems.  For "Standard-level" users, Twitter restricts status lookup requests to 900 Tweets per 15 minute window.  This proved to be a significant bottleneck.  Additionally, since the "Gardenhose" list is from 2011, some of the Tweets are no longer available.  Even among those that are, very few are actually geotagged: out of the first 10000 Tweets we succesfully retrieved, we only had 14 English tweets with locations.  Here is a sample:

```
146853512091926529      2011-12-14 07:26:20     247080042       (36.28099528, 33.51853085)      #5 more #minutes of #Sleep  will feel like a life time ;(
146883743347523584      2011-12-14 09:26:28     282600821       (36.2973968, 33.5292744)        Dec 24: White Christmas at BARADA CLUB http://t.co/lwCH8tgi
146889592937791488      2011-12-14 09:49:42     106813696       (36.29561603, 33.49995398)      Studying Pediatric ^_^ wish me luck :(( – at Al Moujathed H. - Library http://t.co/JqX7eaEC
146893321736945664      2011-12-14 10:04:31     106813696       (36.29561603, 33.49995398)      Studying Vitamin D - A Deficiency  – at Al Moujathed H. - Library http://t.co/JqX7eaEC
146901345226604544      2011-12-14 10:36:24     44654488        (35.90907, 33.839161)           I'm at Zahle http://t.co/qMrB6GDe

```

After looking into the dataset further, we found that none of the Tweet IDs that appeared in Blodgett et al. (2016)'s dataset actually appeared in the Gardenhose list.  Consequently, we're pivoting our approach to use Twitter's [Filtered Streaming API](https://developer.twitter.com/en/docs/tweets/filter-realtime/guides/basic-stream-parameters) to obtain real-time tweets.  We'll filter the stream to only look at Tweets from the regions corresponding to our chosen dialects, and pull Tweets for 3-5 days this upcoming week.  This has the added advantage of ensuring that the Tweets are recent.  Of course, further filtering will be necessary to remove garbage/auto-generated and hashtag-rife Tweets, as well as to control for artifacts.


## References
* Su Lin Blodgett, Lisa Green, and Brendan O’Connor. 2016. Demographic dialectal variation in social media: A case study of African-American English. _Proceedings of EMNLP._
* Fred Morstatter, Jürgen Pfeffer, Huan Liu, Kathleen M Carley. 2013. Is the Sample Good Enough? Comparing Data from Twitter's Streaming API with Twitter's Firehose. _ICWSM 2013._

