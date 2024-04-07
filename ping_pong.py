from pygame import *

width = 1000
height = 800
window = display.set_mode((width, height))
display.set_caption("ping pong")

class Game_Sprite(sprite.Sprite):
     def __init__(self, x,y, path, size, speed):
          super().__init__()
          self.path = path
          self.size = size
          self.image = transform.scale(image.load(self.path), self.size)
          self.speed = speed
          self.rect = self.image.get_rect()
          self.rect.x = x
          self.rect.y = y
     def draw_sprite(self):
          window.blit(self.image, (self.rect.x, self.rect.y))
class Player(Game_Sprite):
    def __init__(self, x,y, path, size, speed):
        super().__init__(x,y, path, size, speed)
    def update1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > -140:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 400:
            self.rect.y += self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > -140:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed

bg = transform.scale(image.load("background.png"), (width, height))
playing = True
player1 = Player(50, 100, "platform.png", (100,800), 10)
player2 = Player(850, 100, "platform.png", (100,800), 10)
while playing:
    for ev in event.get():
        if ev.type == QUIT:
            playing = False
    window.blit(bg,(0,0))
    player1.draw_sprite()
    player2.draw_sprite()
    player1.update1()
    player2.update2()
    display.update()
