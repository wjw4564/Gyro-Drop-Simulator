import pygame

pygame.init()

screen_width = 480 #horizional
screen_height = 640 #vertical
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Physhics")

background = pygame.image.load("D:\.역대과제\\2024-10-24-물리 파이게임 전자기유도 시뮬\\background.png")
bar = pygame.image.load("D:\.역대과제\\2024-10-24-물리 파이게임 전자기유도 시뮬\\bar.png")
bar = pygame.transform.scale(bar, (300, 500))
seats = pygame.image.load("seats-common.png")
seats = pygame.transform.scale(seats, (188, 81))
topb = pygame.image.load("top-blue.png")
topb = pygame.transform.scale(topb, (89, 74))
topr = pygame.image.load("top-red.png")
topr = pygame.transform.scale(topr, (89, 74))
side = 188

magnet_type = True #red
seats_show = False
print("스페이스를 누르면 시뮬레이터가 실행되고, 화살표 윗쪽 키와 화살표 아랫쪽 키를 입력함으로써 각각 자석의 극 변경과 좌석에 배치된 자석이 일으키고 있는 자기장을 볼 지 말 지에 대한 여부를 조절할 수 있습니다.")

running = True #게임 진행 확인
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        screen.blit(background, (0, 0))
        screen.blit(bar, (90, 100))
        screen.blit(seats, (240-94, 450)) #100을 최고점으로, 450을 최저점로, 350이 전자기유도시행
        screen.blit(topr, (25, 50))
        screen.blit(topb, (30,50+74))

        if event.type == pygame.KEYUP and event.key == pygame.K_UP:
            if magnet_type == True:
                magnet_type = False
            else:
                magnet_type = True

        if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
            if seats_show == False:
                seats_show = True
            else:
                seats_show = False

        if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            screen.blit(background, (0, 0))
            screen.blit(bar, (90, 100))
            screen.blit(seats, (240-94, 100))
            screen.blit(topr, (25, 50))
            screen.blit(topb, (30,50+74))
            a = 100
            pygame.display.update()
            while a < 350:
                screen.blit(background, (0, 0))
                screen.blit(bar, (90, 100))
                screen.blit(seats, (240-94, a))
                screen.blit(topr, (25, 50))
                screen.blit(topb, (30,50+74))
                pygame.display.update()
                a = a + 2 * a * a / 10000
                pygame.time.delay(10)

            if magnet_type == True:
                if seats_show == True:
                    seats = pygame.image.load("seats-red.png")
                    seats = pygame.transform.scale(seats, (293, 212))
                    side = 293
            else:
                if seats_show == True:
                    seats = pygame.image.load("seats-blue.png")
                    seats = pygame.transform.scale(seats, (293, 213))      
                    side = 293

            print("자석이 기둥의 철판에 가까워져 전자기 유도가 일어나는데, 자석의 아래에 있는 철판은 좌석의 자석을 밀어내기 위해 자석이 만들어내는 자기장과 반대되는 자기장을 형성하고, 자석의 위에 있는 철판은 자석을 끌어당기기 위해 자기장과 같은 자기장을 형성한다. 형성되는 자기장에 의한 전류의 흐름은 좌측 상단에 있는 화살표의 색을 비교하여 판단하면 된다.")
            
            while a < 450:
                if magnet_type == False:
                    screen.blit(background, (0, 0))
                    screen.blit(bar, (90, 100))
                    r = pygame.image.load("arrow-red.png") #화살표는 69 기준 490이 최저, 370이 최상
                    r = pygame.transform.scale(r, (300, 540-a))
                    b = pygame.image.load("arrow-blue.png")
                    b = pygame.transform.scale(b, (300, a-300+94))
                    if seats_show == True:
                        screen.blit(seats, (240-side/2, a-65.5))
                    else:
                        screen.blit(seats, (240-side/2, a))
                    screen.blit(r, (90, 94+a-50))
                    screen.blit(b, (90, 370-70))
                    screen.blit(topr, (25, 50))
                    screen.blit(topb, (30,50+74))
                    pygame.display.update()
                    a = a + 2.5
                    pygame.time.delay(50)
                else:
                    screen.blit(background, (0, 0))
                    screen.blit(bar, (90, 100))
                    r = pygame.image.load("arrow-blue.png") #화살표는 69 기준 490이 최저, 370이 최상
                    r = pygame.transform.scale(r, (300, 540-a))
                    b = pygame.image.load("arrow-red.png")
                    b = pygame.transform.scale(b, (300, a-300+94))
                    if seats_show == True:
                        screen.blit(seats, (240-side/2, a-66))
                    else:
                        screen.blit(seats, (240-side/2, a))
                    screen.blit(seats, (240-side/2, a))
                    screen.blit(r, (90, 94+a-50))
                    screen.blit(b, (90, 370-70))
                    screen.blit(topr, (25, 50))
                    screen.blit(topb, (30,50+74))
                    pygame.display.update()
                    a = a + 2.5
                    pygame.time.delay(50)

            bar = pygame.image.load("bar.png")
            bar = pygame.transform.scale(bar, (300, 500))
            seats = pygame.image.load("seats-common.png")
            seats = pygame.transform.scale(seats, (188, 81))
            side = 188

            screen.blit(background, (0, 0))
            screen.blit(bar, (90, 100))
            screen.blit(seats, (240-94, 450))
            screen.blit(topr, (25, 50))
            screen.blit(topb, (30,50+74))
            pygame.display.update()
        pygame.display.update()
pygame.quit()