
import pygame  

Blå = (0, 0, 255)
Grønn = (0, 255, 0)
Rød = (255, 0, 0)
Lilla = (150, 0, 220)
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

    def oppdater(self, rom):

        
        if self.ilufta:
            self.y_fart += rom.g
            self.y += self.y_fart
            #tester for landing
            for v in rom.vegger:
                if self.x + self.sx > v.x and self.x < v.x + v.sx:
                    if self.y + self.sy > v.y and self.y + self.sy < v.y + v.sy:
                        self.ilufta = False
                        self.y = v.y - self.sy
                        self.y_fart = 0

        else:
            på_vegg = False
            for v in rom.vegger:
                if self.x + self.sx > v.x and self.x < v.x + v.sx:
                    if self.y + self.sy + 1 >= v.y:
                        på_vegg = True
            if på_vegg == False:
                self.ilufta = True
        
        
    def test(self):
        print(self.sx, self.sy)

class rom_klasse:
    def __init__(self, vegger, fiender, ting, farge, g, start_posx, start_posy):
        self.vegger = vegger
        self.fiender = fiender
        self.ting = ting
        self. farge = farge
        self.g = g
        self.start_posx = start_posx
        self.start_posy = start_posy
    
    def tegn(self, bg):
        bg.fill(self.farge)
        for v in self.vegger: v.tegn(bg)

class vegg_klasse:
    def __init__(self, x, y, sx, sy, type = 0, farge = Blå):
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        self.type = type
        self.farge = farge
    
    def tegn(self, bg):
        if self.type == 0:
            pygame.draw.rect(bg, self.farge, (self.x, self.y, self.sx, self.sy))
        elif self.type == 1:
            pygame.draw.rect(bg, self.farge, (self.x, self.y, self.sx, self.sy), 8)
    

def lag_rom():
   
    alle_rom = []

    vegger = []
    vegger.append(vegg_klasse(0, 400, 500, 50))
    vegger.append(vegg_klasse(450, 300, 100, 30))
    vegger.append(vegg_klasse(600, 300, 100, 30, 1))

    alle_rom.append(rom_klasse(vegger, [], [], Hvit, 0.001, 200, 200))

    vegger = []
    vegger.append(vegg_klasse(450, 600, 100, 30))
    vegger.append(vegg_klasse(600, 600, 100, 30, 1))

    alle_rom.append(rom_klasse(vegger, [], [], Rød, 0.0015, 400, 200))


    
    return alle_rom

def spill():

    fortsett = True  

    alle_rom = lag_rom()

    rom_nr = 0

    rom = alle_rom[rom_nr]
    
    def tegn_brett():
        rom.tegn(bg)
        spiller.tegn(bg)
        
        pygame.display.update()



    pygame.init()
    bg = pygame.display.set_mode((1000,700))
    pygame.display.set_caption("celeste??")
    
    spiller = spiller_klasse(rom.start_posx, rom.start_posy, 50, 50, Lilla, True, 0, 0)


    while fortsett:
        
        for klikk in pygame.event.get():
            if klikk.type == pygame.QUIT:
                fortsett = False
            if klikk.type == pygame.KEYDOWN:
                if klikk.key == pygame.K_ESCAPE:
                    fortsett = False
                if klikk.key == pygame.K_0:
                    rom_nr = 0
                    rom = alle_rom[rom_nr]
                if klikk.key == pygame.K_1:
                    rom_nr = 1
                    rom = alle_rom[rom_nr]
        spiller.bevegelse()
        spiller.oppdater(rom)
        tegn_brett()

    pygame.quit()

spill()