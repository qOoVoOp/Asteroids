from circleshape import *
import random
from constants import ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)
  
  def draw(self, screen):
    pygame.draw.circle(surface=screen, color="white", center=(self.position), radius= self.radius, width=LINE_WIDTH)
  
  def update(self, dt):
    self.position += self.velocity * dt

  def split(self):
    Asteroid.kill(self)
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    else:
      
    
      random_angle = random.uniform(20, 50)

      old_radius = self.radius
      new_radius = old_radius - ASTEROID_MIN_RADIUS

      v1 = self.velocity.rotate(random_angle)
      v2 = self.velocity.rotate(-random_angle)

      new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
      new_asteroid1.velocity = v1
      
      new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius) 
      new_asteroid2.velocity = v2

      log_event("asteroid_split")

    

      

      

  