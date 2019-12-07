class FaradayRotation():
	"""	A class for Faraday Rotation measurements to determine 
	interstellar magnetic fields.
	"""

	def __init__(self, polarization_angles):
		self.polarization_angles = polarization_angles

	def _get_magnetic_field_map(self):
		r"""
		Testing math docstring.

		Parameters
		----------
		polarization_angles : numpy array
		    Polarization angles measurements in radians.
		faraday_constant : float
			An arbitrary constant that determines the magnetic field in
			CGS units.
		
		Returns
		-------
		map : numpy array
		    Array representing the magnetic field map. Here
		    :math:`\alpha < \beta`. I am here refenrencing publication
		    by Viana [1]_.

		Example
		-------
		Hello.

		>>> print('Olá')
		Olá

		Notes
		-----
		Random notes about random things.

		.. math:: \hat{H}\phi = E\phi

		References
		----------

		.. [1] Viana, A. The H.E.S.S Colaboration.

	    """

		return np.linspace(0, 10, 10)
	
