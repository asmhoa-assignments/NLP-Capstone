---
layout: post
title:  "Evaluating Ideas"
categories: team
---

We've spent the past couple days looking at the feasibility of each of the three
ideas in our previous post.  There are still many open questions, but we're
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
3. **Idea 3 (Translation)**

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

