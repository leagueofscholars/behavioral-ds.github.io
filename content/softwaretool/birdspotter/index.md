---
title: "birdspotter: A toolkit for analyzing and labelling Twitter users"
authors:
  - Rohit Ram
date: "2021-03-09"
output: html_document
tags: [python]
categories: [package]

links:
- icon: github-alt
  icon_pack: fab
  name: Code
  url: https://github.com/behavioral-ds/birdspotter
---

<img src="/img/birdspotter_logo.png" alt="Birdspotter Logo" width="200"/>


<!-- Motivation -->

<!-- Framing: Problem -> Solution -->
<!-- Context -->
Social media platforms, although relatively new, host millions of users and billions of interactions daily. As tied as we are to these platforms, they profoundly impact our social institutions through phenomena such as disinformation, political polarization, and social bots. 

<!-- Problem  -->
Researchers are increasingly interested in trying to form an understanding of phenomena and their implications. Social scientists, political scientists, and data practitioners alike curate expansive datasets to combat these potentially adverse effects on our society; however, they lack the appropriate tooling.

<!-- Solution -->
`birdspotter` is an **easy-to-use** tool that models Twitter users' attributes and labels them. It comes prepackaged with a **state-of-the-art bot detector** and an **influence quantification** system based on tweet dynamics. `birdspotter` features a generalized user labeler, which can be retrained easily with the engineered features to address a variety of use cases. Also, [birdspotter.ml](http://birdspotter.ml/) is a web application that can be utilized to explore datasets and derive a narrative around a dataset.

In this post, I'll showcase the basic usage of `birdspotter` and [birdspotter.ml](http://birdspotter.ml/).

## Installation

The package can be installed in the canonical python way:
```{bash}
pip install birdspotter
```

## Getting a dataset
The Twitter T&Cs restrict the sharing of tweet data directly online; however, they do allow the sharing of tweet-ids, which can be converted to full tweet data through a process called *hydration*. Tools like [twarc](https://github.com/DocNow/twarc) can be used to hydrate a Tweet ID dataset. The resulting dataset will be in `jsonl` (line delimited `json`) format, which `birdspotter` accepts directly. 


In the below examples, we use two datasets; a collection of COVID-19 related tweets from January 31st, 2020 [1], and a collection of tweets about politicians on Twitter [2].

The politicians' dataset was acquired through the following process (and a similar process was taken for the COVID-19 dataset):
```{bash}
pip install twarc
wget http://twitterpoliticians.org./downloads/base/all_tweet_ids.csv
twarc hydrate all_tweet_ids.csv > tweets.jsonl
```

## Basic Usage

The code below imports the main class `Birdspotter`, extracts the tweets from their standard format, labels the users with the default bot detector and influence, and reformats the retweet cascades into a tidier format.

```{python}
## Import birdspotter
from birdspotter import BirdSpotter 

## Extracts the tweets from the raw jsonl [https://github.com/echen102/COVID-19-TweetIDs]
bs = BirdSpotter('covid19.jsonl') 

## Uses the default bot labeller and influence quantification systems
bs.getLabeledUsers() 

## Formats the retweet cascades, such that expected retweet structures can extracted
bs.getCascadesDataFrame() 

## Access the botness labels and influence scores
bs.featureDataframe[['botness', 'influence']]
```

From here, the dataset is readily profile-able:
```{python}
botness_dist = sns.histplot(data=bs.featureDataframe, x="botness")
influence_eccdf = sns.ecdfplot(data=bs.featureDataframe, x="influence", complementary=True).set(xscale="log", yscale="log")
```

![**COVID Dataset Profile**: (Left) The distribution of bot scores of users; (Right) The ECCDF of influence scores of users, showing a long-tailed (rich-gets-richer) paradigm](/img/covid_profile.png)

## The visualizer
An alternative way to profile a dataset is the use [`birdspotter.ml`](http://birdspotter.ml), which facilitates dataset exploration and narrative construction. 

![**birdspotter.ml visualizer**: The various components shown include the scatterplot panel (Left), the user information panel (Top Right), and the retweet cascades panel (Bottom Right)](/img/auspol_teaser.png)

The visualizer features a scatterplot (on the left) of influence and botness for a sample of users and the population density. The colors represent the hashtags (a proxy for the topic) that the users most tweet about in the dataset. Users within the scatterplot are hoverable and selectable, and their information populates in the components on the right.

The top right component shows information and metrics about the selected user and links the user's profile. 

The bottom right component shows the retweet cascades where a user has participated and highlights their participation. The points represent the follower counts (social capital) of users and their retweets/tweets' timing. The points are also hoverable and selectable.  

## Customising the labeller
By default, the labeler is trained as a bot detection system, comparable to the state-of-the-art [`botometer`](https://botometer.osome.iu.edu/). Notable, `birdspotter` is provided in an offline package and can be applied at scale, while `botometer` is accessible only via an online API, which is often prohibitively rate-limited.

`birdspotter` is a versatile tool and can be utilized by practitioners for a variety of use-cases. For example, we could train the labeler to identify political leaning. This process is a bit involved, so we summarise it below;
1. We hydrate some tweets from the Twitter Parlimentarian Database
2. We filter the tweets to include only **Australian Politicians**.
3. We **label right-wing partied politicians positively**, and others negatively (with `bs_pol.getBotAnnotationTemplate` for example)
4. We **retrain `birdspotter`** with these new labels and label all users (i.e., including users the politicians retweeted) using the new model

<!-- ```{python class.source = 'fold-hide'} -->
<!-- # This is the guts of the code; it does what is described above -->
<!-- politicians = pd.read_csv('./full_member_info.csv', encoding='utf16') -->
<!-- politicians_aus = politicians[politicians['country'] == 'Australia'] -->
<!-- politicians_aus_available = politicians_aus[~politicians_aus['uid'].isnull()] -->

<!-- def classify_party(party_id): -->
<!--     mapping = { -->
<!--         464 : 1, # Liberal Party of Australia -->
<!--         465 : -1, # Australian Labor Party -->
<!--         467 : 1, # The Nationals -->
<!--         468 : 0, # Nick Xenophon Team -->
<!--         469 : -1, # Australian Greens -->
<!--         471 : np.nan, -->
<!--         475 : 1, # Katter's Australian Party -->
<!--     } -->
<!--     return mapping[party_id] -->

<!-- politicians_aus_available['isright'] = politicians_aus_available['party_id'].apply(classify_party) -->
<!-- politicians_aus_available['user_id'] = politicians_aus_available['uid'].astype(int).astype(str) -->
<!-- politicians_aus_available = politicians_aus_available.set_index('user_id') -->

<!-- with open('./tweets.jsonl', 'r') as rf, open('./aus_tweets.jsonl', 'w') as wf: -->
<!--     for line in tqdm(rf): -->
<!--         try: -->
<!--             j = json.loads(line) -->
<!--             if j['user']['id_str'] in politicians_aus_available['uid'].astype(int).astype(str).values: -->
<!--                 wf.write(json.dumps(j) + '\n') -->
<!--         except Exception as e: -->
<!--             print(j) -->
<!--             print(e) -->
<!--             break -->

<!-- bs = BirdSpotter('aus_tweets.jsonl') -->
<!-- bs.getLabeledUsers() -->
<!-- bs.getCascadesDataFrame() -->

<!-- with open('bs_aus_module.pk', 'wb') as wf: -->
<!--     pk.dump(bs,wf, protocol=4) -->

<!-- bs.featureDataframe['isright'] = politicians_aus_available['isright'] -->

<!-- ground_truth = bs.featureDataframe[~bs.featureDataframe['isright'].isnull()][['isright']] -->
<!-- ground_truth['isbot'] = ground_truth['isright'] == 1 -->
<!-- ground_truth = ground_truth[~ground_truth.index.duplicated()] -->

<!-- data = bs.featureDataframe.copy()[bs.featureDataframe.index.isin(ground_truth.index)] -->
<!-- data = data[~data.index.duplicated()] -->
<!-- del data['isright'] -->
<!-- del data['botness'] -->
<!-- del data['influence'] -->
<!-- del data['cascade_membership'] -->
<!-- data = data[list(data.columns[data.dtypes != 'object'])] -->
<!-- data['isbot'] = ground_truth['isbot'].loc[data.index] -->

<!-- with open('pol_training_data.pickle', 'wb') as wf: -->
<!--         pk.dump(data,wf, protocol=4) -->

<!-- from birdspotter import BirdSpotter -->
<!-- import pickle as pk -->

<!-- # bs_pol = BirdSpotter('aus_tweets.jsonl') -->

<!-- with open('bs_aus_module.pk', 'rb') as rf: -->
<!--     bs_pol = pk.load(rf) -->
<!-- print("Loaded module") -->
<!-- bs_pol.trainClassifierModel('pol_training_data.pickle') -->
<!-- print("finished training") -->
<!-- del bs_pol.featureDataframe['botness'] -->
<!-- print("removed botness column") -->
<!-- bs_pol.getBotness() -->
<!-- bs_pol.getLabeledUsers() -->
<!-- print("got labels") -->

<!-- with open('pol_booster.pickle', 'wb') as wf: -->
<!--     pk.dump(bs_pol.booster, wf, protocol=4) -->
<!-- print("pickled booster") -->
<!-- with open('aus_pol_bs_module.pickle', 'wb') as wf: -->
<!--     pk.dump(bs_pol, wf, protocol=4) -->

<!-- with open('pol_booster.pickle', 'wb') as wf: -->
<!--         pk.dump(bs.booster, wf, protocol=4) -->
<!-- ``` -->



<!-- This is context: -->
<!-- I want to start with the opportunity namely the analysis of large amounts of population data tranparently showing the interactions and discourse of people, allowing practictioners to model important applications in society. I also want to highlight the research issues which require investigation, namely social bots, misinformation, polarization, etc. -->

<!-- This is content -->
<!-- I then want to move into the problem, namely that there is a lack of tooling to analyse these huge swaths of data -->

```{python}
bs_pol = BirdSpotter('aus_tweets.jsonl')
bs_pol.trainClassifierModel('pol_training_data.pickle')
bs_pol.getLabeledUsers()
```

On this limited of Australian politicians dataset, a 10-fold CV of `birdspotter` garners an average AUC (Area under ROC) of 0.986.

## Conclusion
`birdspotter` aims to democratize social analyzes that were once the domain of machine learning experts, generating insights and understanding of online phenomena and mitigating their potentially adverse effects on our society. This post shows how `birdspotter` can be used in both a simple and advanced way to recover such insights. 

## References
[1] Chen, E. et al. 2020. Tracking social media discourse about the covid-19 pandemic: Development of a public coronavirus twitter data set. JMIR Public Health and Surveillance. 6, 2 (2020), e19273.

[2] Vliet, L. van et al. 2020. The twitter parliamentarian database: Analyzing twitter politics across 26 countries. PloS one. 15, 9 (2020), e0237073.

