
from schema.component import Component, Property
from spec.hierarchy_model import tire_ns


# Define the Tire component with its properties
tire = Component(
    name="Tire",
    description="Tire signals for wheel",
    namespace=tire_ns.path,
)

tire_pressure = Property(
            name="Tire.Pressure",
            description="Tire pressure in kilo-Pascal.",
            basetype="uint16"
        )

tire_is_pressure_low = Property(
            name="IsPressureLow",
            description="Tire Pressure Status. True = Low tire pressure. False = Good tire pressure.",
            basetype="boolean"
        )

tire_temperature = Property(
            name="Tire.Temperature",
            description="Tire temperature in Celsius.",
            basetype="float"
        )


tire.properties = [
    tire_pressure,
    tire_is_pressure_low,
    tire_temperature
]