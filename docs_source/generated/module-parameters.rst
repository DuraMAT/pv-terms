
  .. _alpha_imp:

* **alpha_imp** [A/°C]: Temperature coefficient of current at maximum power point and reference conditions.

  .. _alpha_isc:

* **alpha_isc** [A/°C]: The temperature coefficient of short-circuit current at reference conditions. [Deprecated/alternates: *alpha_sc*]

  .. _alpha_isc_norm:

* **alpha_isc_norm** [1/°C]: alpha_isc/isc_ref. The temperature coefficient of short-circuit current at reference conditions divided by the short-circuit current at reference conditions.

  .. _band_gap_ref:

* **band_gap_ref** [eV]: Energy bandgap at reference temperature. 1.121 eV for crystalline silicon. EgRef must be >0. For parameters from the SAM CEC module database, EgRef=1.121 is implicit for all cell types in the parameter estimation algorithm used by NREL. [Deprecated/alternates: *Egref,EgRef,Eg_ref*]

  .. _band_gap_temperature_coeff:

* **band_gap_temperature_coeff** [1/K]: The temperature dependence of the energy bandgap at reference conditions in units of 1/K.

  .. _beta_vmp:

* **beta_vmp** [V/°C]: Temperature coefficient of voltage at maximum power point and reference conditions.

  .. _beta_voc:

* **beta_voc** [V/°C]: Temperature coefficient of open-circuit voltage at reference conditions.

  .. _beta_voc_norm:

* **beta_voc_norm** [1/°C]: beta_voc/voc_ref. Temperature coefficient of open-circuit voltage at reference conditions divided by the open-circuit voltage at reference conditions.

  .. _cells_in_series:

* **cells_in_series** [dimensionless]: Number of cells in series in a PV module.

  .. _diode_factor:

* **diode_factor** [dimensionless]: Diode ideality factor.

  .. _fill_factor:

* **fill_factor** [dimensionless]: Fill factor of the PV pmp/(voc*isc)

  .. _gamma_pmp:

* **gamma_pmp** [W/°C]: Temperature coefficient of power at maximum power point and reference conditions. [Deprecated/alternates: *gamma_pdc*]

  .. _gamma_pmp_norm:

* **gamma_pmp_norm** [W/°C]: Normalized temperature coefficient of power at maximum power point and reference conditions, equal to gamma_pmp/pmp_ref. [Deprecated/alternates: *gamma_pdc*]

  .. _imp_ref:

* **imp_ref** [A]: Current at maximum power point at reference conditions.

  .. _irradiance_ref:

* **irradiance_ref** [W/m^2]: Reference irradiance. Typical value is 1000 W/m^2. [Deprecated/alternates: *irrad_ref*]

  .. _isc_ref:

* **isc_ref** [A]: Short circuit current at reference conditions. [Deprecated/alternates: *i_sc_ref*]

  .. _module_area:

* **module_area** [m^2]: Module aperture area. The area inside the frame for a rectangular module.

  .. _module_area_active:

* **module_area_active** [m^2]: Total area of cells in a module.

  .. _module_area_external:

* **module_area_external** [m^2]: External dimensions of a module.

  .. _nNsVth:

* **nNsVth** [V]: The product of the usual diode ideality factor (n, unitless), number of cells in series (Ns), and cell thermal voltage.

  .. _nNsVth_ref:

* **nNsVth_ref** [V]: The product of the usual diode ideality factor (n, unitless), number of cells in series (Ns), and cell thermal voltage at reference conditions. [Deprecated/alternates: *a_ref*]

  .. _noct:

* **noct** [°C]: Nominal operating cell temperature.

  .. _photocurrent:

* **photocurrent** [A]: Photo-generated current. [Deprecated/alternates: *I_L*]

  .. _photocurrent_ref:

* **photocurrent_ref** [A]: Photocurrent at reference conditions. [Deprecated/alternates: *I_L_ref*]

  .. _pmp_ref:

* **pmp_ref** [W]: Power at maximum power point at reference conditions. [Deprecated/alternates: *p_mp_ref*]

  .. _resistance_series:

* **resistance_series** [Ohm]: Series resistance. [Deprecated/alternates: *R_s,Rs*]

  .. _resistance_series_ref:

* **resistance_series_ref** [Ohm]: Series resistance at reference conditions. [Deprecated/alternates: *R_s_ref,resistance_series*]

  .. _resistance_shunt:

* **resistance_shunt** [Ohm]: Shunt resistance. [Deprecated/alternates: *R_sh,Rsh*]

  .. _resistance_shunt_ref:

* **resistance_shunt_ref** [Ohm]: Shunt resistance at reference conditions. [Deprecated/alternates: *R_sh_ref*]

  .. _saturation_current:

* **saturation_current** [A]: The dark or diode reverse saturation current. [Deprecated/alternates: *I_o*]

  .. _saturation_current_ref:

* **saturation_current_ref** [A]: The dark or diode reverse saturation current at reference conditions. [Deprecated/alternates: *I_o_ref*]

  .. _temperature_ref:

* **temperature_ref** [°C]: Reference temperature. Typical value is 25 °C. [Deprecated/alternates: *temp_ref*]

  .. _vmp_ref:

* **vmp_ref** [V]: Voltage at maximum power point at reference conditions. [Deprecated/alternates: *v_mp_ref*]

  .. _voc_ref:

* **voc_ref** [V]: Open circuit voltage at reference conditions. [Deprecated/alternates: *v_oc_ref*]

  .. _voltage_thermal:

* **voltage_thermal** [V]: Thermal voltage per cell, equal to k_B*T/q where k_B is the boltzman constant (in J/K), T is the temperature (in Kelvin) and q is the electron charge (in Coulombs). 