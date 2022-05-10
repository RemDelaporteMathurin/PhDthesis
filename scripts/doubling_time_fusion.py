import numpy as np
import matplotlib.pyplot as plt
import matplotx
from labellines import labelLines

t = np.linspace(0, 70, num=500)  # years


def fusion_power(t, doubling_time, fp_0):
    return 2 ** (t / doubling_time) * fp_0


fp_0 = 1e-3  # TW
doubling_times = [2, 5, 10]  # years

with plt.style.context(matplotx.styles.dufte):
    plt.figure(figsize=(6.4, 4))
    lines = []
    for doubling_time in doubling_times:
        (l,) = plt.plot(
            t,
            fusion_power(t, doubling_time, fp_0),
            label=r"$\tau_2 =" + "{:.0f}".format(doubling_time) + "$y",
        )
        lines.append(l)
    plt.xlabel("Time after first reactor (years)")
    matplotx.ylabel_top("Maximum fusion \n power (TW)")
    labelLines(lines)
    plt.ylim(0, 1.1)
    plt.xticks([0, 20, 40, 60])
    plt.tight_layout()
    plt.show()
