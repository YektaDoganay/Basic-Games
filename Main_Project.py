import pygame
from sys import exit
from random import randint

#Functions
def display_time():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_font = pygame.font.Font("font/Pixeltype.ttf",30)
    score_surface = score_font.render(f"Score: {current_time}",False,"#363636")
    score_rect = score_surface.get_rect(topleft = (650,50))
    screen.blit(score_surface,score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rects in obstacle_list:
            obstacle_rects.left -= 5

            if obstacle_rects.y == 265:
                screen.blit(snail_surface,obstacle_rects)
            else:
                screen.blit(fly_surface,obstacle_rects)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.left > -50]
        
        return obstacle_list
    else:
        return []
def obstacle_movement2(obstacle_list):
    if obstacle_list:
        for obstacle_rects in obstacle_list:
            obstacle_rects.left -= 1

            if obstacle_rects.y == 265:
                screen.blit(snail_surface,obstacle_rects)
            else:
                screen.blit(fly_surface,obstacle_rects)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.left > -50]
        
        return obstacle_list
    else:
        return []
def obstacle_movement3(obstacle_list):
    if obstacle_list:
        for obstacle_rects in obstacle_list:
            obstacle_rects.left -= 2

            if obstacle_rects.y == 265:
                screen.blit(snail_surface,obstacle_rects)
            else:
                screen.blit(fly_surface,obstacle_rects)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.left > -50]
        
        return obstacle_list
    else:
        return []

def collisions(player,obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                died_sound.play()
                return True
            else:
                return False

def player_animation():
    global player_surface, player_index

    if player_rectangle.bottom < 216:
        player_surface = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk): 
            player_index = 0
        player_surface = player_walk[int(player_index)]


pygame.init()

#Musics
jump_sound = pygame.mixer.Sound("audio/jump.mp3")
jump_sound.set_volume(0.05)

theme_sound = pygame.mixer.Sound("audio/Light Ambience 3.mp3")
theme_sound.set_volume(0)

died_sound = pygame.mixer.Sound("audio/died.mp3")
died_sound.set_volume(0.1)

#Begin
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Jumper Alien")
pygame.display.set_icon(pygame.image.load("yekta.jpg"))
clock = pygame.time.Clock()
theme_sound.play(loops = -1)

#score_font = pygame.font.Font("font/Pixeltype.ttf",30)
#score_surface = score_font.render("Score:",False,"#363636")
#score_rect = score_surface.get_rect(topleft = (650,50))

#Name of Game
gameName_font = pygame.font.Font("font/Pixeltype.ttf",50)
gameName_surface = gameName_font.render("Jumper Alien",False,"#FFF5EE")
gameName_rect = gameName_surface.get_rect(center = (400,30))

#Environment Surfaces
sky_surface = pygame.image.load("graphics/Sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()

#Obstacles
snail_frame1 = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_frame2 = pygame.image.load("graphics/snail/snail2.png").convert_alpha()
snail_frames = [snail_frame1, snail_frame2]
snail_frame_index = 0
snail_surface = snail_frames[snail_frame_index]

fly_frame1 = pygame.image.load("graphics/fly/fly1.png").convert_alpha()
fly_frame2 = pygame.image.load("graphics/fly/fly2.png").convert_alpha()
fly_frames = [fly_frame1, fly_frame2]
fly_frame_index = 0
fly_surface = fly_frames[fly_frame_index]


obstacle_rect_list = []

#Player
player_walk1 = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
player_walk2 = pygame.image.load("graphics/Player/player_walk_2.png").convert_alpha()
player_walk = [player_walk1,player_walk2]
player_index = 0

player_jump = pygame.image.load("graphics/Player/jump.png").convert_alpha()

player_surface = player_walk[player_index]
player_rectangle = player_surface.get_rect(topleft = (20,216))
player_gravity = 0

#Died Player
player_stand = pygame.image.load("graphics/Player/Player_stand.png").convert_alpha()
player_stand = pygame.transform.scale(player_stand,(125,150))
player_stand_rect = player_stand.get_rect(center = (400,170))

#Died Name of Game
gameName_font1 = pygame.font.Font("font/Pixeltype.ttf",60)
gameName_surface1 = gameName_font1.render("Jumper Alien",False,"#FFF5EE")
gameName_rect1 = gameName_surface1.get_rect(center = (400,50))

#Died Press SPACE
space_font = pygame.font.Font("font/Pixeltype.ttf",52)
space_surf = space_font.render("Press SPACE to Begin Game!",False,"#FFF5EE")
space_rect = space_surf.get_rect(center = (400,320))

#Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer,500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer,150)

score_list = []

game_over = False

start_time = 0

while True:

    #Events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        #if event.type == pygame.MOUSEMOTION:
            #if player_rectangle.collidepoint(event.pos):
                #print("collision")

        if not game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and 290 <= player_rectangle.bottom <= 300:                                           
                    player_gravity = -20
                    jump_sound.play()
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_over = False                
                start_time = int(pygame.time.get_ticks() / 1000)
        
        if not game_over:
            if event.type == obstacle_timer:
                if randint(0,2):
                    obstacle_rect_list.append(snail_surface.get_rect(topleft = (randint(800,1000),265)))
                else:
                    obstacle_rect_list.append(fly_surface.get_rect(topleft = (randint(800,1000),150)))

            if event.type == snail_animation_timer:
               if snail_frame_index == 0: 
                   snail_frame_index = 1
               else:
                   snail_frame_index = 0
               snail_surface = snail_frames[snail_frame_index]

            if event.type == fly_animation_timer:
                if fly_frame_index == 0:
                    fly_frame_index = 1
                else:
                    fly_frame_index = 0
                fly_surface = fly_frames[snail_frame_index]

                
                   
                
        #if event.type == pygame.KEYUP:
            #print("key up")
       

    #Action Game
    if not game_over:
        #snail_rectangle.left -= 5
        #if snail_rectangle.right < 0:
            #snail_rectangle.left = 800
        #screen.blit(snail_surface,snail_rectangle)
    
        
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        #screen.blit(score_surface,score_rect)
        score = display_time()
        
        
        
        #Player Jump
        player_gravity += 1
        player_rectangle.y += player_gravity
        if player_rectangle.bottom >= 300:
            player_rectangle.bottom = 300
        player_animation()
        screen.blit(player_surface,player_rectangle)

        #Obstacles Movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        if 25 <= score <= 50:
            obstacle_rect_list = obstacle_movement2(obstacle_rect_list)
        elif score > 50:
            obstacle_rect_list = obstacle_movement3(obstacle_rect_list)


        pygame.draw.rect(screen,"#32CD32",gameName_rect,0,6)
        screen.blit(gameName_surface,gameName_rect)

        #if snail_rectangle.colliderect(player_rectangle):
            #game_over = True
        game_over = collisions(player_rectangle,obstacle_rect_list)

    #Died Game
    else:
        screen.fill((95,130,160))
        screen.blit(player_stand,player_stand_rect)
        screen.blit(gameName_surface1,gameName_rect1)
        screen.blit(space_surf,space_rect)
        obstacle_rect_list.clear()
        player_rectangle.topleft = (20,216)
        player_gravity = 0

        #Died High Score
        score_list.append(score)
        score_list.sort(reverse = True)

        high_score = pygame.font.Font("font/Pixeltype.ttf",25)
        high_score_surf = high_score.render(F"HIGH SCORE : {score_list[0]}",False,"#FF4500")
        high_score_rect = high_score_surf.get_rect(center = (715,30)) 
        screen.blit(high_score_surf,high_score_rect)
       

        score_font = pygame.font.Font("font/Pixeltype.ttf",35)
        score_massage = score_font.render(f"Your Score :  {score}",False,30)
        score_rect = score_massage.get_rect(center = (400,360))
        screen.blit(score_massage,score_rect)
    
        #keys = pygame.key.get_pressed()
        #if keys[pygame.K_SPACE]:
            #print("jump")

        #if player_rectangle.colliderect(snail_rectangle):
            #print("collidence")

        #mouse_position = pygame.mouse.get_pos()
        #if player_rectangle.collidepoint(mouse_position):
            #print(pygame.mouse.get_pressed())
    

    pygame.display.update()
    clock.tick(60)
