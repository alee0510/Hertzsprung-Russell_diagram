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

# slicing data
A = []
B = []
F = []
G = []
K = []
M = []
O = []
x =len(paralax)
for index in range(0, x):
    if spectrum[index] == 'A':
        A.append(spectrum[index])
    elif spectrum[index] == 'B':
        B.append(spectrum[index])
    elif spectrum[index] == 'F':
        F.append(spectrum[index])
    elif spectrum[index] == 'G':
        G.append(spectrum[index])
    elif spectrum[index] == 'K':
        K.append(spectrum[index])
    elif spectrum[index] == 'M':
        M.append(spectrum[index])
    else:
        O.append(spectrum[index])

# define a font properties using dict
font = {'family' : 'Times New Roman',
        'color' : 'black',
        'weight' : 'normal',
        'size' : 12
        }

a = len(A)
b = len(A) + len(B)
f = b + len(F)
g = f + len(G)
k = g + len(K)
m = k + len(M)

# visualizating data for each spectrum
plt.title("Hertzsprung-Russell Diagram", fontdict = font, fontsize = 14)
plt.xlabel("Blue Visual Magnitude", fontdict = font)
plt.ylabel("Luminosity", fontdict = font)

plt.scatter(blueVisualMagnitude[0 : a], luminosity[0 : a], s = 0.1 , alpha = 0.5, color = "red")
plt.scatter(blueVisualMagnitude[a : b], luminosity[a : b], s = 0.1 , alpha = 0.5, color = "green")
plt.scatter(blueVisualMagnitude[b : f], luminosity[b : f], s = 0.1 , alpha = 0.5, color = "blue")
plt.scatter(blueVisualMagnitude[f : g], luminosity[f : g], s = 0.1 , alpha = 0.5, color = "orange")
plt.scatter(blueVisualMagnitude[g : k], luminosity[g : k], s = 0.1 , alpha = 0.5, color = "purple")
plt.scatter(blueVisualMagnitude[k : m], luminosity[k : m], s = 0.1 , alpha = 0.5, color = "cyan")
plt.scatter(blueVisualMagnitude[m : x+1], luminosity[m : x+1], s = 0.1 , alpha = 0.5, color = "magenta")
##plt.scatter(blueVisualMagnitude, luminosity, s = 0.1 , alpha = 1, color = "blue")

plt.show()