from scipy import stats
from .rv import DiscreteRV

class Hypergeometric(DiscreteRV):
    def __init__(self, N, M, K):
        self.N = N
        self.M = M
        self.K = K
        self._rv = stats.hypergeom(M=N, n=M, N=K)

    def __repr__(self):
        return f"Hypergeometric(N={self.N}, M={self.M}, K={self.K})"
