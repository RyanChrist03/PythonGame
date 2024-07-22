import pygame

class AudioManager :
    def __init__(self):
        self.sounds = {
        'click'     : pygame.mixer.Sound("PygameAssets/sounds/click.ogg"),
        'game_over' : pygame.mixer.Sound("PygameAssets/sounds/click.ogg"),
        'meteorite' : pygame.mixer.Sound("PygameAssets/sounds/click.ogg"),
        'tir'       : pygame.mixer.Sound("PygameAssets/sounds/click.ogg"),
}
    def play(self,name):
        self.sounds[name].play()