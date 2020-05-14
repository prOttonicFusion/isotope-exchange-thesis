import matplotlib.pyplot as plt
import sys

print('Loading the plot style from {}'.format(__file__))

# ------------------------------ Plot-style ------------------------------
fsize = 13  # Font size
pltm = 1.3  # Plot object size multiplier

plt.rcParams['figure.dpi'] = 150         # figure resolution in dots/inch
plt.rcParams['axes.titlesize'] = fsize
plt.rcParams['axes.labelsize'] = fsize
plt.rcParams['axes.linewidth'] = 1.5*pltm
plt.rcParams['axes.grid'] = True           # grid on/off
plt.rcParams['grid.alpha'] = 0.4           # grid transparency; 1.0=opaque
plt.rcParams['grid.linestyle'] = 'dotted'
plt.rcParams['legend.fontsize'] = fsize 
plt.rcParams['legend.facecolor'] = 'white'
plt.rcParams['legend.framealpha'] = 1.0   # Legend transparency
plt.rcParams['legend.fancybox'] = False    # Round corners on legend frame?
plt.rcParams['legend.borderaxespad'] = 0.4
plt.rcParams['legend.edgecolor'] = 'black'
plt.rcParams['lines.linewidth'] = 1.4*pltm
plt.rcParams['lines.markersize'] = 4*pltm
plt.rcParams['xtick.direction'] = 'in'     # Ticks inside, outside or both
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['xtick.minor.visible'] = False # Show/hide smaller ticks
plt.rcParams['ytick.minor.visible'] = False
plt.rcParams['xtick.minor.size'] = 4.0*pltm    # Size of smaller ticks
plt.rcParams['ytick.minor.size'] = 4.0*pltm
plt.rcParams['xtick.minor.width'] = 1.0*pltm
plt.rcParams['ytick.minor.width'] = 1.0*pltm
plt.rcParams['xtick.major.size'] = 6.1*pltm    # Size of larger ticks
plt.rcParams['ytick.major.size'] = 6.1*pltm
plt.rcParams['xtick.major.width'] = 1.5*pltm
plt.rcParams['ytick.major.width'] = 1.5*pltm
plt.rcParams['xtick.labelsize'] = fsize
plt.rcParams['ytick.labelsize'] = fsize
plt.rcParams['xtick.major.pad']= 4*pltm      # Space between tick label & axis
plt.rcParams['ytick.major.pad']= 4*pltm
plt.rcParams['font.family'] = 'DeJaVu Serif'   # E.g. Bitstream Vera Sans/serif
plt.rcParams['font.weight'] = 'normal'        # Ticks & legend bold/normal
plt.rcParams['axes.labelweight'] = 'normal' # axis labels bold/normal

# Font for fig. titles
font = {'family': 'DeJaVu Serif', 'color':  'black', 'weight': 'bold','size': fsize+1}

# Plot marker & line styles
#H_iso_color, T_iso_color, T_diff_color = ['#40bad5','#035aa6','#120136']  # All-blue 
H_iso_color, T_iso_color, T_diff_color = ['#ffa41b','#0de2ea','#025297']  # Blue-orange 
#H_iso_color, T_iso_color, T_diff_color = ['#003f5c','#bb053c','#ffa41b']  # Germany
#H_iso_color, T_iso_color, T_diff_color = ['#ff7f0e','#ff7f0e','#2ca02c']  # Matplotlib default-ish

H_iso_style = {'linestyle':':', 'color':H_iso_color, 'markerfacecolor':H_iso_color, 'markeredgecolor':H_iso_color}
T_iso_style = {'linestyle':'-', 'color':T_iso_color, 'markerfacecolor':T_iso_color, 'markeredgecolor':T_iso_color}
T_diff_style = {'linestyle':'--', 'color':T_diff_color, 'markerfacecolor':T_diff_color, 'markeredgecolor':T_diff_color}
isoEx_style = {'H_iso':H_iso_style, 'T_iso':T_iso_style, 'T_diff':T_diff_style} 

# Labels
isoEx_labels = {'H_iso':'H; isoEx', 'T_iso':'T; isoEx', 'T_diff':'T; diffusion'}


