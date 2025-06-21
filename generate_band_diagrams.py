from band_diagram import save_band_diagram_img
import math
import cairosvg
import sys


p = int(sys.argv[1])
q = int(sys.argv[2])
digits = q / 2 - 1
for i in range(int(2 ** digits)):
    band_code = str(bin(i))[2:]
    while len(band_code) < digits:
        band_code = '0' + band_code
    save_band_diagram_img(p, q, f'imgs/({p}, {q}).svg', 30, .7, 1.2, 4096, 4096, band_code)
    cairosvg.svg2png(url=f'imgs/({p}, {q})/{band_code}.svg', write_to=f'imgs/({p}, {q})/{band_code}.png')
