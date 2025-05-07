
import yaml
from pyqubo import Binary
def build_qubo(path='contradiction.yaml'):
    spec = yaml.safe_load(open(path))
    x = Binary('x')
    w = spec['options']['cell_thickness']['weight']
    e = abs(spec['options']['cell_thickness']['effect_lambda'])
    H = w*x + e*x
    Q,_ = H.compile().to_qubo()
    return Q
