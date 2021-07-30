import pygame
import os
import numpy as np
import math
from settings import PURPLE

TOWER_IMAGE = pygame.image.load(os.path.join("images", "rapid_test.png"))


class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def collide(self, enemy):
        x1,y1 = enemy.get_pos()  #get enemy pos
        x2,y2 = self.center   #get center pos
        p1 = np.array([x1,y1])  #Create an array
        p2 = np.array([x2,y2])
        p3 = p2-p1
        p4 = math.hypot(p3[0],p3[1])
        
        if p4 < self.radius:
            return True
        else :
            return False
        
        """
        Q2.2)check whether the enemy is in the circle (attack range), if the enemy is in range return True
        :param enemy: Enemy() object
        :return: Bool
        """

        """
        Hint:
        x1, y1 = enemy.get_pos()
        ...
        """
       

    def draw_transparent(self, win):
        
        #pygame.draw.circle(win,PURPLE,self.center,self.radius)
        # create semi-transparent surface
        transparent_surface = pygame.Surface((1024, 600), pygame.SRCALPHA)
        transparency = 100 # define transparency: 0~255, 0 is fully transparent
        # draw the rectangle on the transparent surface
        pygame.draw.circle(transparent_surface,(192,192, 192,transparency),self.center,self.radius)
        win.blit(transparent_surface, (0,0)) 
         
        """
        Q1) draw the tower effect range, which is a transparent circle.
        :param win: window surface
        :return: None
        """
        
class Tower:
    def __init__(self, x, y):
        self.image = pygame.transform.scale(TOWER_IMAGE, (70, 70))  # image of the tower
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)  # center of the tower
        self.range = 150  # tower attack range
        self.damage = 2   # tower damage
        self.range_circle = Circle(self.rect.center, self.range)  # attack range circle (class Circle())
        self.cd_count = 0  # used in self.is_cool_down()
        self.cd_max_count = 60  # used in self.is_cool_down()
        self.is_selected = True  # the state of whether the tower is selected
        self.type = "tower"

    def is_cool_down(self):
        if self.cd_count < self.cd_max_count:
            self.cd_count += 1
            return False
        else:
            self.cd_count = 0
            return True
        
        
        """
        Q2.1) Return whether the tower is cooling down
        (1) Use a counter to computer whether the tower is cooling down (( self.cd_count
        :return: Bool
        """

        """
        Hint:
        let counter be 0
        if the counter < max counter then
            set counter to counter + 1
        else 
            counter return to zero
        end if
        """
        

    def attack(self, enemy_group):
        for en in enemy_group.get():
            if self.is_cool_down() and self.range_circle.collide(en):
                en.get_hurt(1)
                return
        
        """
        Q2.3) Attack the enemy.
        (1) check the the tower is cool down ((self.is_cool_down()
        (2) if the enemy is in attack range, then enemy get hurt. ((Circle.collide(), enemy.get_hurt()
        :param enemy_group: EnemyGroup()
        :return: None
        """
        

    def is_clicked(self, x, y):
        
        if self.rect.x < x < self.rect.w + self.rect.x and self.rect.y < y < self.rect.h + self.rect.y:
            return True
        else:
            return False
        """
        Bonus) Return whether the tower is clicked
        (1) If the mouse position is on the tower image, return True
        :param x: mouse pos x
        :param y: mouse pos y
        :return: Bool
        """
        

    def get_selected(self, is_selected):
        """
        Bonus) Change the attribute self.is_selected
        :param is_selected: Bool
        :return: None
        """
        self.is_selected = is_selected

    def draw(self, win):
        """
        Draw the tower and the range circle
        :param win:
        :return:
        """
        # draw range circle
        if self.is_selected:
            self.range_circle.draw_transparent(win)
        # draw tower
        win.blit(self.image, self.rect)


class TowerGroup:
    def __init__(self):
        self.constructed_tower = [Tower(250, 380), Tower(420, 400), Tower(600, 400)]

    def get(self):
        return self.constructed_tower

