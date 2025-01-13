"""
This example represents a simple simulation of some particles moving in a 2D space.
The result of this simulation is saved in the form of deltas to reconstruct it afterwards.
"""

class Particle:

    def __init__(
        self,
        position: list = [0, 0],
        velocity: list = [0, 0],
        radius: float = 0,
    ):
        self.position = position
        self.velocity = velocity
        self.radius = radius

    def update(self, delta_t: float = 0):
        new_x = self.position[0] + self.velocity[0] * delta_t
        new_y = self.position[1] + self.velocity[1] * delta_t
        self.position = [new_x, new_y]

    def serialize(self):
        """
        Conver the data defining the particle into a Python data format
        """
        return {
            'position': self.position,
            'velocity': self.velocity,
            'radius': self.radius,
        }
    
    def deserialize(self, data):
        """
        Load the object from the proper Python data format
        """
        self.position = data['position']
        self.velocity = data['velocity']
        self.radius = data['radius']


class Model:

    def __init__(self):
        self.particles = []

    def add(self, agent: Particle):
        self.particles.append(agent)
    
    def update(self, delta_t):
        for particle in self.particles:
            particle.update(delta_t)

    def run(self, step_size: float = 1, steps: int = 1):
        for _ in range(steps):
            self.update(step_size)

    def serialize(self):
        result = []
        for particle in self.particles:
            result.append(particle.serialize())
        return result
    
    def deserialize(self, data):
        self.particles = []
        for particle_data in data:
            particle = Particle()
            particle.deserialize(particle_data)
            self.particles.append(particle)


if __name__ == '__main__':

    import keepdelta as kd

    # Setup simulation
    steps = 10
    step_size = 1
    model = Model()
    particle_1 = Particle(position=[1, 2], velocity=[0.1, 0.2], radius=0.3)
    model.add(particle_1)
    particle_2 = Particle(position=[4, -2], velocity=[0.1, 0.2], radius=0.5)
    model.add(particle_2)
    particle_3 = Particle(position=[1, 0], velocity=[0.1, 0.2], radius=0.1)
    model.add(particle_3)
    
    # Run simulation
    initial_state = model.serialize()  # Initial state of model before running simulation
    result = []  # Simulation results in form of deltas
    for _ in range(steps):
        # Create delta by comparing model before and after update
        old_var = model.serialize()
        model.update(step_size)  # Update model
        new_var = model.serialize()
        delta = kd.create(old_var, new_var)
        result.append(delta)

    # Load simulation from deltas
    loaded_model = Model()
    loaded_model.deserialize(initial_state)  # Create the initial model before simulation
    for delta in result:
        # Apply the changes to the model using deltas instead of running simulation
        old_var = loaded_model.serialize()
        new_var = kd.apply(old_var, delta)  
        loaded_model.deserialize(new_var)