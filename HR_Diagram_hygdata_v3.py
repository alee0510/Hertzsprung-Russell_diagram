# Hertzsprung-Russell Diagram
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
import numpy as np

# import and managing data
data = pd.read_csv("hygdata_v3.csv")                        # read csv file
data.fillna(0, inplace = True)                              # fill n.a. data with 0
df = data[data.spect !=0]                                   # delete row in spect column if has 0 value
df = df.drop(columns = ["hr","gl", "bf", "rv", "proper", "bayer", 
                   "flam", "con", "comp", "base", "var", "var_min", "var_max"])

df["spect"] = df["spect"].str.replace('[0-9]','')
df["spect"] = df["spect"].str.replace('[:, +, /, ., I, V, (, ), -]','')
df["spect"] = df["spect"].str.upper()
df["spect"] = df["spect"].str.replace('[C-E, H-J, L, N, P-Z]','')

df.sort_values(by = "spect", inplace = True)

# create ne data frame
df2 = df[df.spect !=""]
df3 = df2[df2.spect.str.len() <=1]

df3 = df3.convert_objects(convert_numeric = True)           # attempt to coerce to numbers (including strings)
df3["spect"] = df3.spect.astype(str)

# extract string value from column spect
spect =  df3["spect"].str.extract("(?P<letter>[A-Z])", expand = False)

# get data value
distance = df3["dist"].values                               # distance in parsec(parallax seconds)
visualMagnitude = df3["mag"].values
blueVisualMagnitude = df3["ci"].values
spectrum = spect.values

# calculate each parameter values
sunAbsMagnitude = 4.83                                      # sun's absolute magnitude                                 
absMagnitude = visualMagnitude + (5 - 5 * np.log10(distance))
luminosity = (absMagnitude - sunAbsMagnitude) / (-2.5)
temperature = 4600 * ((1/(0.92*blueVisualMagnitude+1.7)) +(1/(0.92*blueVisualMagnitude+0.62)))

# slicing data
A = []
B = []
F = []
G = []
K = []
M = []
O = []
x =len(distance)

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

plt.scatter(blueVisualMagnitude[0 : a], luminosity[0 : a], s = 1 , alpha = 0.5, color = "red", label = "$A$")
plt.scatter(blueVisualMagnitude[a : b], luminosity[a : b], s = 1 , alpha = 0.5, color = "green", label = "$B$")
plt.scatter(blueVisualMagnitude[b : f], luminosity[b : f], s = 1 , alpha = 0.5, color = "blue", label = "$F$")
plt.scatter(blueVisualMagnitude[f : g], luminosity[f : g], s = 1 , alpha = 0.5, color = "orange", label = "$G$")
plt.scatter(blueVisualMagnitude[g : k], luminosity[g : k], s = 1 , alpha = 0.5, color = "purple", label = "$K$")
plt.scatter(blueVisualMagnitude[k : m], luminosity[k : m], s = 1 , alpha = 0.5, color = "cyan", label = "$M$")
plt.scatter(blueVisualMagnitude[m : x+1], luminosity[m : x+1], s = 1 , alpha = 0.5, color = "magenta", label = "$O$")

plt.legend(loc = 'upper right')

plt.show()