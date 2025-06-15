from spherogram import Link
import math

could_be_slice = True
l = Link(Link([(54,35,55,36), (17,36,18,37), (21,41,22,40), (59,30,60,31), (91,75,92,74), (15,91,16,90), (39,14,40,15), (67,22,68,23), (83,67,84,66), (7,83,8,82), (47,6,48,7), (29,49,30,48), (38,89,39,90), (19,88,20,89), (20,13,21,14), (85,42,86,43), (77,50,78,51), (76,31,77,32), (1,32,2,33), (52,34,53,33), (53,56,54,57), (34,55,35,56), (69,13,70,12), (68,41,69,42), (86,12,87,11), (10,43,11,44), (60,49,61,50), (2,51,3,52), (16,74,17,73), (37,72,38,73), (18,71,19,72), (84,23,85,24), (9,24,10,25), (8,66,9,65), (44,26,45,25), (45,64,46,65), (46,81,47,82), (26,63,27,64), (27,80,28,81), (61,5,62,4), (75,59,76,58), (92,58,1,57), (70,88,71,87), (28,5,29,6), (62,80,63,79), (78,4,79,3)]))
l.simplify('global')
floer = l.knot_floer_homology()
print('Seifert Genus: ' + str(floer['seifert_genus']))
determinant = l.determinant()
if not math.sqrt(determinant).is_integer:
    could_be_slice = False
print('Determinant: ' + determinant)
signature = l.signature()
if signature != 0:
    could_be_slice = False
print('Signature: ' + signature)
factored_alexander = l.alexander_polynomial(factored=True)
print('Factore Alexander: ' + factored_alexander)
print('Could be Slice: ' + 'Yes' if could_be_slice else 'No')
