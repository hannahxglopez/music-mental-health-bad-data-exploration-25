# Hypothesis Testing

## Description

Data on how listening to music correlates with mental health. 
Dataset includes: time, hours per day, survey respondent demographics,
self-reported mental health, and frequency of genres. 

## Data Source(s)

* [Kaggle](https://www.kaggle.com/datasets/catherinerasgaitis/mxmh-survey-results?resource=download)


## Hypothesis

I hypothesize that for those respondents who listened between 3-7 hours of music per day, the level of 
anxiety (0 - 10 scale) of survey respondents who play instrument(s) (Group A) is less than (direction) 
the anxiety level (0 - 10 scale) of survey respondents who don't play instruments (Group B).

I believe this will be the case because musicians typically seem to enjoy music more because of their
familiarity with it is typically greater than it is with regular people, and therefore it might feel 
more relaxing for them to listen to music.

## Dependent Variable

* anxiety level (0 - 10 scale)

## Independent Variable(s)

* if they play a(n) instrument(s)

## Controlled Variable(s)

* only respondents who listened between 3-7 hours of music per day
* only respondents between the ages of 10 and 85


## Uncontrolled Variable(s)

* the people who responded to the survey
* trauma incidents per person and their home life
* if the person was forced to learn an instrument or not

## Planned t-Test

* One-tailed or two-tailed: one-tailed, because I'm hoping musician anxiety (while listening to music) < non-musician anxiety (while listening to music)

* Independent or paired samples: independent

## Results

I ran the normality tests and observed the following:
Test 1: musicians: p=0.0005238052
Test 2: musicians: p=0.0000056246
Test 1: non-musicians: p=0.0000041726
Test 2: non-musicians: p=0.0000000352

The p-values were so low, that I concluded my data was not normally distributed and the 
samples were independent (unpaired); so, I used ss.mannwhitneyu().

Here are the results of my t-test:
mann-whitney U test for musician anxiety < non musician anxiety: p=0.9147186241

So, the probability of musician and non-musician anxieties being from the same distribution
was about 91%, which is way above 5%, so I cannot reject the null hypothesis, 
and furthermore, I cannot accept my alternative hypothesis that
musician anxiety < non musician anxiety
i.e., My hypothesis was wrong
