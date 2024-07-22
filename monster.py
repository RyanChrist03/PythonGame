import pygame
import random
import animation


class Monster(animation.AnimateSprite):
    def __init__(self,game, name, size):
        super().__init__(name,size)
        self.game = game
        self.health     = 100
        self.max_health = 100
        self.attack     = 0.2
        #self.image = pygame.image.load('PygameAssets\mummy')
        self.rect        = self.image.get_rect()
        self.rect.x      = 1000 + random.randint(0, 100)
        self.rect.y      = 550
        self.loot_amount = 10
        self.start_animation()

    def set_speed(self, speed):
        self.default_speed = speed
        self.velocity      = random.randint(1, 4)

    
    def damage(self, amount):
        self.health -= amount
        if self.health <= 0 :
            self.rect.x     = 1000 + random.randint(0, 100)
            self.velocity   = random.randint(1, self.default_speed)
            self.health     = self.max_health
            self.game.score += self.loot_amount

            if self.game.comet_event.is_full_loaded():
                self.game.all_monster.remove(self)
                self.game.comet_event.attempt_fall()

    def update_animation(self):
        self.animate(loop = True)

    def update_health_bar(self,surface,):

        pygame.draw.rect( surface, (60, 63, 60),  [self.rect.x +10, self.rect.y -5, self.max_health, 3])
        pygame.draw.rect( surface, (111, 210, 46), [self.rect.x +10, self.rect.y -5, self.health, 3])
    
    def forward(self):
        if not self.game.check_collision(self,self.game.all_player):
            self.rect.x -= self.velocity
        else :
            self.game.player.damage(self.attack)

class Mummy (Monster):
    def __init__(self, game):
        super().__init__(game, "mummy", (130,130))
        self.set_speed(4)

class Alien(Monster):

    def __init__(self, game):

        super().__init__(game, "alien", (300,300))
        self.health      = 200
        self.max_health  = 200
        self.attack      = 0.5
        self.velocity    = random.randint(2, 4)
        self.rect        = self.image.get_rect()
        self.rect.x      = 1000 + random.randint(0, 100)
        self.rect.y      = 425
        self.set_speed(2)
        self.loot_amount = 80
