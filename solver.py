
import pandas as pd
from neal import SimulatedAnnealingSampler
from qubo_builder import build_qubo

def solve(n_reads=500):
    Q, binaries, spec = build_qubo()
    sampler = SimulatedAnnealingSampler()
    response = sampler.sample_qubo(Q, num_reads=n_reads, num_sweeps=2000)

    records = []
    # сопоставим порядок битов и имён
    var_order = list(binaries.keys())

    for sample, _ in zip(response.record.sample, response.record.energy):
        sel = dict(zip(var_order, sample))

        lambda_neg = 0
        mass = 0
        for name, bit in sel.items():
            cfg = spec["options"][name]
            lambda_neg += cfg["effect_lambda"] * bit
            mass       += cfg["weight"]       * bit

        records.append({"lambda_neg": lambda_neg, "mass": mass})

    df = pd.DataFrame(records)
    df.to_csv("results.csv", index=False)
    return df
