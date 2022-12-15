import pygame

from . import globals

class Paddle(pygame.sprite.Sprite):
    def __init__(self, x_pos=0, y_pos=0, width=globals.WIDTH_UNIT, height=globals.PADDLE_HEIGHT, color=globals.WHITE):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.color = color
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
    
    def __str__(self):
        return "X: " + str(self.rect.x) + "\n\tY: " + str(self.rect.y)

class Wall(pygame.sprite.Sprite):
    def __init__(self, x_pos=0, y_pos=0):
        super().__init__()

        self.image = pygame.Surface([globals.WIDTH_UNIT, globals.PADDLE_HEIGHT*8])
        self.image.fill(globals.BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos

class ClassicalBlocks():
    def __init__(self, x_pos):
        self.blocks = []
        colors = [globals.WHITE, globals.BLUE, globals.GREEN, globals.RED]
        j = 0
        y = 0
        for i in range(32):
            self.blocks.append(Paddle(x_pos=x_pos + j*4*globals.WIDTH_UNIT, y_pos=y*globals.PADDLE_HEIGHT, width=globals.WIDTH_UNIT*3, color=colors[j]))
            print(colors[j])
            y += 1
            print("blocks["+ str(i) +"]:", self.blocks[i])
            if (i+1) % 8 == 0:
                j += 1
                y = 0 

class QuantumPaddles:
    def __init__(self, x_pos=0):
        self.paddles = []
        for i in range(2**globals.NUM_QUBITS):
            self.paddles.append(Paddle(x_pos, i*globals.PADDLE_HEIGHT))
