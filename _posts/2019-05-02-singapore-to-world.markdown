---
layout: post
title:  "From Singapore to the World"
categories: team
---

This week, we finalize our dataset extraction mechanism and try it with the Tweets that we've collected from Singapore.  As a reminder, here's our schedule, adjusted based on feedback and updates in our methodology:

- 5/2 (today) - For at least one region (*Singapore* or India) extract and clean the English tweets
- 5/9 - Extract/clean tweets for the rest of the regions, and begin labeling and compiling the dataset; decide on additional annotations, if feasible
- 5/16 - Build V1 classifier and/or make annotations, plus error analysis
- 5/23 - Expand on V1 classifier

We've also updated our methodology.  Specifically, since we're not too familiar with the minutiae of each region's dialect, we're foregoing our original idea of extracting the vernacular.  Instead, we are essentially compiling a dataset of "social media English" from throughout the world.  So, our primary methodology consists of macro-region classification, followed by cleaning and language-filtering process, which we describe below.

## Data Collection Update
Over five days last week, we scraped 1.6 million+ Tweets from the Twitter Streaming API.  We specified regional bounding boxes for the regions that we are interested in.  The data are grouped by their reported country name, which is the country from which the Tweet was sent, in the language of the user's profile.  To compile the Tweets for a given country, we will combine the outputs from the different country names.

We're still working on obtaining Tweets for the US dialects, since our methodology involves running two scraping tools in parallel, and we've had issues with obtaining a second API key.  We will run one instance for the entire US, and another instance for the specific regional dialects.  For the general US data, we will take the set difference of {entire US} \ {regional}.

## Cleaning Process
Originally, we considered six different components to clean from Tweets.  We describe and (un)justify each below; bolded components were included in our finally methodology:
- *URLs*
    - We remove any token beginning with "http://" or "https://" - it is unlikely that these provide any semantic information.
- *Repeated Punctuation*
    - Since informal punctuation can be erratic, we essentially perform lemmatization to make the data more consistent.  For any group ("blob") of punctuation containing one or more question mark, exclamation point, period, or comma:
        - If there is a question mark, we replace the entire punctuation blob with `?`
        - Otherwise, if there is an exclamation point, we replace the entire punctuation blob with `!`
        - Otherwise, if the punctuation blob contains `...` (ellipsis), we replace the entire blob with `...`
        - Otherwise, we take the first character in the punctuation blob
    - This seeks to extract the most important semantic aspects of each punctuation blob.  For instance, in the blob `...?`, the question mark arguably contributes more than the ellipsis.
- Hashtags and @-mentions
    - We originally considered removing hashtags and @-mentions, but realized that they could be used as part of a sentence, e.g., `Bought #coffee from @husky_grind`
- Emoji
    - Similarly, emoji could convey meaning and might be used more in some regions than others: `I’m feeling 😂 today`
- *Short Tweets*
    - Since it is unlikely that Tweets under a current length are sufficiently contentful, we remove them.  The threshold is currently <= 2; we may tune this as necessary.

## Language-Filtering Process
We've frequently observed that even in majority-English-speaking parts of the world, a nontrivial proportion of the Tweets are not in English.  To automatically remove these Tweets from our dataset, we propose two methods:
1. ASCII conversion - since English fits entirely within extended ASCII, we will convert the Tweet text to ASCII and see if it significantly decreases in length.  However, we will still preserve the original Unicode in the final dataset in order to properly display Emoji, etc.
2. Dictionary lookup - we will check the Tweet's tokens against an English dictionary to ensure that at least 1/4 of the tokens are English.  Ostensibly, this will cover over OOV, lexical differences, and misspellings.  Again, we may tune this threshold.

## Singaporean Data
Our preliminary dataset for Singapore can be found on the master branch of our [repository](https://github.com/Asmhoa/481-dialects) (we were having some issues with copying it over here).
