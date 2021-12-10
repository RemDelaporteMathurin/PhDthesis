import numpy as np
import matplotlib.pyplot as plt

r = np.linspace(1, 20, num=100)

V_0 = 45
R = 4.5
a = 1

Vn = -V_0/(1+np.exp(-(R-r)/a))

e = 1.44
z1 = z2 = 7

Vc = e * z1 * z2 / r

V = Vn + Vc

plt.plot(r, V)
plt.hlines(0, 0, 20, linestyles="dashed", color="grey")
# plt.axis("off")
# plt.savefig('potential_energy.pdf', transparent=True)
plt.ylabel("Potential energy")
plt.xlabel("Distance between nuclei")

plt.annotate("Coulomb barrier", (7, 10), color="grey")
plt.annotate("Attractive \n potential well", (5, -10), color="grey")

plt.gca().set_xticks([])
plt.gca().set_yticks([])
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.show()
