import numpy as np
import matplotlib.pyplot as plt
from plotStyle import *

path = '/home/otto/Drive2/isoEx_NVT/GB_isoEx_results/'

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
tTH_isoEx_500K = readData(path+'GB_9600W_150H_369T_500K_1000ns/HinGB.out', [0,1,2])
tT_diff_500K = readData(path+'GB_9600W_0H_369T_500K_1000ns/HinGB.out', [0,1])

# Convert timesteps --> time in ns
cf = 1e-6
tTH_isoEx_500K[:,0] *= cf
tT_diff_500K[:,0] *= cf


# ============================== PLOT STUFF =============================
print('Drawing figures ...')

# Figure dimensions [x, y]
fsize = [6.0, 3.5]

# Upper x-axis limit
xulim = 1300.0

# axis labels
ylbl = 'Atoms bound to GB'
xlbl = 'Time [ns]'

# ------------------------ H&T isoEx vs diffusion --------------------------
plt.figure(1,fsize)

# Plotting function
def plotter(x, y, isoExStle, lbl):
    plt.plot(x, y, **isoExStle, label=lbl)

# 500 K
init, step, final = [0,100,-1]
plotter(tTH_isoEx_500K[init:final:step, 0], tTH_isoEx_500K[init:final:step, 2], isoEx_style['H_iso'], isoEx_labels['H_iso'])
plotter(tTH_isoEx_500K[init:final:step, 0], tTH_isoEx_500K[init:final:step, 1], isoEx_style['T_iso'], isoEx_labels['T_iso'])
plotter(tT_diff_500K[:, 0], tT_diff_500K[:, 1], isoEx_style['T_diff'], isoEx_labels['T_diff'])
plt.xlim((1, xulim))
plt.xlabel(xlbl)
plt.ylabel(ylbl)
#plt.text(400, 5.3, '(iii) 500 K', font)
#leg = plt.legend()
#leg.get_frame().set_linewidth(1.5*pltm)  # Legend bow linewidth
#plt.gca().axes.get_xaxis().set_ticklabels([]) # Hide x-axis tick labels

# Show & save figure                                                                                       
plt.tight_layout()                                                                                   
plt.savefig('../figures/GB_isoEx_HT.png')                                                                     
plt.show()   


# ------------------------ H&T isoEx vs diff log --------------------------
plt.figure(2,fsize)

# Plotting function
def plotter(x, y, isoExStle, lbl):
    plt.semilogx(x, y, **isoExStle, label=lbl)

# 500 K
init, step, final = [0,100,-1]
plotter(tTH_isoEx_500K[init:final:step, 0], tTH_isoEx_500K[init:final:step, 2], isoEx_style['H_iso'], isoEx_labels['H_iso'])
plotter(tTH_isoEx_500K[init:final:step, 0], tTH_isoEx_500K[init:final:step, 1], isoEx_style['T_iso'], isoEx_labels['T_iso'])
plotter(tT_diff_500K[:, 0], tT_diff_500K[:, 1], isoEx_style['T_diff'], isoEx_labels['T_diff'])
plt.xlim((1, xulim))
plt.xlabel(xlbl)
plt.ylabel(ylbl)
#plt.text(2, 5.3, '(iii) 500 K', font)
leg = plt.legend()
leg.get_frame().set_linewidth(1.5*pltm)  # Legend bow linewidth
#plt.gca().axes.get_xaxis().set_ticklabels([]) # Hide x-axis tick labels

# Show & save figure                                                                                       
plt.tight_layout()                                                                                   
plt.savefig('../figures/GB_isoEx_HT_log.png')                                                                     
plt.show() 

print('Done!')