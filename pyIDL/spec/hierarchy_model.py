from schema.namespace import NameSpace

# Create the root NameSpace for 'vehicle'
vehicle_ns = NameSpace(name='vehicle')

# Define branches for 'vehicle'
body_ns = vehicle_ns.add_branch('body')
chassis_ns = vehicle_ns.add_branch('chassis')
powertrain_ns = vehicle_ns.add_branch('powertrain')
adas_ns = vehicle_ns.add_branch('adas')

# Define branches for 'chassis'
wheel_ns = chassis_ns.add_branch('wheel')

# Define branches for 'wheel'
brake_ns = wheel_ns.add_branch('brake')
tire_ns = wheel_ns.add_branch('tire')

# Define branches for 'adas'
cruise_control_ns = adas_ns.add_branch('cruiseControl')
lane_departure_ns = adas_ns.add_branch('laneDepartureDetection')
obstacle_detection_ns = adas_ns.add_branch('obstacleDetection')
anti_lock_braking_ns = adas_ns.add_branch('antiLockBraking')
traction_control_ns = adas_ns.add_branch('tractionControl')

