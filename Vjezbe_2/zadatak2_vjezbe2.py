import numpy as np
import matplotlib.pyplot as plt

def dvostruko_gibanje(v0, theta, duration, dt):
    
    theta_rad = np.radians(theta)  
    num_steps = int(duration / dt)  
    t_values = np.linspace(0, duration, num_steps + 1)  
    x_values = np.zeros(num_steps + 1)  
    y_values = np.zeros(num_steps + 1)  
    vx_values = np.zeros(num_steps + 1)  
    vy_values = np.zeros(num_steps + 1)  

    x_values[0] = 0
    y_values[0] = 0
    vx_values[0] = v0 * np.cos(theta_rad)
    vy_values[0] = v0 * np.sin(theta_rad)

    for i in range(num_steps):
        x_values[i + 1] = x_values[i] + vx_values[i] * dt
        y_values[i + 1] = y_values[i] + vy_values[i] * dt
        vx_values[i + 1] = vx_values[i]
        vy_values[i + 1] = vy_values[i] - 9.81 * dt

    return t_values, x_values, y_values

v0 = 10  
theta = 45  
duration = 10  
dt = 0.01  

t_values, x_values, y_values = dvostruko_gibanje(v0, theta, duration, dt)

plt.figure(figsize=(12, 10))

# x-y graf
plt.subplot(3, 1, 1)
plt.plot(x_values, y_values)
plt.title('Graf položaja čestice u dvije dimenzije')
plt.xlabel('Položaj po x-osi (m)')
plt.ylabel('Položaj po y-osi (m)')


# x-t graf
plt.subplot(3, 1, 2)
plt.plot(t_values, x_values)
plt.title('Graf položaja čestice po x-osi u ovisnosti o vremenu')
plt.xlabel('Vrijeme (s)')
plt.ylabel('Položaj po x-osi (m)')


# y-t graf
plt.subplot(3, 1, 3)
plt.plot(t_values, y_values)
plt.xlabel('Vrijeme (s)')
plt.ylabel('Položaj po y-osi (m)')
plt.title('Graf položaja čestice po y-osi u ovisnosti o vremenu')


plt.tight_layout()
plt.show()