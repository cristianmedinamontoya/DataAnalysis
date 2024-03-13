def reject_null_hypothesis(p_value):
  """
  Returns the truthiness of whether the null hypothesis can be rejected

  Takes a p-value as its input and assumes p <= 0.05 is significant
  """
  return p_value <= 0.05

hypothesis_tests = [0.1, 0.009, 0.051, 0.012, 0.37, 0.6, 0.11, 0.025, 0.0499, 0.0001]

for p_value in hypothesis_tests:
    reject_null_hypothesis(p_value)
