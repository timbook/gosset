class RandomVariable:
    def cdf(self, *args, **kwargs):
        return self._rv.cdf(*args, **kwargs)

    def quantile(self, *args, **kwargs):
        return self._rv.ppf(*args, **kwargs)

    def sample(self, *args, **kwargs):
        return self._rv.rvs(*args, **kwargs)

    def prob_between(self, a, b):
        return self.cdf(max(a, b)) - self.cdf(min(a, b))

    @property
    def mean(self):
        return self._rv.mean()

    @property
    def var(self):
        return self._rv.var()

    @property
    def std(self):
        return self._rv.std()

    @property
    def median(self):
        return self._rv.median()

class ContinuousRV(RandomVariable):
    def pdf(self, *args, **kwargs):
        return self._rv.pdf(*args, **kwargs)
    
class DiscreteRV(RandomVariable):
    def pmf(self, *args, **kwargs):
        return self._rv.pmf(*args, **kwargs)
