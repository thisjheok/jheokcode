import pygame
import random
###################################################################################
# 기본 초기화 (반드시 해야함)
pygame.init() #초기화 반드시 필요

#화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("avoidYellow") #게임 이름

#FPS
clock = pygame.time.Clock()
###################################################################################

# 1. 사용자 게임 초기화(배경화면, 게임 이미지, 좌표, 속도, 폰트 등)

#배경 이미지 불러오기
background = pygame.image.load("C:/Users/재혁/Desktop/python workspace/pygame_basic/backgroundd.png")

#스프라이트 불러오기
character = pygame.image.load("C:/Users/재혁/Desktop/python workspace/pygame_basic/character.png")
character_size = character.get_rect().size #이미지 크기 구해오기
character_width = character_size[0] #캐릭터의 가로 크기
character_height = character_size[1] #캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2) #화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
character_y_pos = screen_height - character_height #화면 세로 크기 가장 아래에 해당하는 곳에 위치(세로)

enemy = pygame.image.load("C:/Users/재혁/Desktop/python workspace/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size #이미지 크기 구해오기
enemy_width = enemy_size[0] #캐릭터의 가로 크기
enemy_height = enemy_size[1] #캐릭터의 세로 크기
enemy_x_pos = random.randint(0,480)
enemy_y_pos = 70

count = 0 

# 폰트 정의
game_font = pygame.font.Font(None, 40) #폰트 객체 생성 (폰트, 크기)

running = True 
while running:
    dt = clock.tick(30) 

    # 2. 이벤트 처리
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 
    # 3. 게임 캐릭터 위치 정의

    #이동할 좌표
    to_x=0
    to_y=0

    drop_y=0

    #이동 속도 
    characater_speed = 0.6
    enemy_speed = 0.7
    drop_y -= enemy_speed
    if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: #캐릭터를 왼쪽으로 
                to_x -= characater_speed
            elif event.key == pygame.K_RIGHT: #캐릭터를 오른쪽
                to_x += characater_speed

    if event.type == pygame.KEYUP: #방향키를 떼면
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    character_x_pos += to_x*dt #프레임에 따라 캐릭터 이동 속도가 달라지지 않게 하기 위해 dt를 곱함
    character_y_pos -= to_y*dt
    enemy_y_pos -= drop_y*dt

    #가로 경계값 처리
    if character_x_pos<0:
        character_x_pos = 0
    elif character_x_pos>screen_width - character_width:
        character_x_pos = screen_width - character_width

    #노랑이 넘어갔다면
    if enemy_y_pos >screen_height:
        enemy_x_pos = random.randint(0,410)
        enemy_y_pos = 70
        count += 1

    # 4. 충돌 처리

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    #충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False


    # 5. 화면에 그리기 

    screen.blit(background, (0,0)) # 배경 그리기
    screen.blit(character,(character_x_pos, character_y_pos)) #캐릭터 그리기
    screen.blit(enemy,(enemy_x_pos, enemy_y_pos))

    counter = game_font.render(str(int(count)),True,(255,255,255))
    #출력할 글자, True, 글자 색상
    screen.blit(counter,(10,10))
    pygame.display.update() # 게임화면 다시 그리기(계속 해서)


#pygame 종료
pygame.quit()
