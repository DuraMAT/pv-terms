.. generated on 2020-03-16T09:12:40.488883

.. csv-table:: Abbreviations
    :header: "Term", "Description"

    ".. _dc:

    dc","direct current"
    ".. _ac:

    ac","alternating current"
    ".. _poa:

    poa","plane of array (irradiance)"
    ".. _dni:

    dni","direct normal irradiance"
    ".. _dhi:

    dhi","direct horizontal irradiance"
    ".. _ghi:

    ghi","global horizontal irradiance"
    ".. _ref:

    ref","reference"
    ".. _aoi:

    aoi","angle of incidence"
    ".. _mp:

    mp","maximum power"
    ".. _oc:

    oc","open circuit"
    ".. _sc:

    sc","short circuit"
    ".. _vmp:

    vmp","voltage at maximum power"
    ".. _imp:

    imp","current at maximum power"
    ".. _pmp:

    pmp","power at maximum power"
    ".. _isc:

    isc","current at short circuit"
    ".. _voc:

    voc","voltage at open circuit"
    ".. _num:

    num","number"
    ".. _aod:

    aod","aerosol optical depth"
    ".. _noct:

    noct","nominal operating cell temperature"
    ".. _stc:

    stc","standard test conditions"

.. csv-table:: PV system information
    :header: "Term", "Description"

    ".. _modules_per_string:

    modules_per_string","Number of modules in series in each string"
    ".. _num_strings:

    num_strings","Number of parallel strings in an array of modules"
    ".. _tracking:

    tracking","Tracker type, can be 'fixed', 'single-axis' or 'two-axis'"
    ".. _current_dc_inv_XX:

    current_dc_inv_XX","DC current for inverter XX, where XX is the name of the inverter."
    ".. _voltage_dc_inv_XX:

    voltage_dc_inv_XX","DC voltage for inverter XX, where XX is the name of the inverter."
    ".. _power_dc_inv_XX:

    power_dc_inv_XX","DC power for inverter XX, where XX is the name of the inverter."
    ".. _irradiance_poa_o_XX:

    irradiance_poa_o_XX","Plane-of-array irradiance for sensor XX, in W/m^2."
    ".. _temperature_module_o_XX:

    temperature_module_o_XX","Back of module temperature for sensor XX, in C"
    ".. _temperature_ambient_o_XX:

    temperature_ambient_o_XX","Ambient (dry bulb) temperature for sensor XX, in C"
    ".. _elevation:

    elevation","elevation of system, in meters"
    ".. _pressure:

    pressure","pressure, in pascal"
    ".. _ground_coverage_ratio:

    ground_coverage_ratio","nan"
    ".. _zenith_apparent:

    zenith_apparent","nan"
    ".. _azimuth_apparent:

    azimuth_apparent","nan"
    ".. _surface_tilt:

    surface_tilt","nan"
    ".. _surface_azimuth:

    surface_azimuth","nan"
    ".. _zenith_solar:

    zenith_solar","nan"
    ".. _azimuth_solar:

    azimuth_solar","nan"

.. csv-table:: pvlib-python
    :header: "Term", "Description"

    ".. _tz:

    tz","timezone"
    ".. _latitude:

    latitude","latitude, in degrees"
    ".. _longitude:

    longitude","longitude, in degrees"
    ".. _dni:

    dni","direct normal irradiance"
    ".. _dni_extra:

    dni_extra","direct normal irradiance at top of atmosphere (extraterrestrial)"
    ".. _dhi:

    dhi","diffuse horizontal irradiance"
    ".. _ghi:

    ghi","global horizontal irradiance"
    ".. _aoi:

    aoi","angle of incidence between 90deg90deg and 90deg90deg, in degrees"
    ".. _aoi_projection:

    aoi_projection","cos(aoi)"
    ".. _airmass:

    airmass","airmass"
    ".. _airmass_relative:

    airmass_relative","relative airmass"
    ".. _airmass_absolute:

    airmass_absolute","absolute airmass"
    ".. _poa_ground_diffuse:

    poa_ground_diffuse","in plane ground reflected irradiation"
    ".. _poa_direct:

    poa_direct","direct/beam irradiation in plane"
    ".. _poa_diffuse:

    poa_diffuse","total diffuse irradiation in plane. sum of ground and sky diffuse."
    ".. _poa_global:

    poa_global","global irradiation in plane. sum of diffuse and beam projection."
    ".. _poa_sky_diffuse:

    poa_sky_diffuse","diffuse irradiation in plane from scattered light in the atmosphere (without ground reflected irradiation)"
    ".. _effective_irradiance:

    effective_irradiance","irradiance reaching the module's cells, i.e., in the plane of array, reduced by soiling and reflections, adjusted for spectrum"
    ".. _g_poa_effective:

    g_poa_effective","broadband plane of array effective irradiance."
    ".. _array_tilt:

    array_tilt","tilt angle of the surface, in degrees"
    ".. _array_azimuth:

    array_azimuth","azimuth angle of the surface, in degrees"
    ".. _solar_elevation:

    solar_elevation","elevation angle of the sun in degrees"
    ".. _solar_zenith:

    solar_zenith","zenith angle of the sun in degrees"
    ".. _apparent_elevation:

    apparent_elevation","refraction-corrected solar elevation angle in degrees"
    ".. _apparent_zenith:

    apparent_zenith","refraction-corrected solar zenith angle, in degrees"
    ".. _solar_azimuth:

    solar_azimuth","azimuth angle of the sun in degrees East of North"
    ".. _temperature_cell:

    temperature_cell","temperature of the cell, in C"
    ".. _temperature_module:

    temperature_module","temperature of the module, in C"
    ".. _temperature_air:

    temperature_air","temperature of the air"
    ".. _dew_point:

    dew_point","dewpoint temperature, in C"
    ".. _relative_humidity:

    relative_humidity","relative humidity. The ratio of the partial pressure of water vapor to the equilibrium vapor pressure of water at a given temperature, unitless."
    ".. _specific_humidity:

    specific_humidity","nan"
    ".. _absolute_humidity:

    absolute_humidity","nan"
    ".. _vmp:

    vmp","voltage at the maximum power point in Volts"
    ".. _imp:

    imp","current at the maximum power point in Volts"
    ".. _pmp:

    pmp","power at the maximum power point in Volts"
    ".. _voc:

    voc","open circuit module voltage"
    ".. _isc:

    isc","short circuit module current"
    ".. _current_x, current_xx:

    current_x, current_xx","Sandia Array Performance Model IV curve parameters"
    ".. _transposition_factor:

    transposition_factor","the gain ratio of the radiation on inclined plane to global horizontal irradiation: 𝑝𝑜𝑎_𝑔𝑙𝑜𝑏𝑎𝑙𝑔ℎ𝑖poa_globalghi"
    ".. _power_dc_rated:

    power_dc_rated","nameplate DC rating"
    ".. _power_dc:

    power_dc","dc power"
    ".. _power_ac:

    power_ac","ac power"
    ".. _efficiency_inverter:

    efficiency_inverter","inverter efficiency"
    ".. _efficiency_inverter_ref:

    efficiency_inverter_ref","reference inverter efficiency"
    ".. _efficiency_inverter_nominal:

    efficiency_inverter_nominal","nominal inverter efficiency"
    ".. _spectral_mismatch:

    spectral_mismatch","nan"