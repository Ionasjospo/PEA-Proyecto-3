from scipy.stats import binom
from scipy.stats import geom
from scipy.stats import poisson

def binomial_distribution(n,p):
    return binom.rvs(n,p,size = 1000)

def geometric_distribution(p):
    return geom.rvs(p,size = 1000)

def poisson_distribution(L):
    return poisson.rvs(L,size = 1000)
