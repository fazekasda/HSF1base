import math
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import gridspec


def GOplotFix(Ptitle, Pfile, Pdata, Xmin, Xmax, Smin, Smax, Plegend=False):

    titles = [i[3] for i in Pdata]
    labels = [i[0] if i[0] != "---" else "" for i in Pdata]
    values = [abs(math.log10(i[2])) if i[0] != "---" else 0 for i in Pdata]
    Xminn = abs(math.log10(Xmin))
    Xmaxn = abs(math.log10(Xmax))

    normalize = matplotlib.colors.Normalize(
        vmin=Smin, vmax=Smax)

    def size_normalize(s): return normalize(s)*500+25

    cmap = matplotlib.colors.LinearSegmentedColormap.from_list(
        "", [[0, "blue"], [1, "red"], ])
    size = [size_normalize(i[1]) if i[0] != "---" else 0 for i in Pdata]
    colors_v = [cmap(normalize(i[1])) for i in Pdata]

    fig = plt.figure(figsize=(10, 10))
    if Plegend:
        gs = gridspec.GridSpec(1, 3, width_ratios=[3, 3, 1])
    else:
        gs = gridspec.GridSpec(1, 2, width_ratios=[1, 1])
    ax = plt.subplot(gs[1])
    sc = ax.scatter(values, titles, c=colors_v, s=size, cmap=cmap)
    ax.grid()

    if len(Pdata) > 3:
        size_legend_ticks = [
            Smin,
            Smin + (Smax-Smin) * 0.333,
            Smin + (Smax-Smin) * 0.666,
            Smax,
        ]
    elif len(Pdata) == 3:
        size_legend_ticks = [
            Smin,
            Smin + (Smax-Smin) * 0.5,
            Smax,
        ]
    else:
        size_legend_ticks = [
            Smin,
            Smax,
        ]
    if Smax-Smin < 5 or Smax < 10:
        size_legend_ticks_label = [f"{i:.1f}" for i in size_legend_ticks]
    else:
        size_legend_ticks_label = [f"{i:.0f}" for i in size_legend_ticks]
    if Plegend:
        legend = ax.legend(
            [
                plt.scatter([], [], s=size_normalize(i),
                            color=cmap(normalize(i)))
                for i in size_legend_ticks
            ],
            size_legend_ticks_label,
            scatterpoints=1,
            labelspacing=1.5,
            borderpad=1,
            # loc="upper right",
            bbox_to_anchor=(1.5, 1),
            title="Fold Enrichment"
        )
    ax.set_xticks(
        [i for i in range(int(Xmaxn), int((Xminn+1)*1.1), int((Xminn-Xmaxn)/5))])
    plt.yticks(titles, labels, fontsize=20, fontname="Arial")
    plt.xticks(fontname="Arial")
    for i in Pdata:
        if i[0] == "---":
            ax.yaxis.get_major_ticks()[i[3]].draw = lambda *args: None

    plt.xlabel("FDR (-log10)", fontname="Arial")
    plt.title(Ptitle, fontsize=24, fontname="Arial")

    plt.ylim(len(Pdata), -1)
    plt.xlim(
        Xmaxn+(Xmaxn-Xminn)*0.1,
        Xminn-(Xmaxn-Xminn)*0.1)
    fig_h = len(Pdata)*0.5+1
    # if fig_h < 2:
    #     fig_h == 2
    fig.set_size_inches(12, fig_h)

    plt.savefig(Pfile, dpi=300, bbox_inches='tight')
    # plt.show()
    plt.close()
