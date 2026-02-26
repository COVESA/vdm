# Vehicle Data Model
This repository hosts the COVESA's _Vehicle Data Model (VDM)_.
VDM aims to formalize data of common interest across vehicle-related sub-domains.
In other words, it is not limited to in-vehicle generated data, but can also cover adjacent areas from a vehicle perspective—for example, charging sessions of electric vehicles, in-cabin activities, smart city infrastructure, and nearly anything involved in a "Connected Vehicle" scenario.

As a general rule, only sub-domains of interest to multiple stakeholders are included in `VDM`.
In other words, the `VDM` is expected to cover only those sub-domains that member organizations (or community) can actively contribute to and maintain.
For example, those targeting standardization. 
Private projects can also adopt this modeling approach to manage sub-domains specific to their needs.

![VDM multiple sub-domains](/figures/VDM.png)

VDM is modeled according to the [Simplified Semantic Data Modeling (S2DM)](https://github.com/COVESA/s2dm) approach.

> [!NOTE] In S2DM, domain experts author the specification using the [GraphQL Schema Definition Language (SDL)](https://spec.graphql.org). SDL is used for its simplicity and friendly syntax and does not require implementation of a GraphQL API.

## Getting started
### Explore releases
VDM is released as versioned artifacts as it evolves.
You might want to first explore what is already available.
* Review the released artifacts.
* Pick one and explore its content using the [S2DM tools](https://github.com/COVESA/s2dm).

If the current releases don't meet your needs, consider suggesting additions or modifications to the source files, or create a private complementary model.

### Modifying source files
Source files for the VDM model are available in the `/spec` folder.
To contribute changes to the current VDM model:
* Create an issue describing what is missing or incorrect.
* Discuss it in the issue thread and at maintenance meetings.
* Define an action plan.
* Create a Pull Request (PR) that addresses the issue.

### Complementing with your own model
If you want to specify things outside the scope of VDM, import the VDM (or a subset of it) into your own modeling project.

## Other resources
* [VDM presentation at COVESA's AMM Fall 2025](https://www.youtube.com/watch?v=iYTF1sD1HdQ) - Intro and deep dive sessions. Slides available [HERE](https://covesa.atlassian.net/wiki/spaces/WIK4/pages/184025089/COVESA+All+Member+Meeting+~+October+22-23+2025).
* [Simplified Semantic Data Modeling (S2DM)](https://covesa.github.io/s2dm/).
