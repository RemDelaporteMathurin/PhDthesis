import numpy as np
import matplotlib.pyplot as plt
import matplotx


def get_fluxes(filename):
    data = np.genfromtxt(filename, names=True, delimiter=",")

    x = data["x"]

    flux_D_atm = data["D_flux_atm"]
    flux_D_ion = data["D_flux_ion"]
    flux_He_atm = data["He_flux_atm"]
    flux_He_ion = data["He_flux_ion"]

    flux_total = flux_D_atm + flux_D_ion + flux_He_atm + flux_He_ion

    return x, flux_D_atm, flux_D_ion, flux_He_atm, flux_He_ion


with plt.style.context(matplotx.styles.dufte):
    fig, axs = plt.subplots(nrows=1, ncols=2, sharey=True)

    plt.sca(axs[0])

    x, flux_D_atm, flux_D_ion, flux_He_atm, flux_He_ion = get_fluxes(
        "2399_inner_target.csv"
    )

    plt.plot(x, flux_D_atm + flux_D_ion, label="D \n atoms + ions", color="tab:blue")
    plt.plot(x, flux_He_atm + flux_He_ion, label="He \n atoms + ions", color="#fd9a21")

    plt.sca(axs[1])
    x, flux_D_atm, flux_D_ion, flux_He_atm, flux_He_ion = get_fluxes(
        "2399_outer_target.csv"
    )

    plt.plot(x, flux_D_atm + flux_D_ion, label="D \n atoms + ions", color="tab:blue")
    plt.plot(x, flux_He_atm + flux_He_ion, label="He \n atoms + ions", color="#fd9a21")

    matplotx.ylabel_top("Particle \n flux (m$^{-2}$ s$^{-1}$)", ax=axs[0])

    axs[0].annotate("Radiation", xy=(0.5, 1), color="tab:blue")
    axs[0].annotate("Particle", xy=(0.120, 5), color="tab:orange")
    axs[0].set_yscale("log")
    axs[0].set_xlabel("Distance IVT")
    axs[1].set_xlabel("Distance OVT (m)")
    matplotx.line_labels(axs[1])
    plt.tight_layout()
    plt.show()
