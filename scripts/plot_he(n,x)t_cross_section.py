import json
import matplotlib.pyplot as plt
import matplotx

with open("He(n,xT).json") as f:
    data = json.load(f)

cross_section = data[0]["cross section"]
energy = data[0]["energy"]

with plt.style.context(matplotx.styles.dufte):
    plt.loglog(energy, cross_section)
    plt.xlabel("Energy (eV)")
    plt.ylabel("Microscopic cross section (barns)")
    plt.annotate("$^3$He(n,T)H", (1e1, 1e3), color="tab:blue")
    plt.tight_layout()
    plt.show()
