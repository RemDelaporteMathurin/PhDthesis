import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation
import matplotx
from matplotlib.ticker import FormatStrFormatter

nb_frames_still_beg = 200
nb_frames_still_end = 100

y_lim_still_beginning = np.ones(nb_frames_still_beg) * 30
y_lim = np.linspace(30, 750, num=50)
y_lim_still = np.ones(nb_frames_still_end) * 750

y_lim = np.concatenate([y_lim_still_beginning, y_lim, y_lim_still])

x_lim_still_beginning = np.ones(nb_frames_still_beg) * 2
x_lim = np.linspace(2, 5, num=50)
x_lim_still = np.ones(nb_frames_still_end) * 5
x_lim = np.concatenate([x_lim_still_beginning, x_lim, x_lim_still])

with plt.style.context(matplotx.styles.dufte_bar):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    pos = [-1.5, 0, 1.5]
    labels = ["calculated", r"80 % error", r"50 % Tritium"]
    (bar) = plt.bar(pos, [14, 14 * 1.8, 14 * 1.8 * 0.5])
    plt.xticks(pos, labels)
    ax.set_ylim(0, y_lim[0])
    ax.set_xlim(-x_lim[0], x_lim[0])
    # matplotx.show_bar_values("{:.0f} g")
    plt.hlines(700, -4, 4, colors="tab:green", linestyles="dashed")
    plt.annotate("ITER safety limit", xy=(0, 725), color="tab:green", ha="center")
    plt.gca().yaxis.set_major_formatter(FormatStrFormatter("%d g"))


def update(i):
    ax.set_ylim(0, y_lim[i])
    ax.set_xlim(-x_lim[i], x_lim[i])
    if i > nb_frames_still_beg:
        for child in ax.get_children():
            if isinstance(child, matplotlib.text.Text):
                if child.get_text() != "ITER safety limit":
                    child.set(visible=False)
    if i > nb_frames_still_beg + 15:
        plt.xticks([])


ani = mpl.animation.FuncAnimation(
    fig, update, frames=y_lim.size, blit=False, repeat=False
)
plt.tight_layout()
ani.save("animation_divertor_inventories.gif", writer="imagemagick", fps=60)
# plt.show()
