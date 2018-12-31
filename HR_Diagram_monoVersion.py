# Hertzsprung-Russell Diagram
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# import data
data = pd.read_csv("hygdata_edit.csv")                      # read csv file
df = data.convert_objects(convert_numeric = True)           # attempt to coerce to numbers (including strings)
data["spect"] = data.spect.astype(str)

# extract string value from column spect
spect =  data["spect"].str.extract("(?P<letter>[A-Z])", expand = False)
print(spect.values)

# get data value
paralax = df["paralax"].values
visualMagnitude = df["vmag"].values
blueVisualMagnitude = df["ci"].values
spectrum = spect.values

# calculate each parameter values
sunAbsMagnitude = 4.83                                      # sun's absolute magnitude
distance = 1000/paralax                                     # distance in parsec(parallax seconds)
absMagnitude = visualMagnitude + 5 - 5 * np.log(distance)
luminosity = (absMagnitude - sunAbsMagnitude) / -2.5
temperature = 4600 * ((1 / (0.93 * blueVisualMagnitude + 1.7)) + (1 / (0.92 * blueVisualMagnitude + 0.62)))

# define a font properties using dict
font = {'family' : 'Arial',
        'color' : 'black',
        'weight' : 'normal',
        'size' : 12
        }

# visualizating data
plt.title("Hertzsprung-Russell Diagram", fontdict = font)
plt.xlabel("Blue Visual Magnitude", fontdict = font)
plt.ylabel("Luminosity", fontdict = font)

plt.scatter(blueVisualMagnitude, luminosity, s = 0.1 , alpha = 1, color = "blue")

plt.show()