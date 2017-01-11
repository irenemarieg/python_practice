# Project 1: Health Potion (The Python Bible Course udemy)
import random

health = 50
potion_health = random.randint(25,50)
difficulty = 3 #1: easy, 2: medium, 3: difficult

health += potion_health
health /= difficulty

print (health)