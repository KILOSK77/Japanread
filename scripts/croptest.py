import json
from pathlib import Path
from PIL import Image


# -------------------------
# PATHS
# -------------------------

ROOT = Path(r"E:\\japanread\\dataset\\raw\\openmantra")

JSON_PATH = ROOT / "annotation.json"

SAVE_PATH = Path(
    r"E:\japanread\dataset\raw\cropped\test.jpg"
)


# -------------------------
# LOAD JSON
# -------------------------

with open(
    JSON_PATH,
    "r",
    encoding="utf-8"
) as f:

    data = json.load(f)


# -------------------------
# GET FIRST SAMPLE
# -------------------------

book = data[0]

page = book["pages"][0]

text = page["text"][0]


# -------------------------
# LOAD IMAGE
# -------------------------

img_path = (
    ROOT /
    page["image_paths"]["ja"]
)

img = Image.open(
    img_path
)


# -------------------------
# READ COORDINATES
# -------------------------

x = text["x"]

y = text["y"]

w = text["w"]

h = text["h"]


# -------------------------
# CROP
# -------------------------

crop = img.crop(
(
    x,
    y,
    x + w,
    y + h
)
)


# -------------------------
# KEEP ASPECT RATIO
# -------------------------

target = 256

crop.thumbnail(
(
target,
target
)
)

canvas = Image.new(
"L",
(
target,
target
),
255
)

offset_x = (
target -
crop.width
)//2

offset_y = (
target -
crop.height
)//2

canvas.paste(
crop,
(
offset_x,
offset_y
)
)

crop = canvas
# -------------------------
# SAVE
# -------------------------

SAVE_PATH.parent.mkdir(
    parents=True,
    exist_ok=True
)

crop.save(
    SAVE_PATH
)


# -------------------------
# OUTPUT
# -------------------------

print("\nDONE\n")

print(
"Saved:"
)

print(
SAVE_PATH
)

print(
"\nJP:"
)

print(
text["text_ja"]
)

print(
"\nEN:"
)

print(
text["text_en"]
)