import numpy as np
import matplotlib.pyplot as plt
import matplotx

x = np.linspace(0, 10e-9, num=500)
width = 1e-9
imp_depth = 1.5e-9
gaussian_distribution = (
    1 / (width * (2 * np.pi) ** 0.5) * np.exp(-0.5 * ((x - imp_depth) / width) ** 2)
)  # m-1
flux = 5e25  # He/m2/s

gaussian_area = np.trapz(gaussian_distribution, x)

normalised_gaussian = gaussian_distribution / gaussian_area

volumetric_source = flux * normalised_gaussian  # He/m3/s

max_generation_from_decay = 6.5e12  # He/m3/s  from FESTIM sim

with plt.style.context(matplotx.styles.dufte):
    plt.plot(x * 1e9, volumetric_source, label="Direct \n implantation")

    plt.plot(
        [0, 10],
        [max_generation_from_decay] * 2,
        linestyle="dashed",
        label="Max generation \n from T decay",
    )

    plt.yscale("log")
    matplotx.ylabel_top("He generation \n (m$^{-3}$ s$^{-1}$)")
    plt.xlabel("Depth (nm)")
    plt.ylim(bottom=1e10, top=1e35)
    matplotx.line_labels()
    plt.tight_layout()
    plt.show()
