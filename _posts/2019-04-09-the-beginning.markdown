---
layout: post
title:  "The Beginning of Team //Todo: Name"
date:   2019-04-09 01:19:23 -0700
categories: team
---
We are: Emma Casper, Ethan Chau, Amol Sharma (Group 3)

## Top 3 Project Ideas
1. Building or adding to low-resource datasets
2. Building a supervised dialect classifier
3. "Translate" a text in one dialect into another dialect

## Action Plan
1. **Datasets**
    - **Viable Plan:**
    - Decide on a language with dialect differences but a lack of defining resources
    - Identify short comings, if any, with existing dialect datasets
    - Devise a method for obtaining and classifying textual data
      - Scrape twitter/facebook/blogs and read user language preferences. (i.e. English UK vs English US)
    - Clean, format and annotate data
    - **Stretch Goal:**
    - Attempt to identify dialects in a region (such as the US) based on markers such as geographic location or morpho-syntactic phenomena based on linguistic studies
2. **Supervised Classifier**
    - **Viable Plan:**
    - Find a labelled corpus of dialects of a language
    - Design a multi-class classifier
        - Word embeddings will not help us differentiate between dialects as the embeddings between similar words in different dialects will still be similar
        - n-grams still perform somewhat better but we don't think either way on its own is good enough
        - Try different kinds of combined architectures such as an HMM where the probabilities are neurally learned
    - **Stretch Goal:**
    - Annotate features of a given text that point towards the chosen classification
    - State how probable each dialect is given the text. e.g. "I ate chips" can be both American and British English
3. **"Translation"**
    - **Viable Plan?/Stretch Goal:**
    - Find a parallel corpus between dialects (is this viable?)
    - Explore options with bitext alignment, IBM Models, and other alteratives to decide on one.
    - Develop the system
    - This seems like a challenge primarily due to lack of data. It may work better as an extension of project 1. 
 

## Github URL
[https://github.com/Asmhoa/481-dialects/tree/master](https://github.com/Asmhoa/481-dialects/tree/master)
