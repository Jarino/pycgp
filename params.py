FUNSET = {}

def protected_div(x, y):
    if y == 0:
        return 1
    try:
        return x / y
    except ZeroDivisionError:
        return 1


FUNSET[0] = lambda x, y: x + y
FUNSET[1] = lambda x, y: x - y
FUNSET[2] = lambda x, y: x * y
FUNSET[3] = lambda x, y: protected_div(x, y)

DEFAULT_PARAMS = {
    'n_inputs': 3,
    'n_outputs': 2,
    'n_cols': 2,
    'n_rows': 1,
    'funset': FUNSET
}
