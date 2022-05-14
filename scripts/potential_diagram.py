import numpy as np
import matplotlib.pyplot as plt


def well(x, pos: int, depth: float = 1.5):
    well = np.zeros(x.shape)
    indexes = np.where((x > (pos - 0.5) * np.pi) & (x < (pos + 1.5) * np.pi))
    well[indexes] = depth * (np.sin(x[indexes]) - 1)

    return well


def well_2d(x, y, pos: int, depth: float = 1.5):
    well = np.zeros(x.shape)
    indexes = np.where(
        (x > (pos - 0.5) * np.pi)
        & (x < (pos + 1.5) * np.pi)
        & (y > (pos - 0.5) * np.pi)
        & (y < (pos + 1.5) * np.pi)
    )
    well[indexes] = -depth * ((np.sin(x[indexes]) - 1) * (np.sin(y[indexes]) - 1))

    return well


x = np.linspace(0, 15.5 * np.pi, num=1000)
potential_energy = np.sin(x)

potential_energy += well(x, 3, depth=2.5)
potential_energy += well(x, 9, depth=1)


plt.figure(figsize=(7.5, 4.8))
plt.plot(x, potential_energy)

# well 1
plt.annotate("", xy=(14.2, -1), xytext=(14.2, -6), arrowprops=dict(arrowstyle="<->"))

plt.annotate("", xy=(14.2, 1), xytext=(14.2, -1), arrowprops=dict(arrowstyle="<->"))

# well 2
plt.annotate("", xy=(33, -1), xytext=(33, -3), arrowprops=dict(arrowstyle="<->"))

plt.annotate("", xy=(33, 1), xytext=(33, -1), arrowprops=dict(arrowstyle="<->"))

# E_D
plt.annotate("", xy=(50, 1), xytext=(50, -1), arrowprops=dict(arrowstyle="<->"))

plt.yticks([])
plt.xticks([])
plt.gca().axis("off")
plt.ylim(-7, 1.5)
# plt.show()

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
x = np.linspace(0, 5 * np.pi, num=500)
y = np.linspace(0, 5 * np.pi, num=500)
xx, yy = np.meshgrid(x, y)
potential_energy = np.sin(xx) * np.sin(yy)
potential_energy += well_2d(xx, yy, 3, depth=1.5)

ax.plot_surface(
    xx, yy, potential_energy, linewidth=0, antialiased=False, cmap="viridis"
)
ax.set_zlim(-7, 1.5)
plt.gca().axis("off")
plt.show()
