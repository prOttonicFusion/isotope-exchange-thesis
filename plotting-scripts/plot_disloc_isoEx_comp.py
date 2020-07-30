import numpy as np
import matplotlib.pyplot as plt
from plotStyle import *
from dataUtils import dataRootPath as path
from dataUtils import readData

# ============================== READ DATA ==============================

path += 'disloc_isoEx_results/'

# HinVac.out format: Timestep NTinVac NHinVac NTinCell
tTH_isoEx_400K = readData(path+'disloc_isoEx_400K_500ns/HinDisl.out', [0,1,2])
tT_diff_400K = readData(path+'disloc_isoEx_400K_0H_500ns/HinDisl.out', [0,1])
tTH_isoEx_500K = readData(path+'disloc_isoEx_500K_300ns/HinDisl.out', [0,1,2])
tT_diff_500K = readData(path+'disloc_isoEx_500K_0H_300ns/HinDisl.out', [0,1])

# Convert timesteps --> time in ns
cf = 1e-6
tTH_isoEx_400K[:,0] *= cf
tT_diff_400K[:,0] *= cf
tTH_isoEx_500K[:,0] *= cf
tT_diff_500K[:,0] *= cf


# ============================== PLOT STUFF =============================
print('Drawing figures ...')

# Figure dimensions [x, y]
fsize = [6.0, 7.0]

# Upper x-axis limit [ns]
xulim = 400.0

# axis labels
ylbl = 'Atoms bound to disl.'
xlbl = 'Time [ns]'

init, step, final = [0, 50, -1]

# ------------------------ H&T isoEx vs diffusion --------------------------
plt.figure(1,fsize)

# Plotting function
def plotter(x, y, isoExStle, lbl):
    plt.plot(x, y, **isoExStle, label=lbl)


# 400 K
plt.subplot(2,1,1)
plotter(tT_diff_400K[:, 0], tT_diff_400K[:, 1], isoEx_style['T_diff'], isoEx_labels['T_diff'])
plotter(tTH_isoEx_400K[init:final:step, 0], tTH_isoEx_400K[init:final:step, 2], isoEx_style['H_iso'], isoEx_labels['H_iso'])
plotter(tTH_isoEx_400K[init:final:step, 0], tTH_isoEx_400K[init:final:step, 1], isoEx_style['T_iso'], isoEx_labels['T_iso'])
plotter(tTH_isoEx_400K[init:final:step, 0], tTH_isoEx_400K[init:final:step,1]+tTH_isoEx_400K[init:final:step,2], isoEx_style['H+T'], isoEx_labels['H+T']) 
plt.xlim((1, xulim))
plt.ylabel(ylbl)
plt.text(50, 122.5, '(i) 400 K', font)
plt.gca().axes.get_xaxis().set_ticklabels([]) # Hide x-axis tick labels

# 500 K
plt.subplot(2,1,2)
plotter(tT_diff_500K[:, 0], tT_diff_500K[:, 1], isoEx_style['T_diff'], isoEx_labels['T_diff'])
plotter(tTH_isoEx_500K[init:final:step, 0], tTH_isoEx_500K[init:final:step, 2], isoEx_style['H_iso'], isoEx_labels['H_iso'])
plotter(tTH_isoEx_500K[init:final:step, 0], tTH_isoEx_500K[init:final:step, 1], isoEx_style['T_iso'], isoEx_labels['T_iso'])
plotter(tTH_isoEx_500K[init:final:step, 0], tTH_isoEx_500K[init:final:step,1]+tTH_isoEx_500K[init:final:step,2], isoEx_style['H+T'], isoEx_labels['H+T']) 
plt.xlim((1, xulim))
plt.xlabel(xlbl)
plt.ylabel(ylbl)
plt.text(50, 122.5, '(ii) 500 K', font)
leg = plt.legend(loc='upper right', bbox_to_anchor=(0.999, 0.999), framealpha=0.8) 
leg.get_frame().set_linewidth(1.5*pltm)  # Legend bow linewidth
#plt.gca().axes.get_xaxis().set_ticklabels([]) # Hide x-axis tick labels

# Show & save figure
plt.tight_layout()
plt.savefig('../figures/disloc_isoEx_HT.png')
plt.show()   


# ------------------------ H&T isoEx vs diff log --------------------------
plt.figure(2,fsize)

# Plotting function
def plotter(x, y, isoExStle, lbl):
    plt.semilogx(x, y, **isoExStle, label=lbl)

# 400 K
plt.subplot(2,1,1)
plotter(tT_diff_400K[:, 0], tT_diff_400K[:, 1], isoEx_style['T_diff'], isoEx_labels['T_diff'])
plotter(tTH_isoEx_400K[init:final:step, 0], tTH_isoEx_400K[init:final:step, 2], isoEx_style['H_iso'], isoEx_labels['H_iso'])
plotter(tTH_isoEx_400K[init:final:step, 0], tTH_isoEx_400K[init:final:step, 1], isoEx_style['T_iso'], isoEx_labels['T_iso'])
plotter(tTH_isoEx_400K[init:final:step, 0], tTH_isoEx_400K[init:final:step,1]+tTH_isoEx_400K[init:final:step,2], isoEx_style['H+T'], isoEx_labels['H+T']) 
plt.xlim((1, xulim))
plt.ylabel(ylbl)
plt.text(1.3, 88, '(i) 400 K', font)
#leg = plt.legend(loc='lower right', bbox_to_anchor=(0.99, 0.03))
#leg.get_frame().set_linewidth(1.5*pltm)  # Legend bow linewidth
plt.gca().axes.get_xaxis().set_ticklabels([]) # Hide x-axis tick labels

# 500 K
plt.subplot(2,1,2)
plotter(tT_diff_500K[:, 0], tT_diff_500K[:, 1], isoEx_style['T_diff'], isoEx_labels['T_diff'])
plotter(tTH_isoEx_500K[init:final:step, 0], tTH_isoEx_500K[init:final:step, 2], isoEx_style['H_iso'], isoEx_labels['H_iso'])
plotter(tTH_isoEx_500K[init:final:step, 0], tTH_isoEx_500K[init:final:step, 1], isoEx_style['T_iso'], isoEx_labels['T_iso'])
plotter(tTH_isoEx_500K[init:final:step, 0], tTH_isoEx_500K[init:final:step,1]+tTH_isoEx_500K[init:final:step,2], isoEx_style['H+T'], isoEx_labels['H+T']) 
plt.xlim((1, xulim))
plt.xlabel(xlbl)
plt.ylabel(ylbl)
plt.text(1.3, 88, '(ii) 500 K', font)
#plt.gca().axes.get_xaxis().set_ticklabels([]) # Hide x-axis tick labels

# Show & save figure
plt.tight_layout()
plt.savefig('../figures/disloc_isoEx_HT_log.png')
plt.show() 

print('Done!')
