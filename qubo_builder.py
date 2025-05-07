
import yaml
from pyqubo import Binary

def build_qubo(path='contradiction.yaml'):
    spec = yaml.safe_load(open(path))
    H = 0      # гамильтониан
    binaries = {}
    # проходим по опциям и создаём биты
    for name, cfg in spec["options"].items():
        # если bits == 1 — один бит; можно потом обобщить на N
        x = Binary(name)
        binaries[name] = x
        H += cfg["weight"] * x + abs(cfg["effect_lambda"]) * x
    Q, _ = H.compile().to_qubo()
    return Q, binaries, spec

