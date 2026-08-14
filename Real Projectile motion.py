<<<<<<< HEAD
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox
#PJ in a Vacuum


class Projectile:
    def __init__(self, u, theta):
        self.u = u
        self.theta = theta
        self.ux = u * np.cos(theta)
        self.uy = u * np.sin(theta)


class Environment:
    def __init__(self, g):
        self.g = g


class Simulation:
    def __init__(self, projectile, environment, t):
        self.p = projectile
        self.env = environment
        self.t = t

        # displacement
        self.arrx = []
        self.arry = []
        # velocity
        self.arrv = []
        self.arrt = []

        self.t_final = None

    def run(self):
        p = self.p
        env = self.env
        t = self.t

        #physics
        print(p.ux)
        x = p.ux * t
        y = (p.uy * t) - ((0.5 * env.g) * (t ** 2))  # g is negative
        #instantaneous velocity
        iy = p.uy + ((-1 * env.g) * t)
        instav = np.sqrt((iy ** 2) + (p.ux ** 2))
        print(f' Horizontal Displacement at {t}s is {x.round(2)}m')
        print(f' Vertical Displacement at {t}s is {y.round(2)}m')
        print(f' Velocity at {t}s is {instav.round(2)}m/s')

        t_roots = np.roots([(-0.5 * env.g), p.uy, 0])
        t_final = t_roots[t_roots != 0]
        self.t_final = t_final

        #Numerical methods for time steps
        for ms in np.arange(0, t_final[0], 0.01):
            self.arrt.append(ms)
            self.arrx.append(p.ux * ms)
            tempy = (p.uy * ms) - ((0.5 * env.g) * (ms ** 2))
            self.arry.append(tempy)
            temp_uy = p.uy + ((-1 * env.g) * ms)
            self.arrv.append(np.sqrt((temp_uy ** 2) + (p.ux ** 2)))

        print(f' Maximum height is at {(t_final/2).round(2)}s with Vertical height of {max(self.arry).round(2)}m')
        print(f' Time taken for object to hit ground is {t_final.round(2)} seconds')

    def plot(self):
        # Simulation/ graphical representation
        plt.subplot(1, 2, 1)
        plt.plot(self.arrx, self.arry)
        plt.title("Projectile Motion in a Vacuum")
        plt.xlabel("Horizontal Displacement (m)")
        plt.ylabel("Vertical Displacement (m)")
        plt.subplot(1, 2, 2)
        plt.plot(self.arrt, self.arrv)
        plt.title("Velocity-Time Graph for projectile motion in a Vacuum")
        plt.xlabel("Time(s)")
        plt.ylabel("Velocity (m/s)")
        plt.show()

        plt.subplot(2, 2, 1)
        plt.plot(self.arrt, self.arrx)
        plt.title("Horizontal Displaecment against Time")
        plt.xlabel("Time (s)")
        plt.ylabel("Horizontal Displacement(m)")
        plt.subplot(2, 2, 2)
        plt.plot(self.arrt, self.arry)
        plt.title("Vertical Displacement against Time")
        plt.xlabel("Time (s)")
        plt.ylabel("Vertical Displacement (m)")
        plt.suptitle("Projectile Motion")
        plt.show()


"""
u = float(input("Enter the Inital Velocity:"))
theta = np.radians(float(input("Enter the Angle the projectile makes to the horizontal: ")))
g = float(input("Enter the gravity of your environment: "))
t = float(input("Enter the time at which you want x and y displacement(in seconds): "))
print(t)"""

u = 20
theta = 45
g = 9.81
t = 1

projectile = Projectile(u, theta)
environment = Environment(g)
sim = Simulation(projectile, environment, t)
sim.run()
sim.plot()
=======
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox
#PJ in a Vacuum
"""
u = float(input("Enter the Inital Velocity:"))
theta = np.radians(float(input("Enter the Angle the projectile makes to the horizontal: ")))
g = float(input("Enter the gravity of your environment: "))
t = float(input("Enter the time at which you want x and y displacement(in seconds): "))
print(t)"""

u = 20
theta = 45
g = 9.81
t = 1




ux = 20 * np.cos(theta)
uy = 20 * np.sin(theta)



print(ux)
x = ux * t
y = (uy * t) - ((0.5 * g) * (t ** 2)) # g is negative


#instantaneous velocity
iy = uy + ((-1 * g) * t)
instav = np.sqrt((iy ** 2)+(ux ** 2))

print(f' Horizontal Displacement at {t}s is {x.round(2)}m')
print(f' Vertical Displacement at {t}s is {y.round(2)}m')
print(f' Velocity at {t}s is {instav.round(2)}m/s')

t_roots = np.roots([(-0.5 * g),uy,0])
t_final = t_roots[t_roots != 0]



#displacement
arrx=[]
arry=[]

#velocity

arrv =[]
arrt = []
for ms in np.arange(0,t_final[0],0.01):
    arrt.append(ms)
    arrx.append(ux * ms)
    tempy = (uy * ms) - ((0.5 * g) * (ms ** 2))
    arry.append(tempy)

    temp_uy = uy + ((-1 * g) * ms)
    arrv.append(np.sqrt((temp_uy ** 2)+ (ux ** 2)))
    


print(f' Maximum height is at {(t_final/2).round(2)}s with Vertical height of {max(arry).round(2)}m')
print(f' Time taken for object to hit ground is {t_final.round(2)} seconds')



plt.subplot(1,2,1)
plt.plot(arrx,arry)
plt.title("Projectile Motion in a Vacuum")
plt.xlabel("Horizontal Displacement (m)")
plt.ylabel("Vertical Displacement (m)")


plt.subplot(1,2,2)
plt.plot(arrt,arrv)
plt.title("Velocity-Time Graph for projectile motion in a Vacuum")
plt.xlabel("Time(s)")
plt.ylabel("Velocity (m/s)")


plt.suptitle("Projectile Motion")
plt.show()

    
>>>>>>> 5e6d5c1dbf00d91b1bc86f15010c6446fd88aff1
