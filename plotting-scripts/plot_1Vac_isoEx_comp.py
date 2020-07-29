import numpy as np
import matplotlib.pyplot as plt
from plotStyle import *
from dataUtils import dataRootPath as path
from dataUtils import readData

# ============================== READ DATA ==============================

path += '1Vac_isoEx_results/'

# HinVac.out format: Timestep NTinVac NHinVac NTinCell
tTH_isoEx_400K = readData(path+'1Vac_2000W_20H_6T_400K_3100ns/HinVac.out', [0,1,2])
tTH_isoEx_450K = readData(path+'1Vac_2000W_20H_6T_450K_1200ns/HinVac.out', [0,1,2])
tTH_isoEx_500K = readData(path+'1Vac_2000W_20H_6T_500K_200ns/HinVac.out', [0,1,2])
#tTH_isoEx_500K_inverse = readData(path+'1Vac_2000W_6H_20T_500K_300ns/HinVac.out', [0,1,2])
tT_diff_400K = readData(path+'1Vac_2000W_0H_6T_400K_3200ns/HinVac.out', [0,1])
tT_diff_450K = readData(path+'1Vac_2000W_0H_6T_450K_1600ns/HinVac.out', [0,1]) 
tT_diff_500K = readData(path+'1Vac_2000W_0H_6T_500K_800ns/HinVac.out', [0,1]) 

# Convert timesteps --> time in ns
cf = 1e-6
tTH_isoEx_400K[:,0] *= cf
tTH_isoEx_450K[:,0] *= cf
tTH_isoEx_500K[:,0] *= cf
#tTH_isoEx_500K_inverse[:,0] *= cf 
tT_diff_400K[:,0] *= cf
tT_diff_450K[:,0] *= cf
tT_diff_500K[:,0] *= cf


# ============================== PLOT STUFF =============================
print('Drawing figures ...')

# Figure dimensions [x, y]
fsize = [6.0, 8.0]

# Upper x-axis limit [ns]
xulim = 3000.0

# axis labels
ylbl = 'Atoms bound to Vac'
xlbl = 'Time [ns]'

# ------------------------ H&T isoEx vs diffusion --------------------------
plt.figure(1,fsize)

# Plotting function
def plotter(x, y, isoExStle, lbl):
    plt.plot(x, y, **isoExStle, label=lbl)

# 400 K
plt.subplot(3,1,1)
init, final, step = [0,-1,10]
plotter(tTH_isoEx_400K[init:final:step, 0], tTH_isoEx_400K[init:final:step,2], isoEx_style['H_iso'], isoEx_labels['H_iso'])
plotter(tTH_isoEx_400K[init:final:step, 0], tTH_isoEx_400K[init:final:step,1], isoEx_style['T_iso'], isoEx_labels['T_iso'])
plotter(tTH_isoEx_400K[init:final:step, 0], tTH_isoEx_400K[init:final:step,1]+tTH_isoEx_400K[init:final:step,2], isoEx_style['H+T'], isoEx_labels['H+T'])
plotter(tT_diff_400K[:, 0], tT_diff_400K[:, 1], isoEx_style['T_diff'], isoEx_labels['T_diff'])
plt.xlim((1, xulim))
#plt.xlabel(xlbl)
plt.ylabel(ylbl)
plt.text(1500, 5.3, '(i) 400 K', font)
plt.gca().axes.get_xaxis().set_ticklabels([]) # Hide x-axis tick labels

# 450 K
plt.subplot(3,1,2)
init, step, final = [0,10,-1]
plotter(tTH_isoEx_450K[init:final:step, 0], tTH_isoEx_450K[init:final:step, 2], isoEx_style['H_iso'], isoEx_labels['H_iso'])
plotter(tTH_isoEx_450K[init:final:step, 0], tTH_isoEx_450K[init:final:step, 1], isoEx_style['T_iso'], isoEx_labels['T_iso'])
plotter(tTH_isoEx_400K[init:final:step, 0], tTH_isoEx_400K[init:final:step,1]+tTH_isoEx_400K[init:final:step,2], isoEx_style['H+T'], isoEx_labels['H+T'])
plotter(tT_diff_450K[:, 0], tT_diff_450K[:, 1], isoEx_style['T_diff'], isoEx_labels['T_diff'])
plt.xlim((1, xulim))
#plt.xlabel(xlbl)
plt.ylabel(ylbl)
plt.text(1500, 5.3, '(ii) 450 K', font)
plt.gca().axes.get_xaxis().set_ticklabels([]) # Hide x-axis tick labels

# 500 K
plt.subplot(3,1,3)
init, step, final = [0,10,-1]
plotter(tTH_isoEx_500K[init:final:step, 0], tTH_isoEx_500K[init:final:step, 2], isoEx_style['H_iso'], isoEx_labels['H_iso'])
plotter(tTH_isoEx_500K[init:final:step, 0], tTH_isoEx_500K[init:final:step, 1], isoEx_style['T_iso'], isoEx_labels['T_iso'])
plotter(tTH_isoEx_500K[init:final:step, 0], tTH_isoEx_500K[init:final:step,1]+tTH_isoEx_500K[init:final:step,2], isoEx_style['H+T'], isoEx_labels['H+T'])
plotter(tT_diff_500K[:, 0], tT_diff_500K[:, 1], isoEx_style['T_diff'], isoEx_labels['T_diff'])
plt.xlim((1, xulim))
plt.xlabel(xlbl)
plt.ylabel(ylbl)
plt.text(1500, 5.3, '(iii) 500 K', font)
leg = plt.legend(loc='lower right', bbox_to_anchor=(0.99, 0.05))
leg.get_frame().set_linewidth(1.5*pltm)  # Legend bow linewidth
#plt.gca().axes.get_xaxis().set_ticklabels([]) # Hide x-axis tick labels

# 500 K; inverse isotopes
#plt.subplot(4,1,4)
#init, step, final = [0,10,-1]
#plotter(tTH_isoEx_500K_inverse[init:final:step, 0], tTH_isoEx_500K_inverse[init:final:step, 2], isoEx_style['H_iso'], isoEx_labels['H_iso'])
#plotter(tTH_isoEx_500K_inverse[init:final:step, 0], tTH_isoEx_500K_inverse[init:final:step, 1], isoEx_style['T_iso'], isoEx_labels['T_iso'])
#plt.xlim((1, xulim))
#plt.xlabel(xlbl)
#plt.ylabel(ylbl)
#plt.text(700, 5.3, '(iv) 500 K; inverted', font)

# Show & save figure
plt.tight_layout()
plt.savefig('../figures/1Vac_isoEx_HT.png')
plt.show()   


# ------------------------ H&T isoEx vs diff log --------------------------
plt.figure(2,fsize)

# Plotting function
def plotter(x, y, isoExStle, lbl):
    plt.semilogx(x, y, **isoExStle, label=lbl)

# 400 K
plt.subplot(3,1,1)
init, final, step = [0,-1,10]
plotter(tTH_isoEx_400K[init:final:step, 0], tTH_isoEx_400K[init:final:step,2], isoEx_style['H_iso'], isoEx_labels['H_iso'])
plotter(tTH_isoEx_400K[init:final:step, 0], tTH_isoEx_400K[init:final:step,1], isoEx_style['T_iso'], isoEx_labels['T_iso'])
plotter(tTH_isoEx_400K[init:final:step, 0], tTH_isoEx_400K[init:final:step,1]+tTH_isoEx_400K[init:final:step,2], isoEx_style['H+T'], isoEx_labels['H+T'])
plotter(tT_diff_400K[:, 0], tT_diff_400K[:, 1], isoEx_style['T_diff'], isoEx_labels['T_diff'])
plt.xlim((1, xulim))
#plt.xlabel(xlbl)
plt.ylabel(ylbl)
plt.text(2, 5.3, '(i) 400 K', font)
plt.gca().axes.get_xaxis().set_ticklabels([]) # Hide x-axis tick labels

# 450 K
plt.subplot(3,1,2)
init, step, final = [0,10,-1]
plotter(tTH_isoEx_450K[init:final:step, 0], tTH_isoEx_450K[init:final:step, 2], isoEx_style['H_iso'], isoEx_labels['H_iso'])
plotter(tTH_isoEx_450K[init:final:step, 0], tTH_isoEx_450K[init:final:step, 1], isoEx_style['T_iso'], isoEx_labels['T_iso'])
plotter(tTH_isoEx_450K[init:final:step, 0], tTH_isoEx_450K[init:final:step,1]+tTH_isoEx_450K[init:final:step,2], isoEx_style['H+T'], isoEx_labels['H+T'])
plotter(tT_diff_450K[:, 0], tT_diff_450K[:, 1], isoEx_style['T_diff'], isoEx_labels['T_diff'])
plt.xlim((1, xulim))
#plt.xlabel(xlbl)
plt.ylabel(ylbl)
plt.text(2, 5.3, '(ii) 450 K', font)
plt.gca().axes.get_xaxis().set_ticklabels([]) # Hide x-axis tick labels

# 500 K
plt.subplot(3,1,3)
init, step, final = [0,10,-1]
plotter(tTH_isoEx_500K[init:final:step, 0], tTH_isoEx_500K[init:final:step, 2], isoEx_style['H_iso'], isoEx_labels['H_iso'])
plotter(tTH_isoEx_500K[init:final:step, 0], tTH_isoEx_500K[init:final:step, 1], isoEx_style['T_iso'], isoEx_labels['T_iso'])
plotter(tTH_isoEx_500K[init:final:step, 0], tTH_isoEx_500K[init:final:step,1]+tTH_isoEx_500K[init:final:step,2], isoEx_style['H+T'], isoEx_labels['H+T'])
plotter(tT_diff_500K[:, 0], tT_diff_500K[:, 1], isoEx_style['T_diff'], isoEx_labels['T_diff'])
plt.xlim((1, xulim))
plt.xlabel(xlbl)
plt.ylabel(ylbl)
plt.text(2, 5.3, '(iii) 500 K', font)
#plt.gca().axes.get_xaxis().set_ticklabels([]) # Hide x-axis tick labels

# 500 K; inverse isotopes
#plt.subplot(4,1,4)
#init, step, final = [0,10,-1]
#plotter(tTH_isoEx_500K_inverse[init:final:step, 0], tTH_isoEx_500K_inverse[init:final:step, 2], isoEx_style['H_iso'], isoEx_labels['H_iso'])
#plotter(tTH_isoEx_500K_inverse[init:final:step, 0], tTH_isoEx_500K_inverse[init:final:step, 1], isoEx_style['T_iso'], isoEx_labels['T_iso'])
#plt.xlim((1, xulim))
#plt.xlabel(xlbl)
#plt.ylabel(ylbl)
#plt.text(2, 5.3, '(iv) 500 K; inverted', font)

# Show & save figure
plt.tight_layout()
plt.savefig('../figures/1Vac_isoEx_HT_log.png')
plt.show() 

print('Done!')
