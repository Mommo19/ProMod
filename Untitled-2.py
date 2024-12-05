
import pygame

Blå = (0, 0, 255)
Grønn = (0, 255, 0)
Rød = (255, 0, 0)
sort = (0, 0, 0)
Hvit = (255, 255, 255)
x = 200
y = 200

pygame.init()
bakgrunnd = pygame.display.set_mode((1000,700))
pygame.display.set_caption("celeste??")
bakgrunnd.fill(Hvit)
pygame.draw.rect(bakgrunnd, Blå, (x, y, 50, 50))

pygame.display.update()


while True:
    for klik in pygame.event.get():
        if klik.type == pygame.QUIT:
            pygame.quit()
        if klik.type == pygame.KEYDOWN:
            if klik.key == pygame.K_d:
                x += 20
            if klik.key == pygame.K_ESCAPE:
                pygame.quit()
    bakgrunnd.fill(Hvit)
    pygame.draw.rect(bakgrunnd, Blå, (x, y, 50, 50))
    pygame.display.update()
pygame.quit()