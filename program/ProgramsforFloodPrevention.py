import pygame
import sys
from cmath import rect
import os

# 상대경로 -> 절대경로
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# 시작 화면
pygame.init()
MAX_WIDTH = 1500
MAX_HEIGHT = 900

screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
WHITE = (255,255,255)

# 이미지 선언
current_path = os.path.dirname(__file__)
seoul_map = pygame.image.load(os.path.join(current_path, resource_path("seoul_map.png")))
seoul_2023 = pygame.image.load(os.path.join(current_path, resource_path("2023_seoul.png")))

rain_ydp = pygame.image.load(os.path.join(current_path, resource_path("rain_ydp.png")))
rain_gj = pygame.image.load(os.path.join(current_path, resource_path("rain_gj.png")))

map_ydp = pygame.image.load(os.path.join(current_path, resource_path("map_ydp.png")))
map_gj = pygame.image.load(os.path.join(current_path, resource_path("map_gj.png")))

ydp_m = pygame.image.load(os.path.join(current_path, resource_path("ydp_m.png")))
gj_m = pygame.image.load(os.path.join(current_path, resource_path("gj_m.png")))

ydp_manhole = pygame.image.load(os.path.join(current_path, resource_path("ydp_manhole.png")))
gj_manhole = pygame.image.load(os.path.join(current_path, resource_path("gj_manhole.png")))

ydp_height = pygame.image.load(os.path.join(current_path, resource_path("ydp_height.png")))
gj_height = pygame.image.load(os.path.join(current_path, resource_path("gj_height.png")))

ydp_flooding = pygame.image.load(os.path.join(current_path, "ydp_flooding.png"))
gj_flooding = pygame.image.load(os.path.join(current_path, "gj_flooding.png"))

# 메인
def main(): 
    # 첫 번째 화면 
    running1 = True
    while running1:
        background_x = (MAX_WIDTH - 1098) / 2
        background_y = (MAX_HEIGHT - 900) / 2
        
        screen.fill(WHITE)
        screen.blit(seoul_map, (background_x, background_y))
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # print(pygame.mouse.get_pos())
                pos = pygame.mouse.get_pos() 
                # 좌표 판단
                x = pos[0]
                y = pos[1]
                if (x > 533 and x < 630) and (y > 572 and y < 593):
                    ydp()
                if (x > 1009 and x < 1088) and (y > 492 and y < 518):
                    gj()
        pygame.display.update()

# 영등포구 데이터 시각화
def ydp():
    running2 = True 
    screen_ydp = ydp_flooding
    background_x = (MAX_WIDTH - 1063) / 2
    background_y = (MAX_HEIGHT - 900) / 2
    while running2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
                pos = pygame.mouse.get_pos() 
                # 좌표 판단
                x = pos[0]
                y = pos[1]
                
                # 영등포구 침수흔적도
                if(x > 1460 and x < 1480) and (y > 90 and y < 110):
                    # 영등포구 침수흔적도
                    screen_ydp = ydp_flooding
                    # 이미지 좌표
                    background_x = (MAX_WIDTH - 930) / 2
                    background_y = (MAX_HEIGHT - 900) / 2
                
                # 영등포구 강수량
                if(x > 1460 and x < 1480) and (y > 190 and y < 210):
                    # 영등포구 강수량
                    screen_ydp = rain_ydp
                    # 이미지 좌표
                    background_x = (MAX_WIDTH - 1500) / 2
                    background_y = (MAX_HEIGHT - 806) / 2
                
                # 영등포구 맨홀 & 빗물받이
                if(x > 1460 and x < 1480) and (y > 290 and y < 310):
                    # 영등포구 맨홀 빗물받이 갯수
                    screen_ydp = ydp_manhole
                    # 이미지 좌표
                    background_x = (MAX_WIDTH - 1365) / 2
                    background_y = (MAX_HEIGHT - 900) / 2
                
                # 영등포구 m 관거개거...더보기
                if(x > 1460 and x < 1480) and (y > 390 and y < 410):
                    # 영등포구 m
                    screen_ydp = ydp_m
                    # 이미지 좌표
                    background_x = (MAX_WIDTH - 995) / 2
                    background_y = (MAX_HEIGHT - 900) / 2
                
                # 영등포구 해발고도
                if (x > 1460 and x < 1480) and (y > 490 and y < 510):
                    # 영등포구 해발고도
                    screen_ydp = ydp_height
                    # 이미지 좌표
                    background_x = (MAX_WIDTH - 1500) / 2
                    background_y = (MAX_HEIGHT - 631) / 2
                
                # 2024 강수량
                if (x > 1460 and x < 1480) and (y > 590 and y < 610):
                    # 강수량
                    screen_ydp = seoul_2023
                    # 이미지 좌표
                    background_x = (MAX_WIDTH - 1362) / 2
                    background_y = (MAX_HEIGHT - 900) / 2
                    
                # 홈화면 돌아가기
                if (x > 1460 and x < 1480) and (y > 690 and y < 710):
                    main()
                    
        screen.fill(WHITE)
        screen.blit(screen_ydp, (background_x, background_y))
        
        # 메뉴 선택(원 그리기)
        color = [(255, 0, 0), (255, 204, 0), (255, 255, 0), (0, 204, 0), (0, 102, 255), (102, 51, 153), (0, 0, 0)]  # 원의 색상 (빨간색)
        for i in range(1, 8):
            pygame.draw.circle(screen, color[i-1], (1470, (i*100)), 10)
        
        
        pygame.display.update()

# 광진구 데이터 시각화
def gj():
    running3 = True 
    screen_gj = gj_flooding
    background_x = (MAX_WIDTH - 974) / 2
    background_y = (MAX_HEIGHT - 900) / 2
    while running3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
                pos = pygame.mouse.get_pos() 
                # 좌표 판단
                x = pos[0]
                y = pos[1]
                
                # 광진구 침수흔적도
                if(x > 1460 and x < 1480) and (y > 90 and y < 110):
                    # 광진구 침수흔적도
                    screen_gj = gj_flooding
                    # 이미지 좌표
                    background_x = (MAX_WIDTH - 974) / 2
                    background_y = (MAX_HEIGHT - 900) / 2
                
                # 광진구 강수량
                if(x > 1460 and x < 1480) and (y > 190 and y < 210):
                    # 광진구 강수량
                    screen_gj = rain_gj
                    # 이미지 좌표
                    background_x = (MAX_WIDTH - 1500) / 2
                    background_y = (MAX_HEIGHT - 771) / 2
                
                # 광진구 맨홀 & 빗물받이
                if(x > 1460 and x < 1480) and (y > 290 and y < 310):
                    # 광진구 맨홀 빗물받이 갯수
                    screen_gj = gj_manhole
                    # 이미지 좌표
                    background_x = (MAX_WIDTH - 1381) / 2
                    background_y = (MAX_HEIGHT - 900) / 2
                
                # 광진구 m 관거개거...더보기
                if(x > 1460 and x < 1480) and (y > 390 and y < 410):
                    # 광진구 m
                    screen_gj = gj_m
                    # 이미지 좌표
                    background_x = (MAX_WIDTH - 977) / 2
                    background_y = (MAX_HEIGHT - 900) / 2
                
                # 광진구 해발고도
                if (x > 1460 and x < 1480) and (y > 490 and y < 510):
                    # 광진구 해발고도
                    screen_gj = gj_height
                    # 이미지 좌표
                    background_x = (MAX_WIDTH - 1500) / 2
                    background_y = (MAX_HEIGHT - 637) / 2
                
                # 2024 강수량
                if (x > 1460 and x < 1480) and (y > 590 and y < 610):
                    # 강수량
                    screen_gj = seoul_2023
                    # 이미지 좌표
                    background_x = (MAX_WIDTH - 1362) / 2
                    background_y = (MAX_HEIGHT - 900) / 2
                    
                # 홈화면 돌아가기
                if (x > 1460 and x < 1480) and (y > 690 and y < 710):
                    main()
                    
        screen.fill(WHITE)
        screen.blit(screen_gj, (background_x, background_y))
        
        # 메뉴 선택(원 그리기)
        color = [(255, 0, 0), (255, 204, 0), (255, 255, 0), (0, 204, 0), (0, 102, 255), (102, 51, 153), (0, 0, 0)]  # 원의 색상 (빨간색)
        for i in range(1, 8):
            pygame.draw.circle(screen, color[i-1], (1470, (i*100)), 10)
        
        
        pygame.display.update()



                
if __name__ == '__main__':
    main()
    
pygame.time.delay(1000)
pygame.quit()