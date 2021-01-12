from simple_pendulum import SimplePendulum
from phase_space import multiple_phase_plot
from energy import plot_energy
import matplotlib.pyplot as plt
import sys

initialAngle = int(sys.argv[1])
figure_title = "Simple Pendulum | Initial Angle = " + str(initialAngle) + " Degrees"

fig, axs = plt.subplots(2, 2)

fig.suptitle(figure_title)

theta, omega = multiple_phase_plot(initialAngles = initialAngle)
axs[0, 0].set_title("Phase Space Trajectory")
axs[0, 0].set_xlabel(r"$\theta$")
axs[0, 0].set_ylabel(r"$\dot{\theta}$")
axs[0, 0].plot(theta, omega)

time, Kinetic_Energy, Potential_Energy, Energy = plot_energy(initialAngle = initialAngle)
axs[0, 1].set_title("Energy")
axs[0, 1].set_xlabel("Time (seconds)")
axs[0, 1].set_ylabel("Energy")
axs[0, 1].plot(time, Kinetic_Energy, label = "Kinetic Energy")
axs[0, 1].plot(time, Potential_Energy, label = "Potential Energy")
axs[0, 1].plot(time, Energy, label = "Total Energy")
axs[0, 1].legend(prop = {"size": 6}, loc = "lower right")

pendulum = SimplePendulum(initialAngle = initialAngle)
time, theta, omega, p_theta = pendulum.non_linear_rk4()
axs[1, 0].set_title(r"$\theta$")
axs[1, 0].set_xlabel("Time (seconds)")
axs[1, 0].set_ylabel(r"$\theta$")
axs[1, 0].plot(time, theta)

axs[1, 1].set_title(r"$\dot{\theta}$")
axs[1, 1].set_xlabel("Time (seconds)")
axs[1, 1].set_ylabel(r"$\dot{\theta}$")
axs[1, 1].plot(time, omega)

plt.tight_layout()

plt.show()