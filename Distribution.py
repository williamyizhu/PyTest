import pandas as pd
import numpy as np
from scipy.stats import norm
from scipy.stats import lognorm
import matplotlib.pyplot as plt

# ----------------------------- scipy.stats.normal -----------------------------
# The location (loc) keyword specifies the mean. The scale (scale) keyword specifies the standard deviation.

# Calculate a few first moments:
mean, var, skew, kurt = norm.stats(moments='mvsk')

# Display the probability density function (pdf):
x = np.linspace(norm.ppf(0.01), norm.ppf(0.99), 100)

fig, ax = plt.subplots(1, 1)
ax.plot(x, norm.pdf(x), 'r-', lw=5, alpha=0.6, label='norm pdf')

# from scipy.stats.mstats import mquantiles
# mquantiles(x)

# Freeze the distribution and display the frozen pdf:
rv = norm()
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')

# Check accuracy of cdf and ppf:
vals = norm.ppf([0.001, 0.5, 0.999])
np.allclose([0.001, 0.5, 0.999], norm.cdf(vals))

# Generate random numbers:
r = norm.rvs(size=1000, loc=10, scale=1)

# And compare the histogram:
ax.hist(r, normed=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show()

# ----- example -----
fig, ax = plt.subplots(1, 1)
mean = 2750
sigma = 2750 * (0.4)**2
rv = norm(loc=mean, scale=sigma)
x = np.linspace(mean-3*sigma, mean+3*sigma, 1000)
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')

# ----------------------------- scipy.stats.lognormal -----------------------------
# lognorm takes s as a shape parameter.
# The probability density above is defined in the ¡°standardized¡± form. 
# To shift and/or scale the distribution use the loc and scale parameters. 
# Specifically, lognorm.pdf(x, s, loc, scale) is identically equivalent to lognorm.pdf(y, s) / scale with y = (x - loc) / scale.
# If log(x) is normally distributed with mean mu and variance sigma**2, 
# then x is log-normally distributed with shape parameter sigma and scale parameter exp(mu).

s = 0.954
mean, var, skew, kurt = lognorm.stats(s, moments='mvsk')
x = np.linspace(lognorm.ppf(0.01, s), lognorm.ppf(0.99, s), 100)

fig, ax = plt.subplots(1, 1)
ax.plot(x, lognorm.pdf(x, s), 'r-', lw=5, alpha=0.6, label='lognorm pdf')

# Freeze the distribution and display the frozen pdf:
rv = lognorm(s)
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')

# Check accuracy of cdf and ppf:
vals = lognorm.ppf([0.001, 0.5, 0.999], s)
np.allclose([0.001, 0.5, 0.999], lognorm.cdf(vals, s))

# Generate random numbers:
r = lognorm.rvs(s, size=1000)

# And compare the histogram:
ax.hist(r, normed=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show()

# ----------------------------- numpy.lognormal -----------------------------
# mean and standard deviation
mu = 3.0
sigma = 1.0

# generate random number
s = np.random.lognormal(mu, sigma, 1000)

# hist plot and line plot
count, bins, ignored = plt.hist(s, 100, normed=True, align='mid')
x = np.linspace(min(bins), max(bins), 10000)
pdf = np.exp(-(np.log(x) - mu)**2 / (2 * sigma**2)) / (x * sigma * np.sqrt(2 * np.pi))

plt.plot(x, pdf, linewidth=2, color='r')
plt.axis('tight')
plt.grid()
plt.show()

# ----- log of samples from lognormal distribution follows normal distribution -----
log_s = np.log(s)

# hist plot and line plot
count, bins, ignored = plt.hist(log_s, 100, normed=True, align='mid')
x = np.linspace(min(bins), max(bins), 10000)
pdf = 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp( - (x - mu)**2 / (2 * sigma**2))

plt.plot(x, pdf, linewidth=2, color='r')
plt.axis('tight')
plt.grid()
plt.show()                    

# Demonstrate that taking the products of random samples from a uniform distribution can be fit well by a log-normal probability density function.
# Generate a thousand samples: each is the product of 100 random
# values, drawn from a normal distribution.
b = []
for i in range(1000):
    a = 10. + np.random.random(100)
    b.append(np.product(a))

# scale values to be positive
b = np.array(b) / np.min(b) 
count, bins, ignored = plt.hist(b, 100, normed=True, align='mid')

# calculate mu and sigma of b
sigma = np.std(np.log(b))
mu = np.mean(np.log(b))
x = np.linspace(min(bins), max(bins), 10000)

pdf = (np.exp(-(np.log(x) - mu)**2 / (2 * sigma**2)) / (x * sigma * np.sqrt(2 * np.pi)))
plt.plot(x, pdf, color='r', linewidth=2)
plt.show()

# ----------------------------- numpy.normal -----------------------------
# Draw samples from the distribution:
# mean and standard deviation
mu = 0
sigma = 0.1 
s = np.random.normal(mu, sigma, 1000)

# Verify the mean and the variance:
abs(mu - np.mean(s)) < 0.01
abs(sigma - np.std(s, ddof=1)) < 0.01

# Display the histogram of the samples, along with the probability density function:
count, bins, ignored = plt.hist(s, 30, normed=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ), linewidth=2, color='r')
plt.show()

