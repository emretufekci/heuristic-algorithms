import random

# The speed of sound in water (in m/s)
c = 1450

# The maximum distance that the dolphin can detect objects (in meters)
max_distance = 100

# The resolution of the echolocation (the smaller the value, the higher the resolution)
resolution = 0.1

# The position of the dolphin
position = [0, 0]

# The position of the object to be detected
object_position = [random.uniform(-max_distance, max_distance), random.uniform(-max_distance, 
max_distance)]

# The time it takes for the sound to travel to the object and back (in seconds)
travel_time = 2 * (((object_position[0] - position[0]) ** 2 + (object_position[1] - position[1]) 
** 2) ** 0.5) / c

# The distance to the object (in meters)
distance = travel_time * c / 2

# The position of the object (rounded to the nearest multiple of the resolution)
estimated_position = [round(object_position[0] / resolution) * resolution, 
round(object_position[1] / resolution) * resolution]

# Print the results
print("Actual position:", object_position)
print("Estimated position:", estimated_position)
print("Distance:", distance)

