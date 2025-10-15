The COVESA Vehicle Data Model (VDM) is a prototype domain model designed for vehicle-related data. It leverages the [GraphQL Schema Definition Language (SDL)](https://spec.graphql.org) to define data structures and adopts the [Simplified Semantic Data Modeling (S2DM)](https://github.com/COVESA/s2dm) approach.

> [!NOTE] The use of `S2DM` and `VDM` does not imply the implementation of a GraphQL API. The `SDL` is chosen for its simplicity and effectiveness in formalizing domain-specific data with certain level of semantics.

## Getting Started
* Watch the [VDM introduction presentation](https://www.youtube.com/watch?v=cLobUt5tO58) to learn the basics and to understand its purpose.
* Get familiar with [S2DM](https://covesa.github.io/s2dm/).
* Check out the [how-to guides](/docs/how_to.md).

## VDM scope
The `SDL` can be used to model various sub-domains related to vehicles. 
For example, the model can consits of:
* In-vehicle generated data (i.e., coming from sensor measurements)
* Person data
* Vehicle cloud services
* Tank or charging stations
* Other infrastructure
* In-cabin activities
* etc.

![VDM multiple sub-domains](/docs/figures/VDM.png)

However, **_the exact scope of the `VDM` is still under discussion_** within the COVESA alliance. 
In general, the `VDM` is expected to cover only those sub-domains that member organizations can actively contribute to and maintain.
For example, those that target standarization. 
Private projects can also adopt this modeling approach to manage sub-domains specific to their needs.

> Checkout other branches which include provisional examples of what `VDM` could cover. Those that find agreement in COVESA will appear in the `main` branch.
