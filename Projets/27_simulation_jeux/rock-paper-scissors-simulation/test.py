#!/usr/bin/env python3

import pygame
import random
import math

# Initialize pygame
pygame.init()

# Constants
WINDOW_WIDTH = 810
WINDOW_HEIGHT = 1440
ENTITY_RADIUS = 5
SPEED = 3
DETECTION_RADIUS = 100
CONVERSION_RADIUS = 20
EDGE_AVOID_RADIUS = 50
REPULSION_RADIUS = 20

class Entity:
    def __init__(self, x, y, tribe):
        self.x = x
        self.y = y
        self.tribe = tribe

    def move_towards(self, target_x, target_y):
        angle = math.atan2(target_y - self.y, target_x - self.x)
        self.x += (SPEED + random.uniform(-0.3, 0.3)) * math.cos(angle)
        self.y += (SPEED + random.uniform(-0.3, 0.3)) * math.sin(angle)
        self.avoid_edges()

    def move_away_from(self, target_x, target_y):
        angle = math.atan2(target_y - self.y, target_x - self.x)
        self.x -= (SPEED + random.uniform(-0.3, 0.3)) * math.cos(angle)
        self.y -= (SPEED + random.uniform(-0.3, 0.3)) * math.sin(angle)
        self.avoid_edges()

    def distance_to(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def repel_from(self, other):
        if self.distance_to(other) < REPULSION_RADIUS:
            self.move_away_from(other.x, other.y)

    def draw(self):
        # Vous pouvez ajouter ici du code pour afficher les entités à l'écran si nécessaire
        pass

    def avoid_edges(self):
        if self.x < EDGE_AVOID_RADIUS:
            self.move_towards(self.x + EDGE_AVOID_RADIUS, self.y)
        elif self.x > WINDOW_WIDTH - EDGE_AVOID_RADIUS:
            self.move_towards(self.x - EDGE_AVOID_RADIUS, self.y)
        if self.y < EDGE_AVOID_RADIUS:
            self.move_towards(self.x, self.y + EDGE_AVOID_RADIUS)
        elif self.y > WINDOW_HEIGHT - EDGE_AVOID_RADIUS:
            self.move_towards(self.x, self.y - EDGE_AVOID_RADIUS)

entities = [Entity(random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT), 'rock') for _ in range(50)] + \
           [Entity(random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT), 'paper') for _ in range(50)] + \
           [Entity(random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT), 'scissors') for _ in range(50)]

def adjust_movement():
    for entity in entities:
        if entity.tribe == 'rock':
            targets = [e for e in entities if e.tribe == 'scissors']
            threats = [e for e in entities if e.tribe == 'paper']
        elif entity.tribe == 'paper':
            targets = [e for e in entities if e.tribe == 'rock']
            threats = [e for e in entities if e.tribe == 'scissors']
        else:
            targets = [e for e in entities if e.tribe == 'paper']
            threats = [e for e in entities if e.tribe == 'rock']

        for other in entities:
            if entity != other and entity.tribe == other.tribe:
                entity.repel_from(other)

        closest_target = min(targets, key=entity.distance_to, default=None)
        closest_threat = min(threats, key=entity.distance_to, default=None)

        if closest_threat and entity.distance_to(closest_threat) < DETECTION_RADIUS:
            entity.move_away_from(closest_threat.x, closest_threat.y)
        elif closest_target and entity.distance_to(closest_target) < DETECTION_RADIUS:
            entity.move_towards(closest_target.x, closest_target.y)
            if entity.distance_to(closest_target) < CONVERSION_RADIUS:
                closest_target.tribe = entity.tribe
        else:
            entity.move_towards(random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT))

        entity.draw()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Rock Paper Scissors Simulation")
clock = pygame.time.Clock()
running = True

# Game loop
while running:
    screen.fill((0, 0, 0))  # Remplir l'écran avec une couleur de fond (noir dans ce cas)
    adjust_movement()
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
