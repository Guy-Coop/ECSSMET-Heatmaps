import numpy as np


def _repair_slice_average(slice: np.ndarray, max_diff: 0.1) -> np.ndarray:
    """
    Repair the data by replacing values that are too far from the average of
    their neighbors.

    :param slice:
    :param max_diff:
    :return:
    """
    for i in range(0, slice.shape[0]):
        for j in range(0, slice.shape[1]):
            i_low = max(0, i - 1)
            i_high = min(slice.shape[0], i + 2)
            j_low = max(0, j - 1)
            j_high = min(slice.shape[1], j + 2)
            sub_grid = slice[i_low:i_high, j_low:j_high]
            avg = (np.sum(sub_grid) - slice[i][j]) / (sub_grid.size - 1)

            if abs(slice[i][j] - avg) > (avg * max_diff):
                slice[i][j] = avg
    return slice


def _repair_average(data: np.ndarray, max_diff: 0.1, **_) -> np.ndarray:
    """
    Repair the data by replacing values that are too far from the average of
    their neighbors.

    :param data:
    :param max_diff:
    :return:
    """
    for i in range(0, data.shape[0]):
        data[i] = _repair_slice_average(data[i], max_diff)
    return data


repair = {
    "average": _repair_average,
}


def db_scale(data: np.ndarray, max_: float = None) -> np.ndarray:
    """
    rescale the data to a db scale
    either relative to the provided maximum or the max of each slice
    """
    for i in range(0, data.shape[0]):
        this_max = np.max(data[i]) if max_ is None else max_
        data[i] = 10 * np.log10(data[i] / this_max)
    return data
