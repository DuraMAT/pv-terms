
  .. _dhi:

* **dhi** [W/m^2]: Diffuse horizontal irradiance.

  .. _dni:

* **dni** [W/m^2]: Direct normal irradiance; irradiance taken on a plane normal to direction of the sun.

  .. _dni_toa:

* **dni_toa** [W/m^2]: Direct normal irradiance at the top of the atmosphere; dni if the atmosphere did not exist. Also sometimes called extraterrestrial irradiance.

  .. _effective_irradiance:

* **effective_irradiance** [W/m^2]: Irradiance reaching the module's cells, i.e., in the plane of array, reduced by soiling and reflections, adjusted for spectrum.

  .. _ghi:

* **ghi** [W/m^2]: Global horizontal irradiance.

  .. _ghi_toa:

* **ghi_toa** [W/m^2]: Global horizontal irradiance at the top of the atmosphere; ghi as if the atmosphere did not exist.

  .. _poa_toa:

* **poa_toa** [W/m^2]:  Plane-of-array irradiance if the atmosphere did not exist.

  .. _poa_diffuse:

* **poa_diffuse** [W/m^2]: Total diffuse irradiation in plane. sum of ground and sky diffuse.

  .. _poa_direct:

* **poa_direct** [W/m^2]: Direct/beam irradiation in plane.

  .. _poa_global:

* **poa_global** [W/m^2]: Global irradiation in plane. sum of diffuse and beam projection.

  .. _poa_ground_diffuse:

* **poa_ground_diffuse** [W/m^2]: In plane ground reflected irradiation [Deprecated/alternates: *gti*]

  .. _poa_sky_diffuse:

* **poa_sky_diffuse** [W/m^2]: Diffuse irradiation in plane from scattered light in the atmosphere (without ground reflected irradiation)

  .. _clearness_ghi:

* **clearness_ghi** [dimensionless]: Horizontal clearness index, clearness_ghi = ghi/ghi_toa 

  .. _clearness_dni:

* **clearness_dni** [dimensionless]: Normal clearness index, clearness_dni = dni/dni_toa 

  .. _clearness_poa_global:

* **clearness_poa_global** [dimensionless]: Clearness index in plane-of-array, clearness_poa_global = poa_global/poa_toa 

  .. _clearness_poa_direct:

* **clearness_poa_direct** [dimensionless]: Clearness index in plane-of-array, clearness_poa_direct = poa_direct/poa_toa 

  .. _fraction_beam:

* **fraction_beam** [dimensionless]: Fraction of irradiance in beam component, beam_fraction = 1 - dhi/ghi

  .. _fraction_diffuse:

* **fraction_diffuse** [dimensionless]: Fraction of irradiance in diffuse component, beam_fraction = dhi/ghi