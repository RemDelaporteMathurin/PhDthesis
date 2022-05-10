import numpy as np
import matplotlib.pyplot as plt
import matplotx
from scipy.interpolate import interp1d


class State:
    def __init__(self, E, copies=3) -> None:
        self.E = E
        self.copies = copies


class Diagram:
    def __init__(self, states) -> None:
        self.states = states
        self.x_raw, self.energies = self.make_x_y_raw()
        self.x, self.y = self.make_curve()

    def make_x_y_raw(self):
        x_raw, y_raw = [], []
        eps = 0.05
        for i, state in enumerate(self.states):
            x_raw += [i + j * eps for j in range(state.copies)]
            y_raw += [state.E] * state.copies
        return x_raw, y_raw

    def make_curve(self, nb_samples=500):
        f = interp1d(self.x_raw, self.energies, kind="quadratic")

        x_new = np.linspace(min(self.x_raw), max(self.x_raw), nb_samples)
        y_smooth = f(x_new)
        return x_new, y_smooth

    def add_arrow(
        self, state1, state2, text="", loc_text="middle-right", kwargs_arrow={}, kwargs_text={}
    ):
        # arrow
        plt.annotate(
            text="",
            xy=(self.states.index(state1), state1.E),
            xytext=(self.states.index(state1), state2.E),
            arrowprops=dict(arrowstyle="<->"),
            **kwargs_arrow
        )

        if loc_text == "middle-right":
            xytext = (self.states.index(state1) + 0.1, (state1.E + state2.E) / 2)
            ha = "left"
        elif loc_text == "middle-left":
            xytext = (self.states.index(state1) - 0.1, (state1.E + state2.E) / 2)
            ha = "right"
        elif loc_text == "top":
            xytext = (self.states.index(state1), (state1.E + state2.E)/2 + abs(state1.E - state2.E)/2 + 0.1)
            ha = "center"
        elif loc_text == "bottom":
            xytext = (self.states.index(state1), (state1.E + state2.E) / 2 - abs(state1.E - state2.E)/2 - 0.1)
            ha = "center"

        # text
        plt.annotate(
            text=text,
            xy=xytext,
            ha=ha,
            va="center",
            **kwargs_text
        )

    def add_dotted_line(self, state, dx_left=0, dx_right=0, **kwargs):
        index = self.states.index(state)
        plt.hlines(
            y=state.E,
            xmin=index - dx_left,
            xmax=index + dx_right,
            linestyles="dashed",
            **kwargs
        )


energies = [-0.5, 0.2, -1, 1.3, *[0, 1] * 12]


states = [State(E=E) for E in energies]

states[10].E = -2.5
states[20].E = -1.5
my_diagram = Diagram(states)
with plt.style.context(matplotx.styles.dufte):
    plt.figure(figsize=(10, 4.8))
    plt.plot(my_diagram.x, my_diagram.y)

    my_diagram.add_dotted_line(states[20], dx_right=2)
    my_diagram.add_dotted_line(states[21], dx_right=1)
    my_diagram.add_arrow(states[22], states[20], "$E_{\mathrm{b},2}$")
    my_diagram.add_arrow(states[22], states[23], "$E_{\mathrm{k},2}$", loc_text="top")

    my_diagram.add_dotted_line(states[15], dx_right=1)
    my_diagram.add_arrow(states[16], states[17], "$E_\mathrm{D}$", loc_text="top")

    my_diagram.add_dotted_line(states[10], dx_right=2)
    my_diagram.add_dotted_line(states[11], dx_right=1)
    my_diagram.add_arrow(states[12], states[10], "$E_{\mathrm{b},1}$")
    my_diagram.add_arrow(states[12], states[13], "$E_{\mathrm{k},1}$", loc_text="top")


    my_diagram.add_dotted_line(states[3], dx_right=1)
    my_diagram.add_arrow(states[4], states[3], "$E_{\mathrm{des}}$", loc_text="top")

    my_diagram.add_dotted_line(states[1], dx_right=1, dx_left=1)
    my_diagram.add_arrow(states[2], states[1], "$E_{\mathrm{recomb}}$", loc_text="bottom")

    my_diagram.add_dotted_line(states[2], dx_right=1)
    my_diagram.add_arrow(states[3], states[2], "$E_{\mathrm{abs}}$", loc_text="top")
    my_diagram.add_arrow(states[0], states[1], "$E_{\mathrm{diss}}$", loc_text="top")

    my_diagram.add_dotted_line(states[0], dx_right=4)
    my_diagram.add_arrow(states[4], states[0], "$E_{\mathrm{S}}$")

    plt.ylim(-3, 2)
    plt.xticks([])
    plt.yticks([])
    # plt.scatter(my_diagram.x_raw, my_diagram.energies)
    plt.tight_layout()
    plt.show()
