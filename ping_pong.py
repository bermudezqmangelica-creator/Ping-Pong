from pygame import *
from random import *

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

        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[K_s] and self.rect.y < 370:
            self.rect.y += self.speed

    def update_R(self):
        keys = key.get_pressed()

        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[K_DOWN] and self.rect.y < 370:
            self.rect.y += self.speed



player1 = Player('racket.png',10,200,40,150,10)
player2 = Player('racket.png',650,200,40,150,10)
ball = Player('ball.png',300,100,70,70,10)

window = display.set_mode((700,500))
display.set_caption('Ping-Pong')
window.fill((95, 172, 191))

game = True
finish = False
clock = time.Clock()

speed_x = 3
speed_y = 3

font.init()
font = font.Font(None, 50)
perdiste1 = font.render('Jugador 1 perdio',True,(0,0,0))
perdiste2 = font.render('Jugador 2 perdio',True,(0,0,0))


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.fill((95, 172, 191))
        #movimiento de plataforma
        player2.update_R()
        player1.update_L()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        ball.reset()
        player1.reset()
        player2.reset()

        if sprite.collide_rect(player1,ball) or sprite.collide_rect(player2,ball):
            speed_x *= -1
            speed_y *= -1

        if ball.rect.y > 450 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            window.blit(perdiste1,(200,200))
            finish = True

        if ball.rect.x > 700:
            window.blit(perdiste2,(200,200))
            finish = True


    display.update()
    clock.tick(60)
        
