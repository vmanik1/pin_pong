from pygem import *
'''Необхідні класи'''

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, haight))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys [K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

back = (200, 255, 255)
win_width = 600 
win_haight = 500
window = display.set_mode((win_width, win_haight))
window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60 

racket1 = Player('img.png', 30, 200, 4, 50, 150)
racket2 = Player('img.png', 520, 200, 4, 50, 150)
ball = GameSprite('png', 200, 200, 4, 50, 50)
