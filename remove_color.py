from PIL import Image
import os
import sys
color = '#D5D3D3'
p = int(sys.argv[1])
q = int(sys.argv[2])

def find_pngs(folder):
    pngs = []
    for filename in os.listdir(folder):
        if filename.lower().endswith(".png"):
            pngs.append(filename[:-4])
    return pngs

def hex_to_rgba(hex_code):
    hex_code = hex_code.lstrip('#')
    if len(hex_code) == 6:
        hex_code += 'FF'  # assume fully opaque if no alpha provided
    return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4, 6))

def remove_color(image_path, hex_code, output_path):
    img = Image.open(image_path).convert('RGBA')
    data = img.getdata()

    target_color = hex_to_rgba(hex_code)
    new_data = []

    for item in data:
        if item[:3] == target_color[:3]:
            new_data.append((0, 0, 0, 0))
        else:
            new_data.append(item)

    img.putdata(new_data)
    img.save(output_path, 'PNG')

pngs = find_pngs(os.getcwd() + f'/imgs/({p}, {q})')
for png in pngs:
    remove_color(os.getcwd() + f'/imgs/({p}, {q})/{png}.png', color, os.getcwd() + f'/imgs/({p}, {q})/{png}_updated.png')