import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from pathlib import Path
import numpy as np
import os
import imageio


def _save_heatmap(slice, fname, title, **kwargs):
    fig, ax = plt.subplots(figsize=(8, 9))
    plt.title(f"{title}")
    sns.heatmap(
        slice,
        ax=ax,
        xticklabels=False,
        yticklabels=False,
        cbar_kws={"label": "dB"},
        **kwargs,
    )
    ax.xaxis.set_major_locator(mticker.MultipleLocator(3))
    ax.yaxis.set_major_locator(mticker.MultipleLocator(50))
    plt.savefig(fname)
    plt.close()


def save_heatmaps(data, center_frequencies, path: Path, global_scale=False):
    if not os.path.exists(path):
        os.makedirs(path)
    kwargs = {"vmin": np.min(data), "vmax": np.max(data)} if global_scale else {}
    # kwargs = {"vmin": -16, "vmax": 0} if global_scale else {}
    for i, slice in enumerate(data):
        _save_heatmap(
            slice,
            path / f"{i:03d}.png",
            f"{center_frequencies[i]}Hz",
            **kwargs,
        )


def generate_gif(path: Path, gif_path: Path, fps=10):
    if not os.path.exists(gif_path.parent):
        os.makedirs(gif_path.parent)
    images = []
    for filename in sorted(os.listdir(path)):
        if filename.endswith(".png"):
            images.append(imageio.imread(path / filename))
    imageio.mimsave(gif_path, images, fps=fps)
