import numpy as np
from .hyptest import HypothesisTest
from ..rvs.normal import StandardNormal

class OneSampleZ(HypothesisTest):
    def __init__(self, data, sigma=1, mu0=0, alternative='two-sided', alpha=0.05):
        self.mu0 = mu0
        self.sigma = sigma
        self.alpha = alpha
        self.alternative = alternative
        self._stat_sym = 'z'
        self.startup(data)

    def _run_test(self, data):
        self.n = len(data)
        self.xbar = np.mean(data)
        self.sd = self.sigma
        self.se = self.sd / np.sqrt(self.n)
        self.distn = StandardNormal()
        self.null_stat = self.z0 = self.distn.quantile(1 - self.alpha/2)
        self.stat = self.z = (self.xbar - self.mu0) / self.se

        if self.alternative in ['two-sided', 'ne', '!=']:
            self.pvalue = 2*self.distn.cdf(-np.abs(self.t))
            self.alt_sym = '\\ne'
        elif self.alternative in ['less', 'lt', '<']:
            self.pvalue = self.distn.cdf(self.t)
            self.alt_sym = '<'
        elif self.alternative in ['greater', 'gt', '>']:
            self.pvalue = 1 - self.distn.cdf(self.t)
            self.alt_sym = '>'
        else:
            raise ValueError("Valid alternative values: 'two-sided', 'less', or 'greater'")

        self.text_h0 = f"\mu = {self.mu0}"
        self.text_ha = f"\mu {self.alt_sym} {self.mu0}"

class OneSampleZFromStats(HypothesisTest):
    def __init__(self, xbar, sigma, n, mu0=0, alternative='two-sided', alpha=0.05):
        self.mu0 = mu0
        self.alpha = alpha
        self.alternative = alternative
        self._stat_sym = 'z'

        self.xbar = xbar
        self.sd = sigma
        self.n = n

        self.startup_from_stats()

    def _run_test(self):
        self.se = self.sd / np.sqrt(self.n)
        self.df = self.n - 1
        self.distn = StandardNormal()
        self.null_stat = self.z0 = self.distn.quantile(1 - self.alpha/2)
        self.stat = self.z = (self.xbar - self.mu0) / self.se

        if self.alternative in ['two-sided', 'ne', '!=']:
            self.pvalue = 2*self.distn.cdf(-np.abs(self.t))
            self.alt_sym = '\\ne'
        elif self.alternative in ['less', 'lt', '<']:
            self.pvalue = self.distn.cdf(self.t)
            self.alt_sym = '<'
        elif self.alternative in ['greater', 'gt', '>']:
            self.pvalue = 1 - self.distn.cdf(self.t)
            self.alt_sym = '>'
        else:
            raise ValueError("Valid alternative values: 'two-sided', 'less', or 'greater'")

        self.text_h0 = f"\mu = {self.mu0}"
        self.text_ha = f"\mu {self.alt_sym} {self.mu0}"
