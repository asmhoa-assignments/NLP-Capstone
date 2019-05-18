---
layout: post
title:  "Back to America"
categories: team
---

# Back to America

This week, we analyze our worldwide data and turn our attention to American dialects, where we prepare to train our (lightly) supervised classifier.  As mentioned last week, we encountered some delays in data collection and needed to postpone our original benchmark for this week:

- 5/16 - ~~Build V1 classifier and/or make annotations, plus error analysis~~
    - Re-collect and process Canadian data
    - Perform error analysis on worldwide data
    - Collect data for Chicano/AAVE, and label data in anticipation of classifier
- 5/23 - ~~Expand on V1 classifier~~
    - Collect general US data
    - Train and run a classifier for the US data
    - Perform error analysis on the US data

## Regarding Canada
As noted last week, we expanded our Canada data to include the entire country, partitioned into majority English-speaking and majority French-speaking.  This data is now available with the [rest of our JSONL data](https://github.com/Asmhoa/481-dialects/tree/dataset/jsonl).

## Error Analysis: World Social Media Englishes
For error analysis, we randomly sampled 50 Tweets from each of the final datasets and examined them for unique features and/or anomalies.  We also specifically compared the subregions within UK and Canada with each other.  In addition to the features below, all regions contained mentions of place/person names specific to their location.

As is customary, we are obliged to warn readers that the following contains unfiltered social media data that may be considered offensive.

### Australia
Potentially unique words: pal, digging, bludge
Tweets of note: n/a

### Canada-English
Potentially unique words: lmao
Tweets of note:
```
1127092485728002049     2019-05-11 06:06:03     138418838       Vancouver, British Columbia     Canada  False   UTC -7 | AUNZ —   Scotty Morrison smooths troubled waters after 'Pākehā' called a racist term   [49.28248253, -123.12721877]
```
This Canadian Tweet concerns a news report about Australia/New Zealand and includes a Maori word, which we might expect to find only in New Zealand.

### Canada-French
Potentially unique words: 'bout
Tweets of note: n/a
Other comments: there was a general theme of Mothers' Day, likely due to the time of collection.

### India
Potentially unique words: tata steel, muthoot, lakh (Indian number), bhai, drubbing, Amritsar (location), numb (instead of no. or num. to denote "number")
Tweets of note: 
```
1121456800342126592     2019-04-25 16:51:51     116657077       Bhilwara, India India   False   @IndianMathsProf Math teacher ko maths Mai medal mat do <U+1F602>
1121587703496134656     2019-04-26 01:32:01     15054362        Bengaluru South, India  India   False   @gregariousgargi yeh kaun hain, kyun hain. confidently showing stupidity
1121647732060409858     2019-04-26 05:30:33     1073162776128905216     Dhanbad, India  India   False   Tu kyu nhi kiraye ka bhid bula leta hai, apne rally me @Dr_Uditraj ,Don't spread lie on the issue of "Mega Road Sho…
```
These Tweets exhibit codeswitching between English and romanizations of other languages.

### Ireland
Potentially unique words: cos (instead of coz/cuz), pal
Tweets of note: n/a

### New Zealand
Potentially unique words: com'on (instead of c'mon)
Tweets of note: n/a

### Singapore
Potentially unique words: n/a
Tweets of note:
```
1121629396958191617     2019-04-26 04:17:41     4430235432      North-East Region, Singapore    Singapore       False   Taehyung umaakyat ka nanaman. Jusko how to get over with this look. <U+1F97A>
1121670512252338176     2019-04-26 07:01:04     1050975217005211649     East Region, Singapore  Singapore       False   balik keje straightaway sakit perut! stressss idh time f this
```
These Tweets exhibit codeswitching between English and romanizations of other languages (e.g., Malay in the second Tweet).

### England (excl. London)
Potentially unique words: eh
Tweets of note:
```
1121742083256143872     2019-04-26 11:45:28     177982062       Lincoln, England        United Kingdom  True    When you next coming to Lincoln @deb_connor ? Cafe Shanti is now fully vegan <U+1F603>☯️x
1121732029979271170     2019-04-26 11:05:31     397230528       North West, England     United Kingdom  True    Amazing how my tweet has been changed &amp; regurgitated I’m so many different ways isn’t it...  Glazers eh?

```
The first Tweet has an interesting case of copula ellision.  The second uses "eh" and also contains a typo ("I'm" instead of "in").

### Isle of Man
nothing of note

### London Metro Area
Potentially unique words: pass out (to mean "retire")
Tweets of note:
```
1121777366794153985     2019-04-26 14:05:40     288470641       Harrow, London  United Kingdom  True    Proud day watching Firefighter Owen pass out as a full time Member of the London Fire Brigade! <U+1F525><U+1F6A8> @ Harrow, Unite…      [51.57798, -0.33741]
```

### Northern Ireland
nothing of note

### Scotland
nothing of note

### Wales
Potentially unique words: aye, ace
```

1121720356451028992     2019-04-26 10:19:08     948225572005711872      Hawarden, Wales United Kingdom  True    @Stdomingo78 She’s ace mate and she’s spent a lot of time with her through consultation they’re based in Chester ca…
1121690569720254464     2019-04-26 08:20:46     472376014       Tonypandy, Wales        United Kingdom  True    @craigreddy Aye and I know<U+1F602><U+1F92A>
1121746254126567424     2019-04-26 12:02:02     562419621       Carmarthen, Wales       United Kingdom  True    @poltawards thanks Mike for having @poltawards follow me #diolch Sir!
```
In the third Tweet, the hashtag #diolch is a Welsh word meaning "thanks."

### Concluding Thoughts
The Western dialects are rather difficult to tease apart, except for a small number of casual phrases.  Codeswitching features prominently in Singapore and India, where it is likely that standardization movements are well-challenged by deeply established vernacular traditions.
Canada-English and Canada-French were very difficult to tell apart; there did not seem to be much French influence in the latter's English.

## Classifying America
This past week, we collected several hundred thousand Tweets from the AAVE and Chicano regions we identified in our last blog post.  For this upcoming week, we plan to hand-label a few hundred Tweets from these data, compiling a small dataset with Tweets labeled as one of the following:
- AAVE
- Chicano
- "Standard American"
- "other"

With this data, we will train a small classifier (likely a non-neural Softmax classifier), which we will run on the remainder of the AAVE/Chicano data.  In order to get a representative sample of the entire US, we're also collecting data from the whole country and will run our classifier on it also.

With respect to labeling, we are classifying Tweets as AAVE or Chicano based on the presence of the following features:

### AAVE
With AAVE, we saw that there were many features common to other dialects such as "ain't" or subtleties that we would have to take a deep dive into to construct a more robust way of identifying tweets in this vernacular. Instead, we sifted through the dataset and identified tweets we thought might be AAVE, and then compared features to previous work. This may give us a lower recall, but vastly decreases our development time. We may reconsider this depending on our baseline model performance.

The features that often showed up were:
* ain't
    * ain't is one of the words that appears in both AAVE and other US English dialects
    * It is unique to AAVE when it appears as a contraction of "do not" as opposed to 'is not' or 'have not'
    * Example tweet: "now nobody ain’t tell me vapor Vick’s burn"
    * Some occurences were not of the "do not" variation but considering we were only collecting data from high African-American populations, we thought it likely that others were part of AAVE too
    * Howe, Darin. "Negation in African American Vernacular English", from Aspects of English Negation. p.185.
* Zero copula
    * There were many examples of sentences that drop the copula 'is' or omit some form of 'do', which are one of the markers of AAVE
    * Missing 'do': 'Why in the black communities we dismiss mental health issues?' or 'Why you say that ?'
    * Missing 'is': 'broke boy gone run if he ain’t gettin no money'
    * Bender, Emily M. Syntactic variation and linguistic competence: The case of AAVE copula absence. Stanford, California: stanford university, 2000.
* Use of 'be'
    * Another important marker is the use of 'be' where we might not expect it in "Standard" dialects of English
    * It's also used to mark aspects of tense
    * "we be having fucking fun". In this case "be having" indicates that this is present tense. If this was "been having fun" or "been had fun" instead, this would be in different aspects of past tense.
    * Fickett, Joan G. (1972), "Tense and aspect in Black English", Journal of English Linguistics, 6 (1): 17–19
* Other common features we observed but did not see studies for
    * 'yo' instead of 'you/your'
    * 'ima' as a contraction of 'I will'
    * 'been' replaces 'have been': "I been dancing"
    * Verbs often don't have second-person forms. i.e. 'He needs' is simply 'he need'

### Chicano
Again, there is a lot of overlap in features that tend to show up in writing (we haven't seen many examples of phonological variation in the data). Semantic and morphological variation is hard to find without context because it mainly means that we may interpret the meaning incorrectly but have no way of knowing just from the isolated utterance. So mainly we are relying on syntactic and lexical features from [this article](https://www.pdx.edu/multicultural-topics-communication-sciences-disorders/chicano-english):
* Zero Copula
* Using unexpected prepositions
    * One example: 'gonna wait to more evidence'
    * This seems related to
According to the article, there are other features we will be on the lookout for (but that have not been seen in the data so far):
* Topicalization and embedded question inversion
    * Changes in large-scale sentence structure: moving the topic to the end of the sentence, or moving an embedded question to the beginning
    * e.g: 'Where is the library could you tell me?' vs 'Could you tell me where the library is' (this is an example from the article, not from our data)
* Intensifiers:
    * Using 'all' (e.g. 'she was all mad') (although this really just sounds like a California thing to me? Haven't seen it in the data yet either)
* Multiple negation
    * Also implicit 'not' in '... until'
* Changes in past tense:
    * Phonological features can cause the past tense to be pronounced the same as the present tense. Unsure whether this would show up in writing.
    * It is unclear whether we would notice if this did show up in writing, since it would just look like present tense without the context
* Leveling of present tense verbs (third person singular is not different from rest)

## Samples (updated data can be seen [here](https://github.com/Asmhoa/481-dialects/tree/dataset))
### AAVE 
```
1129280224661843968	2019-05-17 06:59:21	1525890858	Staten Island, NY	United States	True	@4_theKidDuncan They not gonna be ready bro	
1129280285659549701	2019-05-17 06:59:35	275146822	Baltimore, MD	United States	True	Agree 100%. Geek fandom need to calm TF down! 🤬😒 #DemThrones #ThronesYall	
1129280286817247233	2019-05-17 06:59:36	927213904794734593	Marlow Heights, MD	United States	True	Oooh you high. Imma catch you up there for those free drinks lol	
1129280287643508736	2019-05-17 06:59:36	201021454	Georgia, USA	United States	True	@TreyTheStoner When I found out they were Christian I was SHOOOOK.	
1129280326801481728	2019-05-17 06:59:45	32939076	New Orleans, LA	United States	True	Ebony got a husband tryna fw Dolla 💀 I’m weak	
1129280403033022465	2019-05-17 07:00:03	3317023604	Louisiana, USA	United States	True	broke boy gone run if he ain’t gettin no money	
1129280495324467201	2019-05-17 07:00:25	987668234	Atlanta, GA	United States	True	Not sure what guys they’ve been around but Ima step out 👞 just like you 👠	
1129280641999212544	2019-05-17 07:01:00	3168896071	Baton Rouge, LA	United States	True	I don’t do get back I just gtf	
1129280657287503872	2019-05-17 07:01:04	210971573	Chicago, IL	United States	True	Lmatfoooo....he hopped around the car like he was frfr saving the day🤣	
1129280651017052160	2019-05-17 07:01:02	1307997668	Starlets Gentlemen's Club	United States	True	Lmaoooo homie is throwing up in the ice bucket #dusse	
1129280662857486338	2019-05-17 07:01:05	2825212823	New Orleans, LA	United States	True	Y’all keep dms just to say ninja shot at y’all..	
1129280686265917440	2019-05-17 07:01:11	18880568	Manhattan, NY	United States	True	she like the cleuuuub but she don’t dance theough	
1129280761360732160	2019-05-17 07:01:29	2331268759	Atlanta, GA	United States	True	Coming back to chatt soon holla at meeee all summer
```

### Chicano
```
1128375563272560641 2019-05-14 19:04:33 165464451   Texas, USA  United States   True    @stephenasmith why you cut Marc Stein off when he was about to give us more goods on KD/Kyrie to Brooklyn.
1128375563733700608 2019-05-14 19:04:33 1393542794  Los Angeles, CA United States   True    WTF?! Gonna wait to more evidence comes out but still this isn’t a good look whatsoever. 🤦🏽<200d>♂️
1128375580339183618 2019-05-14 19:04:37 3168091021  Pasadena, TX    United States   True    Lol what you worried for ?
1128375582062833664 2019-05-14 19:04:37 986482435314532353  Los Angeles, CA United States   True    My IG is on private ... it’s not getting deleted this time .... FAWK THAT
1128375587729358848 2019-05-14 19:04:38 2330654514  Inglewood, CA   United States   True    You shouldn’t even wanna let everybody know ya business on social 🤦🏽<200d>♂️
1128375604590596097 2019-05-14 19:04:42 499381524   Homestead, FL   United States   True    Wow my niece have a boyfriend and she only like 13/14 🤨
1128375607895707649 2019-05-14 19:04:43 3300465327  Houston, TX United States   True    This court place getting a one star review on YELP cause bitches having attitudes here
1128375663931613185 2019-05-14 19:04:57 2881506710  Grand Prairie, TX   United States   True    I was going down the freeway and I see a sign that says unhealthy air quality and I look up and the sky looks insan… https://t.co/vH7N9l1dSZ
1128375718629363712 2019-05-14 19:05:10 1005528644108906496 Illinois, USA   United States   True    Older ladies at call center jobs be messy asf say I’m lying 🤣🤣🤣😹
1128375955704221696 2019-05-14 19:06:06 2988201669  Florida, USA    United States   True    I can’t trust her she too fine
1128376040621895681 2019-05-14 19:06:26 2926782154  Nevada, USA United States   True    Working on it with my daughter!
```
