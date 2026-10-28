import numpy as np
import matplotlib.pyplot as plt
import time as times
#PJ in a Vacuum
u = float(input("Enter the Inital Velocity:"))
theta = np.radians(float(input("Enter the Angle the projectile makes to the horizontal: ")))
g = float(input("Enter the gravity of your environment: "))
t = float(input("Enter the time at which you want x and y displacement(in seconds): "))


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




def euler(uy, ux,y, x,a, dt):
        
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



#_,xy_next_n,_ = heun(10,17.32,0,0,10,0.1)
# Euler
maxy = []
for dt in [0.5, 0.1, 0.05, 0.01]:
    xy = 0
    xx = 0

    h_xy = 0
    h_xx = 0
    uy_euler =  u * np.sin(theta)
    while xy >= 0:
        uy_euler,xy, xx = euler(uy_euler, ux, xy, xx, g, dt)

        if xy >= 0:
            euler_t.append(euler_t[-1] + dt)
            euler_x.append(xx)
            euler_y.append(xy)
            euler_v.append(uy_euler)
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


plot_error(euler_t,euler_error,"yeuler","black", "analytical",ax=axs[1,0])
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

plot_error(heun_t,heun_error,"yheun","black","analytical",ax=axs2[1,0])
axs2[1,0].legend()

max_height_error(heun_max_y,"Black",ax=axs2[1,1])

plt.tight_layout()

plt.show()





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
    return ax,rk4_x, rk4_time,rk4_y






ax3,_, rk4_time, rk4_y = rk4(u,g,0,0.01)
plot_traj(euler_x, euler_y, "Euler", "brown",ax=ax3)
plot_traj(heun_x,heun_y,"Heun","green",ax=ax3)
ax3.legend()
plt.show()


rk4_error = [0]

for y in range(len(arry)):
        rk4_error.append(float(arry[y]) - float(rk4_y[y]) )

fig3,axs3 = plt.subplots(figsize=(6, 5))
plot_error(heun_t,heun_error,"yheun","black","analytical",ax=axs3)
plot_error(euler_t,euler_error,"euler","red","analytical",ax=axs3)
plot_error(rk4_time,rk4_error,"RK4","green","analytical",ax=axs3)
axs3.set_yscale('log')
axs3.legend()
plt.show()

# drag:

pnts = {"earth":[9.81, 1.225], "Moon":[1.62,0], "mars":[3.71,0.020]}
proj = {"mass": 0.15, "cd":0.47, "area":0.0044 } # sphere: apple

#env = {"g":pnts["earth"][0], "rho": pnts["earth"]}
#proj = {"mass": 0.15, "cd":0.47, "area":0.0044 } # sphere: apple
env = {"g":pnts["earth"][0], "rho":pnts["earth"][1], "wind_x":-5,"wind_y":0}

def drag(v, env, proj):
    if isinstance(env, float):
        return 0.5 * env * proj["cd"] * proj["area"] * v**2 / proj["mass"]
    else:
        return 0.5 * env["rho"] * proj["cd"] * proj["area"] * v**2 / proj["mass"]

def acceleration(vx, vy, env, proj, y):
    #rho = env["rho"] * np.exp(-y / env["sh"]) if env.get("sh") else 0.0
    rho = env["rho"] * np.exp(-y / env["sh"]) if env.get("sh") else env["rho"]
    wind_x = env.get("wind_x", 0.0)
    wind_y = env.get("wind_y", 0.0)

    v_rel_x = vx - wind_x
    v_rel_y = vy - wind_y

    v = np.sqrt((v_rel_x ** 2) + (v_rel_y ** 2)) # calculating magnitude of the velocity
    if v > 1e-8:
        drags = drag(v, rho, proj) # calculating the drag using previous function
        ax = (v_rel_x/v) * (-1 * drags) # calculating horizontal acceleration with drag
        ay = (v_rel_y/v) * (- drags) - env["g"] # calculating vertical acc with drag + gravity is subtracted since its falling.
    else:
        ax = 0
        ay = -env["g"] # to counter divinding by 0 error if v is 0/very small
    return ax, ay


def drag_euler(uy, ux, xy,dt,env,proj):
    x = 0
    
    t = [0]
    s_y = [xy]
    s_x = [0]

    while xy >= 0: 
        ax, ay = acceleration(ux,uy,env,proj, xy)
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
    s_y = [xy]
    s_x = [0]

    while xy >= 0:
        ax1, ay1 = acceleration(ux, uy, env, proj,xy)          
        vx_guess = ux + ax1 * dt                              
        vy_guess = uy + ay1 * dt

        ax2, ay2 = acceleration(vx_guess, vy_guess, env, proj,xy)  

        avg_ax = (ax1 + ax2) / 2
        avg_ay = (ay1 + ay2) / 2

        vx_new = ux + avg_ax * dt
        vy_new = uy + avg_ay * dt

        average_vel_x = (ux + vx_new) / 2
        average_vel_y = (uy + vy_new) / 2

        xy = xy + average_vel_y * dt
        x = x + average_vel_x * dt

        uy = vy_new
        ux = vx_new

        t.append(t[-1] + dt)
        s_y.append(xy)
        s_x.append(x)
    return s_y, s_x, t


def drag_rk4(uy, ux, y,dt,env,proj):
    x = 0
    rk4_y = [y] 
    rk4_x = [0]
    rk4_time = [0]
    
    while y >= 0:
        k_ax,k_ay = acceleration(ux,uy,env,proj,y)
        
        k1_v = uy
        k1_vx = ux

        k2_v = uy + ((dt/2) * (k_ay))
        k2_vx = ux + ((dt/2) * (k_ax))
        k_ax2,k_ay2 = acceleration(k2_vx,k2_v,env,proj,y)

        k3_v = uy + ((dt/2) * (k_ay2))
        k3_vx = ux + ((dt/2) * (k_ax2))
        k_ax3,k_ay3 = acceleration(k3_vx,k3_v,env,proj,y)

        k4_v = uy + ((dt) * (k_ay3))
        k4_vx = ux + ((dt) * (k_ax3))
        k_ax4,k_ay4 = acceleration(k4_vx,k4_v,env,proj,y)
        


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
        rk4_time.append(rk4_time[-1] + dt)
        

    return rk4_y,rk4_x, rk4_time

def landing_x(x_arr, y_arr): # removes overshooting by calcualtign the fraction at which 0 lies at. 
    x1, x2 = x_arr[-2], x_arr[-1] 
    y1, y2 = y_arr[-2], y_arr[-1]
    frac = y1 / (y1 - y2)
    return x1 + frac * (x2 - x1)





drag_euler_y, drag_euler_x, drag_euler_t = drag_euler(uy,ux,0,dt, env,proj)
drag_heun_y, drag_heun_x, drag_heun_t = drag_heun(uy,ux,0,dt, env,proj)
drag_rk4_y,drag_rk4_x, drag_rk4_time= drag_rk4(uy,ux,0,dt, env,proj)

if len(drag_heun_y) != len(drag_rk4_y):
    drag_heun_rk4 = [0]
else:
    drag_heun_rk4 = []

for i in range(len(drag_heun_t)):
    drag_heun_rk4.append(abs(drag_heun_y[i] - drag_rk4_y[i])) 

drag_refer_y,drag_refer_x, drag_refer_t, = drag_rk4(uy,ux,0,1e-5, env,proj)
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
    time_step(drag_eulert_x,drag_eulert_y,f"drag Euler dt={time}","Euler")
plt.legend()
plt.show()
for time in dt_error:
    drag_heunt_y, drag_heunt_x, drag_heunt_t = drag_heun(uy,ux,0,time, env,proj)
    drag_heun_error.append(abs(landing_x(drag_heunt_x, drag_heunt_y) - refer_drag_landing))
    time_step(drag_heunt_x,drag_heunt_y,f"drag Heun dtt={time}","Heun")
plt.legend()
plt.show()
for time in dt_error:
    drag_rk4_y, drag_rk4_x, drag_rk4_time = drag_rk4(uy,ux,0,time, env,proj)
    drag_rk4_error.append(abs(landing_x(drag_rk4_x, drag_rk4_y) - refer_drag_landing))
    time_step(drag_rk4_x,drag_rk4_y,f"drag RK4 dt={time}","RK4")
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




pnts = {"earth":[g, 1.225, float('inf')], "Moon":[1.62,0, float('inf')], "mars":[3.71,0.020,11]}


for planets in pnts.keys():

    env = {"g":pnts[planets][0], "rho": pnts[planets][1],"sh": pnts[planets][2]}
    proj = {"mass": 0.15, "cd":0.47, "area":0.0044 } # sphere: apple

    dt = 0.01

    drag_rk4_y,drag_rk4_x, drag_rk4_time = drag_rk4(uy,ux,0,dt, env,proj)

    plt.plot(drag_rk4_x,drag_rk4_y, label=f"RK4 on {planets}")
    plt.xlabel("x (m)")
    plt.ylabel("y (m)")
    plt.title("Trajectory")
    plt.legend()
    


plt.show()

pnts = {"earth": [g, 1.225, float('inf')], "mars": [3.71, 0.020, 11]}

for planets in pnts.keys():

    env = {"g":pnts[planets][0], "rho": pnts[planets][1],"sh": pnts[planets][2]}
    proj = {"mass": 0.15, "cd":0.47, "area":0.0044 } # sphere: apple
    env_no_drag = {"g": pnts[planets][0], "rho": 0.0, "sh": pnts[planets][2]}

    dt = 0.01

    
    y1, x1, t1 = drag_rk4(uy, ux, 0, dt, env, proj)
    y2, x2, t2 = drag_rk4(uy, ux, 0, dt, env_no_drag, proj)
    percent = ((x2[-1] - x1[-1]) / x1[-1]) * 100
    print(f'{planets} increase: {percent} %')
    plt.plot(x1, y1, label=f"{planets} (with drag)")
    plt.plot(x2, y2, linestyle='--', label=f"{planets} (no drag)")

    plt.xlabel("x (m)")
    plt.ylabel("y (m)")
    plt.title("Gravity vs Drag Contribution")
    plt.legend()
plt.show()

ux =  u * np.cos(theta)
uy =  u * np.sin(theta)

fig4, windplot = plt.subplots(2, 2, figsize=(12, 10))
windspeed = {"no wind":0, "Headwind":-100, "Tailwind":100 } # wind speed
# horizontal wind
for i, w in enumerate(windspeed.keys()):
    windx = windspeed.get(w)
    windy =  0

    row = i // 2  
    col = i % 2  

    env = {"g":pnts["earth"][0], "rho":pnts["earth"][1], "wind_x":windx,"wind_y":windy}
    print("done")
    y1, x1, t1 = drag_rk4(uy, ux, 0, 0.01, env, proj)
    plot_traj(x1,y1,f"{w} at {windx}m/s  + RK4 + Drag","red", ax=windplot[row,col])
    windplot[row,col].legend()
    


plt.suptitle("Wind Trajectory comparison")
plt.tight_layout()

plt.show()
#fig4, windplot = plt.subplots(2, 2, figsize=(12, 10))

#plot_traj(x1,y1,label="No Wind + RK4 + Drag", red, ax=windplot[0,0])




def rk4_one_step(uy, ux,x, y,dt,env,proj):
    k_ax,k_ay = acceleration(ux,uy,env,proj,y)        
    k1_v = uy
    k1_vx = ux

    k2_v = uy + ((dt/2) * (k_ay))
    k2_vx = ux + ((dt/2) * (k_ax))
    k_ax2,k_ay2 = acceleration(k2_vx,k2_v,env,proj,y)

    k3_v = uy + ((dt/2) * (k_ay2))
    k3_vx = ux + ((dt/2) * (k_ax2))
    k_ax3,k_ay3 = acceleration(k3_vx,k3_v,env,proj,y)

    k4_v = uy + ((dt) * (k_ay3))
    k4_vx = ux + ((dt) * (k_ax3))
    k_ax4,k_ay4 = acceleration(k4_vx,k4_v,env,proj,y)
    


    average_ax = (k_ax + 2*k_ax2 + 2*k_ax3 + k_ax4)/6
    average_ay = (k_ay + 2*k_ay2 + 2*k_ay3 + k_ay4)/6
    average_vel_y = (k1_v + (2 * (k2_v + k3_v)) + k4_v) / 6
    average_vel_x = (k1_vx + (2 * (k2_vx + k3_vx)) + k4_vx) / 6
    y = y + (average_vel_y * dt) # since average_v is already the y increase
    x = x + ((average_vel_x) * (dt))

    uy = uy + (dt * average_ay)
    ux = ux + (dt * average_ax)
    

    return x, y, ux, uy

def adt_rk4(uy0, ux0,x0, y0,dt,tol,env,proj):
    x,y,uy,ux = x0,y0,uy0,ux0
    xs, ys, ts = [x],[y],[0]
    uxs,uys = [ux],[uy]


    while y >= 0:
        x_big, y_big, ux_big, uy_big = rk4_one_step(uy, ux, x, y, dt, env, proj)
        x_mid, y_mid, ux_mid, uy_mid = rk4_one_step(uy, ux, x, y, dt/2, env, proj)
        x_small, y_small, ux_small, uy_small = rk4_one_step(uy_mid, ux_mid, x_mid, y_mid, dt/2, env, proj)

        
        error = np.sqrt((x_big - x_small)**2 + (y_big - y_small)**2)

        if error < tol:
            x, y, ux, uy = x_small, y_small, ux_small, uy_small

            xs.append(x)
            ys.append(y)
            ts.append(ts[-1] + dt)
            uxs.append(ux)
            uys.append(uy)
            dt *= 1.2  
        else:
            dt *= 0.5

        if ys[-1] < 0: # overshooting/negative y values
            frac = ys[-2] / (ys[-2] - ys[-1])  
            x_land = xs[-2] + frac * (xs[-1] - xs[-2])
            xs[-1], ys[-1] = x_land, 0.0
            uxs[-1] = uxs[-2] + frac * (uxs[-1] - uxs[-2])
            uys[-1] = uys[-2] + frac * (uys[-1] - uys[-2])
            ys[-1] = 0.0

    return np.array(xs), np.array(ys), np.array(ts), np.array(uxs), np.array(uys)

pnts = {"earth":[9.81, 1.225], "Moon":[1.62,0], "mars":[3.71,0.020]}
env = {"g":pnts["earth"][0], "rho": pnts["earth"][1]}
dt = 0.1
xs,ys,ts,uxs,uys = adt_rk4(uy,ux,0,0,dt,1e-5,env,proj)

plt.plot(xs,ys, '-o', markersize=3, label="RK4 + drag")
plt.title("Adaptive Time with RK4")
plt.xlabel("x metres")
plt.ylabel("y metres")
plt.legend()
plt.show()



dts = np.diff(ts)
plt.plot(ts[1:], dts, '-o', markersize=3)
plt.xlabel("t (s)")
plt.ylabel("dt (s)")
plt.title("Adaptive Step Size vs Time")
plt.show()




def compute_energies(xs, ys, uxs, uys, mass, g):
    v_squared = uxs**2 + uys**2
    KE = 0.5 * mass * v_squared
    PE = mass * g * ys
    total = KE + PE
    return KE, PE, total



# drag:
env = {"g":pnts["earth"][0], "rho": 1.225}

xs_e,ys_e,ts_e,uxs_e,uys_e = adt_rk4(uy,ux,0,0,dt,1e-5,env,proj)

ke, pe, kepe = compute_energies(xs_e,ys_e,uxs_e,uys_e,proj["mass"], env["g"])

plt.figure()
plt.plot(ts_e, ke, label="Kinetic") 
plt.plot(ts_e, pe, label="Potential")
plt.plot(ts_e, kepe, label="Total")
plt.xlabel("t (s)")
plt.ylabel("Energy (J)")
plt.title("Energy vs Time (With Drag)")
plt.legend()
plt.show()




env = {"g":pnts["earth"][0], "rho": 0.0} # drag removed since air desnity is removed
xs_e,ys_e,ts_e,uxs_e,uys_e = adt_rk4(uy,ux,0,0,dt,1e-5,env,proj)

ke, pe, kepe = compute_energies(xs_e,ys_e,uxs_e,uys_e,proj["mass"], env["g"])

plt.figure()
plt.plot(ts_e, ke, label="Kinetic")
plt.plot(ts_e, pe, label="Potential")
plt.plot(ts_e, kepe, label="Total")
plt.xlabel("t (s)")
plt.ylabel("Energy (J)")
plt.title("Energy vs Time (Without Drag)")
plt.legend()
plt.show()


def analytical_x_y(t, ux, uy, g):
    x = ux * t
    y = uy * t - 0.5 * g * t**2
    return x, y


def euler_no_drag(ux0, uy0, dt, g):
    x, y, ux, uy = 0, 0, ux0, uy0
    xs, ys = [x], [y]
    
    while True:
        x_new = x + ux * dt
        y_new = y + uy * dt
        uy_new = uy - g * dt
        
        if y_new < 0:
            frac = y / (y - y_new)
            x_land = x + frac * (x_new - x)
            xs.append(x_land)
            ys.append(0.0)
            break
        
        x, y, uy = x_new, y_new, uy_new
        xs.append(x)
        ys.append(y)
    
    return np.array(xs), np.array(ys)


g = 9.81
#Error analysis
dts = [0.1, 0.05,0.025, 0.0125, 0.00625]

err_eul, err_heun, err_rk4 = [],[],[]

for e_dt in dts:
    ex,ey = euler_no_drag(ux,uy,e_dt, g)
    _, rx, _, ry = rk4(u, g,0, e_dt)
    hy, hx, _ = heun(uy,ux,0,0,g,e_dt)

    t_land = 2 * uy / g
    x_analytical, _ = analytical_x_y(t_land, ux, uy, g)

    err_eul.append(abs(ex[-1] - x_analytical))
    err_heun.append(abs(hx[-1] - x_analytical))
    err_rk4.append(abs(rx[-1] - x_analytical))
    plt.close()

plt.loglog(dts, err_eul, 'o-', label='Euler')
plt.loglog(dts, err_rk4, 'o-', label='RK4')
plt.loglog(dts, err_heun, 'o-', label='Heun')

plt.xlabel('dt')
plt.ylabel('Error in landing x (m)')
plt.legend()
plt.title('Convergence: Error vs Step Size')
plt.show()


euler_slope, _ = np.polyfit(np.log(dts), np.log(err_eul), 1)
heun_slope, _ = np.polyfit(np.log(dts), np.log(err_heun), 1)

print(f'Eulers order: {euler_slope:.2f}')
print(f' Heuns order; {heun_slope:.2f}')


#max range

angle_deg = np.arange(0,91)
angle_rad = np.radians(angle_deg)
angle_x, angle_y = np.cos(angle_rad), np.sin(angle_rad)

def rk4_adapter(u, angle_y, angle_x, y, dt, env, proj):
    _, x, _ = drag_rk4(u * angle_y, u * angle_x, y,dt,env,proj)

    return max(x)



v_rk4_drag = np.vectorize(rk4_adapter,  excluded=['env', 'proj'])
drag_x_max = v_rk4_drag(45, angle_y, angle_x, 0,0.01,env,proj)

best_idx = np.argmax(drag_x_max)
max_x = drag_x_max[best_idx]

plt.plot(angle_deg, drag_x_max, label=f'Intial Velocity = 45 m/s')
drag_x_max = v_rk4_drag(30, angle_y, angle_x, 0,0.01,env,proj)
plt.plot(angle_deg, drag_x_max, label=f'Intial Velocity = 30 m/s')
drag_x_max = v_rk4_drag(60, angle_y, angle_x, 0,0.01,env,proj)
plt.plot(angle_deg, drag_x_max, label=f'Intial Velocity = 60 m/s')
drag_x_max = v_rk4_drag(80, angle_y, angle_x, 0,0.01,env,proj)
plt.plot(angle_deg, drag_x_max, label=f'Intial Velocity = 80 m/s')


plt.legend()
plt.xlabel("Angle to horizontal (deg)")
plt.ylabel("Range (m)")
plt.title("Optimal angle with Max range")
plt.show()


# finding minimum velcoity and angle to reach target range starting y = 0.

tolerance = 3
target = 67
vel = np.linspace(10, 100, 100)
min_max_values = []
 # too slow
"""
min_max_values = []

for v in vel:
    angle_rad = np.radians(angle_deg)
    angle_x, angle_y = np.cos(angle_rad), np.sin(angle_rad)
    drag_x_max = v_rk4_drag(v, angle_y, angle_x, 0,0.01,env,proj)

    values_ind = np.where(abs(drag_x_max - target) <= tolerance)[0]
    print(values_ind)
    for idx in values_ind:
        min_max_values.append((v, angle_deg[idx]))



if min_max_values:
    min_max_values.sort()
    print(f'Target of {target}m is reached when Velocity is {min_max_values[0][0]}m/s at angle {min_max_values[0][1]} degrees.')
else:
    print("No combinations found.")
"""
 #tenery search 

def optimal_angle(v0, env, proj, dt, tol=0.01):
    lo, hi = 0.0, 90.0
    while hi - lo > tol:
        m1 = lo + (hi - lo) / 3
        m2 = hi - (hi - lo) / 3
        
        x1,_,_,_, _ = adt_rk4(v0*np.sin(np.radians(m1)), v0*np.cos(np.radians(m1)), 0,0, dt, 0.01,env, proj)
        x2,_,_,_, _ = adt_rk4(v0*np.sin(np.radians(m2)), v0*np.cos(np.radians(m2)), 0,0, dt, 0.01,env, proj)
        r1, r2 = max(x1), max(x2)
        
        if r1 < r2:
            lo = m1
        else:
            hi = m2
    
    angle = (lo + hi) / 2
    x,_,_,ux, uy = adt_rk4(v0*np.sin(np.radians(angle)), v0*np.cos(np.radians(angle)),0,0, dt, 0.01,env, proj)
    
    return max(x), angle, v0


min_speed = []

for targ in [30,60,90,100]:
    min_max_values = []
    for v in vel:
        max_x, xangle, velocity = optimal_angle(v, env,proj, 0.01)
        min_max_values.append((velocity, max_x, xangle))

    nums = [entry for entry in min_max_values if abs(entry[1] - targ) <= tolerance]

    if nums:
        nums.sort()
        print(nums)
        print(f'Target of {targ}m is reached when Velocity is {nums[0][0]:2f}m/s at angle {nums[0][2]:.2f} degrees.')
        min_speed.append(round(nums[0][0], 2)) 
    else:
        print("No combinations found.")
        min_speed.append(None) 
    

plt.plot([30,60,90,100], min_speed, '-o', markersize=3)
plt.title("Min-Speed-Distance graph")
plt.xlabel("distance (m)")
plt.ylabel("Speed (m/s)")
    
plt.show()



#ditance of 30 at v = 18m/s and angle of 42deg
#uy, ux, y,dt,env,proj, rk4_y,rk4_x, rk4_time

_,test_x,_ = drag_rk4(18 * np.sin(np.radians(42)), 18 * np.cos(np.radians(42)), 0, 0.01, env, proj)
print(f'x value of test is {test_x[-1]}m')






#Monte carlo


sim = 10000

# v: Mean(0 - 100), Variation: 1.5 m/s
v0_samples = np.random.normal(50.0, 1.5, sim)

# 0: mean  degrees(0-90), Variation: 1.0 degree)
theta_samples = np.radians(np.random.normal(45.0, 1.0, sim))

# height Mean: 1.5  Variation: 0.05 
h0_samples = np.random.normal(1.5, 0.05, sim)


monte_x_final = []


for i in range(sim):
    m_v0 = v0_samples[i]
    m_0 = theta_samples[i]
    m_h0 = h0_samples[i]

    xs, ys, ts, _, _ = adt_rk4(m_v0 * np.sin(m_0), m_v0 * np.cos(m_0), 0, m_h0, 0.01, 1e-5, env, proj)
    monte_x_final.append(xs[-1])


    if i < 50:
        plt.plot(xs, ys, color='blue', alpha=0.1)


plt.title("Monte Carlo Projectile (sample Size: 50/10,000)")
plt.xlabel("Range (m)")
plt.ylabel("Height (m)")
plt.grid(True)
plt.show()


lp_arr = np.array(monte_x_final)
mean_x = np.mean(lp_arr)
sd_x = np.std(lp_arr)
start = mean_x - 20
end = mean_x + 20
lower, upper = np.percentile(lp_arr, [2.5, 97.5])

total_hits = np.sum((lp_arr >= start) & (lp_arr <= end))
hit_percent = (total_hits / sim) * 100

plt.hist(lp_arr, bins=50, color='skyblue', alpha=0.8)
plt.axvspan(start, end, color='green', alpha=0.15, label=f'target Zone: Hit percentage = {hit_percent}%')
plt.axvline(mean_x, color='red', linestyle='-', linewidth=2, label=f'Mean: {mean_x:.1f}m')
plt.axvline(lower, color='orange', linestyle=':')
plt.axvline(upper, color='orange', linestyle=':', label='95% Confidence Bounds')

plt.xlabel("Distance (m)")
plt.ylabel("Number of Projectiles")
plt.title("Monte Carlo: Distribution of range")
plt.legend()
plt.show()


#np.array(xs), np.array(ys), np.array(ts), np.array(uxs), np.array(uys)
#ef adt_rk4(uy0, ux0,x0, y0,dt,tol,env,proj):    


start = times.perf_counter()


def rk4_adt_adapter(u, angle_y, angle_x, y, dt, env, proj):
    x, _, _, _, _= adt_rk4(u * angle_y, u * angle_x,0, y,dt,1e-8,env,proj)

    return max(x)


ran_ang = np.linspace(1, 89, 500)
ran_vel = np.linspace(5, 50, 50)
ran_ran = np.zeros((len(ran_vel), len(ran_ang)))

ang_grid, vel_grid = np.meshgrid(ran_ang, ran_vel)
ang_grid_rad = np.radians(ang_grid)


v_rk4_drag = np.vectorize(rk4_adt_adapter,  excluded=['env', 'proj'])
x_grid = v_rk4_drag(vel_grid,np.sin(ang_grid_rad), np.cos(ang_grid_rad), 0, 0.01, env, proj)

plt.pcolormesh(ang_grid, vel_grid, x_grid, shading='auto', cmap='viridis')
plt.colorbar(label='Range (m)')
plt.xlabel('Angle (°)')
plt.ylabel('Speed (m/s)')
plt.show()



optimal_angle_idx = np.argmax(x_grid, axis=1)  # index of max range, per speed row
optimal_angles = ran_ang[optimal_angle_idx]

plt.plot(ran_vel, optimal_angles)
plt.xlabel('Speed (m/s)')
plt.ylabel('Optimal angle (°)')
plt.title("Parameter sweep heatmap")
plt.show()

print(f"{times.perf_counter() - start:.2f} s")
