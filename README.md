# vss-next-demo

## VSS - Original Intent
The Vehicle Signal Specification (VSS) - aimed at standardizing the way vehicle data is structured, accessed, and utilized across the industry.

* Common Hierarchical Vehicle Data Model
* Common Interface Definitions


## What we need to consider?
- Data model layer:
  - Define entities, relationships, and constraints clearly.
- Interface layer:
  - IDL schema for defining interfaces.
  - Interfaces on both server and client sides for real-time vehicle queries.
  - Provide mechanisms for querying data collected from vehicle and stored in cloud.
- Connector Layer:
  - Distinguish between the abstract data model (what exists) and interface definitions (how to access it).
  

## Alternatives


### VSS-EVO - evolved or extended

* Updates existing VSS to straightforwardly define hierarchy as namespaces and elements, simplifying the structure and making it more intuitive for developers to implement and understand.


### pyIDL with pydantic

* Provides local validation during instance creation, allowing for custom validators.
* It effectively represents hierarchy models and schemas in Python and can be packaged and distributed.
* Data in objects can be easily converted to various file formats, eliminating the need for further file processing.
* Supports extensions for interface development, providing flexibility and adaptability in implementing interfaces.
* https://docs.pydantic.dev/latest/



### GraphQL

* Primarily used for querying and mutating data with a focus on schema definition for data execution. While it is powerful for data retrieval and manipulation, its role in interface control and real-time operations may be limited unless combined with other technologies.

## Open ended questions
1. What are the use-cases of VSS Spec?
   1. Derive Interfaces (APIs) to interface with Vehicle in real-time?
   2. Translation layer to extract and standardize schema for data collected from vehicles in cloud?

2. GraphQL is primarily used for schema definition to execute operations on data, but it's not inherently effective for data definition itself. What complementary tools or methodologies can be integrated with GraphQL to facilitate both schema and data object creation? 
3. Can GraphQL be effectively employed to build command and control interfaces for vehicles, or is its strength primarily in querying vehicle data for representation purposes?

4. For operations that require control or command functionalities, what are the best practices for implementing interfaces on the vehicle server side using GraphQL?
- 

## Vehicle Data Model NameSpace Specification - Alternative


## **Purpose**: 
To outline the guidelines and best practices for using a dot naming convention in vehicle data models, facilitating consistent naming across various vehicle systems and ensuring clarity, interoperability, and ease of integration.


## Hierarchical Structure

The naming structure follows a hierarchical pattern:
```
<Vehicle>.<Domain>.<Component>.<Subcomponent>.<Element>
```
## Element Definitions:

- Vehicle: The root node, always starting the hierarchy.
- Domain: Major subsystems (e.g., Powertrain, Chassis, Body, Electronics).
- Component: Distinct parts within a domain (e.g., Engine, Transmission, Door).
- Subcomponent: Further divisions within a component if needed (e.g., FrontLeft, CoolingSystem).

- ElementType: Specifies whether the element is an attribute, property, status, action.
- ElementName: Descriptive name of the element (e.g., RPM, Temperature, Start).

## Naming Conventions
CamelCase: Use CamelCase for multi-word names (e.g., EngineCoolant).
Descriptive Names: Use clear and descriptive names that convey the purpose and function.
Avoid Abbreviations: Unless widely recognized (e.g., ABS for Anti-lock Braking System).

#### Elements and Their Valid Constructs

**Vehicle**

- **Valid Constructs**:
  - `Vehicle.<Domain>`
  - `Vehicle.attribute.<ElementName>`
  - `Vehicle.action.<ElementName>`

- **Examples**:
  - `Vehicle.Powertrain`
  - `Vehicle.attribute.VIN`
  - `Vehicle.action.Reset`

**Domain**

- **Valid Constructs**:
  - `<Vehicle>.<Domain>`
  - `<Vehicle>.<Domain>.attribute.<ElementName>`
  - `<Vehicle>.<Domain>.action.<ElementName>`
  - `<Vehicle>.<Domain>.<Component>`

- **Examples**:
  - `Vehicle.Chassis`
  - `Vehicle.Chassis.attribute.Weight`
  - `Vehicle.Electronics.action.UpdateFirmware`
  - `Vehicle.Body.Door`

**Component**

- **Valid Constructs**:
  - `<Vehicle>.<Domain>.<Component>`
  - `<Vehicle>.<Domain>.<Component>.attribute.<ElementName>`
  - `<Vehicle>.<Domain>.<Component>.action.<ElementName>`
  - `<Vehicle>.<Domain>.<Component>.<Subcomponent>`

- **Examples**:
  - `Vehicle.Body.Door`
  - `Vehicle.Powertrain.Engine.attribute.RPM`
  - `Vehicle.Chassis.Brakes.action.Apply`
  - `Vehicle.Body.Door.FrontLeft`

**Subcomponent**

- **Valid Constructs**:
  - `<Vehicle>.<Domain>.<Component>.<Subcomponent>.attribute.<ElementName>`
  - `<Vehicle>.<Domain>.<Component>.<Subcomponent>.action.<ElementName>`

- **Examples**:
  - `Vehicle.Body.Door.FrontLeft.attribute.Status`
  - `Vehicle.Chassis.Wheel.FrontLeft.action.Steer`

#### ElementType and ElementName

- **ElementTypes**: `attribute`, `property`, `action`, `status`
- **ElementNames**: Should be descriptive, using CamelCase for multi-word names (e.g., `Temperature`, `LockDoor`, `EngineCoolant`).


## References
https://wiki.covesa.global/display/WIK4/Data+Models+and+Ontologies?preview=%2F53510159%2F136183835%2FVSS+next.pdf

https://wiki.covesa.global/display/WIK4/Vehicle+Data+Model+Requirements+and+Proposed+Solutions

https://wiki.covesa.global/display/WIK4/Data+Models+and+Ontologies?preview=/53510159/133169352/COVESA_Towards%20vehicle%20DATA%20specification_AMM_04.2024.pdf

https://wiki.covesa.global/display/WIK4/VSS+-+Vehicle+Signal+Specification?preview=/16614221/27099356/COVESA%20Intro%20to%20VSS_AMM2022%20Final%206.pptx#VSSVehicleSignalSpecification-UnderstandingVSS

