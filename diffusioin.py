import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import imageio

# Define the grid with lower resolution
N = 20  # Reduce the number of points for lower resolution
x = np.linspace(0, 1, N)
y = np.linspace(0, 1, N)
X, Y = np.meshgrid(x, y)

# Initialize temperature array
T = np.zeros_like(X)

# Apply boundary conditions
T[:, 0] = 100  # Boundary condition: dT/dy = 0 (left face)
T[:, -1] = 100  # Boundary condition: dT/dy = 0 (right face)
T[0, :] = 100  # Boundary condition: dT/dx = 0 (bottom face)
T[-1, :] = 100  # Boundary condition: dT/dx = 0 (top face)

# Define corner temperature (average of adjacent points)
T_corner = np.mean([T[0, 0], T[0, -1], T[-1, 0], T[-1, -1]])
T[0, 0] = T_corner
T[0, -1] = T_corner
T[-1, 0] = T_corner
T[-1, -1] = T_corner

# Parameters for simulation
D = 0.01  # Diffusion coefficient
dt = 0.01  # Time step
num_steps = 100  # Number of simulation steps

# Function to perform one simulation step
def simulate_step(T, D, dt):
    T_new = T.copy()
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            T_new[i, j] = T[i, j] + D * dt * (
                (T[i + 1, j] - 2 * T[i, j] + T[i - 1, j]) / (x[1] - x[0])**2 +
                (T[i, j + 1] - 2 * T[i, j] + T[i, j - 1]) / (y[1] - y[0])**2
            )
    return T_new

# Create a GIF of the temperature distribution
fig, ax = plt.subplots(figsize=(8, 6))

# Plot 1: Temperature Distribution
def update(frame):
    global T
    ax.clear()
    T = simulate_step(T, D, dt)
    ax.contourf(X, Y, T, cmap='hot', levels=20)
    ax.set_title(f'Temperature Distribution (Step {frame})')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    plt.grid(True)

# Save the animation as a GIF
animation_file = 'temperature_distribution0p01.gif'
animation = FuncAnimation(fig, update, frames=num_steps, interval=200)
animation.save(animation_file, writer='imagemagick')

# Save mean temperature variation plot
mean_temperatures = []

def calculate_mean_temperature(T):
    return np.mean(T)

for frame in range(num_steps):
    T = simulate_step(T, D, dt)
    mean_temp = calculate_mean_temperature(T)
    mean_temperatures.append(mean_temp)

mean_temp_plot_file = 'mean_temperature_variation.png'
plt.figure()
plt.plot(range(num_steps), mean_temperatures, marker='*')
plt.title('Mean Temperature Variation with Time')
plt.xlabel('Time Step')
plt.ylabel('Mean Temperature')
plt.grid(True)
plt.savefig(mean_temp_plot_file)
plt.show()

print(f'Temperature distribution animation saved as {animation_file}')
print(f'Mean temperature variation plot saved as {mean_temp_plot_file}')
