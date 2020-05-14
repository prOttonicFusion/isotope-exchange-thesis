import numpy as np
import matplotlib.pyplot as plt
from plotStyle import *

path = '/home/otto/Drive2/isoEx_NVT/2Vac_isoEx_results/'

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

# HinVac.out format: Timestep NTinVac NHinVac NTinCell
tTH_isoEx = readData(path+'2Vac_2000W_20H_10T_500K_1000ns/HinVac.out', [0,1,2])
tTH_diff  = readData(path+'2Vac_2000W_0H_10T_500K_1000ns/HinVac.out', [0,1,2])

# Convert timesteps --> time in ns
cf = 1e-6
tTH_isoEx[:,0] *= cf
tTH_diff[:,0]  *= cf



# ============================== PLOT STUFF =============================
print('Drawing figures ...')

# Figure dimensions [x, y]
fsize = [6.0, 3.3]

# axis labels
ylbl = 'Atoms bound to Vac'
xlbl = 'Time [ns]'

# ------------------------ H&T isoEx vs diffusion --------------------------
plt.figure(1,fsize)

# Plotting function
def plotter(x, y, isoExStle, lbl):
    plt.plot(x, y, **isoExStle, label=lbl)

init, final, step = [0,-1,70]
plotter(tTH_isoEx[init:final:step, 0], tTH_isoEx[init:final:step,2], isoEx_style['H_iso'], isoEx_labels['H_iso'])
plotter(tTH_isoEx[init:final:step, 0], tTH_isoEx[init:final:step,1], isoEx_style['T_iso'], isoEx_labels['T_iso'])
plotter(tTH_diff[:, 0], tTH_diff[:, 1], isoEx_style['T_diff'], isoEx_labels['T_diff'])
plt.xlim((1, 1000))
plt.xlabel(xlbl)
plt.ylabel(ylbl)
plt.text(100, 10.1, '2-Vac; 500K', font)
#leg = plt.legend()
#leg.get_frame().set_linewidth(1.5*pltm)  # Legend bow linewidth


# Show & save figure                                                                                        
plt.tight_layout()                                                                                   
plt.savefig('../figures/2Vac_isoEx_HT.png')                                                                     
plt.show()  

# ------------------------ H&T isoEx vs diff log  --------------------------
plt.figure(2,fsize)

# Plotting function
def plotter(x, y, isoExStle, lbl):
    plt.semilogx(x, y, **isoExStle, label=lbl)

init, final, step = [0,-1,70]
plotter(tTH_isoEx[init:final:step, 0], tTH_isoEx[init:final:step,2], isoEx_style['H_iso'], isoEx_labels['H_iso'])
plotter(tTH_isoEx[init:final:step, 0], tTH_isoEx[init:final:step,1], isoEx_style['T_iso'], isoEx_labels['T_iso'])
plotter(tTH_diff[:, 0], tTH_diff[:, 1], isoEx_style['T_diff'], isoEx_labels['T_diff'])
plt.xlim((1, 1000))
plt.xlabel(xlbl)
plt.ylabel(ylbl)
plt.text(2, 10.1, '2-Vac; 500K', font)
leg = plt.legend()
leg.get_frame().set_linewidth(1.5*pltm)  # Legend bow linewidth


# Show & save figure                                                                                        
plt.tight_layout()                                                                                   
plt.savefig('../figures/2Vac_isoEx_HT_log.png')                                                                     
plt.show()  

print('Done!')
