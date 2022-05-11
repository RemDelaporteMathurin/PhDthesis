"""Runs on FESTIM 0.9
"""


import FESTIM as F
import numpy as np

my_model = F.Simulation()

my_model.mesh = F.MeshFromVertices(np.linspace(0, 1.5, num=1000))

my_model.materials = F.Materials([F.Material(id=1, D_0=2, E_D=0.2)])

my_model.traps = F.Traps(
    [F.Trap(k_0=0.01, E_k=0.1, p_0=1, E_p=0.1, materials=1, density=2)]
)

my_model.boundary_conditions = [
    F.DirichletBC(surfaces=1, value=2),
    F.DirichletBC(surfaces=2, value=0),
]

my_model.T = F.Temperature(300)

my_model.dt = F.Stepsize(1)

my_model.settings = F.Settings(
    absolute_tolerance=1e-10, relative_tolerance=1e-10, final_time=2000
)

derived_quantities = F.DerivedQuantities([F.SurfaceFlux("solute", surface=2)])

my_model.exports = F.Exports(
    [
        derived_quantities,
        # F.XDMFExport("solute", checkpoint=False, mode=50),
        # F.XDMFExport("1", checkpoint=False, mode=50),
    ]
)

my_model.initialise()
my_model.run()

import matplotlib.pyplot as plt


def exact_flux(t: np.array, model: F.Simulation):
    c_0 = model.boundary_conditions[0].value
    l = model.mesh.size - model.mesh.start
    T = model.T.T(l / 2)
    mat = model.materials.materials[0]
    D = mat.D_0 * np.exp(-mat.E_D / F.k_B / T)
    trap = model.traps.traps[0]
    k = trap.k_0 * np.exp(-trap.E_k / F.k_B / T)
    p = trap.p_0 * np.exp(-trap.E_p / F.k_B / T)
    n = trap.density[0](l / 2)
    trap_parameter = p / (k * n) + c_0 / n
    # print(trap_parameter)
    # print(c_0 / n)
    D_eff = D / (1 + 1 / trap_parameter)

    m = np.vstack((np.arange(1, 10000),) * t.size)
    summation = (-1) ** m * np.exp(-(m**2) * np.pi**2 * D_eff * t[:, None] / l**2)
    summation = np.sum(summation, axis=1)

    val = c_0 * D / l * (1 + 2 * summation)
    return val


def max_flux(model: F.Simulation):
    l = model.mesh.size - model.mesh.start
    c_0 = model.boundary_conditions[0].value
    mat = model.materials.materials[0]
    T = model.T.T(l / 2)
    D = mat.D_0 * np.exp(-mat.E_D / F.k_B / T)
    return c_0 * D / l


t_final = my_model.settings.final_time

t_2 = np.linspace(0.01, 2000, num=500)

plt.figure(figsize=(6.4, 4))
plt.plot(t_2 / t_final, exact_flux(t_2, my_model) / max_flux(my_model), label="exact")

t = np.array(derived_quantities.data[1:])[:, 0]
flux = -np.array(derived_quantities.data[1:])[:, 1]
plt.plot(t / t_final, flux / max_flux(my_model), label="computed", linestyle="dashed")
plt.ylabel(r"$\varphi / \max{(\varphi)}$")
plt.xlabel("$t/t_f$")
plt.legend()
plt.ylim(0, 1.1)
plt.xlim(0, 1)
plt.gca().spines["right"].set_visible(False)
plt.gca().spines["top"].set_visible(False)
plt.tight_layout()
plt.savefig("mes_festim_effective_diffusion.pdf")
