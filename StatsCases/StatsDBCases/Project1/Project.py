import familiar
#1-Sample Test
from scipy.stats import ttest_1samp
#2-Sample Test
from scipy.stats import ttest_ind
#Chi-Squared
from scipy.stats import chi2_contingency

vein_pack_lifespans = familiar.lifespans(package='vein')
mean_life_expectancy = 71

vein_pack_test = ttest_1samp(vein_pack_lifespans, mean_life_expectancy)

print(vein_pack_test.pvalue, '0.10f')
#This evaluate the fact that if the probability is less than 0.05 in our null hypotesis then the fact that the mean life expectancy is 71 is true (because it proves that make your life longer)
if (vein_pack_test.pvalue < 0.05):
  print("The Vein Pack is Proven To Make You Live Longer")
else:
  print("The Vein Pack Is Probably Good For You Somehow!")

artery_pack_lifespans = familiar.lifespans(package='artery')

# 2-Sample test (Comparison between two datasets)
package_comparison_results = ttest_ind(vein_pack_lifespans, artery_pack_lifespans)
print(package_comparison_results.pvalue)

if (package_comparison_results.pvalue < 0.05):
  print("The Artery Package guarantees even stronger results!")
else:
  print("The Artery Package is also a great product!")

  #------------------------------------------------#
iron_contingency_table = familiar.iron_counts_for_package()

print(iron_contingency_table)
# iron_pvalue is in the second value from Chi-Squared
_, iron_pvalue, _, _ = chi2_contingency(iron_contingency_table)

print(iron_pvalue)
if iron_pvalue < 0.05:
  print("The Artery Package Is Proven To Make You Healthier!")
else:
  print("While We Cant Say The Artery Package Will Help You, I Bet Its Nice!")

