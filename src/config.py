import logging
from pathlib import Path

LOG_LEVEL = logging.INFO  # set to logging.ERROR for reduced logging

DATA_PATH = Path("../CSVs/")

REPAIR_METHOD = None  # "average" or None
REPAIR_KWARGS = {"max_diff": 0.1}  # key-word-arguments for repair method

ONE_THIRD_OCTAVE_BANDS = True  # True or False

# RESCALE_MAX = "global"  # scale the data to the maximum value in the entire dataset
RESCALE_MAX = "local"  # scale the data to the maximum value in each slice

HEATMAP_SCALE = "global"  # scale the heatmap to the maximum value in the entire dataset
# HEATMAP_SCALE = "local" # scale the heatmap to the maximum value in each slice

HEATMAP_PATH = Path(
    f"../heatmaps/"
    f"{'one_third_octaves_' if ONE_THIRD_OCTAVE_BANDS else 'all_frequencies_'}"
    f"{'repaired_' if REPAIR_METHOD is not None else ''}"
    f"dbscale={RESCALE_MAX}_"
    f"figscale={HEATMAP_SCALE}/"
)

GENERATE_GIF = True  # set to False to skip gif generation
GIF_PATH = Path(
    "../gifs/"
    f"{'one_third_octaves_' if ONE_THIRD_OCTAVE_BANDS else 'all_frequencies_'}"
    f"{'repaired_' if REPAIR_METHOD is not None else ''}"
    f"dbscale={RESCALE_MAX}_"
    f"figscale={HEATMAP_SCALE}"
    f".gif"
)
GIF_FPS = 10
