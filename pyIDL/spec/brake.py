
from schema.component import Component, Property

from spec.hierarchy_model import brake_ns

# Define the Brake component with its properties
brake = Component(
    name="Brake",
    description="Brake signals for wheel",
    namespace=brake_ns.path,
    properties=[
        Property(
            name="FluidLevel",
            description="Brake fluid level as percent. 0 = Empty. 100 = Full.",
            basetype="uint8",
            min=0,
            max=100
        ),
        Property(
            name="IsFluidLevelLow",
            description="Brake fluid level status. True = Brake fluid level low. False = Brake fluid level OK.",
            basetype="boolean"
        ),
        Property(
            name="PadWear",
            description="Brake pad wear as percent. 0 = No Wear. 100 = Worn.",
            basetype="uint8",
            min=0,
            max=100
        ),
        Property(
            name="IsBrakesWorn",
            description="Brake pad wear status. True = Worn. False = Not Worn.",
            basetype="boolean"
        )
    ]
)
