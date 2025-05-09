# %%
# 📌 Creatoria-lite: minimal open-source design optimizer
#
# YAML → QUBO → Simulated Annealing → CSV → Pareto
#
# - 🔧 Binary options: `cell_thickness`, `fin_height`
# - 🎯 Objectives: maximize thermal conductivity (−λ), minimize mass
# - 🧊 Solver: `dwave-neal` (Simulated Annealing)
#
# Output: `results.csv`, Pareto chart `pareto.png`

# %%
from solver import solve
from plot_pareto import plot

df = solve()
plot()

# %%
from IPython.display import Image, display
display(Image("pareto.png"))
