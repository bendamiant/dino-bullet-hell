import pygame

class GameObject:

    def __init__(self, image_file, initial_location, scale_factor=1):
        surface = pygame.image.load(image_file).convert_alpha()
        self.location = initial_location
        self.surface = pygame.transform.scale(surface, 
                                              (surface.get_width() * scale_factor, 
                                               surface.get_height() * scale_factor))
        self.hitbox = pygame.Rect(initial_location[0], initial_location[1], surface.get_width(), surface.get_height())
    
    def get_location(self):
        return self.location

    def set_location(self, x, y):
        self.location = (x, y)
        self.hitbox = pygame.Rect(self.get_location()[0], self.get_location()[1], self.surface.get_width(), self.surface.get_height())