import json
from pathlib import Path
from PIL import Image
from pykakasi import kakasi


# ----------------------
# PATHS
# ----------------------

ROOT = Path(
    r"E:\japanread\dataset\raw\openmantra"
)

JSON_PATH = (
    ROOT /
    "annotation.json"
)

CROP_DIR = Path(
    r"E:\japanread\dataset\raw\cropped"
)

OUT = Path(
    r"E:\japanread\dataset\raw\processed\train.json"
)


# ----------------------
# CREATE DIRS
# ----------------------

CROP_DIR.mkdir(
    parents=True,
    exist_ok=True
)

OUT.parent.mkdir(
    parents=True,
    exist_ok=True
)


# ----------------------
# FURIGANA
# ----------------------

kks = kakasi()


def make_furi(jp):

    result = (
        kks.convert(jp)
    )

    return " ".join(
        [
            x["hira"]
            for x in result
        ]
    )


# ----------------------
# LOAD DATASET
# ----------------------

with open(
    JSON_PATH,
    "r",
    encoding="utf-8"
) as f:

    data = json.load(f)


dataset = []

counter = 0


# ----------------------
# BUILD
# ----------------------

for book in data:

    for page in book["pages"]:

        img = Image.open(
            ROOT /
            page["image_paths"]["ja"]
        )

        for text in page["text"]:

            try:

                x = text["x"]
                y = text["y"]
                w = text["w"]
                h = text["h"]

                jp = text["text_ja"]
                en = text["text_en"]


                # ----------------
                # CROP
                # ----------------

                crop = img.crop(
                    (
                        x,
                        y,
                        x + w,
                        y + h
                    )
                )


                # ----------------
                # KEEP RATIO
                # ----------------

                crop.thumbnail(
                    (
                        256,
                        256
                    )
                )

                canvas = Image.new(
                    "L",
                    (
                        256,
                        256
                    ),
                    255
                )

                ox = (
                    256
                    -
                    crop.width
                ) // 2

                oy = (
                    256
                    -
                    crop.height
                ) // 2

                canvas.paste(
                    crop,
                    (
                        ox,
                        oy
                    )
                )


                # ----------------
                # SAVE IMAGE
                # ----------------

                name = (
                    f"{counter:06}.jpg"
                )

                save = (
                    CROP_DIR /
                    name
                )

                canvas.save(
                    save
                )


                # ----------------
                # FURIGANA
                # ----------------

                furi = (
                    make_furi(
                        jp
                    )
                )


                # ----------------
                # TARGET
                # ----------------

                target = (
                    f"<OCR>{jp}"
                    f"<FURI>{furi}"
                    f"<TRANS>{en}"
                    f"<EOS>"
                )


                dataset.append(
                    {
                        "image": str(
                            save
                        ),

                        "target": target
                    }
                )


                counter += 1


            except Exception as e:

                print(
                    "\nERROR:"
                )

                print(
                    e
                )


# ----------------------
# SAVE JSON
# ----------------------

with open(
    OUT,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        dataset,
        f,
        ensure_ascii=False,
        indent=2
    )


# ----------------------
# DONE
# ----------------------

print("\nDONE\n")

print(
    "Samples:",
    counter
)

print(
    "\nSaved:"
)

print(
    OUT
)