import random

class Snake:
    def __init__(self):
        self.x = 400
        self.y = 300
        self.size = 10
        self.change_x = 0
        self.change_y = 0
        self.lenght = 1
        self.tails = []
        self.head = []
        self.head.append(self.x)
        self.head.append(self.y)
        self.tails.append(self.head)

class Apple:
    def __init__(self):
        self.size = 10
        self.x = 0
        self.y = 0

    def randpos(self):
        self.x = round(random.randint(50,740)/10) * 10
        self.y = round(random.randint(50,540)/10) * 10