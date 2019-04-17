---
layout: post
title:  "Project Proposal"
categories: team
---

# Project Proposal

## Introduction: Project, Objective, and Motivations
Most NLP work to date has involved the standard dialects of high-resource languages, due to the ease of obtaining data and the standardized nature of the lexicon and orthography. However, in our social media-driven age, written forms of distinctly dialectal speech are increasingly prevalent, presenting a challenge to NLP systems. We propose to create a dataset of social media English dialects from throughout the world, annotated for both macro- and micro-dialects.  Such a dataset will increase the accuracy of language ID systems and also pave the way for downstream tasks to incorporate dialect information into their understanding of text.

## Minimum Viable Action Plan and Methodology
* Finalize the dialects of English we are targetting, and identify notable features of each (e.g., presence of loanwords/code-switching, geographic location, contractions, names for things). This will be facilitated by sociolinguistic studies and/or consensuses.
* Using [tweepy](https://tweepy.org), scrape the text and metadata of tweets from the "Gardenhose" (Morstatter et al. 2013)
* Automatically annotate each tweet with its "macro" region (United States, New Zealand, Singapore, etc.) using location of the tweet or the user's preferences
* Manually assign regional dialects to a random set of a few hundred tweets using the predetermined features
* Using these classifications, train a model to automatically label the rest of the tweets as their most likely dialect
* Evaluate as we go by taking random samples every 100 tweets and confirming the dialect classification is correct
* Build a classifier for the dialects to serve as a baseline

## Stretch Goals
* Adapt Blodgett et al. (2016)'s Mixed-Membership Demographic-Language Model to other dialects as applicable, and use it to further refine the dataset for those dialects
* Improve/iterate on the classifier
* Annotate the dataset with POS and/or Universal Dependencies

## Resources and Related Work
* Blodgett et al. (2016) and Blodgett et al. (2018)
	* Created a dataset of tweets in African American Vernacular English (AAVE) and devised a model to verify it.  They later annotated part of this dataset with Universal Dependencies.
	* Creating a POS tagger for AAVE text (in multiple domains) using semi-supervised learning. They collected a lot of data, labeled some of it by hand, and labeled the rest with possible tags using a tag dictionary (all possible tags for words, based on dictionary entries and other corpora).
    * They found that their tagger mostly improved on words other taggers didn't know what to do with, particularly phonetic representations of closed class words (e.g. dropped g's like missing -> missin')
* Rabinovich et al. (2018)
	* Part of this paper involves identifying the native language of users on Reddit; we might be able to adapt some of these to identifying native dialect or home region on Twitter or other social media platforms.
    * The most promising idea was using profile information indicating nationality, which we could adapt to looking at bio for location information. For their dataset, they also asked users to post in their native language in another thread; this probably would not work for our purpose since there isn't an great dialect-id classifier the way there is for langauge id.
* Scherrer and Rambow (2010)
	* A review of methods for working with dialects (specifically spoken dialects in a diglossic society), adapting systems that work with the standard (e.g. English-German translation) to work with the dialect (e.g. English-Swiss German translation)
    * The basic idea is a rule-based system including phonological (inferred by spelling variations), lexical, and morpho-syntactic rules.
    * They use a probabilistic model to infer dialect membership as well as dialect area boundaries, using resources like text known to belong to the dialect, and linguistic studies such as dialect atlases. Isoglosses are inferred from dialect atlas maps 
    * Of the applications, methods from dialect classification seem most useful: the authors suggest using the morphological and phonological rules to expand the vocabulary of language models witih region-specific variants, which fixes the problem of dialect text looking made of out-of-vocabulary words
* Lui and Cook (2013)
	* A survey of classification methods for national dialects over a variety of domains (formal text, websites, and twitter). They conclude that treating dialect identification as a text classification problem using a SVM and a bag-of-words model works the best out a variety of model types.


## Evaluation Plan
Once we complete an iteration of the dataset, we plan to follow Blodgett et al. (2016)'s linguistic validation procedure with known linguistic features for each dataset.  Although comprehensive validation is impossible, we will take a random sample of the tweets and verify that they exhibit the phonological/orthographical and syntactic features corresponding to their predicted dialect. We may recruit the aid of linguistic experts.

## References

* Su Lin Blodgett, Lisa Green, and Brendan O’Connor. 2016. Demographic dialectal variation in social media: A case study of African-American English. _Proceedings of EMNLP._
* Su Lin Blodgett, Johnny Tian-Zheng Wei, and Brendan O'Connor. 2018. Twitter Universal Dependency Parsing for African-American and Mainstream American English. _Proceedings of ACL 2018._
* Anna Jørgensen, Dirk Hovy, and Anders Søgaard. 2016. Learning a POS tagger for AAVE-like language. _Proceedings of NAACL 2016._
* Marco Lui and Paul Cok. 2013. Classifying English Documents by National Dialect. _Proceedings of Australasian Language Technology Workshop
* Fred Morstatter, Jürgen Pfeffer, Huan Liu, Kathleen M Carley. 2013. Is the Sample Good Enough? Comparing Data from Twitter's Streaming API with Twitter's Firehose. _ICWSM 2013._
* Ella Rabinovich, Yulia Tsvetkov, and Shuly Witner. 2018. Native Language Cognate Effects on Second Language Lexical Choice. _arXiv preprint arXiv:1805.09590v1._
* Yves Scherrer. 2011. Syntactic transformations for Swiss German dialects. _Proceedings of ACL 2011._
* Yves Scherrer and Owen Rambow. 2010. Natural Language Processing for the Swiss German Dialect Area. _KONVENS 2010._
