import numpy as np
import matplotlib.pyplot as plt
from plotStyle import *
from dataUtils import dataRootPath as path
from dataUtils import readData

# ============================== READ DATA ==============================

path += '2Vac_isoEx_results/'

# HinVac.out format: Timestep NTinVac NHinVac NTinCell
tTH_isoEx = readData(path+'2Vac_2000W_20H_10T_500K_500ns/HinVac.out', [0,1,2])
tTH_diff  = readData(path+'2Vac_2000W_0H_10T_500K_1000ns/HinVac.out', [0,1,2])
tTH_isoEx_400K = readData(path+'2Vac_2000W_20H_10T_400K_700ns/HinVac.out', [0,1,2])
tT_diff_400K  = readData(path+'2Vac_2000W_0H_10T_400K_700ns/HinVac.out', [0,1,2])


# Convert timesteps --> time in ns
cf = 1e-6
tTH_isoEx[:,0] *= cf
tTH_diff[:,0]  *= cf
tTH_isoEx_400K[:,0] *= cf
tT_diff_400K[:,0]  *= cf



# ============================== PLOT STUFF =============================
print('Drawing figures ...')

# Figure dimensions [x, y]
fsize = [6.0, 7.0]

# Upper x-axis limit [ns]
xulim = 2000.0

# axis labels
ylbl = 'Atoms bound to Vac'
xlbl = 'Time [ns]'

# ------------------------ H&T isoEx vs diffusion --------------------------
plt.figure(1,fsize)

# Plotting function
def plotter(x, y, isoExStle, lbl):
    plt.plot(x, y, **isoExStle, label=lbl)

init, final, step = [0,-1,70]
# 400 K
plt.subplot(2,1,1)
plotter(tT_diff_400K[:, 0], tT_diff_400K[:, 1], isoEx_style['T_diff'], isoEx_labels['T_diff'])
plotter(tTH_isoEx_400K[init:final:step, 0], tTH_isoEx_400K[init:final:step, 2], isoEx_style['H_iso'], isoEx_labels['H_iso'])
plotter(tTH_isoEx_400K[init:final:step, 0], tTH_isoEx_400K[init:final:step, 1], isoEx_style['T_iso'], isoEx_labels['T_iso'])
plotter(tTH_isoEx_400K[init:final:step, 0], tTH_isoEx_400K[init:final:step,1]+tTH_isoEx_400K[init:final:step,2], isoEx_style['H+T'], isoEx_labels['H+T'])
plt.xlim((1, xulim))
plt.ylim((0,12))
plt.ylabel(ylbl)
plt.text(800, 10.8, '(i) 400 K', font)
leg = plt.legend(loc='lower right', bbox_to_anchor=(0.99, 0.03))
leg.get_frame().set_linewidth(1.5*pltm)  # Legend bow linewidth
plt.gca().axes.get_xaxis().set_ticklabels([]) # Hide x-axis tick labels

# 500 K
plt.subplot(2,1,2)
plotter(tTH_isoEx[init:final:step, 0], tTH_isoEx[init:final:step,2], isoEx_style['H_iso'], isoEx_labels['H_iso'])
plotter(tTH_isoEx[init:final:step, 0], tTH_isoEx[init:final:step,1], isoEx_style['T_iso'], isoEx_labels['T_iso'])
plotter(tTH_isoEx[init:final:step, 0], tTH_isoEx[init:final:step,1]+tTH_isoEx[init:final:step,2], isoEx_style['H+T'], isoEx_labels['H+T'])
plotter(tTH_diff[0:len(tTH_isoEx[:, 0]), 0], tTH_diff[0:len(tTH_isoEx[:, 0]), 1], isoEx_style['T_diff'], isoEx_labels['T_diff'])
plt.xlim((1, xulim))
plt.ylim((0,12))
plt.xlabel(xlbl)
plt.ylabel(ylbl)
plt.text(800, 10.8, '(ii) 500K', font)


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
# 400 K
plt.subplot(2,1,1)
plotter(tT_diff_400K[:, 0], tT_diff_400K[:, 1], isoEx_style['T_diff'], isoEx_labels['T_diff'])
plotter(tTH_isoEx_400K[init:final:step, 0], tTH_isoEx_400K[init:final:step, 2], isoEx_style['H_iso'], isoEx_labels['H_iso'])
plotter(tTH_isoEx_400K[init:final:step, 0], tTH_isoEx_400K[init:final:step, 1], isoEx_style['T_iso'], isoEx_labels['T_iso'])
plotter(tTH_isoEx_400K[init:final:step, 0], tTH_isoEx_400K[init:final:step,1]+tTH_isoEx_400K[init:final:step,2], isoEx_style['H+T'], isoEx_labels['H+T'])
plt.xlim((1, xulim))
plt.ylim((0,12))
plt.ylabel(ylbl)
plt.text(2, 10.8, '(i) 400 K', font)
plt.gca().axes.get_xaxis().set_ticklabels([]) # Hide x-axis tick labels

# 500 K
plt.subplot(2,1,2)
plotter(tTH_isoEx[init:final:step, 0], tTH_isoEx[init:final:step,2], isoEx_style['H_iso'], isoEx_labels['H_iso'])
plotter(tTH_isoEx[init:final:step, 0], tTH_isoEx[init:final:step,1], isoEx_style['T_iso'], isoEx_labels['T_iso'])
plotter(tTH_isoEx[init:final:step, 0], tTH_isoEx[init:final:step,1]+tTH_isoEx[init:final:step,2], isoEx_style['H+T'], isoEx_labels['H+T'])
plotter(tTH_diff[0:len(tTH_isoEx[:, 0]), 0], tTH_diff[0:len(tTH_isoEx[:, 0]), 1], isoEx_style['T_diff'], isoEx_labels['T_diff'])
plt.xlim((1, xulim))
plt.ylim((0,12))
plt.xlabel(xlbl)
plt.ylabel(ylbl)
plt.text(2, 10.8, '(ii) 500K', font)

# Show & save figure
plt.tight_layout()
plt.savefig('../figures/2Vac_isoEx_HT_log.png')
plt.show()  

print('Done!')
