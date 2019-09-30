import math
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import gridspec


def GOplotFix(Ptitle, Pfile, Pdata, Xmin, Xmax, Smin, Smax, Plegend=False):

    titles = [i[0] for i in Pdata]
    values = [abs(math.log10(i[2])) for i in Pdata]
    colors_v = [i[1] for i in Pdata]
    Xminn = abs(math.log10(Xmin))
    Xmaxn = abs(math.log10(Xmax))

    normalize = matplotlib.colors.Normalize(
        vmin=Smin, vmax=Smax)

    def size_normalize(s): return normalize(s)*500+25

    cmap = matplotlib.colors.LinearSegmentedColormap.from_list(
        "", [[0, "blue"], [1, "red"], ])
    size = [size_normalize(value) for value in colors_v]

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
                            color=sc.cmap(normalize(i)))
                for i in size_legend_ticks
            ],
            size_legend_ticks_label,
            scatterpoints=1,
            labelspacing=1.5,
            borderpad=1,
            #loc="upper right",
            bbox_to_anchor=(1.5, 1),
            title="Fold Enrichment"
        )

    plt.yticks(fontsize=20, fontname="Arial")
    plt.xticks(fontname="Arial")
    plt.xlabel("FDR (-log10)", fontname="Arial")
    plt.title(Ptitle, fontsize=24, fontname="Arial")

    plt.ylim(-1, len(Pdata))
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


def GOplot(Ptitle, Pfile, Pdata):

    titles = [i[0] for i in Pdata]
    values = [abs(math.log10(i[2])) for i in Pdata]
    colors_v = [i[1] for i in Pdata]

    normalize = matplotlib.colors.Normalize(
        vmin=min(colors_v), vmax=max(colors_v))

    def size_normalize(s): return normalize(s)*500+25

    cmap = matplotlib.colors.LinearSegmentedColormap.from_list(
        "", [[0, "blue"], [1, "red"], ])
    colors = [cmap(normalize(value)) for value in colors_v]
    size = [size_normalize(value) for value in colors_v]

    fig = plt.figure(figsize=(10, 10))
    gs = gridspec.GridSpec(1, 3, width_ratios=[1, 2, 0.2])
    ax = plt.subplot(gs[1])
    sc = ax.scatter(values, titles, c=colors_v, s=size, cmap=cmap)
    ax.grid()

    # cbar = plt.colorbar(sc)
    # cbar_ticks = [
    #     min(colors_v),
    #     min(colors_v) + (max(colors_v)-min(colors_v)) * 0.1,
    #     min(colors_v) + (max(colors_v)-min(colors_v)) * 0.2,
    #     min(colors_v) + (max(colors_v)-min(colors_v)) * 0.3,
    #     min(colors_v) + (max(colors_v)-min(colors_v)) * 0.4,
    #     min(colors_v) + (max(colors_v)-min(colors_v)) * 0.5,
    #     min(colors_v) + (max(colors_v)-min(colors_v)) * 0.6,
    #     min(colors_v) + (max(colors_v)-min(colors_v)) * 0.7,
    #     min(colors_v) + (max(colors_v)-min(colors_v)) * 0.8,
    #     min(colors_v) + (max(colors_v)-min(colors_v)) * 0.9,
    #     max(colors_v),
    # ]
    # cbar.set_ticks(cbar_ticks)
    # cbar.set_ticklabels([f"{i:.0f}" for i in cbar_ticks])
    # cbar.set_label("Fold Enrichment")

    if len(Pdata) > 3:
        size_legend_ticks = [
            min(colors_v),
            min(colors_v) + (max(colors_v)-min(colors_v)) * 0.333,
            min(colors_v) + (max(colors_v)-min(colors_v)) * 0.666,
            max(colors_v),
        ]
    elif len(Pdata) == 3:
        size_legend_ticks = [
            min(colors_v),
            min(colors_v) + (max(colors_v)-min(colors_v)) * 0.5,
            max(colors_v),
        ]
    else:
        size_legend_ticks = [
            min(colors_v),
            max(colors_v),
        ]
    if max(colors_v)-min(colors_v) < 5 or max(colors_v) < 10:
        size_legend_ticks_label = [f"{i:.1f}" for i in size_legend_ticks]
    else:
        size_legend_ticks_label = [f"{i:.0f}" for i in size_legend_ticks]
    legend = ax.legend(
        [
            plt.scatter([], [], s=size_normalize(i),
                        color=sc.cmap(normalize(i)))
            for i in size_legend_ticks
        ],
        size_legend_ticks_label,
        scatterpoints=1,
        labelspacing=1.5,
        borderpad=1,
        #loc="upper right",
        bbox_to_anchor=(1.45, 1),
        title="Fold Enrichment"
    )

    plt.xlabel("FDR (-log10)")
    plt.title(Ptitle)

    plt.ylim(-1, len(Pdata))
    plt.xlim(min(values)-(max(values)-min(values))*0.1,
             max(values)+(max(values)-min(values))*0.1)
    fig_h = len(Pdata)*0.5+1
    if fig_h < 2:
        fig_h == 2
    fig.set_size_inches(8, fig_h)

    plt.savefig(Pfile, dpi=300, bbox_inches='tight')
    # plt.show()
    plt.close()


if __name__ == "__main__":
    data = [
        ["chaperone-mediated protein folding", 43.47, 3.07E-10],
        ["protein folding", 16.72, 1.54E-10],
        #["cellular response to heat", 31.48, 5.38E-06],
        #["response to heat", 30.43, 4.95E-06],
        #["cellular response to unfolded protein", 29.64, 5.06E-04],
        #["response to topologically incorrect protein", 19.76, 2.52E-03],
        #["response to unfolded protein", 29.64, 6.07E-04],
    ]
    GOplot("PANTHER GO-Slim Biological Process", "test.png", data)
