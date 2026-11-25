import json
from pathlib import Path

# path to annotation

JSON_PATH = (
    r"E:\\japanread\\dataset\\raw\\openmantra\\annotation.json"
)

with open(
    JSON_PATH,
    "r",
    encoding="utf-8"
) as f:

    data = json.load(f)

print("\nLoaded Dataset\n")

print(
    "Books:",
    len(data)
)

# first book

book = data[0]

print(
    "\nBook:"
)

print(
    book["book_title"]
)

# first page

page = book["pages"][0]

print(
    "\nPage:"
)

print(
    page["page_index"]
)

print(
    "\nImage:"
)

print(
    page["image_paths"]["ja"]
)

# first text

text = page["text"][0]

print(
    "\nCoordinates:"
)

print(
    text["x"],
    text["y"],
    text["w"],
    text["h"]
)

print(
    "\nJapanese:"
)

print(
    text["text_ja"]
)

print(
    "\nEnglish:"
)

print(
    text["text_en"]
)