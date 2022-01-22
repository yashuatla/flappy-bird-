import pygame
import random
import sys
# Global variables for this game
scwidth = 336
scheight = 570
floor_pos = 0
gravity = 0.5
bird_movement = 0
pipe_pos = 0
pipelis = []
off_set = 100
collision =  False
FPS = 40
score = 0
high_score = 0
i = 0
game_quit = False

# pygame.mixer.pre_init(frequency = 44100, size = 16, channels = 1, buffer = 512)
pygame.init()


def welcome():
    while(True):
        photo = pygame.image.load(r"photos\me 4 (2).png").convert_alpha()
        message = pygame.image.load(r"photos\message.png").convert_alpha()
        message = pygame.transform.scale(message,(scwidth - 120,scheight-250))
        down = pygame.image.load(r"photos\Screenshot (17) (1).png").convert_alpha()
        space = pygame.image.load(r"photos\space1.png").convert_alpha()
        space = pygame.transform.scale(space,(600,180))
        # down = pygame.transform.scale(down,(336,100))
        window.blit(background_day,(0,0))
        window.blit(photo,(110,10))
        window.blit(message,(70,130))
        window.blit(down,(-30,380))
        # window.blit(space,(-100,440))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return
        pygame.display.update()
    return

def gameover_():
    while(True):
        
        gameover = pygame.image.load(r"photos\gameover.png").convert_alpha()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return
        window.blit(background_day,(0,0))
        window.blit(gameover,(75,120))
        window.blit(score1,(125,300))
        window.blit(high_score1,(100,440))
        pygame.display.update() 
        clock.tick(FPS)
    return
    
def pipegen(pipelis):
    pipe = pygame.image.load(r"photos\pipe-red.png").convert_alpha()
    pipe_rect = pipe.get_rect(midtop = (570,random.randrange(240,415)))
    pipe_r = pygame.transform.rotate(pipe,180)
    pipe_r_rect = pipe_r.get_rect(midtop = (570,(pipe_rect.midtop[1] - off_set - pipe.get_height())))
    pipelis.append([pipe_rect,pipe_r_rect])
    return pipelis

def iscollide(pipelis):
    for pipes in pipelis:
        if bird_rect.colliderect(pipes[0]) == True or bird_rect.colliderect(pipes[1]) == True:
            return True
        elif bird_rect.midtop[1] <= 0 or bird_rect.midbottom[1] >= 470:
            return True
        else:
            return False
        

def rotate(bird_movement,bird):
    new_bird = pygame.transform.rotozoom(bird,-bird_movement*2.2,1)
    return new_bird

def play(path):
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()

def animation():
    new_bird = bird_list[i]
    new_bird_rect = bird.get_rect(center = (50,bird_rect.centery))
    return new_bird,new_bird_rect
    
try:
    with open("high.txt","r+") as f:
        high_score = int(f.read())
except:
    with open("high.txt","w") as f:
        f.write("0") 
# STARTING THE MAIN FUNCTION
if __name__ == "__main__":
    while game_quit == False:
        game_done = False
        pipelis = []
        bird_movement = 0
        caption = pygame.display.set_caption("yashu bird")
        window = pygame.display.set_mode((scwidth,scheight))

        # Loading background image 
        background = pygame.image.load(r"photos\background-night.png").convert()
        background = pygame.transform.scale(background,(scwidth,scheight))

        background_day = pygame.image.load(r"photos\background-day.png").convert()
        background_day = pygame.transform.scale(background_day,(scwidth,scheight))

        # Loading bird image
        bird = pygame.image.load(r"photos\bluebird-midflap.png").convert_alpha()
        bird_rect = bird.get_rect(center = (50,335))

        # Loading animation puctures
        bird_up = pygame.image.load(r"photos\bluebird-upflap.png").convert_alpha()
        bird_up_rect = bird_up.get_rect(center = (50,bird_rect.centery))
        
        bird_down = pygame.image.load(r"photos\bluebird-downflap.png").convert_alpha()
        bird_down_rect = bird_down.get_rect(center = (50,bird_rect.centery))

        # Making the three birds as a list
        bird_list = [[bird,bird_rect],[bird_up,bird_up_rect],[bird_down,bird_down_rect]]

        # Loading floor image
        floor = pygame.image.load(r"photos\base.png").convert_alpha()
        # Loading upper floor
        floor_r = pygame.transform.rotate(floor,180)

        # Loading pipe image
        pipe = pygame.image.load(r"photos\pipe-red.png").convert_alpha()
        pipe_rect = pipe.get_rect(midtop = (350,random.randrange(240,415)))
        pipe_rect1 = pipe.get_rect(midtop = (550,random.randrange(240,415)))
        pipe_rect2 = pipe.get_rect(midtop = (750,random.randrange(240,415)))
        # Reverse pipe loading
        pipe_r = pygame.transform.rotate(pipe,180)
        pipe_r_rect = pipe_r.get_rect(midtop = (350,pipe_rect.midtop[1] - off_set - pipe.get_height()))
        pipe_r_rect1 = pipe_r.get_rect(midtop = (550,pipe_rect1.midtop[1]- off_set - pipe.get_height()))
        pipe_r_rect2 = pipe_r.get_rect(midtop = (750,pipe_rect2.midtop[1] - off_set - pipe.get_height()))

        pipelis.append([pipe_rect,pipe_r_rect])
        pipelis.append([pipe_rect1,pipe_r_rect1]) 
        pipelis.append([pipe_rect2,pipe_r_rect2])

        timer = pygame.USEREVENT + 1 
        pygame.time.set_timer(timer,1500)
        welcome()
        gameover = False
        clock = pygame.time.Clock()
        score = 0
        # STARTING THE GAME LOOP
        while not gameover:
            bird,bird_rect = animation()
            bird = bird[0]
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    gameover = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bird_movement = -6.5
                        play(r"sounds\swing.mp3")
                        rotated_bird = rotate(bird_movement,bird)
                elif event.type == timer:
                    score += 1
                    play(r"sounds\point.wav")
            # floor movement    
            if floor_pos <= -scwidth:
                floor_pos = 0
            floor_pos -= 2.5
            #  score printing
            font = pygame.font.SysFont(None,30)
            score1 = font.render(f"Score : {str(int(score-1))}",None,(255,255,255))
            score2 = font.render(f"Score : {str(int(0))}",None,(255,255,255))
            # High score display
            font1 = pygame.font.SysFont(None,30)
            high_score1 = font1.render(f"High Score : {str(int(high_score - 1))}",None,(255,255,255))
            
            # Bird movement
            bird_movement += gravity
            rotated_bird = rotate(bird_movement,bird)
            bird_rect.centery += bird_movement
            # pipe movement
            pipelis[0][0].centerx -= 2.5
            pipelis[0][1].centerx -= 2.5
            pipelis[1][0].centerx -= 2.5
            pipelis[1][1].centerx -= 2.5
            pipelis[2][0].centerx -= 2.5
            pipelis[2][1].centerx -= 2.5
            if pipelis[0][0].centerx <= -30:
                del pipelis[0]
                pipelis = pipegen(pipelis)
            # Check collision for the pipes and the bird
            if iscollide(pipelis) == True:
                gameover = True
                play(r"sounds\out.wav")
            if score >= high_score:
                high_score = score
                
            i+=1
            if i>=3:
                i = 0
            
            # playing the windows on the screen
            window.blit(background,(0,0))
            window.blit(pipe,pipelis[0][0])
            window.blit(pipe_r,pipelis[0][1])
            window.blit(pipe,pipelis[1][0])
            window.blit(pipe_r,pipelis[1][1])
            window.blit(pipe,pipelis[2][0])
            window.blit(pipe_r,pipelis[2][1])
            window.blit(rotated_bird,bird_rect)
            window.blit(floor,(floor_pos,470))
            window.blit(floor,(floor_pos+scwidth,470))  
            if score <= 0:
                window.blit(score2,(30,30))
            else:
                window.blit(score1,(30,30))
            window.blit(high_score1,(180,30))
            pygame.display.update()
            clock.tick(FPS)
        if score >= high_score:
            with open("high.txt","w") as f:
                f.write(str(int(high_score)))
        gameover_()
            


