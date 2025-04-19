import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter

theta = np.linspace(0, 20 * np.pi, 3000)
z = np.exp(1j * theta) + np.exp(1j * np.pi * theta)
x = z.real
y = z.imag

fig, ax = plt.subplots(figsize=(6, 6), facecolor='black')
ax.set_facecolor("black")
ax.axis("off")
ax.set_aspect("equal")
ax.set_xlim(-2.2, 2.2)
ax.set_ylim(-2.2, 2.2)

line, = ax.plot([], [], color='cyan', lw=1.5)
dot, = ax.plot([], [], 'ro', markersize=4)
x_data, y_data = [], []

def update(frame):
    x_data.append(x[frame])
    y_data.append(y[frame])
    line.set_data(x_data, y_data)
    dot.set_data([x[frame]], [y[frame]])
    return line, dot

ani = FuncAnimation(fig, update, frames=len(x), interval=1, blit=True)

writer = FFMpegWriter(fps=60)
ani.save("spiral_pi_animation.mp4", writer=writer)

print("✅ Saved: spiral_pi_animation.mp4")
