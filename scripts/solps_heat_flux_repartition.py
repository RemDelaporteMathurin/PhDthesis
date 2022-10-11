import numpy as np
import matplotlib.pyplot as plt
import matplotx

W_to_MW = 1e-6

NORMALISE = True

with plt.style.context(matplotx.styles.dufte):
    fig, axs = plt.subplots(nrows=1, ncols=2, sharey=True)

    plt.sca(axs[0])

    data = np.genfromtxt("2399_inner_target.csv", names=True, delimiter=",")

    x = data["x"]

    flux_total = data["Wtot"] * W_to_MW
    flux_particle = data["Wpart"] * W_to_MW
    flux_rad = data["Wrad"] * W_to_MW

    if NORMALISE:
        flux_particle *= 100 / flux_total
        flux_rad *= 100 / flux_total

    plt.stackplot(
        x, flux_rad, flux_particle, labels=["radiation", "particle"], alpha=0.9
    )
    # plt.plot(x, flux_total)

    plt.sca(axs[1])
    data = np.genfromtxt("2399_outer_target.csv", names=True, delimiter=",")

    x = data["x"]

    flux_total = data["Wtot"] * W_to_MW
    flux_particle = data["Wpart"] * W_to_MW
    flux_rad = data["Wrad"] * W_to_MW

    if NORMALISE:
        flux_particle *= 100 / flux_total
        flux_rad *= 100 / flux_total

    plt.stackplot(
        x, flux_rad, flux_particle, labels=["radiation", "particle"], alpha=0.9
    )
    if NORMALISE:
        matplotx.ylabel_top("Repartition \n heat flux (%)", ax=axs[0])
        axs[1].text(1.4, 10, "Radiation", color="tab:blue")
        axs[1].text(1.4, 90, "Particle", color="tab:orange")
    else:
        matplotx.ylabel_top("Heat flux (MW/m$^2$)", ax=axs[0])

        axs[0].annotate("Radiation", xy=(0.5, 1), color="tab:blue")
        axs[0].annotate("Particle", xy=(0.120, 5), color="tab:orange")
    axs[0].set_xlabel("Distance IVT (m)")
    axs[1].set_xlabel("Distance OVT (m)")
    plt.tight_layout()
    plt.show()
