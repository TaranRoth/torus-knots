from invs.pinch import pinch_condition
from utils import fc_12, fc_13
import pickle
# Indexes of invs: sig 0, ups 1, arf 2, d 3, alexander 4, pinch 5, genus 6, bridge 7, crossing 8, unknotting 9, n3genus 10, alexander_blob 11


def get_lowers(p: int, q: int, invs: list):
    if abs(p) == 1 or abs(q) == 1:
        return [1]
    lowers = [1]
    # Fairchild
    if invs[2] is not None and (invs[0] + 4 * invs[2]) % 8 == 4:
        lowers.append(2)
    if invs[0] is not None and invs[1] is not None:
        lowers.append(abs((-invs[0] / 2) + invs[1]))
    if invs[0] is not None and invs[3] is not None:
        lowers.append((-invs[0] / 2) - invs[3])
    if pinch_condition(p, q) and invs[5] is not None:
        lowers.append(invs[5] - 1)
    lowers.append(fc_12(p, q)[0])
    lowers.append(fc_13(p, q)[0])
    # Jabuka Van Cott

    #Batson
    if max(p, q) % 2 == 0 and max(p, q) - min(p, q) == 1:
        lowers.append(max(p, q) / 2 - 1)

    # Binns
    if invs[4] is not None and invs[11] is not None:
        poly = pickle.loads(invs[11])
        constant_neg = False
        for exp, coeff in poly:
            if exp == 0 and coeff == -1:
                constant_neg = True
        if constant_neg:
            for i in range(len(poly)):
                if poly[i][0] == 0 and len(poly) > i + 1:
                    lowers.append(poly[i + 1][0] - 1)
    

    return lowers

