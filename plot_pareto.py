
import pandas as pd, matplotlib.pyplot as plt
from pymoo.util.nds.non_dominated_sorting import NonDominatedSorting
def plot(csv='results.csv'):
    df = pd.read_csv(csv)
    nd = NonDominatedSorting().do(df[['lambda_neg','mass']].values, only_non_dominated_front=True)
    plt.scatter(df['lambda_neg'], df['mass'], alpha=.3)
    plt.scatter(df.loc[nd,'lambda_neg'], df.loc[nd,'mass'], marker='*', s=80)
    plt.xlabel('-lambda'); plt.ylabel('mass'); plt.tight_layout(); plt.savefig('pareto.png')
if __name__=='__main__':
    plot()
