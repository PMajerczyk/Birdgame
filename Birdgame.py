import pygame, random

start = True
x = 100
y = 225                                                                        # x,y - współrzędne ciała
a = 1000
b = 1200
c = 1400                                                                       # a,b,c,d,e,f - pierwsza współrzędna przeszkody
d = 1600
e = 1800
f = 2000
barriers = [a,b,c,d,e,f]
g = h = k = l = m = n = 150                                                    # g,h,k,l,m,n - randomowe wysokości
randomnr = [g,h,k,l,m,n]
points = 0
bestscore = 0
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((1000,500))                                   # tworzenie okna
image = pygame.image.load('Background.png')                                    # załadowanie tła
font = pygame.font.SysFont("Comic Sans MS", 48)
font1 = pygame.font.SysFont("Comic Sans MS", 16)                               # czcionka i rozmiar
for i in range(len(randomnr)):
    randomnr[i] = random.randint(50, 250)                                      # losowanie wysokości

def character():                                                               # rysowanie gracza
    player = pygame.rect.Rect(x, y, 50, 50)
    pygame.draw.rect(screen, (255,0,0), player)
    pygame.draw.circle(screen, (250,250,250), (x+33,y+12), 8)
    pygame.draw.circle(screen, (250,250,250), (x+17,y+12), 8)
    pygame.draw.circle(screen, (0, 0, 0), (x+33, y+12), 2)
    pygame.draw.circle(screen, (0, 0, 0), (x+17, y+12), 2)
    pygame.draw.polygon(screen,(222, 175, 20),[(x+20,y+20),(x+30,y+20),(x+25,y+30)])

def columns():                                                                 # rysowanie przeszkód
    wall_1 = pygame.rect.Rect(barriers[i], 0, 50, randomnr[i])
    wall_2 = pygame.rect.Rect(barriers[i], randomnr[i] + 200, 50, 300 - randomnr[i])
    pygame.draw.rect(screen, (0, 0, 150), wall_1)
    pygame.draw.rect(screen, (0, 0, 150), wall_2)

def results():                                                                 # wyświetlanie wyników
    text = font.render(str(points), True, [0, 0, 0])
    screen.blit(text, [488, 40])
    text1 = font.render(str(bestscore), True, [0, 0, 0])
    text2 = font1.render('Best score:', True, [0, 0, 0])
    screen.blit(text1, [35, 40])
    screen.blit(text2, [10, 20])

while start:
    for exit in pygame.event.get():
        if exit.type == pygame.QUIT:                                           # zamykanie okna
            start = False
    keys = pygame.key.get_pressed()                                            # pobieranie danych z klawiatury
    if y<450:
        y+=4                                                                   # siła grawitacji
    jump = 20
    if keys[pygame.K_SPACE] and y>=50:                                         # jeśli klikniesz szpacja
        for i in range(1,5):
            y -= jump
            jump -= 5
            screen.blit(image, (0, 0))                                         # rysowanie tła
            pygame.display.flip()
            character()
            for i in range(len(barriers)):
                columns()
                barriers[i] -= 5                                               # przesuwanie się przeszkód
                if barriers[i] == -200:
                    barriers[i] = 1000                                         # przenoszenie przeszkody na koniec
                    randomnr[i] = random.randint(50, 250)
                if x == barriers[i]+50:
                    points += 1                                                # liczenie pkt
            results()
            pygame.display.update()
            pygame.time.Clock().tick(30)
    pygame.time.Clock().tick(30)
    screen.blit(image, (0, 0))                                                 # rysowanie tła
    pygame.display.flip()
    character()
    for i in range(len(barriers)):
        columns()
        barriers[i] -= 5                                                       # przesuwanie się przeszkód
        if barriers[i] == -200:
            barriers[i] = 1000                                                 # przenoszenie przeszkody na koniec
            randomnr[i] = random.randint(50, 250)
        if x == barriers[i]+50:
            points += 1                                                        # liczenie pkt
    results()
    pygame.display.update()
    for i in range(len(barriers)):
        z = barriers[i]
        q = randomnr[i]
        if (y<q or y>q+150) and ((z<150 and z>=50) or z==150):                 # jeśli gracz dotknie przeszkodę
            if points > bestscore:                                             # jeśli więcej pkt od najlepszego wyniku
                bestscore = points
                screen.blit(image, (0, 0))                                     # rysowanie tła
                pygame.display.flip()
                character()
                for i in range(len(barriers)):
                    columns()
                    barriers[i] -= 5                                           # przesuwanie się przeszkód
                    if barriers[i] == -200:
                        barriers[i] = 1000                                     # przenoszenie przeszkody na koniec
                        randomnr[i] = random.randint(50, 250)
                results()
                pygame.display.update()
            while start == True:
                for exit in pygame.event.get():                                # obiekt dotyka przeszkodę
                    if exit.type == pygame.QUIT:
                        start = False
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:                                       # gra od nowa
                    y = 225
                    barriers = [a, b, c, d, e, f]
                    points = 0
                    for i in range(len(randomnr)):                             # losowanie wyskokości
                        pygame.time.Clock().tick(6)                            # opóźnienie
                        randomnr[i] = random.randint(50, 250)
                    break