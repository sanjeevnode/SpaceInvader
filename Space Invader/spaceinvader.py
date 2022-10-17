import pygame
import random,math
from pygame import mixer

# Initilizaion
pygame.init()
S_HEIGHT=600
S_WIDTH=700
screen = pygame.display.set_mode((S_WIDTH,S_HEIGHT))
# Title and icon 
pygame.display.set_caption("Space Invader")
icon = pygame.image.load("cd.png")
pygame.display.set_icon(icon)

# Background
bg = pygame.image.load("bg.jpg")

mixer.music.load("background.mp3")
mixer.music.play(-1)


# Player image 
playerImg = pygame.image.load("spaceship.png")
playerX=330
playerY=500
playerX_change=0
p_speed=2.5
def player(x,y):
    screen.blit(playerImg,(x,y))

#  Enemy image
enemyImg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]

num_enemy = 6

for i in range(num_enemy):
    enemyImg.append(pygame.image.load("alien.png"))
    enemyX.append(random.randint(2,666))
    enemyY.append(random.randint(50,120))
    enemyX_change.append(0.6)
    enemyY_change.append(50)

def enemy(x,y,i):
    screen.blit(enemyImg[1],(x,y))

# Bullet
bulletImg = pygame.image.load("bullet.png")
bulletX =0
bulletY = 500
bulletY_change=3
bullet_state="ready"

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x+8,y+5))

def isCollision(eX,eY,bX,bY):
    d = math.sqrt((eX-bX)**2 + (eY-bY)**2)
    return True if d< 14 else False

# score
score_value=0
font = pygame.font.Font('freesansbold.ttf',35)
textX= 10
textY=10

abtfont = pygame.font.Font('freesansbold.ttf',10)

def show_score(x,y):
    score = font.render("Score: "+str(score_value),True,(255,255,0))
    screen.blit(score,(x,y))
    name= abtfont.render("by Sanjeev kumar Singh",True,(255,255,255))
    screen.blit(name,(2,570))


# Game over Text
gameover_font = pygame.font.Font('freesansbold.ttf',60)

def game_over_text() :
    over_text = gameover_font.render("GAME OVER",True,(255,255,0))
    screen.blit(over_text,(200,250))

# Bullet
bulletImg = pygame.image.load("bullet.png")
bulletX =0
bulletY = 500
bulletY_change=3
bullet_state="ready"

# Game Looop
running=True

while running:
    # screen.fill((0,1,2))
    screen.blit(bg,(0,0))
    # Exiting function 
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            running= False
    # movement left right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change =-p_speed
            if event.key == pygame.K_RIGHT:
                playerX_change =p_speed
            
            if event.key == pygame.K_SPACE:
                if bullet_state =="ready":
                    bullet_sound=mixer.Sound("laser.mp3")
                    bullet_sound.play()
                    bulletX=playerX
                    fire_bullet(bulletX,bulletY)
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                playerX_change =0

    # Player movement 
    playerX+=playerX_change
    if playerX < 2 :
        playerX=2
    elif playerX > 666:
        playerX=666
# Enemy movement
    for i in range(num_enemy):
        # Game over
        if enemyY[i] >=490:
            for i in range(num_enemy):
                enemyY[i]=1500
            game_over_text()
            mixer.music.stop()
            break
        enemyX[i]+=enemyX_change[i]
        if enemyX[i] <= 2 :
            enemyX_change[i]=0.5
            enemyY[i]+=enemyY_change[i]
        elif enemyX[i] >= 666:
            enemyX_change[i]=-0.5
            enemyY[i]+=enemyY_change[i]
        
        # Collision
        collision = isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            explosion_sound=mixer.Sound("explosion.wav")
            explosion_sound.play()
            bulletY=500
            bullet_state="ready"
            score_value+=1
            enemyX[i] =random.randint(2,666)
            enemyY[i] = random.randint(50,120)
    
        enemy(enemyX[i],enemyY[i],i)

    # Bullet movement
    if bulletY<2:
        bulletY=500
        bullet_state="ready"
    if bullet_state=="fire":
        fire_bullet(bulletX,bulletY)
        bulletY-=bulletY_change

    
        
    
    player(playerX,playerY)
    show_score(textX,textY)
    pygame.display.update()



# x= 2.4 ,664 
# y =1.8 566,
