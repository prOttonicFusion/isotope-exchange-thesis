import numpy as np
import matplotlib.pyplot as plt
from plotStyle import *
from dataUtils import dataRootPath as path
from dataUtils import readData

# ============================== READ DATA ==============================

# HinVac.out format: Timestep NTinVac NHinVac NTinCell
tTH_isoEx_400K = readData(path+'yGB_3000W_100H_73T_400K_200ns/HinGB.out', [0,1,2])
tT_diff_400K = readData(path+'yGB_3000W_0H_73T_400K_250ns/HinGB.out', [0,1])
tTH_isoEx_500K = readData(path+'yGB_3000W_100H_73T_500K_300ns/HinGB.out', [0,1,2])
tT_diff_500K = readData(path+'yGB_3000W_0H_73T_500K_300ns/HinGB.out', [0,1])

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

# Upper x-axis limit
xulim = 300.0

# axis labels
ylbl = 'Atoms bound to GB'
xlbl = 'Time [ns]'

# ------------------------ H&T isoEx vs diffusion --------------------------
plt.figure(1,fsize)

# Plotting function
def plotter(x, y, isoExStle, lbl):
    plt.plot(x, y, **isoExStle, label=lbl)

# 400 K
plt.subplot(2,1,1)
init, step, final = [0,100,-1]
plotter(tTH_isoEx_400K[init:final:step, 0], tTH_isoEx_400K[init:final:step, 2], isoEx_style['H_iso'], isoEx_labels['H_iso'])
plotter(tTH_isoEx_400K[init:final:step, 0], tTH_isoEx_400K[init:final:step, 1], isoEx_style['T_iso'], isoEx_labels['T_iso'])
plotter(tT_diff_400K[:, 0], tT_diff_400K[:, 1], isoEx_style['T_diff'], isoEx_labels['T_diff'])
plt.xlim((1, xulim))
plt.xlabel(xlbl)
plt.ylabel(ylbl)
plt.text(105, 70, '(i) 400 K', font)
plt.gca().axes.get_xaxis().set_ticklabels([]) # Hide x-axis tick labels
    
# 500 K
plt.subplot(2,1,2)
init, step, final = [0,100,-1]
plotter(tTH_isoEx_500K[init:final:step, 0], tTH_isoEx_500K[init:final:step, 2], isoEx_style['H_iso'], isoEx_labels['H_iso'])
plotter(tTH_isoEx_500K[init:final:step, 0], tTH_isoEx_500K[init:final:step, 1], isoEx_style['T_iso'], isoEx_labels['T_iso'])
plotter(tT_diff_500K[:, 0], tT_diff_500K[:, 1], isoEx_style['T_diff'], isoEx_labels['T_diff'])
plt.xlim((1, xulim))
plt.xlabel(xlbl)
plt.ylabel(ylbl)
plt.text(105, 70, '(ii) 500 K', font)
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

# 400 K
plt.subplot(2,1,1)
init, step, final = [0,100,-1]
plotter(tTH_isoEx_400K[init:final:step, 0], tTH_isoEx_400K[init:final:step, 2], isoEx_style['H_iso'], isoEx_labels['H_iso'])
plotter(tTH_isoEx_400K[init:final:step, 0], tTH_isoEx_400K[init:final:step, 1], isoEx_style['T_iso'], isoEx_labels['T_iso'])
plotter(tT_diff_400K[:, 0], tT_diff_400K[:, 1], isoEx_style['T_diff'], isoEx_labels['T_diff'])
plt.xlim((1, xulim))
plt.xlabel(xlbl)
plt.ylabel(ylbl)
plt.text(1.5, 58, '(i) 400 K', font)
plt.gca().axes.get_xaxis().set_ticklabels([]) # Hide x-axis tick labels

# 500 K
plt.subplot(2,1,2)
init, step, final = [0,100,-1]
plotter(tTH_isoEx_500K[init:final:step, 0], tTH_isoEx_500K[init:final:step, 2], isoEx_style['H_iso'], isoEx_labels['H_iso'])
plotter(tTH_isoEx_500K[init:final:step, 0], tTH_isoEx_500K[init:final:step, 1], isoEx_style['T_iso'], isoEx_labels['T_iso'])
plotter(tT_diff_500K[:, 0], tT_diff_500K[:, 1], isoEx_style['T_diff'], isoEx_labels['T_diff'])
plt.xlim((1, xulim))
plt.xlabel(xlbl)
plt.ylabel(ylbl)
plt.text(1.5, 58, '(ii) 500 K', font)
leg = plt.legend(loc='lower left', bbox_to_anchor=(0.02, 0.25))
leg.get_frame().set_linewidth(1.5*pltm)  # Legend bow linewidth
#plt.gca().axes.get_xaxis().set_ticklabels([]) # Hide x-axis tick labels

# Show & save figure
plt.tight_layout()
plt.savefig('../figures/GB_isoEx_HT_log.png')
plt.show() 

print('Done!')
