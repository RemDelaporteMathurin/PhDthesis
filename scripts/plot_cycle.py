import matplotlib.pyplot as plt
import matplotx

t = [0, 100, 500, 600, 1600]
flux = [0, 1, 1, 0, 0]

plt.figure(figsize=(8, 3))

plt.plot(t, flux)

plt.vlines(t[1:-1], ymin=0, ymax=1, color="tab:grey", linestyles="dashed")
plt.annotate("Ramp-up", (50, 1.05), ha="center")
plt.annotate("Plateau", (300, 1.05), ha="center")
plt.annotate("Ramp-down", (550, 1.05), ha="center")
plt.annotate("Rest", (1000, 1.05), ha="center")
plt.xticks(t)
plt.yticks([])
plt.xlabel("Cycle time (s)")
matplotx.ylabel_top(r"$\varphi_\mathrm{heat}$" + "\n" + r"$\varphi_\mathrm{imp}$")
plt.gca().yaxis.label.set_size(13)
plt.gca().spines.right.set_visible(False)
plt.gca().spines.top.set_visible(False)
plt.tight_layout()
plt.show()
