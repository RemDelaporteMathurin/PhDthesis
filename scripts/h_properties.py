import h_transport_materials as htm
from h_transport_materials.plotting import *
import matplotx
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

with plt.style.context(matplotx.styles.dufte):

    fig, axs = plt.subplots(3, 1, figsize=(7, 9), sharex=True)

    plt.sca(axs[0])
    plt.yscale("log")

    tungsten_diffusivities = (
        htm.diffusivities.filter(material="tungsten")
        .filter(exclude=True, author=["holzner"], isotope=["h"])
        .filter(exclude=True, author=["esteban"], isotope=["d", "h"])
    )

    for property in tungsten_diffusivities:
        plot(property)

    plt.ylabel("W diffusivity (m$^2$ s$^{-1}$)")
    plt.xlabel("")
    line_labels(fontsize=10)

    # plt.ylabel("Diffusivity \n (m$^2$ s$^{-1}$)")
    # plt.ylim(bottom=1e-15)

    plt.sca(axs[1])
    for property in htm.diffusivities.filter(material="copper").filter(
        exclude=True, author="katz", isotope=["h", "d"]
    ):
        plot(property)

    plt.yscale("log")
    line_labels(fontsize=10)
    plt.ylabel("Cu diffusivity (m$^2$ s$^{-1}$)")
    plt.xlabel("")

    plt.sca(axs[2])
    cucrzr_diffusivities = htm.diffusivities.filter(material="cucrzr").filter(
        author="serra", isotope=["t", "h"], exclude=True
    )
    for property in cucrzr_diffusivities:
        if "refitted" not in property.name:
            plot(property)
    plt.yscale("log")
    line_labels(fontsize=10)
    plt.ylabel("CuCrZr diffusivity (m$^2$ s$^{-1}$)")

    plt.tight_layout()
    plt.show()


with plt.style.context(matplotx.styles.dufte):

    fig, axs = plt.subplots(3, 1, figsize=(7, 9), sharex=True, sharey=True)

    plt.sca(axs[0])
    plt.yscale("log")

    tungsten_solubilities = htm.solubilities.filter(material="tungsten")

    for property in tungsten_solubilities:
        plot(property)

    plt.ylabel("W solubility \n (m$^{-3}$ Pa$^{-0.5}$)")
    plt.xlabel("")
    line_labels(fontsize=10)

    # plt.ylabel("Diffusivity \n (m$^2$ s$^{-1}$)")
    # plt.ylim(bottom=1e-15)

    plt.sca(axs[1])
    for property in htm.solubilities.filter(material="copper"):
        plot(property)

    plt.yscale("log")
    line_labels(fontsize=10)
    plt.ylabel("Cu solubility \n (m$^{-3}$ Pa$^{-0.5}$)")
    plt.xlabel("")

    plt.sca(axs[2])
    cucrzr_solubilities = htm.solubilities.filter(material="cucrzr").filter(
        author="serra", isotope=["t", "h"], exclude=True
    )
    for property in cucrzr_solubilities:
        if "refitted" not in property.name:
            plot(property)
    plt.yscale("log")
    line_labels(fontsize=10)
    # plt.ylim(1e20, 1e22)
    plt.ylabel("CuCrZr solubility \n (m$^{-3}$ Pa$^{-0.5}$)")

    plt.gca().set_xticks(plt.gca().get_xticks()[::2])

    plt.tight_layout()
    plt.show()
