# VSS Refactored or VSS Evolved

## Defining namespaces for hierarchy model

### Purpose of Namespaces
Namespaces are used to organize elements hierarchically within a vehicle data model. They ensure that each element is uniquely identifiable and logically grouped with related elements.

### Naming Conventions
* Use a hierarchical structure separated by dots (e.g., vehicle.chassis.wheel).
* Use snake case to ensure acronyms are seperated by underscrores if at all exist (e.g., vehicle, chassis, wheel).
* Ensure that each namespace is unique within the data model.

## Defining Elements

### Element Types
1. Properties - Quantifiable attributes or states (e.g., speed, temperature).
2. Attributes - Static characteristics (e.g., maxSpeed, fuelType, allowedSAELevels).
3. Actions (Actuators): Commands or control signals (e.g., startEngine, lockDoors).
4. Status (Sensors): Real-time feedback on conditions (e.g., isEngineOn, isDoorOpen).

### Defining Element Fields
1. datatype - Specify the data type (e.g., uint8, float, boolean).
2. unit - Define measurement units where applicable (e.g., km/h, celsius).
3. constraints - Establish constraints such as min, max, allowed values etc.
4. description -Provide a detailed description of the element's function or purpose.


