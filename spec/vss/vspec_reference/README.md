# VSS Reference Files

This directory contains the exact information used to generate the S2DM GraphQL schema.

- Version used: [vss-tools](https://github.com/COVESA/vss-tools) `7.0.0.dev0`.
- Execute `vspec export s2dm --help` in the tools for more details.

It could serve as a supporting reference for traceability or debugging.

## Files

* **vspec_lookup_spec.yaml** - Complete VSS specification tree (fully processed and expanded).
* **vspec_units.yaml** - Unit definitions for VSS signals.
* **vspec_quantities.yaml** - Quantity definitions categorizing measurements.
* **plural_type_warnings.txt** - VSS branches with plural type names (GraphQL prefers singular).

## Documentation

- [S2DM Exporter](https://github.com/COVESA/vss-tools/blob/master/docs/s2dm.md)
- [VSS Tools](https://github.com/COVESA/vss-tools)
- [COVESA VSS](https://github.com/COVESA/vehicle_signal_specification)
- [COVESA S2DM](https://covesa.github.io/s2dm)
