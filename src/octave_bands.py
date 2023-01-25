from typing import List, Tuple

import numpy as np


def _get_third_octave_band_inds(frequencies):
    """
    Get the center frequency and indices of the third octave bands.

    :param frequencies:
    :return:
    """

    center_freqs = [
        12.5,
        16,
        20,
        25,
        31.5,
        40,
        50,
        63,
        80,
        100,
        125,
        160,
        200,
        250,
        315,
        400,
        500,
        630,
        800,
        1000,
        1250,
        1600,
        2000,
        2500,
        3150,
        4000,
        5000,
        6300,
        8000,
    ]
    freqs = np.array(frequencies)
    for i in range(0, len(center_freqs)):
        center_freq = center_freqs[i]
        low = center_freq / 10**0.05
        high = center_freq * 10**0.05
        low_ind = np.argmin(np.abs(freqs - low))
        high_ind = np.argmin(np.abs(freqs - high))
        yield (low_ind, high_ind), center_freq


def apply_one_third_bands(
    data: np.ndarray, frequencies: List[float]
) -> Tuple[np.ndarray, List[float]]:
    """
    Apply the third octave bands to the data.
    :param data:
    :param frequencies:
    :return:
    """
    new_slices = []
    center_frequencies = []
    for (start, stop), center_freq in _get_third_octave_band_inds(frequencies):
        slice = data[start:stop, :, :]
        slice = np.average(slice, axis=0)
        new_slices.append(slice)
        center_frequencies.append(center_freq)
    return np.array(new_slices), center_frequencies
