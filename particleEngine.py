#pygame Particle System
#Made by HaydenD100 
#GitHub: https://github.com/HaydenD100
#This is a particle system, to implement this particle system into your own pygame include all the imports and then inlucde both the Particle and Particle system class



import math
import pygame
import time
import random

class Particle:
    def __init__(self,x,y,vx,vy,size,colour,gravity,lifeTime,time):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.size = size
        self.colour = colour
        self.gravity = gravity
        self.lifeTime = lifeTime
        self.timeSpawned = time
        self.transparency = 255
        
class ParticleSystem:
    def __init__(self,x,y,particleSpeed,size,colour,gravity,lifeTime,time,timePerSpawn,randomParticle,isCircle, gravityForce):
        self.particles = [] #lists of all particles
        self.x = x #x pos of the particle system
        self.y = y #y pos of the particle system
        self.gravityForce = gravityForce #force of gravity on the particle
        self.particleSpeed = particleSpeed #speed of the particle when it is spawned
        self.size = size # size of particle if its a circle this is its radius if its a sqaure this is its width and height
        self.colour = colour # colour of particle this takes a tuple of the 3 RGB values example: (255,0,0) would be red
        self.gravity = gravity #If the particle is affected by gravity
        self.lifeTime = lifeTime # life time of the particle in seconds
        self.timeSpawned = time #time of when the particle is spawned
        self.angle = 0 #angle of the particle that was last spawned this is used when you want a sprinling affect
        self.addedAnlge = 0.6 # this is used for the spirnling affect
        self.timePerSpawn = timePerSpawn #this is how often a particle is spawned in seconds
        self.timeTillNextSpawn = time #this is used too check when the next particle should be spawned
        self.randomParticle = randomParticle #this is a boolean too check if the particles should be spawned at a random angle
        self.isCircle = isCircle #checks if the particle should be a circle if false it will be a sqaure 
        
        
    #updates all the paricles
    def UpdateParticles(self,time):
        for particle in self.particles:
            
            #checks to see if the particle needs too be destoryed
            if(time > particle.timeSpawned + particle.lifeTime):
                self.particles.remove(particle)
            
            #checks if the particle is affected by gravity
            if(particle.gravity == True):
                particle.vy += self.gravityForce
                
            #this is used too check how much time the particle has left and is used too get the transparency value
            precetangeLeft = (particle.timeSpawned + particle.lifeTime - time) / particle.lifeTime
            
            
            particle.transparency = precetangeLeft * 255
            
            #updates particle
            particle.x += particle.vx
            particle.y += particle.vy
        
    #this creates Particles at the a certain time intervule
    def CreateParticles(self,time):
        if(time > self.timeTillNextSpawn + self.timePerSpawn):
            self.timeTillNextSpawn = time 
        
        else:
            return
        
    
        if(self.randomParticle == True):
            self.angle = random.uniform(0,2 * math.pi)
            
           
        vx = math.sin(self.angle) * self.particleSpeed
        vy = math.cos(self.angle) * self.particleSpeed
        self.angle += self.addedAnlge
            
        self.particles.append(Particle(self.x,self.y,vx,vy,self.size,self.colour,self.gravity,self.lifeTime,time))
        
    #this draws the particles
    def DrawParticles(self,screen,ScreenWidth,ScreenHeight):
        surface = pygame.Surface((ScreenWidth,ScreenHeight),pygame.SRCALPHA)

        for particle in self.particles:
            colour = (particle.colour[0],particle.colour[1],particle.colour[2],particle.transparency)
            if(self.isCircle == True):
                pygame.draw.circle(surface,colour,(particle.x,particle.y),particle.size,particle.size)
            else:
                pygame.draw.rect(surface,colour,(particle.x,particle.y,particle.size,particle.size),particle.size)
        screen.blit(surface,(0,0))    
        
        
    #this is used for collison currently used too keep the particles inside the screener
    def Collision(self,screenHeight,ScreenWidth):
        for particle in self.particles:
            
            if(particle.y + particle.size > screenHeight):
                particle.y = screenHeight
                particle.vy *= -1 * 0.6
                
            elif(particle.y + particle.size < 0):
                particle.y = 0
                particle.vy *= -1 * 0.6
                
            if(particle.x + particle.size > ScreenWidth):
                particle.x = ScreenWidth
                particle.vx *= -1 * 0.999
                
            elif(particle.x + particle.size < 0):
                particle.x = 0
                particle.vx *= -1 * 0.999

            

 
ps = ParticleSystem(300,250,2,6,(0,0,200),False,4,time.time(),0.01,True, False,0.3)      

def draw():
    screen.fill((255, 255, 255))
    ps.DrawParticles(screen,640,640)
    pygame.display.update()
    
    
def update():
    ps.CreateParticles(time.time())
    ps.UpdateParticles(time.time())
    ps.Collision(640,640)
    
            

pygame.init()

screen = pygame.display.set_mode((640,640))

running = True
CurrentlyDown = False


LastTIme = time.time()

#this sets the fps the simulation will try too run at
FPS = 60
#for tracking fps
start_time = time.time()
FPSCounter = 0
seconds = 0



while running:
    
    currentTime = time.time()
    if(currentTime <= LastTIme + 1/FPS):
        continue
    LastTIme = currentTime
    
    
    FPSCounter = FPSCounter + 1
    current_time = time.time()
    if current_time - start_time >= seconds:
        seconds = seconds +1
        pygame.display.set_caption("FPS:" + str(FPSCounter))
        FPSCounter = 0
    
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
    
    update()          
    draw()








        
        
            
    
        