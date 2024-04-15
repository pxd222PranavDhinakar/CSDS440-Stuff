from scipy.stats import binom

# number of classifiers
n = 100

# good and bad error rate
er_g = 0.3
er_b = 0.6

# range for k
range_k = []

# majority vote
m_v = (n // 2) + 1


for k in range(0, n + 1):
    m = n - k
    p_correct = 0
    for i in range(m_v, n + 1):
        # probability that good classifiers are correct
        p_g_correct = binom.pmf(i, k, 1 - er_g)
        # probability that the remaining bad classifiers are correct
        p_b_correct = binom.pmf(n - i, m, 1 - er_b)
        # joint probability
        p_correct += p_g_correct * p_b_correct
    
    # Check for normal chance
    if p_correct > 0.5:
        range_k.append(k)

# Return the range
print(range_k)
