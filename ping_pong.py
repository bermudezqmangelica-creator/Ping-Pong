from pygame import *

# clase padre para otros objetos
class GameSprite(sprite.Sprite):
    # constructor de clase
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # llamamos al constructor de la clase (Sprite):
        sprite.Sprite.__init__(self)

        # cada objeto debe almacenar una propiedad image
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        # cada objeto debe almacenar la propiedad rect en la cual está inscrito
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    # método que dibuja al personaje en la ventana
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_L(self):
        keys = key.get_pressed()

        if keys[K_W] and self.rect.x > 5:
            self.rect.x -= self.speed

        if keys[K_S] and self.rect.x < 620:
            self.rect.x += self.speed

    def update_R(self):
        keys = key.get_pressed()

        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed

        if keys[K_RIGHT] and self.rect.x < 620:
            self.rect.x += self.speed

class Enemy(GameSprite):
    def update(self):
        global fallos
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.x = randint(100,600)
            self.rect.y = 0
            fallos += 1

player1 = Player('racket.png',300,400,70,100,10)
player2 = Player('racket.png',300,400,70,100,10)
ball = Enemy('ball.png',300,400,70,100,10)

window = display.set_mode((700,500))
display.set_caption('Ping-Pong')
window.fill((95, 172, 191))

game = True
clock = time.Clock()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(60)
        
