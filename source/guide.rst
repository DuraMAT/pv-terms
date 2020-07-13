User Guide
==========

Modifying Variables
-------------------

Many variables can be directly used without modification. However, there are many cases where the standard set of variables does not cover a particular application. For this reason, we have provided a list of :ref:`optional suffixes<optional_suffixes>` that can be appended to a variable name. 

For example, one application might be to compare simulated and measured maximum-power-point power. In this case, the base variable **pmp** can be modified into **pmp_sim** and **pmp_meas**. 

In order to standardize some common naming modifications, we have chosen a common order.

1. **_cell**, **_module**, **_string**, **_array**, **_inv**.
2. **_rated**, **_sim**, **_meas**
3. **_XX**, where XX is the name of the particular system.
4. **_interval**, **_cumulative**

Some examples:

- **temperature_module_12** Module temperature sensor 12.
- **current_dc_inv_2132**: dc-side current from inverter 2132.
- **temperature_module_meas**, **temperature_module_sim**: measured and simulated module temperature respectively. 
- **beta_voc_module**, **beta_voc_string**: beta_voc for a module and a string respectively.
- **alpha_isc_module_rated**, **alpha_isc_module_meas**: rated and measured module alpha_isc.