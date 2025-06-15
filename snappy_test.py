from spherogram import Link
from sage.all import factor, var
import math


def valid_alexander(poly):
    """
    Checks if poly is of the form f(t) * f(t^-1).
    Input: a Sage polynomial object
    """
    t = var('t')
    factors = factor(poly)

    # Dictionary to count multiplicities of factors and their reciprocals
    factor_counts = {}

    for f, mult in factors:
        f_expr = f(t)
        rev_expr = f_expr.subs(t=1/t) * t**f.degree()
        f_str = str(f_expr.expand())
        rev_str = str(rev_expr.expand())

        if f_str not in factor_counts and rev_str not in factor_counts:
            factor_counts[f_str] = mult
        elif f_str in factor_counts:
            factor_counts[f_str] += mult
        else:
            factor_counts[rev_str] += mult

    # Every irreducible factor must appear with even multiplicity (matched with reciprocal)
    return all(v % 2 == 0 for v in factor_counts.values())
            
could_be_slice = True
l = Link([(21,80,22,81), (48,77,49,78), (22,153,23,154), (127,153,128,152), (49,150,50,151), (76,101,77,102), (149,100,150,101), (128,80,129,79), (179,78,180,79), (180,151,181,152), (206,75,1,76), (1,148,2,149), (205,75,206,74), (133,174,134,175), (87,14,88,15), (191,61,192,60), (31,118,32,119), (103,204,104,205), (45,104,46,105), (175,45,176,44), (15,134,16,135), (61,88,62,89), (161,31,162,30), (117,190,118,191), (176,105,177,106), (129,70,130,71), (131,107,132,106), (20,70,21,69), (18,107,19,108), (16,174,17,173), (81,68,82,69), (83,109,84,108), (85,172,86,173), (66,109,67,110), (64,172,65,171), (62,14,63,13), (197,110,198,111), (195,171,196,170), (193,13,194,12), (37,169,38,168), (166,10,167,9), (164,58,165,57), (162,119,163,120), (143,56,144,57), (145,121,146,120), (147,160,148,161), (6,56,7,55), (4,121,5,122), (2,160,3,159), (97,123,98,122), (99,158,100,159), (52,123,53,124), (50,158,51,157), (181,157,182,156), (126,155,127,156), (23,155,24,154), (112,169,113,170), (114,11,115,12), (116,59,117,60), (35,11,36,10), (33,59,34,58), (141,8,142,9), (95,54,96,55), (183,124,184,125), (102,73,103,74), (47,73,48,72), (46,204,47,203), (178,72,179,71), (177,203,178,202), (130,201,131,202), (132,43,133,44), (19,201,20,200), (17,43,18,42), (82,199,83,200), (84,41,85,42), (86,136,87,135), (67,199,68,198), (65,41,66,40), (63,136,64,137), (196,40,197,39), (194,137,195,138), (192,89,193,90), (165,92,166,93), (163,189,164,188), (142,94,143,93), (144,187,145,188), (146,29,147,30), (5,187,6,186), (3,29,4,28), (96,185,97,186), (98,27,99,28), (51,27,52,26), (182,26,183,25), (125,24,126,25), (111,38,112,39), (113,139,114,138), (115,91,116,90), (36,139,37,140), (34,91,35,92), (32,190,33,189), (167,140,168,141), (7,94,8,95), (53,185,54,184)])
l.simplify('global')
floer = l.knot_floer_homology()
print('Seifert Genus: ' + str(floer['seifert_genus']))
determinant = int(l.determinant())
if not math.sqrt(determinant).is_integer():
    could_be_slice = False
print('Determinant: ' + str(determinant))
signature = l.signature()
if signature != 0:
    could_be_slice = False
print('Signature: ' + str(signature))
alexander = l.alexander_polynomial()
if not valid_alexander(alexander):
    could_be_slice = False
print('Alexander: ' + str(factored_alexander))
print('Maximal Crossing Number: ' + str(len(l.crossings)))
print('Could be Slice: ' + ('Yes' if could_be_slice else 'No'))