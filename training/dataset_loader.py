import json
from PIL import Image


class MangaDataset:

    def __init__(
        self,
        json_path
    ):

        with open(
            json_path,
            "r",
            encoding="utf-8"
        ) as f:

            self.data = (
                json.load(f)
            )



    def __len__(
        self
    ):

        return len(
            self.data
        )



    def __getitem__(
        self,
        idx
    ):

        item = (
            self.data[
                idx
            ]
        )



        image = (
            Image.open(
                item[
                    "image"
                ]
            )
        )



        target = (
            item[
                "target"
            ]
        )



        return (

            image,

            target

        )