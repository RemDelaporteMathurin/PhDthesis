import matplotlib.pyplot as plt


def draw_torus(major_radius, minor_radius, pos, **kwargs):
    background_colour = "white"
    torus = plt.Circle(pos, major_radius + minor_radius, **kwargs)
    hollow = plt.Circle(pos, major_radius - minor_radius, color=background_colour)

    ax = plt.gca()
    ax.add_patch(torus)
    ax.add_patch(hollow)


WEST = {
    "name": "WEST",
    "major_radius": 2.5,
    "minor_radius": 0.5,
    "current": 1,
    "magnetic_field": 3.7,
    "thermal_power": 0,
}

ITER = {
    "name": "ITER",
    "major_radius": 6.2,
    "minor_radius": 2,
    "current": 15,
    "magnetic_field": 5.3,
    "thermal_power": 500,
}
JET = {
    "name": "JET",
    "major_radius": 2.96,
    "minor_radius": 1.25,
    "current": 5,
    "magnetic_field": 3.4,
    "thermal_power": 15,
}
SPARC = {
    "name": "SPARC",
    "major_radius": 1.65,
    "minor_radius": 0.5,
    "current": 7.5,
    "magnetic_field": 12,
    "thermal_power": 140,
}
ARC = {
    "name": "ARC",
    "major_radius": 3.3,
    "minor_radius": 1.13,
    "current": 7.8,
    "magnetic_field": 9.2,
    "thermal_power": 708,
}

reactors = [ITER, ARC, JET, WEST, SPARC]

fig, axs = plt.subplots(4, 1, sharex=True, figsize=(6.4, 8))

# radius
plt.sca(axs[0])
x_positions = []
x_pos = 0
for i, reactor in enumerate(reactors):
    R_0 = reactor["major_radius"]
    a = reactor["minor_radius"]
    x_pos += R_0 + a
    y_pos = 0

    x_positions.append(x_pos)
    if R_0 == max([r["major_radius"] for r in reactors]):
        colour = "tab:red"
    else:
        colour = "tab:blue"
    draw_torus(R_0, a, pos=(x_pos, y_pos), color=colour, alpha=0.5)
    x_pos += (R_0 + a) + 0.5

plt.gca().set_aspect("equal")

plt.xlim(0, x_pos)
ylim = max([r["major_radius"] + r["minor_radius"] for r in reactors])
plt.ylim(-ylim, ylim)
plt.ylabel("Size (m)")

# Mag Field
plt.sca(axs[1])
mag_fields = [reactor["magnetic_field"] for reactor in reactors]

colours = []
for r in reactors:
    if r["magnetic_field"] == max(mag_fields):
        colours.append("tab:red")
    else:
        colours.append("tab:blue")

plt.bar(x_positions, mag_fields, align="center", alpha=0.5, width=3, color=colours)
plt.gca().set_aspect(1.3)
plt.ylabel("Magnetic field (T)")


# current
plt.sca(axs[2])
currents = [reactor["current"] for reactor in reactors]

colours = []
for r in reactors:
    if r["current"] == max(currents):
        colours.append("tab:red")
    else:
        colours.append("tab:blue")

plt.bar(x_positions, currents, align="center", alpha=0.5, width=3, color=colours)
plt.gca().set_aspect(1.05)
plt.ylabel("Plasma current \n (MA)")


# power
plt.sca(axs[3])
powers = [reactor["thermal_power"] for reactor in reactors]

colours = []
for r in reactors:
    if r["thermal_power"] == max(powers):
        colours.append("tab:red")
    else:
        colours.append("tab:blue")

plt.bar(x_positions, powers, align="center", alpha=0.5, width=3, color=colours)
plt.gca().set_aspect(0.0222)
plt.ylabel("Fusion \n power (MW)")


# change xticks
axs[-1].set_xticks(x_positions, [r["name"] for r in reactors])

# add labels on top
plt.sca(axs[0])
for i, r in enumerate(reactors):
    if r["name"] == "ITER":
        y_pos = 0
    else:
        y_pos = r["major_radius"] + r["minor_radius"] + 0.1
    plt.annotate(
        r["name"],
        (x_positions[i], y_pos),
        ha="center",
    )

# remove top and right axes
for ax in axs:
    ax.spines.right.set_visible(False)
    ax.spines.top.set_visible(False)
axs[0].spines.bottom.set_visible(False)
plt.sca(axs[0])
plt.tick_params(
    axis="x",  # changes apply to the x-axis
    which="both",  # both major and minor ticks are affected
    bottom=False,
)
plt.show()
