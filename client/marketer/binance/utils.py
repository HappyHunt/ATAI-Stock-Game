from urllib.parse import urlencode
from .error import ParameterRequiredError

def cleanNoneValue(d) -> dict:
    out = {}
    for k in d.keys():
        if d[k] is not None:
            out[k] = d[k]
    return out


def encoded_string(query, special=False):
    if special:
        return urlencode(query).replace("%40", "@").replace("%27", "%22")
    else:
        return urlencode(query, True).replace("%40", "@")


def check_required_parameters(params):
    """validate multiple parameters
    params = [
        ['btcusdt', 'symbol'],
        [10, 'price']
    ]
    """
    for p in params:
        check_required_parameter(p[0], p[1])


def check_required_parameter(value, name):
    if not value and value != 0:
        raise ParameterRequiredError([name])