import matplotlib as mpl
import matplotlib.cm as cm
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt

#colorbar程式碼

fig = plt.subplots()

# ------colorbar-------
level =[0,1,2,3,4,5,6,7,8,9,10,11]
nlevel = len(level)
cmap1 = mpl.colors.ListedColormap(['purple','blue','deepskyblue','turquoise','mediumturquoise','chartreuse','greenyellow','yellow','gold','orange','orangered','fuchsia'],N=12)
cmap1.set_over('fuchsia')
norm1 = mcolors.Normalize(vmin=0, vmax=11)
norm1 = mcolors.BoundaryNorm(level, nlevel,extend='max')
im = cm.ScalarMappable(norm=norm1, cmap=cmap1)
cbar2 = fig.colorbar(im,extend='max', ticks=level)

# ------colorbar-------
