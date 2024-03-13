# def reject_null_hypothesis(p_value):
#   """
#   Returns the truthiness of whether the null hypothesis can be rejected

#   Takes a p-value as its input and assumes p <= 0.05 is significant
#   """
#   return p_value <= 0.05

# hypothesis_tests = [0.1, 0.009, 0.051, 0.012, 0.37, 0.6, 0.11, 0.025, 0.0499, 0.0001]

# for p_value in hypothesis_tests:
#     reject_null_hypothesis(p_value)
# possible_p_values = [0.1, 0.009, 0.051, 0.012, 0.37, 0.6, 0.11, 0.025, 0.0499, 0.0001]

# def real_reject_null_hypothesis(p_value):
#   return p_value <= 0.05

# for p_val in possible_p_values:
#   learner_answer = reject_null_hypothesis(p_val)
#   real_answer = real_reject_null_hypothesis(p_val)

#   if learner_answer != real_answer:
#     fail_tests("P-Value {val} is {is_sig}, but `reject_null_hypothesis(p_value)` returned {return_val} (instead of {real_val})".format(
#         val=p_val,
#         is_sig="significant" if real_answer else "not significant",
#         return_val=learner_answer,
#         real_val=real_answer))
# pass_tests()


