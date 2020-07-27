import numpy as np
import matplotlib.pyplot as plt
from plotStyle import *

# ============================== READ DATA ==============================
# Function for reading columnsToRead=[i,j,...] columns from file 'fname'
def readData(fname, columnsToRead):
    data = []
    print('Reading: {}'.format(fname))
    with open(fname) as f:
        f.readline() # skip header
        line = f.readline()
        while line:
            spltd = line.split()
            data.append([float(spltd[i]) for i in columnsToRead])
            line = f.readline()
    return np.array(data)

# Read data; format: NH, Ebind
DFT1V = readData('../Ebind-data/Ebind_DFT_1V.dat', [0,1])
MD1V  = readData('../Ebind-data/Ebind_MD_1V.dat', [0,1])
MD2V  = readData('../Ebind-data/Ebind_MD_2V.dat', [0,1])

# ============================== PLOT STUFF =============================
print('Drawing figures ...')

# ------------------------ H&T isoEx vs diffusion --------------------------
plt.figure(1,[6, 3.5])
ax = plt.subplot(111)

# Plot marker & line styles
stl = ['o-', 's--', 'd-']   # H-isoEx, T-isoEx, T-diff

# Labels
lbls = ['MD; 1-Vac', 'DFT; 1-Vac', 'MD; 2-Vac']

# Plotting function
def plotter(x, y, stle, lbl):
    ax.plot(x, y, stle, label=lbl)  # fillstyle='none'

plotter(MD1V[:,0], MD1V[:,1], stl[0], lbls[0])
plotter(DFT1V[:,0], DFT1V[:,1], stl[1], lbls[1])
plotter(MD2V[:,0], MD2V[:,1], stl[2], lbls[2])
plt.xlabel('Number of H atoms')
plt.ylabel('Binding Energy [eV]')
plt.locator_params(axis='x', nbins=10)       # Nr. of x-tick labels
leg = ax.legend(bbox_to_anchor=(0.63, 0.7))
leg.get_frame().set_linewidth(1.5*pltm)  # Legend bow linewidth

# Adjust margins
plt.tight_layout(1, rect=[0, 0, 0.9, 1])

# Show & save figure                                                                                       
#plt.tight_layout()                                                                                   
plt.savefig('../figures/Ebind.png')                                                                     
plt.show()   

print('Done!')
