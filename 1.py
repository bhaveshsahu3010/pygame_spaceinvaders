import pygame as py
import random
from pygame import mixer
import math
# from io import BytesIO
# import requests
# from PIL import Image

# rsp = requests.get('https://situla.bitbit.net/filebin/77c90e5d7d436c2b016745c88671dc08692c83e12de6a6bff715f8d55aea85fd/d29af785c79a16e419e33d703b2a8ac7711fb3fc36c537e4f4510844188797e9?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=HZXB1J7T0UN34UN512IW%2F20230727%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230727T055927Z&X-Amz-Expires=30&X-Amz-SignedHeaders=host&response-cache-control=max-age%3D30&response-content-disposition=filename%3D%22ufo.png%22&response-content-type=image%2Fpng&X-Amz-Signature=c43018a9bc2edec56084fda37f12a6762b8f99c52c00ee7093be1ee3e4b156c1')
# pilimage = Image.open(BytesIO(rsp.content)).convert("RGBA")
# pgimg = py.image.fromstring(pilimage.tobytes(), pilimage.size, pilimage.mode)

py.init()

screen = py.display.set_mode((1300,700))

py.display.set_caption("Space Invaders")
icon = py.image.load('spaceship.png')
py.display.set_icon(icon)

mixer.music.load("background.wav")
mixer.music.play(-1)

playerimg = py.image.load("spaceship.png")
cx = 625
cy = 550
x1 = 0;

ufoimg = []
ex = []
ey = []
x2 = []
y2 = []
n = 6
for i in range(n):
    ufoimg.append(py.image.load("ufo.png"))
    # ufoimg.append(py.image.load(pgimg))
    ex.append(random.randint(0,1236))
    ey.append(random.randint(10,300))
    x2.append(5)
    y2.append(40)

bulletimg = py.image.load("bullet.png")
bx = cx+16
by = 540
# x3 = 4
y3 = 10
bullet_state = "ready"

background = py.image.load("background.png")

def player(x,y):
    screen.blit(playerimg, (x,y))

def ufo(x,y,i):
    screen.blit(ufoimg[i], (x,y))

def bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg,(x+16,y+10))
 
def iscollision(ex,ey,bx,by):
    if math.sqrt((ex-bx)**2 + (ey-by)**2) <= 30:
        return True
    return False
 
score_val = 0
font = py.font.Font("Joynoted Demo.ttf",32)
sx=10
sy=10

highscore_val = 0
highscore_font = py.font.Font("Joynoted Demo.ttf",32)


over_font = py.font.Font("Joynoted Demo.ttf",64)
restart_font = py.font.Font("Joynoted Demo.ttf",32)

def show_score(x,y):
    score = font.render("Score : " + str(score_val), True, (255,255,0))
    highscore = highscore_font.render("High Score : " + str(highscore_val), True, (255,255,0))
    screen.blit(score,(x,y))
    screen.blit(highscore,(x,y+32))

def game_over():
    over_text = over_font.render("GAME OVER", True, (255,255,0))
    screen.blit(over_text,(500,300))
    restart()

def restart():
    restart_text = restart_font.render("Press R to Restart", True, (255,255,0))
    screen.blit(restart_text, (1050,650))

running  = True
flag = 0
while running :
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    if score_val>=highscore_val:
        highscore_val = score_val
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        if event.type == py.KEYDOWN:
            if event.key == py.K_LEFT:
                x1=-5
            if event.key == py.K_a:
                x1=-5
            if event.key == py.K_RIGHT:
                x1=5
            if event.key == py.K_d:
                x1=5
            if event.key == py.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound("gunshot.wav")
                    bullet_sound.play()
                    bx = cx
                    bullet(bx,by)
            if event.key == py.K_r:
                score_val = 0
                for i in range(n):
                    ex[i] = random.randint(0,1236)
                    ey[i] = random.randint(10,300)
                
            # if event.key == py.K_UP::
            #     y1=-0.5
            # if event.key == py.K_DOWN:
            #     y1=0.5
        if event.type == py.KEYUP:
            if event.key == py.K_RIGHT or py.K_LEFT:
                x1=0
                # y1=0
    # x+=0.25
    # y-=0.25 
    cx+=x1
    # py+=y1
    
    if cx <= 0:
        cx=0
    if cx >= 1236:
        cx=1236
    for i in range(n):
        if ey[i] >= 486:
            for j in range(n):
                ey[j]=2000
            game_over()
            break
        ex[i]+=x2[i]
        if ex[i] <= 0:
            x2[i]=5
            ey[i]+=y2[i]
        if ex[i] >= 1236:
            x2[i]=-5
            ey[i]+=y2[i]
        collision = iscollision(ex[i],ey[i],bx,by)
        if collision:
            collision_sound = mixer.Sound("explosion.wav")
            collision_sound.play()
            by = 540
            bullet_state = "ready"
            score_val+=1
            ex[i] = random.randint(0,1236)
            ey[i] = random.randint(10,300)
        ufo(ex[i],ey[i],i)
    
    if by<=0:
        bullet_state = "ready"
        by = 540

    if bullet_state == "fire":
        bullet(bx,by);
        by-=y3
    # if score_val%10==0 and score_val!=0:      ise bhi dekhna h
    #     for i in range(n):
    #         x2[i]+=1;
        
    # if y <= 0:
    #     y=0
    # if y>=636:
    #     y=636
    
    show_score(sx,sy)
    player(cx,cy)
    py.display.update()