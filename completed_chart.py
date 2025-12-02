import matplotlib.pyplot as plot
import numpy as np

galaxies = [
	{"galaxy_type": "nearby_galaxy", "x": 0.167, "y": 110},
    {"galaxy_type": "nearby_galaxy", "x": 0.25, "y": 69},
    {"galaxy_type": "nearby_galaxy", "x": 0.25, "y": 91},
    {"galaxy_type": "nearby_galaxy", "x": 0.277, "y": 100},
    {"galaxy_type": "nearby_galaxy", "x": 0.277, "y": 126},
    {"galaxy_type": "nearby_galaxy", "x": 0.331, "y": 97},
    {"galaxy_type": "nearby_galaxy", "x": 0.413, "y": 115},
    {"galaxy_type": "nearby_galaxy", "x": 0.56, "y": 91},
    {"galaxy_type": "nearby_galaxy", "x": 0.678, "y": 134},
    {"galaxy_type": "nearby_galaxy", "x": 0.834, "y": 83},
    {"galaxy_type": "nearby_galaxy", "x": 0.936, "y": 95},
    {"galaxy_type": "nearby_galaxy", "x": 1.155, "y": 138},
    {"galaxy_type": "nearby_galaxy", "x": 1.175, "y": 99},
    {"galaxy_type": "nearby_galaxy", "x": 1.31,  "y": 100},
    {"galaxy_type": "nearby_galaxy", "x": 1.9,   "y": 83},
    {"galaxy_type": "nearby_galaxy", "x": 2.125, "y": 110},
    {"galaxy_type": "nearby_galaxy", "x": 2.235, "y": 95},

    {"galaxy_type": "distant_galaxy", "x": 3.448, "y": 66.07},
    {"galaxy_type": "distant_galaxy", "x": 4.72,  "y": 79.43},
    {"galaxy_type": "distant_galaxy", "x": 5.093, "y": 47.86},
    {"galaxy_type": "distant_galaxy", "x": 5.093, "y": 75.86},
    {"galaxy_type": "distant_galaxy", "x": 5.773, "y": 38.02},
    {"galaxy_type": "distant_galaxy", "x": 6.651, "y": 69.18},
    {"galaxy_type": "distant_galaxy", "x": 6.911, "y": 69.18},
    {"galaxy_type": "distant_galaxy", "x": 7.817, "y": 69.18},
    {"galaxy_type": "distant_galaxy", "x": 7.817, "y": 33.11}
]

# Variables
accounted_records = []
x = np.arange(0, 11, 1)

# Plotting and Labeling Data
for galaxy in galaxies:
	galaxy_type = galaxy["galaxy_type"]
	galaxy_color = "blue" if galaxy_type == "nearby_galaxy" else "red"
	x_coord, y_coord = galaxy["x"], galaxy["y"]

	if galaxy_type not in accounted_records:
		plot.scatter(x_coord, y_coord, color=galaxy_color, label=galaxy_type)
		accounted_records.append(galaxy_type)
	else:
		plot.scatter(x_coord, y_coord, color=galaxy_color)

# Plot Creation and Settings
plot.title("Supernova Brightness vs. Distance\nBy: Nathan Parker", fontsize=10)
plot.ylabel("Supernova Brightness Value")
plot.ylim(0, 150)

plot.xlabel("Light Travel Time in Billions of Years (Distance)")
plot.xlim(0, 10)
plot.xticks(x)

plot.axhline(y=100, color="black", linestyle="--", label="Expected")

plot.grid(True)
plot.legend(bbox_to_anchor=(0.95, 0.5), loc="center left", borderaxespad=0., fancybox=True, shadow=True)
plot.savefig('supernova_brightness_vs_distance.png', bbox_inches='tight')
plot.show()