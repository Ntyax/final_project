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
    def __init__(self, images):
        super().__init__(images["right"], 70, 100, 40, 40)
        self.speed = 3
        self.dir = "R"
        self.hp = 100
        self.images = {}
        for direction in images:
            self.images[direction] = transform.scale(image.load(images[direction]), (40,40))
        self.image = self.images["right"]


    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x>0:
            self.dir = "L"
            self.image = self.images["left"]
        elif keys[K_RIGHT] and self.rect.x<WIDTH-self.width:
            self.dir = "R"
            self.image = self.images["right"]
        elif keys[K_UP] and self.rect.y>0:
            self.dir = "U"
            self.image = self.images["up"]
        elif keys[K_DOWN] and self.rect.y<HEIGHT-self.height:
            self.dir = "D"
            self.image = self.images["down"]

        else:
            self.dir = "STOP"

        if self.dir == "L":
            self.rect.x -= self.speed
        elif self.dir == "R":
            self.rect.x += self.speed
        elif self.dir == "U":
            self.rect.y -= self.speed
        elif self.dir == "D":
            self.rect.y += self.speed   

        collide_list = sprite.spritecollide(self, walls, False)
        for wall in collide_list:
            if self.dir == "U":
                self.rect.y = wall.rect.bottom
                self.dir = "STOP"
            elif self.dir == "R":
                self.rect.right = wall.rect.left
                self.dir = "STOP" 
            elif self.dir  == "D":
                self.rect.bottom = wall.rect.top
                self.dir = "STOP"
            elif self.dir == "L":
                self.rect.left = wall.rect.right
                self.dir = "STOP"  



class Enemy(GameSprite):
    def __init__(self, images, x, y, level = 1):
        self.dirs = list(images.keys())
        super().__init__(images[self.dirs[0]], x, y, 40, 40)
        self.speed = 3
        self.level = level
        self.direction = self.dirs[0]
        self.images = {}
        for direction in images:
            self.images[direction] = transform.scale(image.load(images[direction]), (40,40))


    def update(self):
        if self.level == 1:
            if self.rect.x >= 350:
                self.direction = "left"
                self.image = self.images["left"]
            elif self.rect.x < 105:
                self.direction = "right"
                self.image = self.images["right"]

        if self.level == 2:
            if self.rect.y >= 400:
                self.direction = "up"
            elif self.rect.y < 100:
                self.direction = "down"

        if self.level == 3:
            if self.rect.y >= 440:
                self.direction = "up"
            elif self.rect.y < 200:
                self.direction = "down"

        if self.level == 4:
            if self.rect.y >= 390:
                self.direction = "up"
            elif self.rect.y < 170:
                self.direction = "down"


        
        if self.direction == "left":
            self.rect.x -= self.speed
        elif self.direction == "right":
            self.rect.x += self.speed
        if self.direction == "up":
            self.rect.y -= self.speed
        elif self.direction == "down":
            self.rect.y += self.speed 



class Wall(GameSprite):
    def __init__(self, image,  x, y, width=40, height=40, color = (255, 113, 31)):
        super().__init__(image, x, y, width, height)



class Treasure(GameSprite):
    def __init__(self, image, x, y):
        super().__init__(image, x, y, 40, 40)



bg = transform.scale(image.load("ground.png"), (WIDTH, HEIGHT))

dirplayer1 = {"right": "player1 right.png",
                "left": "player1 left.png",
                "up": "player1 up.png",
                "down": "player1.png"}

dirplayer2 = {"right": "player2 right.png",
                "left": "player2 left.png",
                "up": "player2 up.png",
                "down": "player2.png"}

dirplayer3 = {"right": "player3 right.png",
                "left": "player3 left.png",
                "up": "player3 up.png",
                "down": "player3.png"}

dirplayer4 = {"right": "player4 right.png",
                "left": "player4 left.png",
                "up": "player4 up.png",
                "down": "player4.png"}



direnemy1 = {"right": "enemy1 right.png",
                "left": "enemy1 left.png",
                "up": "enemy 1 up.png",
                "down": "enemy1.png"}

direnemy2 = {"right": "enemy2 right.png",
                "left": "enemy2 left.png",
                "up": "enemy2 up.png",
                "down": "enemy2.png"}

direnemy3 = {"right": "enemy3 right.png",
                "left": "enemy3 left.png",
                "up": "enemy3 up.png",
                "down": "enemy3.png"}

direnemy4 = {"right": "enemy4 right.png",
                "left": "enemy4 left.png",
                "up": "enemy4 up.png",
                "down": "enemy4.png"}


def new_game(lvl_map, new_player, new_enemy, new_treasure, wall_img, bg_image):   
    global player, enemy, bg, treasure
    bg = transform.scale(image.load(bg_image), (WIDTH, HEIGHT))
    player = new_player
    enemy = new_enemy
    treasure = new_treasure
    x = y = 0
    for row in lvl_map:
        for col in row:
            if col == "W":           
                walls.add(Wall(wall_img, x, y))
            if col == "T":
                treasure.rect.x = x
                treasure.rect.y = y
            x += 40
        y += 40
        x = 0

def start_level1():
    global run
    run = True
    enemy1 = Enemy(direnemy1, 121, 401, 1)
    player1 = Player(dirplayer1)
    treasure1 = Treasure("treasure.png", 0, 0)
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

    new_game(level1, player1, enemy1, treasure1, "wall.png", "floor.jpg")
    menu.disable()


def start_level2():
    global run
    run = True
    enemy2 = Enemy(direnemy2, 470, 400, 2)
    player2 = Player(dirplayer2)
    treasure2 = Treasure("treasure2.png", 0, 0)
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

    new_game(level2, player2, enemy2, treasure2, "wall2.png", "floor2.jpg")
    menu.disable()

def start_level3():
    global run
    run = True
    enemy3 = Enemy(direnemy3, 350, 440, 3)
    player3 = Player(dirplayer3)
    treasure3 = Treasure("treasure3.png", 0, 0)
    level3 = [    
        "WWWWWWWWWWWWWWWWWWWWWWWW",
        "W                   WWWW",
        "W    WWW       W      WW",
        "W       WWW    W       W",
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
        "WWWWWWWWWWWWWWWWWWWWWWWW",
    ]

    new_game(level3, player3, enemy3, treasure3, "wall3.png", "floor3.jpg")
    menu.disable()

def start_level4():
    global run
    run = True
    enemy4 = Enemy(direnemy4, 160, 390, 4)
    player4 = Player(dirplayer4)
    treasure4 = Treasure("treasure4.png", 0, 0)
    level4 = [
        "WWWWWWWWWWWWWWWWWWWWWWWW",
        "W       WWWWW     WWW  W",
        "W              WWW     W",
        "W  WWWWWWWWW           W",
        "WWW  W      WWWWW   WWWW",
        "W                      W",
        "W    WW                W",
        "W      WWWWWWWWWWWWWWWWW",
        "W       W          WWWWW",
        "W                      W",
        "WW    W                W",
        "WWWWWWWWWWWWWWWWWWWW   W",
        "W   W      W     W     W",
        "WT     WW     W        W",
        "WWWWWWWWWWWWWWWWWWWWWWWW",
    ]

    new_game(level4, player4, enemy4, treasure4, "wall4.png", "floor4.jpg")
    menu.disable()

 
# Parse the level string above. W = wall, E = exit

walls = sprite.Group()
treasure = Treasure('treasure.png', 0, 0)



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





menu = pygame_menu.Menu("Maze", 400, 300, theme = pygame_menu.themes.THEME_BLUE)
menu.add.button("Level 1", start_level1)
menu.add.button("Level 2", start_level2)
menu.add.button("Level 3", start_level3)
menu.add.button("Level 4", start_level4)
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
        enemy.update()


        if sprite.collide_rect(player, treasure):
            result = font1.render("YOU WIN", True, (0, 255, 0))
            finish = True
            win_sound.play()
        if sprite.collide_rect(player, enemy):
            result = font1.render("YOU LOSE", True, (255, 0, 0))
            finish = True


        window.blit(bg, (0,0))
        player.draw()
        enemy.draw()
        walls.draw(window)
        treasure.draw()
    else:
        window.blit(result, (300, 300))
    display.update()
    clock.tick(FPS)



#оброби подію «клік за кнопкою "Закрити вікно"»
