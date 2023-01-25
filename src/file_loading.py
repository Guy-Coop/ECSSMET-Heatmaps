from pathlib import Path
from typing import List, Tuple

import numpy as np
import pandas as pd

RUN_TO_GRIDSQUARE_MAP = {
    "11": (0, 0),
    "12": (1, 0),
    "13": (2, 0),
    "14": (3, 0),
    "15": (4, 0),
    "16": (0, 1),
    "17": (1, 1),
    "18": (2, 1),
    "19": (3, 1),
    "20": (4, 1),
    "21": (0, 2),
    "22": (1, 2),
    "23": (2, 2),
    "24": (3, 2),
    "25": (4, 2),
    "26": (0, 3),
    "27": (1, 3),
    "28": (2, 3),
    "29": (3, 3),
    "30": (4, 3),
    "31": (0, 4),
    "32": (1, 4),
    "33": (2, 4),
    "34": (3, 4),
    "35": (4, 4),
    "36": (0, 5),
    "37": (1, 5),
    "38": (2, 5),
    "39": (3, 5),
    "40": (4, 5),
    "41": (0, 6),
    "42": (1, 6),
    "43": (2, 6),
    "44": (3, 6),
    "45": (4, 6),
}


def _get_inner_coordinates(outer_i, outer_j, inner_count):
    x = (outer_i * 3) + (inner_count % 3)
    y = (outer_j * 3) + (inner_count // 3)
    return x, y


def get_data_as_array(
    root_path: Path = Path("./CSV"),
) -> Tuple[np.ndarray, List[float]]:
    """Load the data from the CSV files and return it as a 3D numpy array."""

    arr = None
    frequencies = None

    for f_name, (i, j) in RUN_TO_GRIDSQUARE_MAP.items():
        df = pd.read_csv(root_path / f"run_{f_name}.CSV", header=None, skiprows=2)
        if arr is None:
            frequencies = df[0].tolist()
            arr = np.zeros((len(df), 21, 15))

        for row_ind, row in df.iterrows():
            for col in range(1, 10):
                x, y = _get_inner_coordinates(i, j, col - 1)
                arr[row_ind, y, x] = row[col]

    return arr, frequencies
