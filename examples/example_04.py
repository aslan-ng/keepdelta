"""
A simulation of an object is being dropped on the floor.
The position of the object is saved by deltas
"""

class Model:

    def __init__(
        self,
        position: list,
        velocity: list,
        g: float = 9.81,
        dt:float = 0.01,
        energy_loss: float = 0.8
    ):
        if position[1] < 0:
            raise ValueError
        self.position = position
        self.velocity = velocity
        self.g = g
        self.dt = dt
        self.energy_loss = energy_loss

    def update(self):
        self.position[0] += self.velocity[0] * self.dt  # Update x
        self.position[1] += self.velocity[1] * self.dt  # Update y
        self.velocity[1] -= self.g * self.dt  #  Gravity accelerates the vy

        if self.position[1] <= 0:
            self.position[1] = -self.position[1] * self.energy_loss  # Bounce back (estimation)
            self.velocity[1] = -self.velocity[1] * self.energy_loss  # Reverse and reduce vy


if __name__ == '__main__':

    from copy import deepcopy
    import keepdelta as kd

    model = Model(
        position=[0.0, 10.0],
        velocity=[1.0, 0.0],
        g=9.81,
        dt=0.01,
        energy_loss=0.8
    )
    steps = 1000
    result = {
        'initial_position': deepcopy(model.position),
        'deltas': []
    }
    for _ in range(steps):
        old_position = deepcopy(model.position)
        model.update()
        delta = kd.create(old_position, model.position)
        result['deltas'].append(delta)

    # Loading the result
    position = result['initial_position']
    for delta in result['deltas']:
        position = kd.apply(position, delta)
    print(f'Final position: x:{position[0]:.2f} y:{position[1]:.2f}')
