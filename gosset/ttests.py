import numpy as np
from .t import T

class OneSampleT:
    def __init__(self, data, mu_0, alternative='two-sided', alpha=0.05, na_drop=True):

        if na_drop:
            data = data[~np.isnan(data)]
        else:
            if np.any(np.isnan(data)):
                raise ValueError("Missing values in data detected!")

        self.alpha = alpha
        self.run_test()

    def run_test(self):
        self.xbar = np.mean(data)
        self.sd = np.std(data, ddof=1)
        self.n = len(data)
        self.se = self.sd / np.sqrt(self.n)
        self.t = (self.xbar - mu_0) / self.se
        self.df = self.n - 1
        self.distn = T(df=self.df)

        if alternative == 'two-sided':
            self.pvalue = 2*self.distn.cdf(-np.abs(self.t))
        elif alternative == 'less':
            self.pvalue = self.distn.cdf(self.t)
        elif alternative == 'greater':
            self.pvalue = 1 - self.distn.cdf(self.t)
        else:
            raise ValueError("Valid alternative values: 'two-sided', 'less', or 'greater'")

        self.reject = True if self.pvalue < alpha else False

