---
layout: post
title:  "Evaluating Ideas"
categories: team
---

We've spent the past couple days looking at the feasibility of each of the three
ideas in our previous post. There are still many open questions, but we're
getting closer to a final project proposal.

## Pros and Cons
1. **Idea 1 (Dialect Dataset)**
    - Premise: We would create an annotated dataset of tweets and sentences from
      various dialects of English.  The immediate target is distinguishing
      between "standard" {American, British, Australian, New Zealand, etc.}
      Englishes, with a goal of also obtaining more fine-grained data about the
      vernacular(s) in each area.  To the best of our ability, we would collect
      data in a way that eliminates conflating factors, such as topic.
    - Pros
        - Prior work on constructing datasets from Twitter and about dialects
          exists (Blodgett et al. 2018 is a major example).
        - A couple sociolinguists at UW are familiar with collecting and
          standardizing data for dialects, and we could use them as a resource.
        - This is a space that hasn't seen much exploration, so we would provide
          the NLP community with a new type of data and set a precedent for
          future work.
    - Cons
        - Dialects are unstandardized by nature, and navigating the differences
          in transcription/orthography could be challenging.
        - Controlling for topic and other potential confounding factors could
          make creating a robust dataset difficult.
        - We would have to make several assumptions about what features define a
          dialect, and annotating for them will be time-consuming and difficult.
2. **Idea 2 (Supervised Classifier)**
    - Premise: n-gram models still outperform neural methods when it comes to differentiating language that is very similar. Word embeddings alone cannot help us differentiate between small differences in dialects, especially without a parallel corpus. This project should improve on the n-gram method in terms of accuracy.
    - Pros
        - This work would be useful to the larger community, and the method could be extended to other tasks where we need to find similarities between texts
        - Amol is excited about this one
    - Cons
        - We did not find a suitable corpus in our research so we may not be able to complete this task
3. **Idea 3 (Translation)**
    - Premise: Creating a translation system between dialects of the same language (probably English). After getting data for each dialect and for the standard, we would make language models for each. Language models for the dialects would likely be informed by that of the standard (which can be backed up by more data), and possibly sociolinguistic studies which indicate rule-based transformations. Not having a parallel corpus, we might base our translation system on some semantic representation that connects all the language models.
    - Pros:
        - This is an interesting challenge due to the lack of parallel corpora for dialects
        - This might be helpful as an intermediate step for other tasks: models that work well on the standard might perform better if dialects are first translated to the standard.
    - Cons:
        - The lack of parallel corpora means we can't use machine translation strategies which require one.
        - There might not be sufficient non-parallel corpora, so we would have to collect our own data (which isn't the primary goal for this idea, and I doubt we would be able to do it justice while trying to design the translation part).
        - This isn't very useful by itself in practice: as far as I know there isn't a load of demand for translation between dialects that are fairly similar, which is what we're proposing to work on (there might be more for less mutually intelligible dialects, but I'm not sure this idea would work on those).

## Codebases
We likely won't train any models until our dataset is collected, so most of the
software we'd need to use involves methods for collecting data.  Here's what we
have so far:
- [tweepy](https://tweepy.org) is a Python package for obtaining tweets
- [Amazon Mechanical Turk](https://mturk.com) is a crowdsourcing platform that
  we could use for annotations


## Lecture Topics
It could be helpful to have a lecture or discussion on data mining/collection, 
especially methods for eliminating artifacts and ensuring robustness in 
annotations.

