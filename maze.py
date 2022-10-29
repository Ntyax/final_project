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
        super().__init__("hero.png", 200, 200, 60, 60)
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


class Wall(GameSprite):
    def __init__(self, x, y, width=40, height=40, color = (255, 113, 31)):
        super().__init__("wall.png", x, y, width, height)



class Treasure(GameSprite):
    def __init__(self, x, y):
        super().__init__("treasure.png", x, y, 50, 50)



bg = transform.scale(image.load("ground.png"), (WIDTH, HEIGHT))

player = Player()
cyborg = Enemy(350, 300)



level1 = [
    "WWWWWWWWWWWWWWWWWWWWWWWW",
    "W     W               W",
    "W            WWWWWW   W",
    "W   WWWW          W   W",
    "W   W          WWWW   W",
    "WWWWW  WWWW           W",
    "W T W     W W         W",
    "W   W     W   WWW WW  W",
    "W   WWW WWW   W W     W",
    "W     W   W   W W     W",
    "WWW   W   WWWWW W     W",
    "W W      WW           W",
    "W                 WWWWW",
    "W                 W   W",
    "WWWWWWWWWWWWWWWWWWWWWWW",
]

level2 = [
    "WWWWWWWWWWWWWWWWWWWWWWWW",
    "W  WWW   WW     WWWWWWWW",
    "W        WW     W      W",
    "W        W      WWWW   W",
    "W                      W",
    "WWWWWWWWWWWW     WWW   W",
    "W         WW        WWWW",
    "W   WWWWWWWWWWWWW      W",
    "W               W      W",
    "W    WWWWWWW    W   WWWW",
    "W      W               W",
    "W  WWWWWWWWWWWWWWWWWWWWW",
    "W    WWWW     W   W    W",
    "W                    T W",
    "WWWWWWWWWWWWWWWWWWWWWWWW",
]

level3 = [    
    "WWWWWWWWWWWWWWWWWWWWWWWW",
    "W                   WWWW",
    "WW WWWWW       W      WW",
    "WWW     WWW    W       W",
    "WWWWWWWWWWWWWWWWWW    WW",
    "WWWWWWW      WWWWW     W",
    "WWW              W     W",
    "W                W   WWW",
    "W   WWWWWWWWWWW        W",
    "W   WWW       WWWWWWWWWW",
    "W   W            WW    W",
    "W                      W",
    "WWWWWWWWWWWWWWWWWWWW   W",
    "W T                    W",
    "WWWWWWWWWWWWWWWWWWWWWWWW",]

level4 = [
    "WWWWWWWWWWWWWWWWWWWWWWWW",
    "W       WWWWW     WWW  W",
    "WWWW           WWW     W",
    "WWWWWWWWWWWW           W",
    "WWW  W      WWWWW   WWWW",
    "WW                     W",
    "WW   WW                W",
    "W      WWWWWWWWWWWWWWWWW",
    "W       W          WWWWW",
    "W                      W",
    "WW    W                W",
    "WWWWWWWWWWWWWWWWWWWW   W",
    "W   W      W     W     W",
    "WT     WW     W        W",
    "WWWWWWWWWWWWWWWWWWWWWWWW",
]
 
# Parse the level string above. W = wall, E = exit
x = y = 0
walls = sprite.Group()
treasure = Treasure(0, 0)

for row in level1:
    for col in row:
        if col == "W":           
            walls.add(Wall(x, y))
        if col == "T":
            treasure.rect.x = x
            treasure.rect.y = y
        x += 40
    y += 40
    x = 0



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