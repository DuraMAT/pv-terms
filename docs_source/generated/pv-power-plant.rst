
  .. _modules_per_string:

* **modules_per_string**: Number of modules in series in each string

  .. _parallel_strings:

* **parallel_strings**: Number of parallel strings in an array of modules

  .. _tracker_type:

* **tracker_type**: Tracker type, can be 'fixed', 'single-axis' or 'two-axis'

  .. _current_dc_inv_XX:

* **current_dc_inv_XX**: DC current for inverter XX, where XX is the name of the inverter.

  .. _voltage_dc_inv_XX:

* **voltage_dc_inv_XX**: DC voltage for inverter XX, where XX is the name of the inverter.

  .. _power_dc_inv_XX:

* **power_dc_inv_XX**: DC power for inverter XX, where XX is the name of the inverter.

  .. _current_ac_inv_XX:

* **current_ac_inv_XX**: root-mean-squared AC power for inverter XX, where XX is the name of the inverter, in amps

  .. _voltage_ac_inv_XX:

* **voltage_ac_inv_XX**: root-mean-squared AC voltage for inverter XX, where XX is the name of the inverter, in volts

  .. _power_ac_inv_XX:

* **power_ac_inv_XX**: root-mean-squared AC voltage for inverter XX, where XX is the name of the inverter, in watts

  .. _ground_coverage_ratio:

* **ground_coverage_ratio**: A value denoting the ground coverage ratio of a tracker system which utilizes backtracking; i.e. the ratio between the PV array surface area to total ground area. A tracker system with modules 2 meters wide, centered on the tracking axis, with 6 meters between the tracking axes has a gcr of 2/6=0.333. If gcr is not provided, a gcr of 2/7 is default. gcr must be <=1.

  .. _poa_XX:

* **poa_XX**: Plane-of-array irradiance for sensor XX, in W/m^2.

  .. _temperature_module_XX:

* **temperature_module_XX**: Back of module temperature for sensor XX, in C

  .. _temperature_ambient_XX:

* **temperature_ambient_XX**: Ambient (dry bulb) temperature for sensor XX, in C