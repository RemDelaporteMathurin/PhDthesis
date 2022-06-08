"""
This script has to be executed at the root of the directory
"""

import matplotlib.pyplot as plt
import numpy as np
from divHretention import Exposition
import matplotx

number = 2399
filename_inner = (
    "{}_inner_target.csv".format(
        number, number
    )
)
filename_outer = (
    "{}_outer_target.csv".format(
        number, number
    )
)
res_inner, res_outer = [], []

exp_out = Exposition(filename_outer, filetype="ITER")

exp_in = Exposition(filename_inner, filetype="ITER")

ion_colour = "tab:orange"
atom_colour = "tab:blue"
with plt.style.context(matplotx.styles.dufte):

    fig, (axs_top, axs_mid, axs_bot) = plt.subplots(
        3,
        2,
        sharey="row",
        sharex="col",
        figsize=[6.4, 8],
        gridspec_kw={
            "width_ratios": [
                max(exp_in.arc_length) - min(exp_in.arc_length),
                max(exp_out.arc_length) - min(exp_out.arc_length),
            ]
        },
    )

    W_to_MW = 1e-6

    axs_top[0].plot(exp_in.arc_length, exp_in.net_heat_flux * W_to_MW, color="black")
    axs_top[1].plot(exp_out.arc_length, exp_out.net_heat_flux * W_to_MW, color="black")

    axs_mid[0].plot(exp_in.arc_length, exp_in.atom_flux, color=atom_colour)
    axs_mid[0].plot(exp_in.arc_length, exp_in.ion_flux, color=ion_colour)
    axs_mid[1].plot(exp_out.arc_length, exp_out.atom_flux, color=atom_colour)
    axs_mid[1].plot(exp_out.arc_length, exp_out.ion_flux, color=ion_colour)

    axs_bot[0].plot(exp_in.arc_length, exp_in.E_ion, color=ion_colour)
    axs_bot[0].plot(exp_in.arc_length, exp_in.E_atom, color=atom_colour)
    axs_bot[1].plot(exp_out.arc_length, exp_out.E_ion, color=ion_colour)
    axs_bot[1].plot(exp_out.arc_length, exp_out.E_atom, color=atom_colour)

    axs_mid[0].annotate("Ions", (0.25, 0.5e24), color=ion_colour)
    axs_mid[0].annotate("Atoms", (0.15, 1e24), color=atom_colour)

    axs_top[0].set_title("Inner target")
    axs_top[1].set_title("Outer target")

    sp_in_x, sp_in_y = (
        exp_in.arc_length[np.argmax(exp_in.net_heat_flux)],
        exp_in.net_heat_flux.max() * W_to_MW,
    )
    sp_out_x, sp_out_y = (
        exp_out.arc_length[np.argmax(exp_out.net_heat_flux)],
        exp_out.net_heat_flux.max() * W_to_MW,
    )
    axs_top[0].annotate(
        "Strike point",
        (sp_in_x, sp_in_y),
        (0.3, 6),
        va="center",
        arrowprops={"arrowstyle": "->"},
    )
    axs_top[1].annotate(
        "Strike point",
        (sp_out_x, sp_out_y),
        (0.3, 6),
        va="center",
        arrowprops={"arrowstyle": "->"},
    )

    axs_top[0].set_ylabel("Heat flux \n (MW m$^{-2}$)")
    axs_mid[0].set_ylabel("Particle flux \n (m$^{-2}$ s$^{-1}$)")
    axs_bot[0].set_ylabel("Incident energy \n (eV)")

    # add middle big axis for common x label
    ax = fig.add_subplot(111, frameon=False)
    plt.tick_params(
        labelcolor="none",
        which="both",
        top=False,
        bottom=False,
        left=False,
        right=False,
    )
    ax.set_xticks([])
    ax.set_yticks([])

    plt.xlabel("Distance along divertor (m)", labelpad=40)
    axs_bot[0].set_yscale("log")
    axs_top[0].set_ylim(bottom=0, top=8)
    axs_mid[0].set_ylim(bottom=0)
    axs_bot[0].set_ylim(bottom=1e-1)

    plt.tight_layout()
    # plt.colorbar(sm, label="Divertor neutral pressure (Pa)", ax=ax2)
    # plt.savefig("../Figures/ITER/fluxes_distribution.svg")
    # plt.savefig("../Figures/ITER/fluxes_distribution.pdf")

    plt.show()
