import numpy as np
from IPython.core.display import HTML

class HTResult:
    def __init__(self, stat, pvalue, reject):
        self.stat = stat
        self.pvalue = pvalue
        self.reject = reject

    def __repr__(self):
        return f"HTResult(stat={self.stat}, pvalue={self.pvalue}, reject={self.reject})"

class HypothesisTest:
    def startup(self, data):
        self._na_check(data)
        self._run_test(data)

    def startup_from_stats(self):
        self._run_test()

    def _na_check(self, data):
        if np.any(np.isnan(np.array(data))):
            raise ValueError("Missing values detected in the data.")

    def hypotheses(self):
        null = f"H_0: {self.text_h0}"
        alt = f"H_A: {self.text_ha}"
        return HTML(f"$${null}$$\n$${alt}$$")
        
    def results(self):
        return HTResult(self.stat, self.pvalue, self.reject)

    def summary(self):
        display(self.hypotheses())
        display(HTML(f"${self._stat_sym}$ = {np.round(self.stat, 4)}"))
        display(HTML(f"$p$-value = {np.round(self.pvalue, 4)}"))

    @property
    def reject(self):
        return True if self.pvalue < self.alpha else False
