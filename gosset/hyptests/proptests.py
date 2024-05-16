from .hyptest import HypothesisTest
from ..rvs.normal import StandardNormal


class OneProportionZ(HypothesisTest):
    def __init__(self, x=None, n=None, p0=None, alternative='two-sided', alpha=0.05):
        self.p0 = p0
        self.alpha = alpha
        self.alternative = alternative
        self._stat_sym = 'p'

        # TODO: Allow the use of data?
        self.x = x
        self.n = n

        self.startup_from_stats()

    def _run_test(self):
        self.p_hat = self.x / self.n
        self.se = np.sqrt(self.p0 * (1 - self.p0) / self.n)
        self.distn = StandardNormal()
        self.null_stat = self.z0 = self.distn.quantile(1 - self.alpha / 2)
        self.stat = self.z = (self.p_hat - self.p0) / self.se

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

        self.text_h0 = f"p = {self.p0}"
        self.text_ha = f"p {self.alt_sym} {self.p0}"
