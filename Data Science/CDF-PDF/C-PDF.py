import numpy 
from scipy.stats import norm

numbers = norm.rvs(loc=0, scale=1, size=20)

cdf= norm.cdf(10, loc=1, scale=3)

print(cdf)

pdf = norm.pdf(14, loc=1, scale=1)

print(pdf)


