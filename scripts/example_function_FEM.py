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
plt.plot(x_approx, u(x_approx), linestyle="dashed", marker="+")

# plot basis functions
# for i in range(len(x_approx)):
y_basis = np.zeros(x_approx.shape)
y_basis[3] = 1
plt.plot(x_approx, y_basis, color="tab:blue", zorder=10, linewidth=3)

plt.annotate("$U_i$", (x_approx[3], u(x_approx[3]) + 0.1), alpha=0.7, ha="center")
plt.annotate(
    r"$\phi_i$",
    (x_approx[3] - 0.05, 1.15),
    color="tab:blue",
)
plt.fill_between(x_approx, y_basis, alpha=0.3, color="tab:blue")

plt.annotate("$u$", (0.35 * np.pi, u(2) + 0.1), color="tab:blue")
plt.annotate("$u_h$", (1.5 * np.pi, u(6)), color="tab:orange")

plt.xlabel("$x$")
plt.yticks([0, 1, u(0)], ["0", "1", "$U_0$"], alpha=0.7)
plt.xticks([], [])
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["bottom"].set_visible(False)
plt.gca().spines["right"].set_visible(False)
plt.xlim(left=0)
plt.ylim(bottom=-0.1)
plt.show()
