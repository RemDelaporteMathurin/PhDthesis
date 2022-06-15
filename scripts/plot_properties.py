import h_transport_materials as htm
import matplotlib.pyplot as plt

diffusivity_w = htm.diffusivities.filter(
    material="tungsten", author="fernandez", isotope="h"
)[0]
diffusivity_cu = htm.diffusivities.filter(material="copper", author="reiter")[0]
diffusivity_cucrzr = htm.diffusivities.filter(material="cucrzr", author="serra")[5]

solubility_w = htm.solubilities.filter(material="tungsten", author="frauenfelder")[0]
solubility_cu = htm.solubilities.filter(material="copper", author="reiter")[0]
solubility_cucrzr = htm.solubilities.filter(material="cucrzr", author="serra")[1]


def thermal_cond_W(T):
    return -7.84154e-9 * T**3 + 5.03006e-5 * T**2 - 1.07335e-1 * T + 1.75214e2


def thermal_cond_Cu(T):
    return -3.93153e-08 * T**3 + 3.76147e-05 * T**2 - 7.88669e-02 * T + 4.02301e02


def thermal_cond_CuCrZr(T):
    return 5.25780e-7 * T**3 - 6.45110e-4 * T**2 + 2.57678e-01 * T + 3.12969e2


def rho_cp_W(T):
    return 5.15356e-6 * T**3 - 8.30703e-2 * T**2 + 5.98312e2 * T + 2.48160e6


def rho_cp_Cu(T):
    return 1.68402e-4 * T**3 - 6.14079e-2 * T**2 + 4.67353e2 * T + 3.45899e6


def rho_cp_CuCrZr(T):
    return -1.79134e-4 * T**3 - 1.51383e-1 * T**2 + 6.22091e2 * T + 3.46007e6


grey_W = "tab:grey"
orange_Cu = (228 / 255, 146 / 255, 64 / 255)
yellow_CuCrZr = (180 / 255, 95 / 255, 6 / 255)

fig, axs = plt.subplots(2, 1, sharex=True)

plt.sca(axs[0])
htm.plotting.plot(diffusivity_w, label="W", color=grey_W)
htm.plotting.plot(diffusivity_cu, label="Cu", color=orange_Cu)
htm.plotting.plot(diffusivity_cucrzr, label="CuCrZr", color=yellow_CuCrZr)
plt.xlabel("")
plt.yscale("log")
plt.ylabel("Diffusivity (m$^2$ s$^{-1}$)")
htm.plotting.line_labels()

plt.sca(axs[1])
htm.plotting.plot(solubility_w, label="W", color=grey_W)
htm.plotting.plot(solubility_cu, label="Cu", color=orange_Cu)
htm.plotting.plot(solubility_cucrzr, label="CuCrZr", color=yellow_CuCrZr)
plt.yscale("log")
plt.ylabel("Solubility (m$^{-3}$ Pa$^{-1/2}$)")
htm.plotting.line_labels()

for ax in axs:
    ax.spines.right.set_visible(False)
    ax.spines.top.set_visible(False)
plt.tight_layout()
plt.show()

fig, axs = plt.subplots(2, 1, sharex=True)
