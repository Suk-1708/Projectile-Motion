#projectile motion
import numpy as np
import matplotlib.pyplot as plt

u = float(input("Enter Inital speed:"))
a = float(input("Enter Vertical accerlation(planetory):"))
h = float(input("Enter Initial height:"))
theta = float(input("enter angle of propgation in degrees: "))
displ_time = round(float(input("Enter time you want instantenous displacement: ")), 3)
veloc_time = round(float(input("Ener time you want instantenous velocity: ")),2)
rad = np.radians((theta))
hu = (u) * (np.cos((rad)))
vu = (u) * (np.sin((rad)))


t = None
for i in np.roots([(0.5 * a), vu, h]):   #coefficent of t^2 quadratic from s= ut + 1/2at^2 is u :
    if i > 0:
        t = round(i,3)
        print(t)

if t == None:
    raise ValueError("No positive root found")

    
x = []
y = []

y_v = []
x_t = []
mxdis = 0
mxvel = 0
instS = (vu * displ_time) + (0.5 * a * (displ_time ** 2))
instV = 0

for i in np.arange(0, t + 0.01, 0.01):# looping for every 0.01 increment of time
        sh = (hu * i) # accerlation horizotnal   = 0/ also range
        sv = (vu * i) + (0.5 * a * (i ** 2))# vertical height
        resultant = np.sqrt((sh ** 2) + (sv ** 2))
        x.append(sh)
        y.append(sv)
        if sv > mxdis:
            mxdis = sv
        if i == veloc_time:
            instV = resultant

        y_v.append(resultant)
        if resultant > mxvel:
            mxvel = resultant
        x_t.append(i)
        




plt.subplot(2,1,1)
plt.xlim(0, max(x)) # Set x-axis
plt.ylim(0, max(y)+(0.1 * max(y)))
plt.plot(x, y)
plt.title("Height-Range Graph", loc = "left")
plt.xlabel("Range(m)")
plt.ylabel("Height(m)")
plt.text((0.01 * max(x)),max(y), "Maximum displacement:" + str(round(mxdis, 2)) + "m", style = "italic", fontsize = 10, color = "black")
if instS > 0:
    plt.text((0.01 * max(x)),max(y) * 0.9, "Displacement at " + str(displ_time)+ "s" + ": " + str(round(instS,2)) + "m", style = "italic", fontsize = 10, color = "black")
else:
    print("TIME HAS NOT ELLASPED")
    print(instS)



plt.subplot(2,1,2)
plt.xlim(0, max(x_t)) # Set x-axis
plt.ylim(0, max(y_v)+(0.1 * max(y_v)))
plt.title("Speed-Time Graph", loc = "left")
plt.xlabel("Time(s)")
plt.ylabel("Speed(m/s)")
plt.plot(x_t,y_v)
plt.text((0.01 * max(x_t)), max(y_v), "Maximum Velocity:" + str(round(mxvel, 2)) + "m/s", style = "italic", fontsize = 10, color = "black")
if instV != 0:
    plt.text(
    0.01 * max(x_t),
    max(y_v) * 0.9,
    f"instantaneous velocity at {veloc_time:.2f}s: {instV:.2f} m/s",
    style="italic",
    fontsize=10,
    color="black"
)
plt.show()


##print out the max height, the range, the time it took. the velocity at any give point, 



    
