# ParticleSystem
Pygame Particle System, the source code incoudes the demo for the particle system but to use this particle system in any pygame game copy and paste the two classes particle system and particle, include all includes from the source code and add the update, create particle system methods to the main update method. Too add window collision add the particle collision method in the main update method.

# v1.0.1
Added image support allowing images to be displayed instead of a circle or sqaure there is an example of this in the third screenshot

#How to create a particle system

particleSystem = ParticleSystem(X position of the particle system, 
Y position of the particle system ,speed of the particles, 
size of the particle system,
Colour of the particles in RGB format (255,255,255),
boolean if particles have gravity, 
lifetime of the particle in seconds , time.time() ,
the interval of time between each spawn of the particle in seconds ,
if the particles should spawn randomly or uniformly ,
if the paritcle is a circle (if false it will be a sqaure ,
gravity force of the particle ,
angle of where the particle will be spawned in degree 0-360,
spread of the particle from the anlge in degree 0-360
)  

Example too create a particle system shown in the second screenshot:
ps = ParticleSystem(300,250,2,6,(0,0,200),False,4,time.time(),0.01,True, False,0.3,0,360)      





------Screenshots of the Particle System------

![screenshot](/docs/assets/screenshot3.png)

![screenshot](/docs/assets/screenshot4.png)

![screenshot](/docs/assets/screenshot5.png)

![screenshot](/docs/assets/screenshot1.png)

![screenshot](/docs/assets/screenshot2.png)
