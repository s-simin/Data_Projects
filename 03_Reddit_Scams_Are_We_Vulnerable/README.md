<img src="http://imgur.com/1ZcRyrc.png" style="float: left; margin: 20px; height: 55px">

# DSI-SG-42 Project 3: Web APIs & NLP

### Reddit Scams: Are We Vulnerable?

---

## Introduction

With a concerning surge in scams cases, recent statistics reveal a staggering increase of 50% in reported cases, from 27,000 cases in 2022 to 43,000 cases in 2023 (*source: The Straits Times, Feb 2024*). This underscores the pressing need for proactive measures to counter fraudulent activities happening within online communities. We believe that there is more to be done, and it is essential to empower Reddit moderators as the primary defense line because they are instrumental in identifying and eliminating potentially harmful content.

In this project, our primary aim is to construct a robust classification model that can accurately discern the origin of posts from two distinct subreddits: r/RandomKindness and r/Scams. The overarching objective is to empower subreddit moderators with a proactive tool to enhance their efficacy in identifying and mitigating potential scam posts within their respective communities.

## Problem Statement

*How Might We Assist Reddit Moderators to Differentiate Online Scams from Legitimate Acts of Kindness within Reddit Posts using a Sensitive & Accurate Natural Language Processing Model*

## Datasets

### Data Collection

Our raw data come from the following two subreddits:

1. r/RandomKindness:

r/RandomKindness is a subreddit where users engage in random acts of kindness by offering assistance, support, or gifts to others without expecting anything in return. Members share heartwarming stories, request help with various needs, and fulfill the requests of fellow community members

2. r/Scams

r/Scams is a subreddit dedicated to raising awareness about various scams and fraudulent activities on the internet. Members share their experiences, warnings, and advice to help others recognize and avoid falling victim to scams.

### Data Dictionary

The data dictionary displays the key columns used for this project:

| Column                                 | Data Type | Dataset              | Description                                                           |
|----------------------------------------|-----------|----------------------|-----------------------------------------------------------------------|
| subreddit                              | Object    | reddit_scrapped_data | The subreddit it belongs to: r/RandomKindness, r/Scams                |
| type                                   | Object    | reddit_scrapped_data | Type of entry: title, body, comment, reply                  |
| text                                   | Object    | reddit_scrapped_data | Text content                                                          |
| id                                     | Object    | reddit_scrapped_data | Unique identifier for the post                                        |
| url                                    | Object    | reddit_scrapped_data | URL of the post                                                       |
| cleaned_text                           | Object    | cleaned_data         | Text content after removal of repetitive words and special characters |
| label                                  | Integer   | cleaned_data         | 0: r/RandomKindness, 1: r/Scams                                       |
| removed_customised_stopwords_stems_str | Object    | rk_sc_final          | Text content after removal of stop words and stemming                 |

## Workflow Process

1. **Web Scraping**

With the help of The Python Reddit API Wrapper (PRAW), we extracted data from the two above-mentioned subreddits.

2. **Data Cleaning**

After we collected the raw data in text form, we cleaned the data according to the following steps:

- Remove duplicates
- Check for null values
- Remove auto-generated bot texts
- Use regex to remove the following:
  - Repetitive words like [Request] or [Offer] commonly used in r/RandomKindness
  - URLs
  - /r which make references to a subreddit
  - Special characters like emoji and punctuations

3. **Exploratory Data Analysis**

We explored the distribution of the following with the help of visualisations:

* Word count and character count
* Posts and comments/ replies

We also identified outliers and documented how we handled them.

4. **Pre-Processing**

We ran n-gram analysis (namely unigram, bigram and trigram) on the cleaned text, followed by tokenizing the text. In addition to removing standard stop words, we also identified customised stop words to remove. After exploring both options of stemming and lemmatization, we eventually decided on stemming based on the end-goal metric that we wanted to optimize.

5. **Modeling**

With the cleaned and processed data, we ran two models (Naive Bayes and Logistic Regression) using two different vectorizers (Count Vectorizer and TF-IDF).

## Conclusion

From the training and testing scores of our baseline models, we identified Multinomial Naive Bayes using TF-IDF as the best scoring model. We performed hypertuning on this model to obtain its best parameters. As a result, we achieved an high accuracy of 0.975 and sensitivity of 0.964.

## Limitations
1. Model to be further trained on other types of text-based data
  - Other commonly-used Forums (e.g. HardwareZone, askSingapore)
  - Social Media
  - Instant Messaging

2. Vernacular terms commonly used in Singapore was not used (e.g. PayNow, PayLah, Singlish terms)

## Recommendations
With the success of our classification model, we have several recommendations:

1. The model can be seamlessly integrated into
 existing moderation tools, featuring functionalities that highlight posts classified as either "Potential Scam" or "Potential Random Kindness," aiding moderators in efficiently identifying and addressing potentially harmful content.

2. A feedback loop could be established, allowing moderators to provide feedback on the accuracy of both scam and kindness classifications—whether correct or incorrect—thus enabling continuous improvement of the model's accuracy and sensitivity in identifying both positive and negative content.

3. To adapt to the evolving landscape of scam tactics, the model will undergo continual retraining with new data. This ensures its capability to recognize future scam baits while accurately identifying genuine acts of kindness, thereby maintaining effectiveness in content moderation.

4. Users will be provided with a Transparency Notice, informing them about the utilization of a NLP model to detect scams and random acts of kindness. This transparency fosters trust and empowers users to contribute to a safer and more positive online environment by engaging with the moderation process.







