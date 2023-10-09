from scipy import stats
from .rv import ContinuousRV

class T(ContinuousRV):
    def __init__(self, df):
        self.df = df
        self._rv = stats.t(df=df)

    def __repr__(self):
        return f"T(df={self.df})"
