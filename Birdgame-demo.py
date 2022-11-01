import pygame
import random

start = True
x = 100                                                  # x,y - współrzędne ciała
y = 225
a = 1000
b = 1200
c = 1400                                                 # a,b,c,d,e,f - pierwsza współrzędna przeszkody
d = 1600
e = 1800
f = 2000
barriers = [a,b,c,d,e,f]
g = 150
h = 150
k = 150
l = 150
m = 150
n = 150
randomnr = [g,h,k,l,m,n]
points = 0
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((1000,500))              # tworzenie okna
player = pygame.rect.Rect(x,y,50,50)                      # tworzenie gracza
font = pygame.font.SysFont("Comic Sans MS", 48)           # czcionka i rozmiar

for i in range(5):
    randomnr[i] = random.randint(100, 200)

while start:
    for exit in pygame.event.get():
        if exit.type == pygame.QUIT:                      # zamykanie okna
            start = False
    keys = pygame.key.get_pressed()                       # pobieranie danych z klawiatury
    if y<450:                                             # siła grawitacji
        y+=4
    jump = 20
    if keys[pygame.K_SPACE] and y>=50:                    # jeśli klikniesz szpacja
        for i in range(1,5):
            y -= jump
            jump -= 5
            screen.fill((38, 110, 54))
            player = pygame.rect.Rect(x, y, 50, 50)
            pygame.draw.rect(screen, (255, 0, 0), player)
            for i in range(len(barriers)):
                wall_1 = pygame.rect.Rect(barriers[i], 0, 50, randomnr[i])                          # przeszkoda góra
                wall_2 = pygame.rect.Rect(barriers[i], randomnr[i] + 200, 50, 300 - randomnr[i])    # przeszkoda dół
                pygame.draw.rect(screen, (0, 0, 150), wall_1)
                pygame.draw.rect(screen, (0, 0, 150), wall_2)
                barriers[i] -= 5                                               # przesuwanie się przeszkód
                if barriers[i] == -200:
                    barriers[i] = 1000
                    randomnr[i] = random.randint(100, 200)
            for i in range(len(barriers)):
                if x == barriers[i]+50:
                    points += 1
            text = font.render(str(points), True, [0, 0, 0])                   # tworzenie wartości
            screen.blit(text, [488, 50])                                       # wyświetlanie wartości
            pygame.display.update()
            pygame.time.Clock().tick(30)
    pygame.time.Clock().tick(30)
    player = pygame.rect.Rect(x, y, 50, 50)
    screen.fill((38, 110, 54))
    pygame.draw.rect(screen,(255, 0, 0),player)
    for i in range(len(barriers)):
        wall_1 = pygame.rect.Rect(barriers[i], 0, 50, randomnr[i])
        wall_2 = pygame.rect.Rect(barriers[i], randomnr[i] + 200, 50, 300 - randomnr[i])
        pygame.draw.rect(screen, (0, 0, 150), wall_1)
        pygame.draw.rect(screen, (0, 0, 150), wall_2)
        barriers[i] -= 5
        if barriers[i] == -200:
            barriers[i] = 1000
            randomnr[i] = random.randint(100, 200)
    for i in range(len(barriers)):
        if x == barriers[i]+50:
            points += 1
    text = font.render(str(points), True, [0, 0, 0])                           # tworzenie wartości
    screen.blit(text, [488, 50])                                               # wyświetlanie wartości
    pygame.display.update()

    for i in range(len(barriers)):
        z = barriers[i]
        q = randomnr[i]
        if (y<q or y>q+150) and ((z<150 and z>=50) or z==150):
            while start == True:
                for exit in pygame.event.get():                                # obiekt dotyka przeszkodę
                    if exit.type == pygame.QUIT:
                        start = False
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:                                       # gra od nowa
                    x = 100
                    y = 225
                    a = 1000
                    b = 1200
                    c = 1400
                    d = 1600
                    e = 1800
                    f = 2000
                    barriers = [a, b, c, d, e, f]
                    points = 0
                    for i in range(len(randomnr)):
                        pygame.time.Clock().tick(6)
                        randomnr[i] = random.randint(100, 200)
                    randomnr = [g, h, k, l, m, n]
                    break