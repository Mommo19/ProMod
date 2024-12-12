
import pygame

Blå = (0, 0, 255)
Grønn = (0, 255, 0)
Rød = (255, 0, 0)
Sort = (0, 0, 0)
Hvit = (255, 255, 255)

class spiller_klasse:
    def __init__(self, x, y, sx, sy, farge, ilufta, x_fart, y_fart):
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        self.farge = farge
        self.ilufta = ilufta
        self.x_fart = x_fart
        self.y_fart = y_fart
    
    def tegn(self, bg):
        pygame.draw.rect(bg, self.farge, (self.x, self.y, self.sx, self.sy))

    def bevegelse(self):
        knaper = pygame.key.get_pressed()
        if knaper [pygame.K_a]:
            self.x -= 0.5
        if knaper [pygame.K_d]:
            self.x += 0.5
        if knaper  [pygame.K_SPACE] and not self.ilufta:
            self.y_fart -= 0.5   
            self.ilufta = True

    def oppdater(self, g):
        if self.ilufta:
            self.y_fart += g
            self.y += self.y_fart
        if self.y > 300:
            self.ilufta = False
            self.y_fart = 0
        

def spill():

    fortsett = True  
    g = 0.001  


    def tegn_brett():
        bg.fill(Hvit)
        pygame.draw.rect(bg, Grønn, (0, 350, 1000, 50))
        spiller.tegn(bg)
        pygame.display.update()


    pygame.init()
    bg = pygame.display.set_mode((1000,700))
    pygame.display.set_caption("celeste??")
    
    spiller = spiller_klasse(200, 200, 50, 50, Blå, True, 0, 0)


    while fortsett:
        
 
        for klikk in pygame.event.get():
            if klikk.type == pygame.QUIT:
                fortsett = False
            if klikk.type == pygame.KEYDOWN:
                if klikk.key == pygame.K_ESCAPE:
                    fortsett = False
        
        spiller.bevegelse()
        spiller.oppdater(g)
        tegn_brett()
    pygame.quit()


spill()