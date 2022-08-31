import numpy as np
import matplotlib.pyplot as plt

k_B = 8.617e-5  # ev/K


def trap_occupancy(p_0, E_p, k_0, E_k, c_m, T):
    p = p_0 * np.exp(-E_p / k_B / T)
    k = k_0 * np.exp(-E_k / k_B / T)
    return 1 / (p / k / c_m + 1)


T = np.linspace(300, 1200, num=300)
c_m = 1e22  # m-3

# trap 1
trap_1_occupancy = trap_occupancy(
    p_0=1e13, E_p=0.87, k_0=8.96e-17, E_k=0.2, c_m=c_m, T=T
)
trap_1_density = 1.1e-3  # at.fr
trap_1_concentration = trap_1_density * trap_1_occupancy

trap_2_occupancy = trap_occupancy(
    p_0=1e13, E_p=1.00, k_0=8.96e-17, E_k=0.2, c_m=c_m, T=T
)
trap_2_density = 4.0e-4  # at.fr
trap_2_concentration = trap_2_density * trap_2_occupancy

# equivalent trap
trap_eq_density = trap_1_density + trap_2_density  # at.fr

trap_eq_occupancy = trap_occupancy(
    p_0=1e13,
    E_p=(0.87 * trap_1_density + 1 * trap_2_density) / trap_eq_density,
    k_0=8.96e-17,
    E_k=0.2,
    c_m=c_m,
    T=T,
)
trap_eq_concentration = trap_eq_density * trap_eq_occupancy

# compute difference
difference = 100 * trap_2_concentration / (trap_1_concentration + trap_2_concentration)

print("Maximum error induced by neglecting trap 2 is {:.0f} %".format(difference.max()))


# PLOTTING

fig, axs = plt.subplots(2, 1, sharex=True)

plt.sca(axs[0])

plt.fill_between(T, 0, trap_1_concentration, label="Trap 1", alpha=0.8)
plt.fill_between(
    T,
    trap_1_concentration,
    trap_1_concentration + trap_2_concentration,
    label="Trap 2",
    alpha=0.8,
)
# plt.plot(T, trap_eq_concentration, label="Trap eq")
# plt.annotate("Equivalent trap", (470, 0.0013), color="tab:blue")

plt.annotate("Trap 1", (320, 0.0005), color="white")
plt.annotate("Trap 2", (320, 0.0012), color="white")

plt.ylabel("Trap concentration (at.fr.)")
plt.ylim(bottom=0)


plt.sca(axs[-1])
plt.plot(T, difference)
plt.ylim(bottom=0, top=80)

plt.xlabel("T (K)")
plt.ylabel("Error (%) \n (neglecting trap 2)")
plt.tight_layout()

for ax in axs:
    ax.spines.right.set_visible(False)
    ax.spines.top.set_visible(False)

plt.show()


# 2D map

c_m = np.logspace(20, 23)
T = np.linspace(300, 1200)

TT, cc = np.meshgrid(T, c_m)

# trap 1
trap_1_occupancy = trap_occupancy(
    p_0=1e13, E_p=0.87, k_0=8.96e-17, E_k=0.2, c_m=cc, T=TT
)
trap_1_concentration = trap_1_density * trap_1_occupancy

trap_2_occupancy = trap_occupancy(
    p_0=1e13, E_p=1.00, k_0=8.96e-17, E_k=0.2, c_m=cc, T=TT
)
trap_2_concentration = trap_2_density * trap_2_occupancy


# compute difference
difference = 100 * trap_2_concentration / (trap_1_concentration + trap_2_concentration)

CF = plt.contourf(TT, cc, difference, levels=100)
plt.yscale("log")
plt.colorbar(label="Error (%)")
plt.xlabel("T (K)")
plt.ylabel("Mobile concentration (m$^{-3}$)")

for c in CF.collections:
    c.set_edgecolor("face")

plt.show()
