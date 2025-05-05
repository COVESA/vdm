
from spec.hierarchy_model import vehicle_ns

from spec.brake import brake
from spec.tire import tire


vehicle_ns.export()

print(brake.model_dump())
print(tire.model_dump())