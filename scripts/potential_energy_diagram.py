import numpy as np
import matplotlib.pyplot as plt
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
        self, state1, state2, text="", offset=0, kwargs_arrow={}, kwargs_text={}
    ):
        # arrow
        plt.annotate(
            text="",
            xy=(self.states.index(state1), state1.E),
            xytext=(self.states.index(state1), state2.E),
            arrowprops=dict(arrowstyle="<->"),
            **kwargs_arrow
        )

        # text
        plt.annotate(
            text=text,
            xy=(self.states.index(state1), (state1.E + state2.E) / 2),
            xytext=(self.states.index(state1), offset + (state1.E + state2.E) / 2),
            ha="left",
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


energies = [0, 0.4, -1, 1.3, *[0, 1] * 10]


states = [State(E=E) for E in energies]

states[10].E = -2.5
states[18].E = -1.5
my_diagram = Diagram(states)

plt.figure(figsize=(7.5, 4.8))
plt.plot(my_diagram.x, my_diagram.y)

my_diagram.add_dotted_line(states[18], dx_right=2)
my_diagram.add_dotted_line(states[20], dx_left=1)
my_diagram.add_arrow(states[20], states[18], "$E_{\mathrm{b},2}$")
my_diagram.add_arrow(states[20], states[21], "$E_{\mathrm{k},2}$")
# plt.scatter(my_diagram.x_raw, my_diagram.energies)
plt.show()
