import logging

import numpy as np

import config as cfg
from data_processing import repair, db_scale
from file_loading import get_data_as_array
from image_generation import save_heatmaps, generate_gif
from octave_bands import apply_one_third_bands

logging.basicConfig(level=cfg.LOG_LEVEL)
_logger = logging.getLogger(__name__)


def main():
    data, frequencies = get_data_as_array(cfg.DATA_PATH)
    _logger.info(f"loaded data into array of shape {data.shape}")

    if cfg.REPAIR_METHOD is not None:
        data = repair[cfg.REPAIR_METHOD](data, **cfg.REPAIR_KWARGS)
        _logger.info(f"repaired data using {cfg.REPAIR_METHOD} method")

    center_frequencies = frequencies
    if cfg.ONE_THIRD_OCTAVE_BANDS:
        data, center_frequencies = apply_one_third_bands(data, frequencies)
        _logger.info(f"applied one-third octave bands to data")

    max_ = np.max(data) if cfg.RESCALE_MAX == "global" else None
    data = db_scale(data, max_)
    _logger.info(f"rescaled data to decibels, using {cfg.RESCALE_MAX} max")

    _logger.info("saving heatmaps")
    save_heatmaps(
        data,
        center_frequencies,
        cfg.HEATMAP_PATH,
        cfg.HEATMAP_SCALE == "global",
    )

    if cfg.GENERATE_GIF:
        _logger.info("generating gif")
        generate_gif(
            cfg.HEATMAP_PATH,
            cfg.GIF_PATH,
            cfg.GIF_FPS,
        )


if __name__ == "__main__":
    main()
