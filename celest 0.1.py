
import pygame  

Blå = (0, 0, 255)
Grønn = (0, 255, 0)
Rød = (255, 0, 0)
Lilla = (150, 0, 220)
Sort = (0, 0, 0)
Hvit = (255, 255, 255)

scr_x = 1100
scr_y = 650

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
            self.x -= 1
        if knaper [pygame.K_d]:
            self.x += 1
        if knaper  [pygame.K_SPACE] and not self.ilufta:
            self.y_fart -= 2.5
            self.ilufta = True

    def oppdater(self, rom):
        
        for v in rom.vegger:
            if (self.y > v.y and self.y < v.y + v.sy) or (self.y + self.sy > v.y and self.y < v.y + v.sy) and v.type == 0:
                if self.x + self.sx == v.x:
                    self.x = v.x - self.sx - 1

        for v in rom.vegger:
            if (self.y > v.y and self.y < v.y + v.sy) or (self.y + self.sy > v.y and self.y < v.y + v.sy) and v.type == 0:
                if self.x == v.x + v.sx:
                    self.x = v.x + v.sx + 1

        if self.ilufta:
            self.y_fart += rom.g
            self.y += self.y_fart
            
            #tester for tak
            for v in rom.vegger:
                if self.x + self.sx > v.x and self.x < v.x + v.sx:
                    if self.y > v.y + v.sy - 3 and self.y < v.y + v.sy and v.type == 0:
                        self.y_fart = 0
                        self.y = v.y + v.sy
            
            #tester for landing
            for v in rom.vegger:
                if self.x + self.sx > v.x and self.x < v.x + v.sx:
                    if self.y + self.sy > v.y and self.y + self.sy < v.y + v.sy and self.y_fart >= 0:
                        self.ilufta = False
                        self.y = v.y - self.sy
                        self.y_fart = 0

        else:
            på_vegg = False
            for v in rom.vegger:
                if self.x + self.sx > v.x and self.x < v.x + v.sx:
                    if self.y + self.sy + 1 == v.y:
                        på_vegg = True
            if på_vegg == False:
                self.ilufta = True
        
        if self.y > scr_y:
            self.x = rom.start_posx
            self.y = rom.start_posy
            self.y_fart = 0
             
        #if self.x > rom.slutt_posx:
            #if self.y < rom.slutt_posy + 50 and self.y > rom.slutt_posy - 50:
                #rom_nr += 1
                #rom = alle_rom[rom_nr]
        
    def test(self):
        print(self.sx, self.sy)

class rom_klasse:
    def __init__(self, vegger, fiender, ting, farge, g, start_posx, start_posy, slutt_posx, slutt_posy):
        self.vegger = vegger
        self.fiender = fiender
        self.ting = ting
        self. farge = farge
        self.g = g
        self.start_posx = start_posx
        self.start_posy = start_posy
        self.slutt_posx = slutt_posx
        self.slutt_posy = slutt_posy
    
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
    vegger.append(vegg_klasse(0, 0, 50, scr_y))
    vegger.append(vegg_klasse(0, 0, scr_x, 50))
    vegger.append(vegg_klasse(scr_x - 50, 150, 50, scr_y - 150))
    vegger.append(vegg_klasse(0, 150, 250, 30))
    vegger.append(vegg_klasse(350, 150, scr_x - 350, 30))
    vegger.append(vegg_klasse(0, scr_y - 50, 500, 50))
    vegger.append(vegg_klasse(450, 500, 100, 30))
    vegger.append(vegg_klasse(650, 450, 100, 30))
    vegger.append(vegg_klasse(900, 450, 100, 30))
    vegger.append(vegg_klasse(950, 350, 100, 30))
    vegger.append(vegg_klasse(750, 270, 100, 30))
    vegger.append(vegg_klasse(570, 320, 100, 30))
    vegger.append(vegg_klasse(370, 300, 100, 30))
    vegger.append(vegg_klasse(250, 250, 80, 30))
    vegger.append(vegg_klasse(250, 150, 100, 30, 1))

    

    alle_rom.append(rom_klasse(vegger, [], [], Hvit, 0.03, 100, scr_y - 100, 500, 350))

    vegger = []
    vegger.append(vegg_klasse(450, 600, 100, 30))
    vegger.append(vegg_klasse(600, 600, 100, 30, 1))

    alle_rom.append(rom_klasse(vegger, [], [], Rød, 0.03, 400, 200, scr_x, 100))


    
    return alle_rom

def spill():

    fortsett = True  

    alle_rom = lag_rom()

    rom_nr = 0

    rom = alle_rom[rom_nr]
    
    # sette utafor ??
    def tegn_brett():
        rom.tegn(bg)
        spiller.tegn(bg)
        
        pygame.display.update()



    pygame.init()

    clock = pygame.time.Clock()
    fps = 200

    bg = pygame.display.set_mode((scr_x, scr_y))
    pygame.display.set_caption("celeste??")
    
    spiller = spiller_klasse(rom.start_posx, rom.start_posy, 25, 50, Lilla, True, 0, 0)


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

        clock.tick(fps)

    pygame.quit()

spill()



# To Do
"""
lage brett
flere rom
!start/slut i rom!
finder/pigger
"""

#to do later
"""
liv??
moren til jakob
ting
start meny
grafik
"""