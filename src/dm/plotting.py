import matplotlib.pyplot as plt
import matlplotlib.colors as colors
import numpy as np

def profile_plot(j_factors, wcs, grid=False, cmap=plt.cm.plasma, **kwargs):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection=wcs)
    im = ax.imshow(j_factors, origin='lower', cmap=cmap, **kwargs)
    cbar = fig.colorbar(im, ax=ax)
    cbar.set_label(r"$\dfrac{d\,J(\theta)}{d\Omega} \times \Delta \Omega_{\mathrm{bin}}$",  fontsize=14,  labelpad=10)
    ax.set_aspect('equal')
    ax.set_ylabel(r'$b$ ($\degree$)')
    ax.set_xlabel(r'$\ell$ ($\degree$)')
    if grid:
        dim_l, dim_b = j_factors.shape
        for x in range(dim_l):
            ax.axvline(x, color='grey', lw=0.3, alpha=0.8)
        for y in range(dim_b):
            ax.axhline(y, color='grey', lw=0.3, alpha=0.8)