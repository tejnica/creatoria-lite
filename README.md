![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License: MIT](https://img.shields.io/badge/license-MIT-green)
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/tejnica/quantriz-v0/blob/main/run_demo.py)

# QuanTriz-lite

Minimal working open-source prototype: YAML → QUBO → Simulated Annealing → CSV → Pareto

## Quick Start

```bash
git clone https://github.com/tejnica/quantriz-v0.git
cd quantriz-v0
pip install -r requirements.txt
python run_demo.py
```

## Example Output

- Pareto front points: (0, 0), (−0.7, 60), (−0.9, 80)
- Simulations: 500 (Simulated Annealing)

![Pareto Chart](pareto.png)

## YAML Parameters

`contradiction.yaml`

| Option         | Bits | Weight | Effect on λ |
|----------------|------|--------|-------------|
| cell_thickness | 1    | 80     | −0.9        |
| fin_height     | 1    | 60     | −0.7        |

© 2025 Eduards Cunskis  – MIT license
