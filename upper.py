from invs.pinch import pinch_condition
from utils import fc_12, fc_13
# Indexes of invs: sig 0, ups 1, arf 2, d 3, alexander 4, pinch 5, genus 6, bridge 7, crossing 8, unknotting 9, n3genus 10, alexander_blob 11

def get_uppers(p: int, q: int, invs: list):
    if abs(p) == 1 or abs(q) == 1:
        return [1]
    uppers = []
    # Fairchild
    if invs[10] is not None:
        uppers.append(invs[10])
    if pinch_condition(p, q) and invs[5] is not None:
        uppers.append(invs[5])
    
    # Jabuka Van Cott
    m, n = max(p, q), min(p, q)
    if m % 2 == 0 and n % 2 == 1 and invs[10] is not None:
        uppers.append(invs[10] - ((m // n) / 2))
    fc12 = fc_12(p, q)[1]
    if fc12 is not None:
        uppers.append(fc12)
    fc13 = fc_13(p, q)[1]
    if fc13 is not None:
        uppers.append(fc13)

    # Batson
    if max(p, q) % 2 == 0 and max(p, q) - min(p, q) == 1:
        uppers.append(max(p, q) / 2 - 1)
    if invs[5] is not None:
        uppers.append(invs[5])

    # Longo
    if q % 4 == 0 and (((q / 2) + 1) ** 2 == p or ((q / 2) - 1) ** 2 == p):
        uppers.append(q / 2 - 1)
    return uppers