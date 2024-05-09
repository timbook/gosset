import numpy as np
from IPython.core.display import HTML
from .rvs.t import T

class HypothesisTest:
    def __init__(self, data, alpha, na_drop, copy_data):
        self.na_drop = na_drop
        self.copy_data = copy_data

        if na_drop:
            data = data[~np.isnan(data)]
        else:
            if np.any(np.isnan(data)):
                raise ValueError("Missing values in data detected!")

        if copy_data:
            self.data = data

        self.alpha = alpha
        self.run_test(data)
        
    def results(self, format='tuple'):
        if format == 'tuple':
            return self.stat, self.pvalue, self.reject
        elif format == 'dict':
            return {'stat': self.stat, 'pvalue': self.pvalue, 'reject': self.reject}
        else:
            raise ValueError("Supported formats: 'tupple' or 'dict'.")

class OneSampleT(HypothesisTest):
    def __init__(self, data, mu_0=0, alternative='two-sided', alpha=0.05, na_drop=True, copy_data=False):

        self.mu_0 = mu_0
        self.alternative = alternative

        super().__init__(data, alpha, na_drop, copy_data)


    def run_test(self, data):

        self.xbar = np.mean(data)
        self.sd = np.std(data, ddof=1)
        self.n = len(data)
        self.se = self.sd / np.sqrt(self.n)
        self.stat = self.t = (self.xbar - self.mu_0) / self.se
        self.df = self.n - 1
        self.distn = T(df=self.df)
        self.t0 = self.distn.quantile(self.alpha/2)

        if self.alternative == 'two-sided':
            self.pvalue = 2*self.distn.cdf(-np.abs(self.t))
        elif self.alternative == 'less':
            self.pvalue = self.distn.cdf(self.t)
        elif self.alternative == 'greater':
            self.pvalue = 1 - self.distn.cdf(self.t)
        else:
            raise ValueError("Valid alternative values: 'two-sided', 'less', or 'greater'")

        self.reject = True if self.pvalue < self.alpha else False

    def interpretation(self, return_html=True):
        alpha_text = r'$\alpha$' if return_html else 'alpha'
        alt_text = {
            'two-sided': 'not equal to',
            'less': 'less than',
            'greater': 'greater than'
        }[self.alternative]
        
        if self.reject:
            concl_text = f"Since the p-value of {round(self.pvalue, 4)} is less than {alpha_text} = {self.alpha}, we reject the null hypothesis and conclude that the true population mean is {alt_text} {self.mu_0}."
        else:
            concl_text = f"Since the p-value of {round(self.pvalue, 4)} is greater than {alpha_text} = {self.alpha}, we fail to reject the null hypothesis and cannot conclude that the true population mean is {alt_text} {self.mu_0}."

        return HTML(concl_text) if return_html else concl_text

    def hypotheses(self):

        alt_sym = {
            'two-sided': r'\ne',
            'less': '<',
            'greater': '>'
        }[self.alternative]

        null = f"H_0: \mu = {self.mu_0}"
        alt = f"H_A: \mu {alt_sym} {self.mu_0}"

        return HTML(f"$${null}$$\n$${alt}$$")

class OneSampleTFromStats(OneSampleT):
    def __init__(self, xbar, sd, n, mu_0=0, alternative='two-sided', alpha=0.05):
        self.mu_0 = mu_0
        self.alternative = alternative
        self.alpha = alpha

        self.xbar = xbar
        self.sd = sd
        self.n = n

        self.run_test()

    def run_test(self):
        self.se = self.sd / np.sqrt(self.n)
        self.stat = self.t = (self.xbar - self.mu_0) / self.se
        self.df = self.n - 1
        self.distn = T(df=self.df)
        self.t0 = self.distn.quantile(self.alpha/2)

        if self.alternative == 'two-sided':
            self.pvalue = 2*self.distn.cdf(-np.abs(self.t))
        elif self.alternative == 'less':
            self.pvalue = self.distn.cdf(self.t)
        elif self.alternative == 'greater':
            self.pvalue = 1 - self.distn.cdf(self.t)
        else:
            raise ValueError("Valid alternative values: 'two-sided', 'less', or 'greater'")

        self.reject = True if self.pvalue < self.alpha else False
