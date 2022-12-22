import random

# Number of particles in the swarm
N = 100

# The dimensions of the search space
D = 2

# The maximum velocity of the particles
V_max = 1

# The maximum number of iterations
max_iterations = 1000

# The target object location
target = [0.5, 0.5]

# Initialize the particle positions and velocities
particles = []
for i in range(N):
    particle = {
        "position": [random.uniform(0, 1) for _ in range(D)],
        "velocity": [random.uniform(-V_max, V_max) for _ in range(D)],
        "best_position": [random.uniform(0, 1) for _ in range(D)],
        "best_value": float("inf")
    }
    particles.append(particle)

# Initialize the global best position and value
global_best_position = [random.uniform(0, 1) for _ in range(D)]
global_best_value = float("inf")

# Iterate over the number of iterations
for iteration in range(max_iterations):
    # Update the particle positions and velocities
    for particle in particles:
        for i in range(D):
            # Update the velocity
            particle["velocity"][i] = 0.7 * particle["velocity"][i] + 0.3 * random.uniform(-1, 1)
            # Limit the velocity
            if particle["velocity"][i] > V_max:
                particle["velocity"][i] = V_max
            if particle["velocity"][i] < -V_max:
                particle["velocity"][i] = -V_max
            # Update the position
            particle["position"][i] += particle["velocity"][i]
            # Limit the position
            if particle["position"][i] > 1:
                particle["position"][i] = 1
            if particle["position"][i] < 0:
                particle["position"][i] = 0

        # Calculate the value of the particle's position
        value = 0
        for i in range(D):
            value += (particle["position"][i] - target[i]) ** 2
        value = value ** 0.5

        # Update the particle's best position and value if necessary
        if value < particle["best_value"]:
            particle["best_position"] = particle["position"].copy()
            particle["best_value"] = value

        # Update the global best position and value if necessary
        if value < global_best_value:
            global_best_position = particle["position"].copy()
            global_best_value = value

# Print the global best position and value
print("Global best position:", global_best_position)
print("Global best value:", global_best_value)

