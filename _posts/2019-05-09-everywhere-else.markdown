---
layout: post
title:  "Everywhere Else"
categories: team
---

# Everywhere Else

This week, we finalize our Tweet-cleaning mechanism and compile the first version of our dataset for non-US dialects.  Here's where we are in our roadmap:

- 5/9 (today) - Extract/clean tweets for the rest of the regions, and begin labeling and compiling the dataset; decide on additional annotations, if feasible
- 5/16 - Build V1 classifier and/or make annotations, plus error analysis
- 5/23 - Expand on V1 classifier

Due to some unforeseen delays in the data collection process, we're only just starting to collect data for our US dialects (AAVE, Chicano, etc.).  Depending on the progress that we make, we may have to postpone our benchmark for 5/16 to 5/23.

## Defining English
In our [previous post](https://asmhoa.github.io/481-dialects/team/2019/05/02/singapore-to-world.html), we briefly described our idea for deciding if a Tweet was in a dialect of English or not.  We've since refined the process.  Specifically, for a given Tweet:
1. Define `raw_tweet` as the Unicode Tweet body in its original form
2. Let `tweet_length` be the number of **characters** in `raw_tweet`
    - Compared to the number of tokens in `raw_tweet`, this becomes a useful measure for filtering Tweets that are in non-Roman script and do not use spaces
4. Let `ascii_tweet` be the result of converting `raw_tweet` to ASCII encoding, removing all characters that do not fit into the Extended ASCII character set
    - This removes all non-Roman scripts (including emoji) from the Tweet
6. For each token `tok` in `ascii_tweet`, check if `tok` is in an English dictionary.  If it is, add the number of characters in `tok` to our total count of English characters
7. If the total count of English characters exceeds a (tunable) threshold, classify the Tweet as English

## Data Cleaning
In this section, we describe our final process for collecting, refining, and finalizing a set of Tweets for a non-US country.  Although we've covered parts of this in previous blog posts, we've continued changing our methodology and haven't ever described it all at once.
1. Compute the bounding box(es) for the country
2. Using our [streaming script](https://github.com/Asmhoa/481-dialects/blob/master/scripts/streamer.py#L7), collect Tweets from the Twitter Streaming API from within the specified bounding box(es)
3. [Partition](https://github.com/Asmhoa/481-dialects/blob/master/scripts/partition.py) the Tweets based on the country associated with the Tweet (this is mostly relevant when collecting data for multiple countries at once)
    - We realize that a) region is not a perfect proxy for dialect; and b) users may send Tweets from countries that they are not native to.  However, given the limitations of our compute and API resources, we believe that this is a reasonable assumption.
4. Twitter reports the country name in the profile language of the user who sent the Tweet.  We manually combine all of the output for a country, excluding files that do not contain any English Tweets.
5. [Clean](https://github.com/Asmhoa/481-dialects/blob/master/scripts/preprocess.py) the Tweets of URLs and repeated punctuation.  The rationale for this is the same as in our [previous post](https://asmhoa.github.io/481-dialects/team/2019/05/02/singapore-to-world.html).
6. [Filter out](https://github.com/Asmhoa/481-dialects/blob/master/scripts/filter_short.py) Tweets that are shorter than a certain length.  We remove anything with fewer than 3 tokens.
7. Join multi-line Tweets together with a space.  This makes the dataset more manageable, especially for downstream use.
8. Filter out non-English Tweets, as described above
9. Remove duplicate Tweets
10. Convert everything to JSONL format

For the UK Tweets, we added an additional step between 9 and 10; namely, we partitioned the dataset based on constituent country names in the Tweet's region.  This worked remarkably well - only about 6,500 (5\%) of the Tweets were ambiguous, and the rest fit nicely into the set of \{London Metro Area, England (not London), Scotland, Wales, Northern Ireland, Isle of Man\}.

Data in JSON-lines format is available [here](https://github.com/Asmhoa/481-dialects/tree/dataset/jsonl), and dataset statistics/hyperparameters are available [here](https://docs.google.com/spreadsheets/d/1T4gB1je5vI5PFzXXAtDmjOfPpOQnEyPG3M1EqiYw-1k/edit?usp=sharing).

## ZIP Code Clustering
Blodgett et al's [paper](https://aclweb.org/anthology/P18-1131) on parsing for AAVE uses a dataset partly based on census demographics. In hopes of  finding bounding boxes, we traced the dataset back to [this paper from 2011](https://pdfs.semanticscholar.org/eb4c/7dcb43bf42b0ecb949d26262a48edce87efe.pdf) but were unable to get access to its data. So, we came up with our own way to make demographics-based bounding boxes. These boxes will be used to collect higher-likelihood AAVE tweets, some of which we can classify by hand and use to train a classifier to run over the rest of the US data.
- For demographic data, we are using the 2017 American Communities Survey 5-year estimates, which are tabulated by zip code. The data can be found [here](https://factfinder.census.gov/faces/tableservices/jsf/pages/productview.xhtml?pid=ACS_17_5YR_S0601&prodType=table) and covers most (but not all) zip codes
- We filtered the zip codes to ones with at least 60% African American population: this gave us 878 zip codes
    - Just using the zip codes would be problematic: Twitter only lets us choose 20 bounding boxes at a time. Also, zip codes are pretty small so the data may be more noisy (we are likely to get people just passing through the area and people who live there may be tweeting elsewhere; with larger areas we might capture places which might have a large community of speakers who spend time in their home area).
- In order to create bounding boxes, we need latitude and longitude information, which we found [here](https://fusiontables.google.com/DataSource?docid=1Lae-86jeUDLmA6-8APDDqazlTOy1GsTXh28DAkw#rows:id=1)
- We clustered the zip codes by joining zips within a few miles of each other into a group, and continuing until all our groups were at least 20 miles apart.
    - This resulted in 131 zip-groups, 60 of which contained only one zip.
    - We decided to work with only the groups with at least 10 zip codes; there are 15 such groups covering 498 zip codes
- Bounding boxes are formed from zip-groups by taking the largest and smallest latitude and longitude of the group. This will make a bigger box than is actually covered by the zip-group but we are doing this to collect higher-likelihood-AAVE data so we would rather include too much than too little.
- Looking at the boxes on a map, most of them are in the southeast US, as well as a couple by the Great Lakes.
We applied the same methodology for Chicano English by filtering on areas with a high Hispanic/Latino population, and got 13 groups of 10+ zips,  containing a total of 506 zip codes (out of the 769 relevant zip codes).

## Steps in Progress
- We're working on AAVE data collection.
    - After collecting a sufficient amount of Tweets, we'll hand-label some of the them as AAVE/not-AAVE and build a classifier for the rest.
    - After refining this methodology, we'll do the same for Chicano English.
- We noticed that the Canada-French group had some Tweets from British Columbia and Nova Scotia (i.e., non-French-majority regions).
    - This might be due to part of the United States bounding box touching Canada during our initial data collection.  
    - We plan to re-collect data for Canada-French and now Canada-English, with regions loosely based on the ethnic majorities noted in [Wikipedia's map of Canadian census divisions](https://en.wikipedia.org/wiki/French_Canadians#/media/File:Censusdivisions-ethnic.png).
    - In order to obtain a more geometric region, we'll define Canada-French to be the region in Canada north of Ottawa, east of Lake Superior, and south of Newfoundland.
    - We define Canada-English to be the remainder of the country (west of Lake Superior, south of Ottawa, and Newfoundland).

## Group Feedback Discussion
Group feedback was generally positive, as we'd recently clarified our vision for this project.  We all agreed that we brainstormed and discussed/explained our work effectively, and that we could work on timely completion of our tasks.  We decided to start assigning concrete deliverables to each person after each class, so that information wouldn't get lost in the information overload that is Slack.
