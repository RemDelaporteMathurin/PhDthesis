import matplotlib.pyplot as plt
import numpy as np
import matplotx

data = np.genfromtxt("data.csv", delimiter=",", dtype=str)


def extract_dataset(header: str):
    index_dataset = np.where(data[00] == header)
    x = data[2:, index_dataset[0]]
    y = data[2:, index_dataset[0] + 1]
    x[x == ""] = "nan"
    y[y == ""] = "nan"
    x = x.astype(float)
    y = y.astype(float)

    x = np.rint(x)  # make sure x has integers
    return x, y

fontsize = 11
max_x = [7, 8, 4, 10, 3, 5]
extra_x_lim = 1
width_ratios = [x - 2 + extra_x_lim for x in max_x]
with plt.style.context(matplotx.styles.dufte):
    fig, axs = plt.subplots(1, 6, sharey=True, gridspec_kw={'width_ratios': width_ratios}, figsize=(12, 3))

    plt.sca(axs[0])
    C, = plt.plot(*extract_dataset("light_impurities_1"), marker=".")
    O, = plt.plot(*extract_dataset("light_impurities_2"), marker=".")
    plt.xticks(np.arange(1, max_x[0]))
    plt.annotate("Light impurities", (1.2, 1.2), fontsize=fontsize)
    plt.annotate("O", (2, 0.7), ha="center", va="center", color=O.get_color(), fontsize=fontsize)
    plt.annotate("C", (4, 0.15), ha="center", va="center", color=C.get_color(), fontsize=fontsize)

    plt.sca(axs[1])
    VH, = plt.plot(*extract_dataset("VH"), marker=".")
    VCH, = plt.plot(*extract_dataset("VCH"), marker=".")
    VOH, = plt.plot(*extract_dataset("VOH"), marker=".")
    plt.xticks(np.arange(1, max_x[1]))
    plt.annotate("VH", (2, 1.6), ha="center", va="center", color=VH.get_color(), fontsize=fontsize)
    plt.annotate("VCH", (3, 0.9), ha="center", va="center", color=VCH.get_color(), fontsize=fontsize)
    plt.annotate("VOH", (6.5, 0.23), ha="center", va="center", color=VOH.get_color(), fontsize=fontsize)

    plt.sca(axs[2])
    GB, = plt.plot(*extract_dataset("GB"), marker=".")
    GB_vac, = plt.plot(*extract_dataset("GB_vac"), marker=".")
    plt.xticks(np.arange(1, max_x[2]))
    plt.annotate("GB", (1, 1.5), va="center", color=GB.get_color(), fontsize=fontsize)
    plt.annotate("GB + V", (2.3, 0.8), va="center", color=GB_vac.get_color(), fontsize=fontsize)

    plt.xlabel("Number of trapped hydrogen atoms")
    plt.sca(axs[3])
    wo_kink, = plt.plot(*extract_dataset("dislo_wo_kink"), marker=".")
    jogged, = plt.plot(*extract_dataset("jogged_dislo"), marker=".")
    loop, = plt.plot(*extract_dataset("dislocation_loop"), marker=".")
    plt.xticks(np.arange(1, max_x[3]))
    plt.annotate("Dislocation loop", (2.5, 1.8), va="center", color=loop.get_color(), fontsize=fontsize)
    plt.annotate("Jogged dislocation", (4, 1.6), va="center", color=jogged.get_color(), fontsize=fontsize)
    plt.annotate("Dislocation \n w/o kink", (1, 0.4), va="center", color=wo_kink.get_color(), fontsize=fontsize)

    plt.sca(axs[4])
    SIA, = plt.plot(*extract_dataset("SIA"), marker=".")
    plt.xticks(np.arange(1, max_x[4]))
    plt.annotate("SIA", (1, 0.7), va="center", color=SIA.get_color(), fontsize=fontsize)


    plt.sca(axs[5])
    Ni, = plt.plot(*extract_dataset("Nickel"), marker=".")
    Fe, = plt.plot(*extract_dataset("iron"), marker=".")
    Cu, = plt.plot(*extract_dataset("copper"), marker=".")
    plt.xticks(np.arange(1, max_x[5]))
    plt.annotate("Heavy impurities", (1.2, 1.5), fontsize=fontsize)
    plt.annotate("Cu", (1, 0.7), va="center", color=Cu.get_color(), fontsize=fontsize)
    plt.annotate("Fe", (2, 1.2), va="center", color=Fe.get_color(), fontsize=fontsize)
    plt.annotate("Ni", (3, 0.9), va="center", color=Ni.get_color(), fontsize=fontsize)


    for i, ax in enumerate(axs):
        ax.set_xlim(ax.get_xlim()[0] - extra_x_lim/2, ax.get_xlim()[1] + extra_x_lim/2)
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        if i != 0:
            ax.spines['left'].set_visible(False)
            # ax.set_yticks([])

    plt.ylim(bottom=0)
    plt.sca(axs[0])
    matplotx.ylabel_top("Detrapping \n energy (eV)")
    plt.tight_layout()
    plt.show()
