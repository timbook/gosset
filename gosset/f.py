from scipy import stats
from .rv import ContinuousRV

class F(ContinuousRV):
    def __init__(self, df1, df2):
        self.df1 = df1
        self.df2 = df2
        self._rv = stats.f(df1, df2)

    def __repr__(self):
        return f"F(df1={self.df1}, df2={self.df2})"
