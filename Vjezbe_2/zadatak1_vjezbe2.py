import numpy as np
import matplotlib.pyplot as plt

def jednoliko_gibanje(F, m, duration, dt):
    
    num_steps = int(duration / dt)  
    t_values = np.linspace(0, duration, num_steps + 1)  
    x_values = np.zeros(num_steps + 1)  
    v_values = np.zeros(num_steps + 1)  
    a_values = np.zeros(num_steps + 1)  

    x_values[0] = 0
    v_values[0] = 0
    a_values[0] = F / m

    for i in range(num_steps):
        a = F / m
        v_values[i + 1] = v_values[i] + a * dt
        x_values[i + 1] = x_values[i] + v_values[i] * dt
        a_values[i + 1] = a

    return t_values, x_values, v_values, a_values

F = 10  
m = 2   
duration = 10  
dt = 0.01  

t_values, x_values, v_values, a_values = jednoliko_gibanje(F, m, duration, dt)

plt.figure(figsize=(12, 10))

#x-t graf 
plt.subplot(3, 1, 1)
plt.plot(t_values, x_values)
plt.title('Graf položaja čestice u ovisnosti o vremenu')
plt.xlabel('Vrijeme (s)')
plt.ylabel('Položaj (m)')

# v-t graf
plt.subplot(3, 1, 2)
plt.plot(t_values, v_values)
plt.title('Graf brzine čestice u ovisnosti o vremenu')
plt.xlabel('Vrijeme (s)')
plt.ylabel('Brzina (m/s)')

# a-t graf
plt.subplot(3, 1, 3)
plt.plot(t_values, a_values)
plt.title('Graf ubrzanja čestice u ovisnosti o vremenu')
plt.xlabel('Vrijeme (s)')
plt.ylabel('Ubrzanje (m/s^2)')

plt.tight_layout()
plt.show()