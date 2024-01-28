import pprint
import copy
def p(v):
    pprint.pprint(v, sort_dicts= False, width=10)

def c(dict):
    dict2 = copy.deepcopy(dict)
    return dict2