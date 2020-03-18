
  .. _alpha_isc:

* **alpha_isc** (*alpha_sc*): The temperature coefficient of short-circuit current for a PV module, in A/C

  .. _beta_voc:

* **beta_voc**: Temperature coefficient of open-circuit voltage in V/C

  .. _gamma_pmp:

* **gamma_pmp** (*gamma_pdc*): Temperature coefficient of power at maximum power point, in W/C

  .. _gamma_vmp:

* **gamma_vmp**: Temperature coefficient of voltage at maximum power point, in V/C

  .. _gamma_imp:

* **gamma_imp**: Temperature coefficient of voltage at maximum power point, in A/C

  .. _photocurrent:

* **photocurrent**: photocurrent

  .. _photocurrent_ref:

* **photocurrent_ref** (*I_L_ref*): The light-generated current (or photocurrent) at reference conditions, in amperes

  .. _saturation_current:

* **saturation_current**: diode saturation current, in amperes

  .. _saturation_current_ref:

* **saturation_current_ref** (*I_o_ref*): The dark or diode reverse saturation current at reference conditions, in amperes

  .. _resistance_series:

* **resistance_series**: series resistance, in Ohms

  .. _resistance_series_ref:

* **resistance_series_ref** (*R_s*): Series resistance at reference conditions, in Ohms

  .. _resistance_shunt:

* **resistance_shunt**: shunt resistance, in Ohms

  .. _resistance_shunt_ref:

* **resistance_shunt_ref**: shunt resistance at reference conditions, in Ohms.

  .. _voltage_thermal:

* **voltage_thermal**: Thermal voltage per cell in Volts, equal to k_B*T/q where k_B is the boltzman constant (in J/K), T is the temperature (in Kelvin) and q is the electron charge (in Coulombs). 

  .. _nNsVth_ref:

* **nNsVth_ref**: The product of the usual diode ideality factor (n, unitless), number of cells in series (Ns), and cell thermal voltage at reference conditions, in units of V.

  .. _nNsVth:

* **nNsVth**: The product of the usual diode ideality factor (n, unitless), number of cells in series (Ns), and cell thermal voltage, in units of V.

  .. _num_cells_in_series:

* **num_cells_in_series**: Number of cells in series in a PV module, unitless

  .. _diode_factor:

* **diode_factor**: diode ideality factor, unitless

  .. _adjust_cec:

* **adjust_cec** (*adjust*): CEC module parameter

  .. _area_module:

* **area_module**: module area

  .. _noct:

* **noct**: Nominal operating cell temperature.

  .. _band_gap_ref:

* **band_gap_ref**: Energy bandgap at reference temperature in units of eV. 1.121 eV for crystalline silicon. EgRef must be >0. For parameters from the SAM CEC module database, EgRef=1.121 is implicit for all cell types in the parameter estimation algorithm used by NREL.

  .. _irradiance_ref:

* **irradiance_ref**: Reference irradiance in W/m^2. Typical value is 1000 W/m^2.

  .. _temperature_ref:

* **temperature_ref**: Reference temperature in C. Typical value is 25 C

  .. _band_gap_temperature_coeff:

* **band_gap_temperature_coeff** (*dEgdT*): The temperature dependence of the energy bandgap at reference conditions in units of 1/K.