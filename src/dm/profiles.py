import scipy.integrate as integrate
import numpy as np

class MassProfile:
    """Generic class to specify dark matter profiles.
    
    :param r_s: scale radius.
    :param rho_s: scale density.
    """
    def __init__(self, r_s, rho_s):
        self.r_s = r_s
        self.rho_s = rho_s
        self._r_sun = 8.33
        self._rho_sun = 0.3
    
    def j_factor(self, theta, factor_type='annihilation', **kwargs):
        """J-factor integral on the observer l.o.s.
        
        :param theta: angle between GC and the observer line of sight (los).
        :param factor_type: j-factor type: annihilation or decay.
        :param *args: scipy integrate.quad arugments
        :return: integrated annihilation J-factor on los.
        """
        if factor_type == "annihilation":
            expr = lambda s: (1/self._r_sun)*(self.density(s, theta,geocentric=True)/self._rho_sun)**2
        elif factor_type == "decay":
            expr = lambda s: (1/self._r_sun)*(self.density(s, theta, geocentric=True)/self._rho_sun)
        j_factor, err = integrate.quad(expr, 0, np.inf, **kwargs)
        return j_factor, err
    
    def j_factor_map(self, coord_grid, factor_type='annihilation', **kwargs):
        """Bidimensional map of J-factors. 
        
        :param coord_grid: grid of angular coordinates in the galactic polar system.
        :param factor_type: j-factor type: annihilation or decay.
        :return: integrated j_factor at each grid position.
        """
        factors = []
        for angle in coord_grid.flatten():
            factors.append(self.j_factor(angle, factor_type, **kwargs)[0])
        factors_grid = np.array(factors).reshape(coord_grid.shape)
        return factors_grid
        
    
    def _geocentric_to_galactocentric(self, s, theta):
        """Convert between geocentric and galactocentric distances. 

        :param r: galactocentric distance.
        :param theta: geocentric angle positive from the GC.
        """
        return np.sqrt(self._r_sun**2 + s**2 - 2*s*self._r_sun*np.cos(theta))

    
class MassProfileNFW(MassProfile):
    """Navarro-Frenk-White dark matter density profile."""
    
    def __init__(self, r_s=24.42, rho_s=0.184):
        super().__init__(r_s, rho_s)
        
    def density(self, r, theta=None, geocentric=False):
        if geocentric:
            r = self._geocentric_to_galactocentric(r, theta)
        return self.rho_s/((r/self.r_s)*(1+r/self.r_s)**2)

    
class MassProfileEinasto(MassProfile):
    """Einasto dark matter density profile """
    def __init__(self, r_s=28.44, rho_s=0.033, alpha=0.17):
        super().__init__(r_s, rho_s)
        self.alpha = alpha
        
    def density(self, r, theta=None, geocentric=False):
        if geocentric:
            r = self._geocentric_to_galactocentric(r, theta)
        return self.rho_s * np.exp(-2/self.alpha*((r/self.r_s)**self.alpha-1))      

    
class MassProfileIsothermal(MassProfile):
    """Isothermal dark matter denstiy profile"""
    def __init__(self, r_s=4.38, rho_s=1.387):
        super().__init__(r_s, rho_s)
    
    def density(self, r, theta=None, geocentric=False):
        if geocentric:
            r = self._geocentric_to_galactocentric(r, theta)
        return self.rho_s/(1+(r/self.r_s)**2)
    

class MassProfileBurkert(MassProfile):
    """Burkert dark matter denstiy profile."""
    def __init__(self, r_s=12.67, rho_s=0.712):
        super().__init__(r_s, rho_s)
        
    def density(self, r, theta=None, geocentric=False):
        if geocentric:
            r = self._geocentric_to_galactocentric(r, theta)
        return self.rho_s/((1+r/self.r_s)*(1+(r/self.r_s)**2))
    

class MassProfileMoore(MassProfile):
    """Moore dark matter denstiy profile."""
    def __init__(self, r_s=30.28, rho_s=0.105):
        super().__init__(r_s, rho_s)
    
    def density(self, r, theta=None, geocentric=False):
        if geocentric:
            r = self._geocentric_to_galactocentric(r, theta)
        return self.rho_s*(self.r_s/r)**(1.16) * (1 + r/self.r_s)**(-1.84)
    