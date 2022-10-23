#створи гру "Лабіринт"!
from pygame import *
import pygame_menu

mixer.init()
font.init()
init()



WIDTH = 900
HEIGHT = 600
window = display.set_mode((WIDTH, HEIGHT))
display.set_caption("Maze")
font1 = font.SysFont("Impact", 50)
result = font1.render("", True, (0, 255, 0))

class GameSprite(sprite.Sprite):
    def __init__(self, image_name, x, y, width, height):
        super().__init__()
        self.image = transform.scale(image.load(image_name), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height

    def draw(self):
        window.blit(self.image, self.rect)

class Player(GameSprite):
    def __init__(self):
        super().__init__("hero.png", 200, 200, 50, 50)
        self.speed = 5
        self.hp = 100

    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x>0:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x<WIDTH-self.width:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y>0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y<HEIGHT-self.height:
            self.rect.y += self.speed


class Enemy(GameSprite):
    def __init__(self, x, y):
        super().__init__("cyborg.png", x, y, 75, 75)
        self.speed = 5
        self.direction = "left"

    def update(self):
        if self.rect.x <= 300:
            self.direction = "right"
        if self.rect.x >= 450:
            self.direction = "left"
        
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

<<<<<<< HEAD
class Wall(GameSprite):
    def __init__(self, x, y, width=50, height=50, color = (255, 113, 31)):
        super().__init__("wall.png", x, y, width, height)

=======
class Wall(sprite.Sprite):
    def __init__(self, img, x, y, width, height):
        super().__init__()
        self.img = Surface((width, height))
        self.rect = self.img.get_rect()
        self.img_width = 50
        self.img_height = 50
        self.picture = transform.scale(image.load(img), (50, 50))
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height
        


    def draw(self):
        if self.width > self.height:      
            self.img_width = 0     
            while self.width > self.img_width:
                self.img.blit(self.img, (self.img_width, 0))
                self.img_width += 50
        window.blit(self.img, self.rect)
>>>>>>> 4b23f12b1c65419f09de62f50edfaa5a967f17e5


class Treasure(GameSprite):
    def __init__(self, x, y):
        super().__init__("treasure.png", x, y, 75, 75)



bg = transform.scale(image.load("ground.png"), (WIDTH, HEIGHT))

player = Player()
cyborg = Enemy(350, 300)

<<<<<<< HEAD

level = [
    "WWWWWWWWWWWWWWWWWWWW",
    "W                  W",
    "W         WWWWWW   W",
    "W   WWWW       W   W",
    "W   W        WWWW  W",
    "W WWW  WWWW        W",
    "W   W     W W      W",
    "W   W     W   WWW WW",
    "W   WWW WWW   W W  W",
    "W     W   W   W W  W",
    "WWW   W   WWWWW W  W",
    "W W      WW        W",
    "W W   WWWW   WWW   W",
    "W     W    T   W   W",
    "WWWWWWWWWWWWWWWWWWWW",
]
 
# Parse the level string above. W = wall, E = exit
x = y = 0
walls = sprite.Group()
treasure = Treasure(0, 0)

for row in level:
    for col in row:
        if col == "W":           
            walls.add(Wall(x, y))
        if col == "T":
            treasure.rect.x = x
            treasure.rect.y = y
        x += 50
    y += 50
    x = 0
=======
wall1 = Wall("wall.png", 50, 50, 20, 500)
wall2 = Wall("wall.png", 70, 50, 770, 20)
wall3 = Wall("wall.png", 300, 70, 20, 150)
wall4 = Wall("wall.png", 840, 50, 20, 500)
walls = [wall1, wall2, wall3, wall4]
>>>>>>> 4b23f12b1c65419f09de62f50edfaa5a967f17e5


mixer.music.load("jungles.ogg")
mixer.music.set_volume(0.5) #гучність фонової музики
mixer.music.play()

win_sound = mixer.Sound("money.ogg")
kick_sound = mixer.Sound("kick.ogg")

run = False
game = False
clock = time.Clock()
FPS = 60
finish = False

def start_game():
    global run
    run = True
    menu.disable()


menu = pygame_menu.Menu("Maze", 400, 300, theme = pygame_menu.themes.THEME_BLUE)
menu.add.button("Play", start_game)
menu.add.button("Exit", pygame_menu.events.EXIT)
menu.mainloop(window)



while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                menu.enable()
                menu.mainloop(window)

    if not finish:
        player.update()
        cyborg.update()

        if sprite.collide_rect(player, treasure):
            result = font1.render("YOU WIN", True, (0, 255, 0))
            finish = True
            win_sound.play()
        if sprite.collide_rect(player, cyborg):
            result = font1.render("YOU LOSE", True, (255, 0, 0))
            finish = True


        window.blit(bg, (0,0))
        player.draw()
        cyborg.draw()
        walls.draw(window)
        treasure.draw()
    else:
        window.blit(result, (300, 300))
    display.update()
    clock.tick(FPS)



#оброби подію «клік за кнопкою "Закрити вікно"»
