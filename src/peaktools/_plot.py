import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_heatmap_and_profile(
    matrix_file: str,
    output_heatmap: str,
    output_profile: str,
    vmin: int = 0,
    vmax: int = None,
    cmap: str = "Purples",
):
    """Plot heatmap and profile from csv file.

    Args:
        matrix_file (str): csv file containing the matrix data.
        output_heatmap (str): Output heatmap pdf file.
        output_profile (str): Output profile pdf file.
        vmin (int, optional): Lower boundary of scale bar. Defaults to 0.
        vmax (int, optional): Upper boundary of scale bar. Defaults to None.
        cmap (str, optional): Color theme of heatmap. Defaults to "Purples".
    """
    df = pd.read_csv(matrix_file)

    # heatmap plot
    plt.rcParams["figure.figsize"] = [5, 10]
    plt.rcParams["figure.autolayout"] = True

    if not vmax:
        vmax = np.quantile(df.iloc[:, 6:].values, 0.99)
    p1 = sns.heatmap(df.iloc[:, 6:], vmin=vmin, vmax=vmax, cmap=cmap, xticklabels=False, yticklabels=False)
    fig_p1 = p1.get_figure()
    fig_p1.savefig(output_heatmap, dpi=300)
    fig_p1.clf()

    a = df.iloc[:, 6:].sum(0) / 61

    # profile plot
    plt.rcParams["figure.figsize"] = [5, 5]
    plt.rcParams["figure.autolayout"] = True

    p2 = sns.lineplot(a)
    p2.set_xticklabels([])
    fig_p2 = p2.get_figure()
    fig_p2.savefig(output_profile, dpi=300)
    fig_p2.clf()