import pygame
import sys
from cmath import rect
import os

# 시작 화면
pygame.init()
MAX_WIDTH = 1500
MAX_HEIGHT = 900

screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
WHITE = (255,255,255)

# 이미지 선언
current_path = os.path.dirname(__file__)
seoul_map = pygame.image.load(os.path.join(current_path, "seoul_map.png"))
seoul_flooding = pygame.image.load(os.path.join(current_path, "Test_ydp.png"))
seoul_2024 = pygame.image.load(os.path.join(current_path, "2024_seoul.png"))

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
                pos = pygame.mouse.get_pos() 
                # 좌표 판단
                x = pos[0]
                y = pos[1]
                if (x > 533 and x < 630) and (y > 572 and y < 593):
                    ydp()
                    running1 = False 
        
        pygame.display.update()

def ydp():
    running2 = True 
    while running2:
        # 영등포구 데이터 시각화
        background_x = (MAX_WIDTH - 1500) / 2
        background_y = (MAX_HEIGHT - 844) / 2
        
        screen.fill(WHITE)
        screen.blit(seoul_flooding, (background_x, background_y))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos() 
                # 좌표 판단
                x = pos[0]
                y = pos[1]
                if (x > 1426 and x < 1478) and (y > 46 and y < 78):
                    end()  
                    running2 = False
        pygame.display.update()

def end():
    while True:
        # 2024 강수량 예측
        background_x = (MAX_WIDTH - 1379) / 2
        background_y = (MAX_HEIGHT - 900) / 2
        
        screen.fill(WHITE)
        screen.blit(seoul_2024, (background_x, background_y))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos() 
                # 좌표 판단
                x = pos[0]
                y = pos[1]
                if (x > 1362 and x < 1416) and (y > 22 and y < 48):
                    main()  
        pygame.display.update()
                

if __name__ == '__main__':
    main()
    


pygame.time.delay(1000)
pygame.quit()