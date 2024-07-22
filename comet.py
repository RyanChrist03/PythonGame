import pygame
import random
from monster import Mummy, Alien


class Comet(pygame.sprite.Sprite):
    def __init__(self, Meteorites) :
        super().__init__()
        self.image       = pygame.image.load('PygameAssets/comet.png')
        self.rect        = self.image.get_rect()
        self.velocity    = random.randint(1, 3)
        self.rect.x      = random.randint(20, 850)
        self.rect.y      = - random.randint(0, 800)
        self.comet_event = Meteorites
    
    def remove(self):
        self.comet_event.all_comets.remove(self)
        self.comet_event.game.sound_manager.play('meteorite')
        if len(self.comet_event.all_comets) == 0:
            print("fin de la chute")
            self.comet_event.reset_percent()
            self.comet_event.game.spawn_monster(Mummy)
            self.comet_event.game.spawn_monster(Mummy)
            self.comet_event.game.spawn_monster(Mummy)
            self.comet_event.game.spawn_monster(Alien)



    def fall(self):
        self.rect.y += (self.velocity)

        if self.rect.y >= 500:
            print ("sol")
            self.remove()

            if len(self.comet_event.all_comets) == 0:
                print("fin de la chute")
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False
            
        if self.comet_event.game.check_collision(self, self.comet_event.game.all_player):
            print("joueur touche !")
            self.remove()
            self.comet_event.game.player.damage(20)
    