import pygame, sys, random
img = pygame.image.load("aitu-logo.png")
pygame.display.set_icon(img)

def ball_animation():
    global ball_speed_x
    global ball_speed_y
    global player1_score
    global player2_score
    global score_time

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        pygame.mixer.Sound.play(pong_sound)
        ball_speed_y *= -1

    if ball.left <= 0:
        pygame.mixer.Sound.play(score_sound)
        player1_score += 1
        score_time = pygame.time.get_ticks()

    if ball.right >= screen_width:
        pygame.mixer.Sound.play(score_sound)
        player2_score +=1
        score_time = pygame.time.get_ticks()

    if ball.colliderect(player1) or ball.colliderect(player2):
        pygame.mixer.Sound.play(pong_sound)
        ball_speed_x *= -1

def player1_animation():
    player1.y += player1_speed
    if player1.top <= 0:
        player1.top = 0
    if player1.bottom >= screen_height:
        player1.bottom = screen_height

def player2_animation():
    if player2.top < ball.y:
        player2.top += player2_speed
    if player2.bottom > ball.y:
        player2.bottom -= player2_speed
    if player2.top <= 0:
        player2.top = 0
    if player2.bottom >= screen_height:
        player2.bottom = screen_height

def ball_restart():
    global ball_speed_x
    global ball_speed_y
    global score_time

    current_time = pygame.time.get_ticks()
    ball.center = (screen_width / 2, screen_height / 2)

    if current_time - score_time < 700:
        number_three = game_font.render("3", False, light_grey)
        screen.blit(number_three, (screen_width/2-10, screen_height/2 + 20))

    if 700 < current_time - score_time < 1400:
        number_three = game_font.render("2", False, light_grey)
        screen.blit(number_three, (screen_width/2-10, screen_height/2 + 20))

    if 1400 < current_time - score_time < 2100:
        number_three = game_font.render("1", False, light_grey)
        screen.blit(number_three, (screen_width/2-10, screen_height/2 + 20))

    if current_time - score_time < 2100:
        ball_speed_y, ball_speed_x = 0, 0
    else:
        ball_speed_y = 7 * random.choice((1, -1))
        ball_speed_x = 7 * random.choice((1, -1))
        score_time = None



#General Setup
pygame.mixer.pre_init(44100,-16,2,1024)
pygame.init()
сlock = pygame.time.Clock()

#Main Window
screen_width = 900
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ping Pong,Artur Kuleken,Zhalgas Kamzabekov,Asanali Tazhigaliev,Amir Shakhaev,CS-2111")

#Game Rectangles
gray=(200, 200, 200)
ball = pygame.draw.circle(screen, gray, (625, 465), radius = 20)
player1 = pygame.Rect(screen_width -20, screen_height/2-70, 10, 140)
player2 = pygame.Rect(10, screen_height/2-70, 10, 140)

#Colors
bg_color = pygame.Color('gray')
light_grey = (200, 200, 200)
bg_color1 = pygame.Color('black')
black = (0, 0, 0)
bg_color2 = pygame.Color('blue')
blue = (0, 191, 255)

#Game Variables
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player1_speed = 0
player2_speed = 7

#Text Variables
player1_score=0
player2_score=0
game_font = pygame.font.Font("freesansbold.ttf",40)

#Score Timer
score_time = True

#Sound
pong_sound = pygame.mixer.Sound("pong.ogg")
score_sound = pygame.mixer.Sound("score.ogg")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player1_speed += 7
            if event.key == pygame.K_UP:
                player1_speed -=7

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player1_speed -= 7
            if event.key == pygame.K_UP:
                player1_speed +=7

#Game Logic
    ball_animation()
    player1_animation()
    player2_animation()

#Visuals
    screen.fill(bg_color1)
    pygame.draw.rect(screen, light_grey, player1)
    pygame.draw.rect(screen, light_grey, player2)
    pygame.draw.rect(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0), (screen_width / 2, screen_height))

    if score_time:
        ball_restart()

    player1_text = game_font.render(f"{player1_score}", False, light_grey)
    screen.blit(player1_text, (700,470))
    player2_text = game_font.render(f"{player2_score}", False, light_grey)
    screen.blit(player2_text, (200, 470))

    pygame.display.flip()
    сlock.tick(60)

