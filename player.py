import pygame
import random
from projectil import projectil
import animation


class Player(animation.AnimateSprite):
    def __init__(self, game):
        super().__init__("player")
        self.game       = game
        self.health     = 100
        self.max_health = 100
        self.attack     = 20
        self.velocity   = 3
        self.all_projectiles = pygame.sprite.Group()
        #self.image = pygame.image.load('PygameAssets/player.png')
        self.rect   = self.image.get_rect()
        self.rect.x = random.randint(450 , 500)
        self.rect.y = 500
    
    def damage(self,amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            self.game.game_over()

    def update_animation(self):
        self.animate()

    def update_health_bar(self,surface):

        pygame.draw.rect( surface, (60, 63, 60),   [self.rect.x +50, self.rect.y +20, self.max_health, 5])
        pygame.draw.rect( surface, (111, 210, 46), [self.rect.x +50, self.rect.y +20, self.health, 5])
    def launch_projectile(self):
       self.start_animation()
       self.all_projectiles.add(projectil(self))
       self.game.sound_manager.play('tir')
   
    def move_right(self):
        if not self.game.check_collision( self,self.game.all_monster):
            self.rect.x += self.velocity
    
    def move_left(self):
        self.rect.x -= self.velocity