__author__ = 'Aditya Vikram Agarwal'
import person


class Princess(person.PersonSprite):
    def __init__(self, image_normal, image_hit, position, width, height, state):
        person.PersonSprite.__init__(self, image_normal, image_hit, position, width, height, state)
