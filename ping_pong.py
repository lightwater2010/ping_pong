from pygame import *
from random import choice
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
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 500:
            self.rect.y += self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500:
            self.rect.y += self.speed
class Ball(Game_Sprite):
    def __init__(self, x,y, path, size, speed, speed_y):
        super().__init__(x,y, path, size, speed)
        self.speed_y = speed_y
        self.random = choice([0,1])
    def update(self):
        if self.random == 0:
            self.rect.x -= self.speed
            self.rect.y += self.speed_y   
        else:
            self.rect.x += self.speed
            self.rect.y += self.speed_y
bg = transform.scale(image.load("background.png"), (width, height))
ball = Ball(400, 400, "ball.png",(120,70), 2, 4)
playing = True
player1 = Player(50, 100, "platform.png", (80,300), 10)
player2 = Player(850, 100, "platform.png", (80,300), 10)

mixer.init()
lose_sound = mixer.Sound("losing_sound.ogg")
font.init()
font1 = font.SysFont(None, 60)
lose1 = font1.render("Player 1 lose", True, (100,0,0))
lose2 = font1.render("Player 2 lose", True, (100,0,0))
finish = False
while playing:
    for ev in event.get():
        if ev.type == QUIT:
            playing = False
    if not finish:
        window.blit(bg,(0,0))
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (300,200))
            lose_sound.play()
        if ball.rect.x > 950:
            finish = True
            window.blit(lose2, (300,200))
            lose_sound.play()
        if ball.rect.y < 0 or ball.rect.y > height-80:
            ball.speed_y *= -1
        if sprite.collide_rect(ball, player1) or sprite.collide_rect(ball, player2):
            ball.speed *= -1
            ball.speed_y *= 1
        player1.draw_sprite()
        player2.draw_sprite()
        ball.draw_sprite()
        player1.update1()
        player2.update2()
        ball.update()
        if ball.speed < 0:
            ball.speed -= 0.01
        else:
            ball.speed += 0.01
        display.update()
