import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
g = 9.8  # gravity
L = 1.0  # length of pendulum
theta = np.pi / 4  # starting angle (in radians)
omega = 0  # initial angular velocity
dt = 0.01  # time step (in seconds)

# Simulation variables
angles = []  # List to store angles
times = []  # List to store time steps

# Initial conditions
time = 0.0
num_steps = 1000  # Number of simulation steps

# Simulate pendulum motion
for _ in range(num_steps):
    alpha = -(g / L) * np.sin(theta)  # Angular acceleration
    omega += alpha * dt  # Update angular velocity
    theta += omega * dt  # Update angle

    # Append data for plotting
    angles.append(theta)
    times.append(time)
    time += dt

# Convert angles to Cartesian coordinates
x = [L * np.sin(angle) for angle in angles]
y = [-L * np.cos(angle) for angle in angles]

# plot setup
fig, ax = plt.subplots()
ax.set_xlim([-L - 0.1, L + 0.1])  # Extend limits slightly for visualization
ax.set_ylim([-L - 0.1, 0.1])
ax.set_aspect('equal')  # Ensure the pendulum appears correctly scaled

line, = ax.plot([], [], 'o-', lw=2)  # Circle marker for pendulum mass


# Animation update function
def update(frame):
    print(f"Frame: {frame}, x: {x[frame]}, y: {y[frame]}")
    line.set_data([0, x[frame]], [0, y[frame]])
    return line,


# creating and saving animation
anim = FuncAnimation(fig, update, frames=num_steps, interval=dt * 1000, blit=True, repeat=False)
anim.save('pendulum2.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
