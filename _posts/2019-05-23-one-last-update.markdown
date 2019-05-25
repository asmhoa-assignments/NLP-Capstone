---
layout: post
title:  "One Last Update"
categories: team
---
# One Last Update
This week, we begin our last hurrah: collecting data from the United States and partitioning it into African American English, Chicano English, Standard American English, or "other."  We first describe one final attempt we make at avoiding hand-labeling, and then report progress on our classifier.

## An Unsuccessful Attempt
Given that we'd collected tens of thousands of Tweets for our Chicano- and AAVE-aligned ZIP codes, we were concerned that a hand-labeled signal from only a few hundred Tweets would be insufficient to generalize to the entire set, let alone data from the entire US.  So, we tried to see if we could automatically get a noisy partition by naively labeling the entire set of Tweets with its alignment.

We collected several hundred thousand additional Tweets from the west coast region of the US (Washington, Oregon, Northern California), which we thought could serve as a sufficient proxy for Standard American English.  We ran our preprocessing, length-filtering, and deduplicating scripts on these Tweets, as well as the Chicano- and AAVE-aligned Tweets.  We randomly chose 75,000 from each and used a 80-10-10 train-dev-test split.  We used this dataset to train our simple classifier, which used a single-layer LSTM followed by a linear layer.  We tried three configurations of embeddings: characters only, tokens + characters, and tokens + characters with fasttext initialization.  Results are as follows:
| Embedding Type                               | Best Epoch | Total Epochs | Final Train Accuracy | Best Dev Accuracy |
|----------------------------------------------|------------|--------------|----------------------|-------------------|
| Characters Only                              | 7          | 16           | 67.45                | 43.9              |
| Token + Characters                           | 0          | 9            | 95.61                | 50.97             |
| Token + Characters (fasttext initialization) | 0          | 9            | 98.23                | 50.84             |

These results suggest that the signal provided by this noisy split is simply too noisy.  The configurations with token-based embeddings are essentially learning to memorize the train set, while the best accuracy occurs on initialization.  That these configurations achieve better dev accuracy than the character-only configuration is likely just luck.  This is not to say that the model learns nothing - all configurations perform better than random chance (33.3%) - but in terms of absolute scale, the current performance is simply insufficient.

## Back to Hand-Labeling
As a result, we're continuing with our hand-labeling of dialects into the four categories described in our previous post, but we're finding that the data distribution is exceptionally lopsided.  For instance, at the time of publication, we've labeled over 1000 Tweets, of which only about 100 are "Chicano."  It may be that the scope of "Standard American" represented in this dataset is more diverse: Tweets falling into that category come from a variety of registers (degrees of formality), whereas "Chicano" Tweets are largely of a more casual register.

Regrettably, this again forces us to delay classification of our Tweets.  In order to obtain sufficient content diversity for our classifier, we need much more than 100 examples per category.  To increase our labeling efficiency, we spent some time writing a command-line tool to streamline the labeling process.  We expect that this will allow us to progress at a much quicker rate as we approach the final report.

## What are we actually capturing  here?
One of the big problems we've encountered is the discrepancy between spoken and written forms of dialect. For the country-based sets, we sidestepped this problem by calling this social media English from X Region, and including everything we find. Since our data is collected by region, it automatically fits our definition.

We can't do that for sociolects which are only somewhat geographically based. In classifying by hand, we have to make decisions about what belongs to various dialects. This does not allow for much ambiguity, and if we are trying to represent spoken dialects, there is a great deal of ambiguity; spoken dialects include phonological and prosodic features which are basically always present, while written forms only have the less ubiquitous lexical and syntactic features. Since they may not be present in every utterance (for lack of a better word) there are a lot of utterances which could belong to any dialect, or a subset of dialects. We can't remove the ambiguous Tweets, because that would remove all our candidates for Standard American English. But we also can't necessarily rule out that they may belong to one of the other dialects.

There are two things we might try to accomplish with this dataset. One is capturing the written-on-social-media form of spoken dialects, which requires that we include some of the ambiguously-standard Tweets in with the ones which obviously belong to a specific dialect. This seems a bit dubious considering we have no idea what dialect the ambiguous Tweets might belong to. One way around that would be to identify users who sometimes Tweet in a specific dialect, and assume all their Tweets are in that dialect (even if they look standard). However, this would be time-consuming and may not be very possible with the amount of data we have (we might not have enough repeat users to draw conclusions about them), and it does not account for code-switching.

The other option is to classify all the ambiguously standard Tweets as standard, and only assign Tweets with attested syntactic or lexical features to AAVE or Chicano. This changes our dataset to representing dialects which exist on social media and are related to spoken dialects and sociolects. We are not representing written versions of spoken dialects -- these are dialects which exist in written form on social media. As future research investigates this dataset, it may shed light on whether these distinctions are significant.
