import matplotlib.pyplot as plt
import numpy as np

# plt.rc('text', usetex=True)
plt.rc("font", family="sans-serif", size=22)


def u(x):
    return 2 + 0.5 * np.sin(x)


x = np.linspace(0, 2 * np.pi)

# plot real solution
plt.plot(x, u(x))

# plot approximated solution
x_approx = np.linspace(0, 2 * np.pi, num=8)
plt.plot(x_approx, u(x_approx), linestyle="dashed")

# plot basis functions
for i in range(len(x_approx)):
    y_basis = np.zeros(x_approx.shape)
    y_basis[i] = 1
    if i == 3:
        plt.plot(x_approx, y_basis, color="tab:blue", zorder=10, linewidth=3)
    else:
        plt.plot(x_approx, y_basis, color="black", alpha=0.7)

    plt.vlines(x_approx[i], 0, u(x_approx[i]), linestyles="dashed", colors="grey")

    if i == 3:
        plt.annotate(
            "$u_" + "{}".format(i) + "$", (x_approx[i], u(x_approx[i]) + 0.1), alpha=0.7
        )
        plt.annotate(r"$\phi_" + "{}".format(i) + "$", (x_approx[i] - 0.05, 0.5))
        plt.fill_between(x_approx, y_basis, alpha=0.3, color="tab:blue")

plt.annotate("$u$", (0.35 * np.pi, u(2) + 0.1), color="tab:blue")
plt.annotate("$u_\mathrm{approx}$", (1.5 * np.pi, u(7) - 0.2), color="tab:orange")

plt.xlabel("$x$")
plt.yticks([1, u(0)], ["1", "$u_0$"], alpha=0.7)
plt.xticks([], [])
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)
plt.xlim(left=0)
plt.ylim(bottom=0)
plt.show()
