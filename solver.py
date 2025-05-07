
import pandas as pd
from neal import SimulatedAnnealingSampler
from qubo_builder import build_qubo
def solve(reads=200):
    Q = build_qubo()
    sampler = SimulatedAnnealingSampler()
    res = sampler.sample_qubo(Q, num_reads=reads)
    df = pd.DataFrame([{'lambda_neg': -0.8*s[0], 'mass': 120*s[0]} for s in res.record.sample])
    df.to_csv('results.csv', index=False)
if __name__=='__main__':
    solve()
