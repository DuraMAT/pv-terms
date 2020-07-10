
  .. _temperature_cell:

* **temperature_cell** [C]: Temperature of the cell.

  .. _temperature_module:

* **temperature_module** [C]: temperature of the module.

  .. _temperature_air:

* **temperature_air** [C]: ambient dry bulb temperature.

  .. _modules_per_string:

* **modules_per_string** [dimensionless]: Number of modules in series in each string.

  .. _parallel_strings:

* **parallel_strings** [dimensionless]: Number of parallel strings in an array of modules.

  .. _tracker_type:

* **tracker_type**: Tracker type, can be 'fixed', 'single-axis' or 'two-axis'.

  .. _ground_coverage_ratio:

* **ground_coverage_ratio** [dimensionless]: A value denoting the ground coverage ratio of a tracker system which utilizes backtracking; i.e. the ratio between the PV array surface area to total ground area. A tracker system with modules 2 meters wide, centered on the tracking axis, with 6 meters between the tracking axes has a gcr of 2/6=0.333. If gcr is not provided, a gcr of 2/7 is default. gcr must be <=1.

  .. _aoi:

* **aoi** [degrees]: Angle between direct beam component and surface normal, between 0 and 90.

  .. _surface_azimuth:

* **surface_azimuth** [degrees]: Surface azimuth angles. The azimuth convention is defined as degrees east of north (e.g. North=0, South=180, East=90, West=270)

  .. _surface_tilt:

* **surface_tilt** [degrees]: Surface tilt angle. The tilt angle is defined as degrees from horizontal (e.g. surface facing up = 0, surface facing horizon = 90)

  .. _array_height:

* **array_height** [m]: Height above ground of the bottom edge of the module for a fixed tilt system.

  .. _axis_height:

* **axis_height** [m]: Height above ground of the axis of rotation for a single axis tracker. 

  .. _axis_azimuth:

* **axis_azimuth** [degrees]: Azimuth of axis of rotation for a single-axis tracking system (e.g. North=0, South=180, East=90, West=270).

  .. _axis_tilt:

* **axis_tilt** [degrees]: Orientation of axis of rotation for a single-axis tracking system relative to horizontal. 0 = horizontal.