
import pygame

Blå = (0, 0, 255)
Grønn = (0, 255, 0)
Rød = (255, 0, 0)
Sort = (0, 0, 0)
Hvit = (255, 255, 255)
x = 200
y = 200
x_fart = 0
y_fart = 0

pygame.init()
bakgrunnd = pygame.display.set_mode((1000,700))
pygame.display.set_caption("celeste??")
bakgrunnd.fill(Hvit)
pygame.draw.rect(bakgrunnd, Blå, (x, y, 50, 50))

pygame.display.update()


while True:
    
    y_fart += 0.001
    x += x_fart
    y += y_fart
    if y > 300:
        y_fart = 0
        y -= 0.001
    for klik in pygame.event.get():
        if klik.type == pygame.QUIT:
            pygame.quit()
        if klik.type == pygame.KEYDOWN:
            if klik.key == pygame.K_SPACE:
                y_fart -= 0.5
#            if klik.key == pygame.K_s:
#                y_fart += 20
            if klik.key == pygame.K_a:
                x_fart -= 1
            if klik.key == pygame.K_d:
                x_fart += 1
            if klik.key == pygame.K_ESCAPE:
                pygame.quit()
    bakgrunnd.fill(Hvit)
    pygame.draw.rect(bakgrunnd, Blå, (x, y, 50, 50))
    pygame.draw.rect(bakgrunnd, Grønn, (0, 350, 1000, 50))
    pygame.display.update()
pygame.quit()