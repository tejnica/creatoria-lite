import pandas as pd
import matplotlib.pyplot as plt

def plot():
    df = pd.read_csv("results.csv")
    df = df.drop_duplicates()

    # Pareto front: lower lambda_neg and lower mass are better
    pareto = df.sort_values(['lambda_neg', 'mass'], ascending=[True, True])
    pareto_front = [pareto.iloc[0]]
    for i in range(1, len(pareto)):
        if pareto.iloc[i]['mass'] < pareto_front[-1]['mass']:
            pareto_front.append(pareto.iloc[i])
    pareto_front = pd.DataFrame(pareto_front)

    plt.figure(figsize=(6, 5))
    plt.scatter(df["lambda_neg"], df["mass"], color="orange", alpha=0.8, label="Candidates", marker="*")
    plt.plot(pareto_front["lambda_neg"], pareto_front["mass"], color="black", label="Pareto front")
    plt.xlabel("-lambda")
    plt.ylabel("mass")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("pareto.png")

if __name__ == "__main__":
    plot()
