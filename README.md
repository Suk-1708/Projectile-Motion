## Part 1 - 3: Euler's method
### What I did:
In this section, I implemented simple Motion equations to graphically display projectile motion in a vacuum. The input parameters were initial velocity, acceleration due to gravity, direction of initial velocity(angle made with the x-axis). For this section, I displayed two graphs, one was a simple x against y, and the other was the Velocity against time. V vs t, clearly shows that velocity reaches 0 at the projectile's max height.
After this, I implemented Euler's First order method. Through this, I produced 5 graphs. 

### Key results:
Through the graphs, it is clear that Euler's first order method was heavily flawed. The difference between the analytical curve against the Euler's curve with different time steps, shows that as the time steps increase in size, the error also increases. Euler's method consistently overestimates the actual height of the projectile. Something that will be countered/improved in the next part (Heun's method).

### graphs:
<img width="1806" height="1002" alt="image" src="https://github.com/user-attachments/assets/25da68d3-ca49-42a3-86aa-b05251a54022" />

#### Eulers graphs:
<img width="1670" height="931" alt="image" src="https://github.com/user-attachments/assets/9f238def-16d6-44e1-9ae8-bacbaf72db8a" />

<img width="1875" height="1003" alt="image" src="https://github.com/user-attachments/assets/5dab5555-c736-4522-a025-41f0d59110ac" />
The difference in the curves of Euler's and Analytical is invisible due to the low resolution of the graph. Here I have zoomed in to show the differences.

<img width="987" height="482" alt="image" src="https://github.com/user-attachments/assets/3aca819d-32fd-419d-aa2c-735d98c2f044" />
The error linearly increases with the time steps magnitude, as seen by the graphs. 


## Part 4: Heun's method
### What I did:
In this section, I implemented the Heun's method on the inputted parameters, and then displayed the results in different ways graphically. Heun's method works by averaging the velocities of the previous time step and the current time step, and then uses this velocity to calculate the y-displacement. This is much more accurate and hardly has any error in situations where acceleration is constant(in this part, acceleration is g). Later I will be working with situations where this is not the case. 

### Key results:
The key results for this part was seeing how much better Heun's method is compared to Euler's First order method. Through my graphs, I was able to see that Heun's trajectory pinpoints the analytical trajectory formed using the motion equations. The negligible error present(displayed in graphical form) was not related to the accuracy of the method itself. Instead, it was caused by the low resolution of python math and rounding(produces error of about 10 ^-16). Although this is very small, if this projectile was in motion over a large distance and required extremely long iterations, the error will accumulate and eventually produce error large enough to make a difference. 

This error is rooted in python itself, and so affects all programs, including the Euler's method that I implemented. However due to the small error scale in Heun's method, the error was much more visible. 

Similarly to Euler's method, larger time step increases the inaccuracy of the program. From the graphs, it can be seen that at time step 0.5s, the line is much more blocky, rather than smooth. Even though at every 0.5s the y displacement calculated matches the analytical point, the large gap due to time step being too large causes the points to be joined up by a straight line, producing an underestimate (since the analyitical curve is concave).

### Graphs:
#### Comparing time steps:
<img width="1726" height="971" alt="image" src="https://github.com/user-attachments/assets/0b542f5c-8546-4601-b8be-054cc4d9265f" />

#### Zoomed in:
<img width="1630" height="918" alt="image" src="https://github.com/user-attachments/assets/0fd8dccd-c6f9-4911-a938-9bee393e41d0" />
You can see from this graph that smaller time steps increases resolution, if the timestep for Heun's method matches the analytical timestep, it will produce identical results. 


#### 4 Graphs:

<img width="1882" height="1013" alt="image" src="https://github.com/user-attachments/assets/2564fc76-bbd9-4634-8b06-46e77130f33c" />

The last graph shows how much 'off'/inaccurate the method gets with lower resolution. 


## Part 5: RK4 Implementation
### What I did:
I implemented RK4 method to my projectile motion. The method was under utilized due to acceleration being constant (lack of drag, this will change in the next part.) Because of this, i finished quite quickly. Anyways, I implemented RK4 method by creating a new RK4 function, which calculated teh velocity at the start, middle, middle, and end. I had to research about simpson's rule to know what values had larger weight when calculating averages, which was quite interesting. 

### Key Results:
I found out how the RK4 method works. Since this method was being executed with constant acceleration, the middle 2 values ended up being the saem for all iterations. This led to the RK4 being a replica/identical to the Heun's method. This is what I meant by it being under-utilized. I had also made two main graphs. One simply showed the trajectory of all 3 methods in one graph. It was clear how the eulers method drifted away from heun and RK4. From the error graph, you could see the errors of the heun and RK4 were identical, in reality there isnt much error there, the graph mainly shows the noise due to the floating point arithametic rounding. 

### Graphs:
<img width="1720" height="952" alt="image" src="https://github.com/user-attachments/assets/4e012277-ae8c-4b74-a8a6-1ed6b5774a13" />
<img width="1693" height="947" alt="image" src="https://github.com/user-attachments/assets/a4628982-506a-4596-b970-f9fd54af137b" />



