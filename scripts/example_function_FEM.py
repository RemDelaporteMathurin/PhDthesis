import matplotlib.pyplot as plt
import numpy as np

# plt.rc('text', usetex=True)
plt.rc('font', family='sans-serif', size=22)


def u(x):
    return 2 + 0.5*np.sin(x)


x = np.linspace(0, 2*np.pi)

# plot real solution
plt.plot(x, u(x))

# plot approximated solution
x_approx = np.linspace(0, 2*np.pi, num=8)
plt.plot(x_approx, u(x_approx), linestyle="dashed")

# plot basis functions
for i in range(len(x_approx)):
    y_basis = np.zeros(x_approx.shape)
    y_basis[i] = 1
    plt.plot(x_approx, y_basis, color="black")

    plt.vlines(
        x_approx[i], 0, u(x_approx[i]),
        linestyles="dashed", colors="grey")

    if i in [3, 7]:
        plt.annotate(
            "$u_" + "{}".format(i) + "$",
            (x_approx[i], u(x_approx[i]) + 0.1))
        plt.annotate(
            r"$\phi_" + "{}".format(i) + "$",
            (x_approx[i]-0.05, 0.5))
        plt.fill_between(x_approx, y_basis, alpha=0.3, color="tab:blue")


plt.xlabel("$x$")
plt.ylabel("$u$")
plt.yticks([1, u(0)], ["1", "$u_0$"])
plt.xticks([], [])
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.xlim(left=0)
plt.ylim(bottom=0)
plt.show()
