import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as ss

data = pd.read_csv("../hypothesis-testing/mxmh_survey_results.csv")
# na_values={'mass(g)':'0'}

# Use only age > 9 (there are missing/invalid ages)
data = data[data['Age'] > 9]
data = data[data['Age'] < 86]

# Use only data with listening 3-7 hours
data = data[data['Hours per day'] > 2]
data = data[data['Hours per day'] < 8]

# Get musicians, and then get just their anxiety levels
musicians = data[data['Instrumentalist'] == 'Yes']
musician_anxiety = musicians['Anxiety']

# Get non-musicians
non_musicians = data[data['Instrumentalist'] == 'No']
non_musician_anxiety = non_musicians['Anxiety']

# plot histogram of musicians and their anxiety levels

# first, compute the mean mass of this group
musician_mean_anxiety = musician_anxiety.mean()
print(f'Musician mean anxiety: {musician_mean_anxiety:.2f}')

plt.figure()
plt.hist(musician_anxiety, label='anxiety level')
plt.axvline(musician_mean_anxiety, c='red', label='mean') # plot a vertical line at the mean
plt.xlabel('Anxiety Level')
plt.ylabel('Count')
plt.title('Musician Anxiety Level')
plt.legend() # add a legend that uses the 'label' of each plotted thing
plt.savefig('hist1.pdf')

# plot histogram of nonmusicians and their anxiety levels

# first, compute the mean mass of this group
non_musician_mean_anxiety = non_musician_anxiety.mean()
print(f'Non-musician mean anxiety: {non_musician_mean_anxiety:.2f}')

plt.figure()
plt.hist(non_musician_anxiety, label='anxiety level')
plt.axvline(non_musician_mean_anxiety, c='red', label='mean') # plot a vertical line at the mean
plt.xlabel('Anxiety Level')
plt.ylabel('Count')
plt.title('Non-Musician Anxiety Level')
plt.legend() # add a legend that uses the 'label' of each plotted thing
plt.savefig('hist2.pdf')

# run tests to verify the normality of each group

# test 1: for musicians:
_, musician_pvalue = ss.normaltest(musician_anxiety)
print(f'Test 1: musicians: p={musician_pvalue:.10f}')
# it is less than 0.05, meaning that it is very unlikely to be normally distributed

# test 2: for musicians
_, musician_pvalue = ss.shapiro(musician_anxiety)
print(f'Test 2: musicians: p={musician_pvalue:.10f}')
# also less than 0.05, meaning that it is very unlikely to be normally distributed

# test 1: for nonmusicians:
_, non_musician_pvalue = ss.normaltest(non_musician_anxiety)
print(f'Test 1: non-musicians: p={non_musician_pvalue:.10f}')
# it is less than 0.05, meaning that it is very unlikely to be normally distributed

# test 2: for musicians
_, non_musician_pvalue = ss.shapiro(non_musician_anxiety)
print(f'Test 2: non-musicians: p={non_musician_pvalue:.10f}')
# also less than 0.05, meaning that it is very unlikely to be normally distributed

# if data is normally distributed:
#	 if samples are paired
#		 use ss.ttest_rel()
#	 else not paired (i.e,. samples are independent):
#		 use ss.ttest_ind()
# else not normally distributed
#	 if samples are paired
#		 use ss.wilcoxon()
#	 else not paired (i.e,. samples are independent):
#	 	 use ss.mannwhitneyu()

# my data is not normally distributed and samples are independent (unpaired);
# so, I will use ss.mannwhitneyu()
# and I will also be very careful to pass the correct parameters in the correct order
# hypothesis: musician anxiety < non musician anxiety
# so, pass in muscian anxiety, then non musician anxiety, then "less"
_, p = ss.mannwhitneyu(musician_anxiety, non_musician_anxiety, alternative='less')
print(f'mann-whitney U test for musician anxiety < non musician anxiety: p={p:.10f}')

# for any of the t-tests, if p <= 0.05, then the probability of the
# two groups of data being from the same underlying distribution is very low,
# therefore we can reject the null hypothesis that they are from the same distribution,
# and accept our alternative hypothesis that they are from different distribution

# in my example, here was my mannwhitneyu test's p-value:
# mann-whitney U test for musician anxiety < non musician anxiety: p=0.9147186241

# so, the probability of musician and non-musician anxieties being from the same distribution
# was about 91%, which is way above 5%, so I cannot reject the null hypothesis,
# and furthermore, I cannot accept my alternative hypothesis that
# musician anxiety < non musician anxiety
# i.e., I was wrong
