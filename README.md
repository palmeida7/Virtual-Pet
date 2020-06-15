# dcpythonproject
This is a game project from Python

The purpose of this project is to feature the Python fundamentals that we have learned over the course of two weeks.

We had implemented different aspects such as Classes, Functions, and Importing from one file to the next. Also we call unique modules into our code, such as Random, to produce random integers or choices based on our logic.

The project was originally intended to be a "Virtual Pet." However, I sought to add more user interactions and randomize outcomes based on how a random function affects relevant attributes .

I am importing Class and methods from maincopy.py into petcopy.py for my final project.

######some code snippets
import random

class Pet:   
    def __init__(self, name, typeof, health, attack, exp_pt):
        self.name = name 
        self.typeof = typeof
        self.health = health
        self.attack = attack
        self.exp_pt = exp_pt

#here is the "randomizer" that controls how much an attribute is "hit"
    def roll(self, min, max):
        roll = random.randint(min,max)
        return roll
        
##hunting replenishes your health
    def hunt(self):
        print("Shall we hunt," +" " + self.name +"?")
        self.health += self.roll(0,20) #demonstrates how the random roll is triggered when the hunt function is called
        self.attack += self.roll(0,10)
        self.exp_pt += self.roll(0,5)       
