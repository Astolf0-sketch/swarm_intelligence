import pygame
import random
import math

WHITE = (255, 255, 255)

scream_into_the_void = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0]

for i in range(len(scream_into_the_void)):
    scream_into_the_void[i] = [pygame.math.Vector2(0, 0), 0, 0]


class Unit(pygame.sprite.Sprite):
    def __init__(self, WIDTH, HEIGHT, poz_ob_A, poz_ob_B, personal_number):
        pygame.sprite.Sprite.__init__(self)
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.poz_ob_A = poz_ob_A
        self.poz_ob_B = poz_ob_B
        self.personal_number = personal_number
        self.image = pygame.Surface((2, 2))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect = pygame.Vector2(random.randint(10, 490), random.randint(10, 490))
        self.counter_A = random.randint(0, 500)
        self.counter_B = random.randint(0, 500)
        self.trend = random.randint(1, 2)
        self.course = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1)).normalize()
        self.hearing_distance = 35

    def distance(self, vector_1, vector_2):
        vector_2 = pygame.math.Vector2(vector_2[0], vector_2[1])
        vector = vector_2 - vector_1
        distance = math.sqrt(vector.x ** 2 + vector.y ** 2)
        return distance

    def direction(self, vector_1, vector_2):
        return vector_2 - vector_1

    def update(self):
        self.rect += self.course
        self.counter_A += 1
        self.counter_B += 1

        if self.rect.y >= self.WIDTH or self.rect.y <= 0:
            self.course *= -1
        elif self.rect.x >= self.HEIGHT or self.rect.x <= 0:
            self.course *= -1

        if self.distance(self.rect, self.poz_ob_A) <= 25:
            self.counter_A = 0
            if self.trend == 1:
                self.course *= -1
                self.trend = 2

        if self.distance(self.rect, self.poz_ob_B) <= 25:
            self.counter_B = 0
            if self.trend == 2:
                self.course *= -1
                self.trend = 1

        scream_into_the_void[self.personal_number] = [self.rect, self.counter_A + self.hearing_distance,
                                                      self.counter_B + self.hearing_distance]

        for i in range(len(scream_into_the_void)):
            if i != self.personal_number:
                if self.distance(self.rect, scream_into_the_void[i][0]) <= self.hearing_distance:
                    if self.counter_A > scream_into_the_void[i][1]:
                        self.counter_A = scream_into_the_void[i][1]
                        if self.trend == 1:
                            self.course = self.direction(self.rect, scream_into_the_void[i][0]).normalize()
                    if self.counter_B > scream_into_the_void[i][2]:
                        self.counter_B = scream_into_the_void[i][2]
                        if self.trend == 2:
                            self.course = self.direction(self.rect, scream_into_the_void[i][0]).normalize()
