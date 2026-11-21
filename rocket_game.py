import pygame
pygame.init()
#create screen
screen = pygame.display.set_mode((800,500))
pygame.display.set_caption("My First Game")
#Load_image
Background = pygame.image.load("sp.jpg")
Player = pygame.image.load("rocket 1.png")
Enemy = pygame.image.load("alien.jpg")
Bullet = pygame.image.load("OIP.webp")
#resize images
Background = pygame.transform.scale(Background,(800,500))
Player = pygame.transform.scale(Player,(150,100))
Enemy = pygame.transform.scale(Enemy,(70,70))
Bullet = pygame.transform.scale(Bullet,(30,50))
#player position
x=340
y=390
player_speed=5
#bullet position
bx=0
by=0
bullet_speed=4
#enemy position
ex=100
ey=50
enemy_speed=1
shoot = False
#score
score=0
font=pygame.font.Font(None,40)
running=True
clock=pygame.time.Clock()
while running:
    screen.blit(Background,(0,0))
    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not shoot:
                bx=x+48
                by = y
                shoot = True
    #move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x-=player_speed
    if keys[pygame.K_LEFT] and x < 680:
        x+=player_speed
    #move enemy slowly
    ex += enemy_speed
    if ex >912:
         ex = 0
    #move bullet
    if shoot:
        by -= bullet_speed
        #check collision
        player_bullet = pygame.Rect(bx,by,24,40)
        enemy_rect = pygame.Rect(int(ex),ey,70,70)
        if player_bullet.colliderect(enemy_rect):
             score += 1
             #reset enemy position
             ex=100
             ey=50
             shoot=False
        #reset bullets when it leaves screen
        if by < 0:
             shoot = False
    #display player
        screen.blit(Player, (x, y))

    # Display enemy
    screen.blit(Enemy, (int(ex), ey))

    # Display bullet
    if shoot:
        screen.blit(Bullet, (bx, by))

    # Display score
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.update()

    clock.tick(60)

pygame.quit()