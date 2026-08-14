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
theta = np.radians(45)
g = 9.81
t = 1




ux =  u * np.cos(theta)
uy =  u * np.sin(theta)



x = ux * t
y = (uy * t) - ((0.5 * g) * (t ** 2)) 


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

plt.tight_layout()
plt.suptitle("Projectile Motion")
plt.show()

    
euler_x = [0]
euler_y = [0]
euler_v = [0]
euler_t = [0]
euler_error = [0]




def euler(uy, ux,y, x,g, dt):
        
    vel_y = uy - (a * dt)

    xy = y + (uy * dt)
    xx = x + (ux * dt)

    return vel_y, xy, xx



#plotting functions

def plot_traj(x,y, labels, colour, ax=None):
    if ax is None:
        fig, ax = plt.subplots(figsize=(6, 5))
    ax.plot(x, y, label=labels, color=colour)
    ax.set_xlabel('x (m)')
    ax.set_ylabel('y (m)')
    ax.set_title('Trajectory')
    
    return ax

def plot_pos_time(x,y,labels,colour,ax=None):
    if ax is None:
        fix, ax = plt.subplots(figsize=(6,5))
    ax.plot(x, y, label=labels, color=colour)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('y (m)')
    ax.set_title('Position vs time')
    return ax

def plot_error(x,y,labels,colour,label_2,ax=None):
    if ax is None:
        fix, ax = plt.subplots(figsize=(6,5))
    if label_2 is None:
        label_2 = "analytical"
    ax.plot(x, y,label=f'Error = {labels}(t) - {label_2}(t)', color=colour)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Error (m)')
    ax.set_title('Error vs Time')
    return ax

def max_height_error(y,colour,ax=None):
    if ax is None:
        fix, ax = plt.subplots(figsize=(6,5))
    ax.plot([0.5,0.1,0.05,0.01], y, color=colour)
    ax.set_xlabel('Time step(s)')
    ax.set_ylabel('Height Error(m)')
    ax.set_xlim(0,0.5)
    ax.set_title('Height Error vs dt')
    return ax


def time_step(x,y,labels,title_label):
    plt.plot(x,y,label=labels)
    plt.xlabel("x (m)")
    plt.ylabel("y (m)")
    plt.title(f'{title_label}Step-Size comparison')


"""
#_,xy_next_n,_ = heun(10,17.32,0,0,10,0.1)
# Euler
maxy = []
for dt in [0.5,0.1,0.05,0.01]:
    xy = 0
    xx = 0

    h_xy = 0
    h_xx = 0
    uy =  u * np.sin(theta)
    while xy >= 0:
        uy,xy, xx = euler(uy, ux, xy, xx, g, dt)

        if xy >= 0:
            euler_t.append(euler_t[-1] + dt)
            euler_x.append(xx)
            euler_y.append(xy)
            euler_v.append(uy)
        else:
            continue

    maxy.append(max(euler_y) - max(arry))
    time_step(euler_x,euler_y,f'Euler dt={dt}s',"Euler")
    #plt.plot(euler_x,euler_y, label=f'Euler dt={dt}s')
    if dt != 0.01:
        euler_x = [0]
        euler_y = [0]
        euler_v = [0]
        euler_t = [0]

time_step(arrx,arry,"Analytical dt=0.01s","Euler")
plt.legend()
plt.show()
for y in range(len(arry)):
    euler_error.append(float(euler_y[y]) - float(arry[y]))
   



fig, axs = plt.subplots(2, 2, figsize=(12, 10))





# Plot 1: trajectory (top-left)
plot_traj(arrx,arry,"Analytical","black",ax=axs[0,0])
plot_traj(euler_x, euler_y, "Euler", "blue",ax=axs[0,0])
axs[0, 0].legend()

plot_pos_time(arrt,arry, "Analytical", "black", ax=axs[0,1])
plot_pos_time(euler_t,euler_y, "Euler", "blue", ax=axs[0,1])
axs[0,1].legend()


plot_error(euler_t,euler_error,"yeuler","black",ax=axs[1,0])
axs[1,0].legend()


max_height_error(maxy,"red", ax=axs[1,1])


plt.tight_layout()
plt.show()






#Heun
def heun(uy,ux,y,x,a,dt):
    
    heun_x =[0]
    heun_y =[0]
    heun_t = [0]
    xx = 0
    xy_next_n = y
    while xy_next_n >= 0:
            int_vel = uy
            
            uy = int_vel - (a * dt)
            #y = y + (uy * dt)
            
            xx += (ux * dt)
            average_v = (int_vel + uy) / 2
            xy_next_n  = xy_next_n + (average_v * dt)
            if xy_next_n >= 0:
                heun_y.append(xy_next_n)
                heun_x.append(xx)
                heun_t.append(heun_t[-1] + dt)
            else:
                continue
    return heun_y,heun_x, heun_t

heun_error = []
heun_max_y = []


for t in [0.5,0.1,0.05,0.01]:

    heun_y,heun_x,heun_t = heun(u * np.sin(theta), u * np.cos(theta), 0, 0, g, t)
    heun_max_y.append(max(arry) - max(heun_y))
    time_step(heun_x,heun_y,f'Heun dt={t}s',"Heun")

    if t != 0.01:
        heun_y = [0]
        heun_x = [0]
        heun_t = [0]

time_step(arrx,arry,"Analytical dt=0.01s","Heun")
plt.legend()
plt.show()
for y in range(len(arry)):
        heun_error.append(float(arry[y]) - float(heun_y[y]) )



    

fig2, axs2 = plt.subplots(2, 2, figsize=(12, 10))

plot_traj(arrx,arry,"Analytical","black", ax=axs2[0,0])
plot_traj(heun_x,heun_y,"Heun","green",ax=axs2[0,0])
axs2[0,0].legend()


plot_pos_time(arrt, arry,'Analytical','black', ax=axs2[0,1])
plot_pos_time(heun_t, heun_y,'Heun','Red', ax=axs2[0,1])
axs2[0,1].legend()

plot_error(heun_t,heun_error,"yheun","black",ax=axs2[1,0])
axs2[1,0].legend()

max_height_error(heun_max_y,"Black",ax=axs2[1,1])

plt.tight_layout()

plt.show()




#RK4 Method
def rk4(u,  a,y, dt):
    ux =  u * np.cos(theta)
    uy =  u * np.sin(theta)
    x = 0
    k_a = a
    rk4_y = []
    rk4_x = []
    rk4_time = [0]
    while y >= 0:
        rk4_time.append(rk4_time[-1] + dt)
        k1_v = uy
        k2_v = uy - ((dt/2) * (k_a))

        k3_v = uy - ((dt/2) * (k_a))

        k4_v = uy - ((dt) * (k_a))
        uy = k4_v 
        average_v = (k1_v + (2 * (k2_v + k3_v)) + k4_v) / 6
        
        rk4_x.append(x)
        rk4_y.append(y)
        y = y + (average_v * dt) # since average_v is already the y increase
        x = x + ((ux) * (dt))
        
        
    ax = plot_traj(rk4_x,rk4_y, "RK4", "blue")
    ax.legend()
    return ax, rk4_time,rk4_y






ax3, rk4_time, rk4_y = rk4(u,g,0,0.01)
plot_traj(euler_x, euler_y, "Euler", "brown",ax=ax3)
plot_traj(heun_x,heun_y,"Heun","green",ax=ax3)
ax3.legend()
plt.show()


rk4_error = [0]

for y in range(len(arry)):
        rk4_error.append(float(arry[y]) - float(rk4_y[y]) )

fig3,axs3 = plt.subplots(figsize=(6, 5))
plot_error(heun_t,heun_error,"yheun","black",ax=axs3)
plot_error(euler_t,euler_error,"euler","red",ax=axs3)
plot_error(rk4_time,rk4_error,"RK4","green",ax=axs3)
axs3.set_yscale('log')
axs3.legend()
plt.show()

"""

# drag:

env = {"g":9.81, "rho": 1.225}
proj = {"mass": 0.15, "cd":0.47, "area":0.0044 } # sphere: apple
dt = 0.01


def drag(v, env, proj):
    return 0.5 * env["rho"] * proj["cd"] * proj["area"] * v**2 / proj["mass"]

def acceleration(vx, vy, env, proj):

    v = np.sqrt((vx ** 2) + (vy ** 2)) # calculating magnitude of the velocity
    if v > 1e-8:
        drags = drag(v, env, proj) # calculating the drag using previous function
        ax = (vx/v) * (-1 * drags) # calculating horizontal acceleration with drag
        ay = (vy/v) * (- drags) - env["g"] # calculating vertical acc with drag + gravity is subtracted since its falling.
    else:
        ax = 0
        ay = -env["g"] # to counter divinding by 0 error if v is 0/very small
    return ax, ay


def drag_euler(uy, ux, xy,dt,env,proj):
    x = 0
    
    t = [0]
    s_y = [0]
    s_x = [0]

    while xy >= 0: 
        ax, ay = acceleration(ux,uy,env,proj)
        vel_y = uy + (ay * dt)
        vel_x = ux + (ax * dt)
        xy = xy + (uy * dt)
        x = x + (ux * dt)
        uy = vel_y
        ux = vel_x

        t.append(t[-1] + dt)
        s_y.append(xy)
        s_x.append(x)
        
    return s_y, s_x, t


def drag_heun(uy, ux, xy,dt,env,proj):
    x = 0
    t = [0]
    s_y = [0]
    s_x = [0]

    while xy >= 0:
        ax, ay = acceleration(ux,uy,env,proj)
        vel_y = uy + (ay * dt)
        vel_x = ux + (ax * dt) 
        average_vel_y = (vel_y + uy)/2
        average_vel_x = (vel_x + ux)/2
        xy = xy + (average_vel_y * dt)
        x = x + (average_vel_x * dt)
        uy = vel_y
        ux = vel_x

        t.append(t[-1] + dt)
        s_y.append(xy)
        s_x.append(x)
    return s_y, s_x, t


def drag_rk4(uy, ux, y,dt,env,proj):
    x = 0
    rk4_y = [0]
    rk4_x = [0]
    rk4_time = [0]
    while y >= 0:
        k_ax,k_ay = acceleration(ux,uy,env,proj)
        rk4_time.append(rk4_time[-1] + dt)
        k1_v = uy
        k1_vx = ux

        k2_v = uy + ((dt/2) * (k_ay))
        k2_vx = ux + ((dt/2) * (k_ax))
        k_ax2,k_ay2 = acceleration(k2_vx,k2_v,env,proj)

        k3_v = uy + ((dt/2) * (k_ay2))
        k3_vx = ux + ((dt/2) * (k_ax2))
        k_ax3,k_ay3 = acceleration(k3_vx,k3_v,env,proj)

        k4_v = uy + ((dt) * (k_ay3))
        k4_vx = ux + ((dt) * (k_ax3))
        k_ax4,k_ay4 = acceleration(k4_vx,k4_v,env,proj)
        


        average_ax = (k_ax + 2*k_ax2 + 2*k_ax3 + k_ax4)/6
        average_ay = (k_ay + 2*k_ay2 + 2*k_ay3 + k_ay4)/6
        average_vel_y = (k1_v + (2 * (k2_v + k3_v)) + k4_v) / 6
        average_vel_x = (k1_vx + (2 * (k2_vx + k3_vx)) + k4_vx) / 6
        y = y + (average_vel_y * dt) # since average_v is already the y increase
        x = x + ((average_vel_x) * (dt))

        uy = uy + (dt * average_ay)
        ux = ux + (dt * average_ax)
        rk4_x.append(x)
        rk4_y.append(y)

    return rk4_y,rk4_x, rk4_time

def landing_x(x_arr, y_arr): # removes overshooting by calcualtign the fraction at which 0 lies at. 
    x1, x2 = x_arr[-2], x_arr[-1] 
    y1, y2 = y_arr[-2], y_arr[-1]
    frac = y1 / (y1 - y2)
    return x1 + frac * (x2 - x1)





drag_euler_y, drag_euler_x, drag_euler_t = drag_euler(uy,ux,0,dt, env,proj)
drag_heun_y, drag_heun_x, drag_heun_t = drag_heun(uy,ux,0,dt, env,proj)
drag_rk4_y,drag_rk4_x, drag_rk4_time = drag_rk4(uy,ux,0,dt, env,proj)

if dt <= 0.01:
    drag_heun_rk4 = [0]
else:
    drag_heun_rk4 = []
for i in range(len(drag_heun_t)):
    drag_heun_rk4.append(abs(drag_heun_y[i] - drag_rk4_y[i])) 

drag_refer_y,drag_refer_x, drag_refer_t = drag_rk4(uy,ux,0,1e-5, env,proj)
refer_drag_landing = landing_x(drag_refer_x, drag_refer_y)


drag_plot1 = plot_traj(drag_euler_x,drag_euler_y, "Euler with Quadratic Drag", "blue")
plot_traj(drag_heun_x,drag_heun_y, "Heun with Quadratic Drag", "green", ax=drag_plot1)
plot_traj(drag_rk4_x,drag_rk4_y, "RK4 with Quadratic Drag", "red", ax=drag_plot1)
plot_traj(drag_refer_x,drag_refer_y, "Reference RK4 with Quadratic Drag", "black", ax=drag_plot1)
drag_plot1.legend()
plt.show()

drag_plot_2 = plot_error(drag_rk4_time,drag_heun_rk4, "RK4", "black", "Heun")
drag_plot_2.set_yscale('log')
drag_plot_2.legend()
plt.show()




drag_euler_error = []
drag_heun_error = []
drag_rk4_error = []
dt_error = [0.01, 0.05, 0.2, 0.5] 
for time in dt_error:
    drag_eulert_y, drag_eulert_x, drag_eulert_t = drag_euler(uy,ux,0,time, env,proj)
    drag_euler_error.append(abs(landing_x(drag_eulert_x, drag_eulert_y) - refer_drag_landing))
    time_step(drag_eulert_x,drag_eulert_y,f"Euler dt={time}","Euler")
plt.legend()
plt.show()
for time in dt_error:
    drag_heunt_y, drag_heunt_x, drag_heunt_t = drag_heun(uy,ux,0,time, env,proj)
    drag_heun_error.append(abs(landing_x(drag_heunt_x, drag_heunt_y) - refer_drag_landing))
    time_step(drag_heunt_x,drag_heunt_y,f"Heun dt={time}","Heun")
plt.legend()
plt.show()
for time in dt_error:
    drag_rk4_y, drag_rk4_x, drag_rk4_time = drag_rk4(uy,ux,0,time, env,proj)
    drag_rk4_error.append(abs(landing_x(drag_rk4_x, drag_rk4_y) - refer_drag_landing))
    time_step(drag_rk4_x,drag_rk4_y,f"RK4 dt={time}","RK4")
plt.legend()
plt.show()




fig3, drag_plot3 = plt.subplots(2,figsize=(6,5))
drag_plot3[0].plot(dt_error, drag_euler_error, color="red", label="Euler final error vs dt")
drag_plot3[0].plot(dt_error, drag_heun_error, color="blue",label="Heun final error vs dt")
drag_plot3[0].plot(dt_error, drag_rk4_error, color="orange", label="rk4 final error vs dt")


drag_plot3[0].set_xlabel('Time step(s)')
drag_plot3[0].set_ylabel('Range error(m)')
drag_plot3[0].set_xlim(0,0.5)
drag_plot3[0].set_title('final error vs dt')
drag_plot3[0].set_yscale("log")
drag_plot3[0].legend()







drag_euler_error = []
drag_heun_error = []
drag_rk4_error = []
dt_error = [0.001,0.005, 0.01, 0.02, 0.05, 0.1]
for time in dt_error:
    drag_eulert_y, drag_eulert_x, drag_eulert_t = drag_euler(uy,ux,0,time, env,proj)
    drag_euler_error.append(abs(landing_x(drag_eulert_x, drag_eulert_y) - refer_drag_landing))
for time in dt_error:
    drag_heunt_y, drag_heunt_x, drag_heunt_t = drag_heun(uy,ux,0,time, env,proj)
    drag_heun_error.append(abs(landing_x(drag_heunt_x, drag_heunt_y) - refer_drag_landing))
for time in dt_error:
    drag_rk4_y, drag_rk4_x, drag_rk4_time = drag_rk4(uy,ux,0,time, env,proj)
    drag_rk4_error.append(abs(landing_x(drag_rk4_x, drag_rk4_y) - refer_drag_landing))



drag_plot3[1].plot(dt_error, drag_euler_error, color="red", label="Euler final error vs dt")
drag_plot3[1].plot(dt_error, drag_heun_error, color="blue",label="Heun final error vs dt")
drag_plot3[1].plot(dt_error, drag_rk4_error, color="orange", label="rk4 final error vs dt")
drag_plot3[1].set_xlabel('Time step(s)')
drag_plot3[1].set_ylabel('Range error(m)')
drag_plot3[1].set_xlim(0,0.5)
drag_plot3[1].set_title('final error vs dt')
drag_plot3[1].set_yscale("log")
drag_plot3[1].set_xlim(0.001,0.05)
drag_plot3[1].set_xscale("log")
plt.tight_layout()
drag_plot3[1].legend()
plt.show()