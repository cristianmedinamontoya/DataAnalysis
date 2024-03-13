import numpy as np
import fetchmaker
import pandas as pd
#1-Sample test
from scipy.stats import binom_test
#ANOVA
from scipy.stats import f_oneway
#Pairwise-tukey - Checking which pairs differ
from statsmodels.stats.multicomp import pairwise_tukeyhsd

#Chi Square
from scipy.stats import chi2_contingency


df = pd.read_csv('dog_data.csv')
print(df.head(5))
rottweiler_tl = fetchmaker.get_tail_length("rottweiler")
# print(rottweiler_tl.head(5))
# print('\n')
print(np.mean(rottweiler_tl))
print(np.std(rottweiler_tl))
# print('\n')
whippet_rescue = fetchmaker.get_is_rescue("whippet")
# print(whippet_rescue)
num_whippet_rescues = np.count_nonzero(whippet_rescue)
# print(num_whippet_rescues)

num_whippets = np.size(whippet_rescue)
# print(num_whippets)
#For the binom_test we use two-sided test: num_whippet = the number of true/counted rescues, num_whippets = the total of whippet database(trials), and the 8% from the expected percentage of probability
print(binom_test(num_whippet_rescues, num_whippets, 0.08))
#The result of 0.58 = 58% is not a strong figure to tell to make a conclusion. If it was below 5% then we could say that whippet adoption rates are significantly different. We could interpret the result as: the whippet adoption rate and mean adoption rates  is just random chance

#To create a table of comparison of datasets according to one type of parameter:get_weight we first have to separate the information from the DB of each type of breed.
w = fetchmaker.get_weight('whippet')
t = fetchmaker.get_weight('terrier')
p = fetchmaker.get_weight('pitbull')
print(f_oneway(w, t, p).pvalue)

#After that its necessary to create a new list of values in a combined array of the previously searched weight values. 
values = np.concatenate([w, t, p])
#Then we may create the labels according to the length of each category's values. Thus thats the reason why we create a label and multiplied it by its array lenght. 
labels = ['whippet'] * len(w) + ['terrier'] * len(t) + ['pitbull'] * len(p)
#We use values and labels as input parameters with a p = 5% to test the null hypotesis.
print(pairwise_tukeyhsd(values, labels, 0.05)) 
#The result table indicates that if we got a True results, then we said that there a significant difference between the evaluated groups. In case we got a False result we may say that the compared groups are not so different. 

#Chi Square - We are evaluating multiple labels for two categories
poodle_colors = fetchmaker.get_color('poodle')
shihtzu_colors = fetchmaker.get_color('shihtzu')

color_table = [
    [np.count_nonzero(poodle_colors == 'black'),np.count_nonzero(shihtzu_colors == 'black')],
    [np.count_nonzero(poodle_colors == 'brown'),np.count_nonzero(shihtzu_colors == 'brown')],
    [np.count_nonzero(poodle_colors == 'gold'),np.count_nonzero(shihtzu_colors == 'gold')],
    [np.count_nonzero(poodle_colors == 'grey'),np.count_nonzero(shihtzu_colors == 'grey')],
    [np.count_nonzero(poodle_colors == 'white'),np.count_nonzero(shihtzu_colors == 'white')]
]
print(color_table)

_, color_pval, _, _ = chi2_contingency(color_table)

print(color_pval)
# Results = 0.00530240829324 bc is less than 0.05, there a difference between poodle colors and shihtzu colors.
