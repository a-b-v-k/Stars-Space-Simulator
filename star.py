import pygame
import random
import math

#IMPORT THE NECESSARY MODULES AND INITIALIZE

pygame.init()

screen = pygame.display.set_mode([500, 500])

clock = pygame.time.Clock()

run = True

#DEFINE A CLASS STAR WHICH HOLDS THE PROPERTIES OF AN INDIVIDUAL STAR
class Star:
    def __init__(self):
        self.size = 1.0
        self.x = 250 #INITIAL CORDINATES 
        self.y = 250 #FOR EVERY STAR
        change_x = random.randrange(-30, 30, 1) #CHOOSE A RANDOM OFFSET 
        change_y = random.randrange(-30, 30, 1) #FROM THE INITIAL VALUE
        self.speed = 1
        if(not(change_x == 0 and change_y == 0)):
            self.angle = math.atan2(change_y, change_x) #CALCULATE THE ANGLE ABOUT THE ORIGIN(250, 250)
        self.x += change_x
        self.y += change_y
        self.prex = self.x #STORE THE PREVIOUS VALUE BEFORE
        self.prey = self.y #GETTING UPDATED

    def draw(self): #DRAWS THE STAR AND A POLYGON AS ITS TAIL
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), self.size)
        pygame.draw.polygon(screen, (255, 255, 255), [(self.x, self.y-self.size), (self.x, self.y+self.size), (self.prex, self.prey)])
    
    def move(self): #UPDATE THE POSTITION WITH THE ANGLE FOUND
        self.prex = self.x
        self.prey = self.y
        self.x += math.cos(self.angle)*self.speed
        self.y += math.sin(self.angle)*self.speed
        self.speed += 1


stars = [Star()] #THIS HOLDS THE INSTANCES OF STARS APPEARING ON THE SCREEN
while(run):
    
    clock.tick(30)

    screen.fill((0, 0, 0))
    
    for star in stars:
        if star.x < 0 or star.x > 500 or star.y < 0 or star.y > 500 or (star.x == 250 and star.y == 250):
            stars.remove(star) #REMOVING STARS THAT GO OUT OF BOUNDARIES
        star.draw()
        star.move()

    if(len(stars) < 200): #THIS THE MAXIMUM COUNT OF STARS THAT APPEAR ON THE SCREEN AT ONCE
        stars.append(Star())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    
pygame.quit()