from pyenergydiagrams import State, Diagram
import matplotx
import matplotlib.pyplot as plt

energies = [-0.5, -0.5, -0.5, 0.2, -1, 1.3, *[0, 1] * 10]


states = [State(E=E) for E in energies]

adsorption_site = states[4]
first_solution_site = states[6]

trap_1 = states[12]
trap_2 = states[22]
trap_1.E = -2.5
trap_2.E = -1.5
my_diagram = Diagram(states)
# my_diagram_2 = Diagram([State(1.5), State(1.5), State(1.5), State(1.5), State(-1)])
with plt.style.context(matplotx.styles.dufte):
    plt.figure(figsize=(10, 4.8))
    plt.plot(my_diagram.x, my_diagram.y)
    # plt.plot(my_diagram_2.x, my_diagram_2.y)

    my_diagram.add_dotted_line(trap_2, dx_right=2)
    my_diagram.add_dotted_line(states[states.index(trap_2) + 1], dx_right=1)
    my_diagram.add_arrow(states[states.index(trap_2) + 1], trap_2, "$E_{\mathrm{b},2}$")
    my_diagram.add_arrow(
        states[states.index(trap_2) + 2],
        states[states.index(trap_2) + 3],
        "$E_{\mathrm{k},2}$",
        loc_text="top",
    )

    my_diagram.add_dotted_line(states[15], dx_right=1)
    my_diagram.add_arrow(states[16], states[17], "$E_\mathrm{D}$", loc_text="top")

    my_diagram.add_dotted_line(trap_1, dx_right=2)
    my_diagram.add_dotted_line(states[states.index(trap_1) + 1], dx_right=1)
    my_diagram.add_arrow(states[states.index(trap_1) + 2], trap_1, "$E_{\mathrm{b},1}$")
    my_diagram.add_arrow(
        states[states.index(trap_1) + 2],
        states[states.index(trap_1) + 3],
        "$E_{\mathrm{k},1}$",
        loc_text="top",
    )

    my_diagram.add_dotted_line(
        states[states.index(first_solution_site) - 1], dx_right=1
    )
    my_diagram.add_arrow(
        first_solution_site,
        states[states.index(first_solution_site) - 1],
        "$E_{\mathrm{bs}}$",
        loc_text="top",
    )

    my_diagram.add_dotted_line(
        states[states.index(adsorption_site) - 1], dx_right=1, dx_left=1
    )
    my_diagram.add_arrow(
        adsorption_site,
        states[states.index(adsorption_site) - 1],
        "$E_{\mathrm{recomb}}$",
        loc_text="bottom",
    )

    my_diagram.add_dotted_line(adsorption_site, dx_right=1)
    my_diagram.add_arrow(
        states[states.index(first_solution_site) - 1],
        adsorption_site,
        "$E_{\mathrm{A}}$",
        loc_text="middle-right",
    )
    my_diagram.add_arrow(
        states[states.index(adsorption_site) - 2],
        states[states.index(adsorption_site) - 1],
        "$E_{\mathrm{diss}}$",
        loc_text="top",
    )

    plt.ylim(-3, 2)
    plt.xticks([])
    plt.yticks([])
    plt.tight_layout()
    plt.show()
