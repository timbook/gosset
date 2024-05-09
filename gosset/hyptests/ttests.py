import numpy as np
from IPython.core.display import HTML
from ..rvs.t import T

class HypothesisTest:
    def startup(self, data):
        self._na_check(data)
        self._run_test(data)

    def _na_check(self, data):
        if np.any(np.isnan(np.array(data))):
            raise ValueError("Missing values detected in the data.")

    def hypotheses(self):
        null = f"H_0: {self.text_h0}"
        alt = f"H_A: {self.text_ha}"
        return HTML(f"$${null}$$\n$${alt}$$")
        
    def results(self, format='tuple'):
        if format == 'tuple':
            return self.stat, self.pvalue, self.reject
        elif format == 'dict':
            return {'stat': self.stat, 'pvalue': self.pvalue, 'reject': self.reject}
        else:
            raise ValueError("Supported formats: 'tupple' or 'dict'.")

    def summary(self):
        display(self.hypotheses())
        display(HTML(f"${self._stat_sym}$ = {np.round(self.stat, 4)}"))
        display(HTML(f"$p$-value = {np.round(self.pvalue, 4)}"))

    @property
    def reject(self):
        return True if self.pvalue < self.alpha else False

class OneSampleT(HypothesisTest):
    def __init__(self, data, mu_0=0, alternative='two-sided', alpha=0.05):
        self.mu_0 = mu_0
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
        self.stat = self.t = (self.xbar - self.mu_0) / self.se

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

        self.text_h0 = f"\mu = {self.mu_0}"
        self.text_ha = f"\mu {self.alt_sym} {self.mu_0}"

#  class OneSampleTFromStats(OneSampleT):
    #  def __init__(self, xbar, sd, n, mu_0=0, alternative='two-sided', alpha=0.05):
        #  self.mu_0 = mu_0
        #  self.alternative = alternative
        #  self.alpha = alpha
        #  self._stat_sym = 't'
        #  self.ref_stat = -super().distn.quantile(self.alpha/2)

        #  self.xbar = xbar
        #  self.sd = sd
        #  self.n = n

        #  self.run_test()

    #  def run_test(self):
        #  self.se = self.sd / np.sqrt(self.n)
        #  self.stat = self.t = (self.xbar - self.mu_0) / self.se
        #  self.df = self.n - 1
        #  self.distn = T(df=self.df)

        #  if self.alternative == 'two-sided':
            #  self.pvalue = 2*self.distn.cdf(-np.abs(self.t))
        #  elif self.alternative == 'less':
            #  self.pvalue = self.distn.cdf(self.t)
        #  elif self.alternative == 'greater':
            #  self.pvalue = 1 - self.distn.cdf(self.t)
        #  else:
            #  raise ValueError("Valid alternative values: 'two-sided', 'less', or 'greater'")

        #  self.reject = True if self.pvalue < self.alpha else False
