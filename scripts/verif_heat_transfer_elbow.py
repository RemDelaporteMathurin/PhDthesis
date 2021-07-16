import FESTIM
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from fenics import *
from mshr import Rectangle, Circle, generate_mesh
from scipy.stats import linregress

omega = 1
pi = 3.14159265358979
u_exact = sp.sin(omega*pi*FESTIM.x)*sp.sin(omega*pi*FESTIM.y)


def thermal_cond_fun(T):
    return 2 + T**2


thermal_cond = thermal_cond_fun(u_exact)

u_x = sp.diff(u_exact, FESTIM.x)
u_y = sp.diff(u_exact, FESTIM.y)

f = -sp.diff(thermal_cond*u_x, FESTIM.x) - sp.diff(thermal_cond*u_y, FESTIM.y)
print(sp.latex(sp.simplify(f)))
parameters = {
    "materials": [
        {
            "D_0": 1,
            "E_D": 0,
            "thermal_cond": thermal_cond_fun,
            "id": 1
        },
    ],
    "boundary_conditions": [],
    "temperature": {
        "type": "solve_stationary",
        "boundary_conditions": [
            {
                "type": "dc",
                "value": u_exact,
                "surfaces": [1],
            },
        ],
        "source_term": [
            {
                "value": f,
                "volume": 1
            },
        ]
    },
    "traps": [],
    "exports": {},
    "solving_parameters": {
        "type": "solve_stationary",
        "newton_solver": {
            "absolute_tolerance": 1e-10,
            "relative_tolerance": 1e-10,
            "maximum_iterations": 15
        },
    }
}


def create_mesh(N):
    # creating a mesh with FEniCS
    lx = ly = 1
    cx = cy = lx / 2.0
    radius = 0.15
    # res = 40
    rectangle = Rectangle(Point(0, 0), Point(lx, ly))
    hole = Rectangle(Point(lx/2, ly/2), Point(lx, ly))
    mesh = generate_mesh(rectangle - hole, N)
    # nx = ny = N
    # mesh = UnitSquareMesh(nx, ny)

    # marking physical groups (volumes and surfaces)
    volume_markers = MeshFunction("size_t", mesh, mesh.topology().dim())
    volume_markers.set_all(1)

    surface_markers = MeshFunction("size_t", mesh, mesh.topology().dim() - 1)
    surface_markers.set_all(0)  # gamma_circle
    boundary = CompiledSubDomain('on_boundary')
    boundary.mark(surface_markers, 1)
    return mesh, volume_markers, surface_markers


def solve(N):
    mesh, vm, sm = create_mesh(N)

    parameters["mesh_parameters"] = {
            "mesh": mesh,
            "meshfunction_cells": vm,
            "meshfunction_facets": sm,
        }
    my_sim = FESTIM.Simulation(parameters)
    my_sim.initialise()

    return my_sim.T, my_sim.V_CG1


def compute_L2_error(N):
    T, V = solve(N)
    u_exact_fun = Expression(sp.printing.ccode(u_exact), degree=6)
    u_exact_fun = interpolate(u_exact_fun, V)
    E = errornorm(u_exact_fun, T, norm_type='L2', degree_rise=3)
    return E


if __name__ == "__main__":
    T, V = solve(128)
    T_exact = Expression(sp.printing.ccode(u_exact), degree=6)
    T_exact = interpolate(T_exact, V)

    plt.figure()
    CF = plot(T, cmap="plasma")
    plt.colorbar(CF)
    for c in CF.collections:
        c.set_edgecolor("face")
    plt.savefig("T.pdf")

    plt.figure()
    CF = plot(T_exact, cmap="plasma")
    plt.colorbar(CF)
    for c in CF.collections:
        c.set_edgecolor("face")
    plt.savefig("T_exact.pdf")

    # E = []
    # N_values = np.array([2, 4, 8, 16, 32, 64, 128])
    # for N in N_values:
    #     E.append(compute_L2_error(N))
    # print(E)
    # plt.loglog(1/N_values, E, marker="+")
    # plt.xlabel("dx")
    # plt.ylabel("L2 error")
    # plt.savefig("out.png")

    # E_P1 = [0.07450902650543327, 0.016092376781255253, 0.004327127438372875, 0.0011100073350497905, 0.0002794618859935794, 6.999139466498881e-05, 1.75057742925809e-05]
    # E_P2 = [0.048168058151553964, 0.001927336172103811, 0.0001437943541900185, 9.513953689764883e-06, 6.044681309358056e-07, 3.795725054155621e-08, 2.3756834300231275e-09]
    # E_P3 = [0.044187320540462045, 0.0014101567867843615, 9.779396089372355e-05, 6.2888082322961795e-06, 3.9600409618333857e-07, 2.4796934487871227e-08, 1.534945641422958e-09]

    # errors = [E_P1, E_P2, E_P3]
    # rates = []
    # plt.figure()
    # for degree in [1, 2, 3]:
    #     res = linregress(np.log10(1/N_values), np.log10(errors[degree-1]))
    #     a = 10**res.intercept
    #     b = res.slope
    #     plt.scatter(1/N_values, errors[degree-1], marker="+")
    #     plt.loglog(1/N_values, a*(1/N_values)**b, linestyle="dashed")
    #     rates.append(b)

    # plt.annotate(
    #     r"$\propto h^{" + "{:.2f}".format(rates[0]) + "}$ (P1)",
    #     (1/N_values[0]*1.1, errors[0][0]),
    #     color="tab:blue")
    # plt.annotate(
    #     r"$\propto h^{" + "{:.2f}".format(rates[1]) + "}$ (P2)",
    #     (1/N_values[0]*1.1, errors[1][0]*0.5),
    #     color="tab:orange")
    # plt.annotate(
    #     r"$\propto h^{" + "{:.2f}".format(rates[2]) + "} $ (P3)",
    #     (1/N_values[0]*1.1, errors[2][0]*0.25),
    #     color="tab:green")

    # plt.xlabel("$h$")
    # plt.ylabel("L2 error")
    # plt.gca().spines['top'].set_visible(False)
    # plt.gca().spines['right'].set_visible(False)
    # plt.savefig("convergence_rate.pdf")
