import numpy as np
from .hyptest import HypothesisTest
from ..rvs.t import T

class OneSampleT(HypothesisTest):
    def __init__(self, data, mu0=0, alternative='two-sided', alpha=0.05):
        self.mu0 = mu0
        self.alpha = alpha
        self.alternative = alternative
        self._stat_sym = 't'
        self.startup(data)

    def _run_test(self, data):
        self.n = len(data)
        self.df = self.n - 1
        self.xbar = np.mean(data)
        self.sd = np.std(data, ddof=1)
        self.se = self.sd / np.sqrt(self.n)
        self.distn = T(df=self.df)
        self.null_stat = self.t0 = self.distn.quantile(1 - self.alpha/2)
        self.stat = self.t = (self.xbar - self.mu0) / self.se

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

class OneSampleTFromStats(HypothesisTest):
    def __init__(self, xbar, sd, n, mu0=0, alternative='two-sided', alpha=0.05):
        self.mu0 = mu0
        self.alpha = alpha
        self.alternative = alternative
        self._stat_sym = 't'

        self.xbar = xbar
        self.sd = sd
        self.n = n

        self.startup_from_stats()

    def _run_test(self):
        self.se = self.sd / np.sqrt(self.n)
        self.df = self.n - 1
        self.distn = T(df=self.df)
        self.null_stat = self.t0 = self.distn.quantile(1 - self.alpha/2)
        self.stat = self.t = (self.xbar - self.mu0) / self.se

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
