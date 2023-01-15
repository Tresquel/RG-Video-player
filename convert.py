from PIL import Image
import json


def rgb_to_hex(rgb):
    return  rgb


info = {
    "frames": 8,
    "fps": 30,
    "data": {
        # frames here
    },
}

for i in range(1, info["frames"] + 1):
    imag = Image.open(f"frames/{i}.png")
    imag = imag.convert("RGB")
    x, y = imag.size

    info["data"][f"frame{i}"] = []

    for ypos in range(0, y):
        for xpos in range(0, x):
            pixelRGB = imag.getpixel((xpos, ypos))

            R, G, B = pixelRGB
            hexcolor = "%02x%02x%02x" % (R, G, B)

            info["data"][f"frame{i}"].append("#" + hexcolor)

with open("image.json", "w") as f:
    f.write(json.dumps(info, indent=4 * " "))
