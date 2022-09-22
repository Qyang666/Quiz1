
from ast import If
from os import stat
import random


'''
Create a Weapon Class definition according to the following specs:

Attributes:
name - user supplied
bullets - random number between 10 and 100000
speed - user supplied
range - user supplied
status - 'Active' (this attribute should be changed to 'Inactive' if bullets 
                    run out.)

Methods:

Create accessor methods for each attribute.

Create a method named 'fire_bullet' that will simulate
firing a bullet. This is accomplished by decreasing the number of bullets by 1 
every time the method is called. When the bullet count reaches zero, it should change
the attribute 'status' to 'Inactive'

'''

class Weapon:
    def __init__(self,name,speed,range):
        self.name = name
        self.bullets = random.randint(10,10000)
        self.speed = speed
        self.range = range
        self.status = 'Active'
     
    
    def fire_bullet(self):
        if self.bullets >0:
            self.bullets =self.bullets - 1 
        else:
            self.bullets=0
            self.status='Inactivde'
        

