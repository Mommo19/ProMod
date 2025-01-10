
import pygame  

# Her definerer jeg farger
Blå = (0, 0, 255)
Grønn = (0, 255, 0)
Rød = (255, 0, 0)
Lilla = (150, 0, 220)
Sort = (0, 0, 0)
Hvit = (255, 255, 255)

# Definerer jeg skjermstørelse
scr_x = 1100
scr_y = 650

class spiller_klasse:   # Lager klasse for spilleren
    def __init__(self, x, y, sx, sy, farge, ilufta, x_fart, y_fart):    # Initsierer klassen
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        self.rect = pygame.Rect(x, y, sx, sy)
        self.farge = farge
        self.ilufta = ilufta
        self.x_fart = x_fart
        self.y_fart = y_fart
    
    def tegn(self, bg):     # Lager en funskjon for å tegne spilerern
        pygame.draw.rect(bg, self.farge, self.rect)     # Tegner spilleren

    def bevegelse(self):    # Lager en funksjon for bevegelse
        knapper = pygame.key.get_pressed()      # Gjør det mulig å holde inne knapper
        if knapper[pygame.K_a] or knapper[pygame.K_LEFT]:   # Tester for A og venstre pil
            self.x -= 1     # Flyter karakteren mot venstre
        if knapper[pygame.K_d] or knapper[pygame.K_RIGHT]:  # Tester for D og høyre pil
            self.x += 1     # Flytter karakteren mot høyre
        if knapper[pygame.K_SPACE] and not self.ilufta:     # Sjekker om space blir klikket og om du skal få lov til å hoppe
            self.y_fart -= 2.5      # Øker farten oppover
            self.ilufta = True      # Gjør at du ikke kan hoppe igjen

    def oppdater(self, rom):    # Lager en funskjon som oppdaterer for handlinger
        
        ferdig = False      # setter ferdig til False

        # Tester om du treffer veggen fra venstre
        for v in rom.vegger:    # Går igjenom alle veggene i nåverende rom
            if (self.y > v.y and self.y < v.y + v.sy) or (self.y + self.sy > v.y and self.y < v.y + v.sy) and v.type == 0:      # Tester om spilleren sine y kordinater overlapper veggene
                if self.x + self.sx == v.x:     # Tester om spillerens x kordinaer går inn i veggene fra venstre
                    self.x = v.x - self.sx - 1  # Flyter karakteren ut av veggen hvis posisjonen overlapper

        # Tester om du treffer vegen fra høyre
        for v in rom.vegger:    # Går igjenom alle veggene i nåverende rom 
            if (self.y > v.y and self.y < v.y + v.sy) or (self.y + self.sy > v.y and self.y < v.y + v.sy) and v.type == 0:
                if self.x == v.x + v.sx:        # Tester om spillerens x kordinaer går inn i veggene fra høyre
                    self.x = v.x + v.sx + 1     # Flyter karakteren ut av veggen hvis posisjonen til spilleren overlapper

        if self.ilufta:
            self.y_fart += rom.g    # Aktiverer tyngdekraften i romet hvis karakteren er i lufta
            self.y += self.y_fart
            
            # Tester om du treffer veggen fra undersiden
            for v in rom.vegger:    # Går igjenom alle veggene i nåverende rom
                if self.x + self.sx > v.x and self.x < v.x + v.sx:     # Tester om spillerens x kordinaer overlapper med veggen 
                    if self.y > v.y + v.sy - 3 and self.y < v.y + v.sy and v.type == 0:     # Tester om spillerens y kordinaer overlapper med veggen og om den er av veggtype 1
                        self.y_fart = 0     # Setter y farten til 0
                        self.y = v.y + v.sy     # Flytter karakteren ut av veggen hvis posisjonen til spilleren overlapper
            
            # Tester for landing
            for v in rom.vegger:    # Går igjenom alle veggene i nåverende rom
                if self.x + self.sx > v.x and self.x < v.x + v.sx:      # Tester om spillerens x kordinaer overlapper med veggen 
                    if self.y + self.sy > v.y and self.y + self.sy < v.y + v.sy and self.y_fart >= 0:   # Tester om spillerens y kordinaer overlapper med veggen
                        self.ilufta = False     # Informerer om at spilleren ikke er i lufta
                        self.y = v.y - self.sy  # Flytter karakteren ut av veggen hvis posisjonen til spilleren overlapper
                        self.y_fart = 0     # Setter y farten til 0

        else:   # Hvis spilleren ikke er i lufta
            på_vegg = False     # Tester om du er på et gulv eller ikke
            for v in rom.vegger:    # Går igjenom alle veggene i nåverende rom
                if self.x + self.sx > v.x and self.x < v.x + v.sx:      # Tester om spillerens x kordinaer overlapper med veggen 
                    if self.y + self.sy + 1 == v.y:     # Tester om spillerens y kordinaer overlapper med veggen 
                        på_vegg = True      # Informerer at du er på bakken
            if på_vegg == False:    # Om du er på bakken
                self.ilufta = True  # Setter i lufta til True
        
        if self.y > scr_y:      # Sjekker om du har falt under skjermen
            self.x = rom.start_posx     # Setter x verdien til startposisjonen i rommet
            self.y = rom.start_posy     # Setter y verdien til startposisjonen i rommet
            self.y_fart = 0             # Setter y farten til 0
             
        if self.x > rom.slutt_posx:     # Sjekkr om spillerns x verdi er den samme som slutten av rommet
            if self.y < rom.slutt_posy + 50 and self.y > rom.slutt_posy - 50:       # Sjekkr om spillerns y verdi er den samme som slutten av rommet
                ferdig = True       # Setter ferdig til True

        for h in rom.hinder:        # Går igjenom alle hinderene i nåverende rom
            if self.rect.colliderect(h.rect):       # Sjekker om spilleren koliderer med hinderene
                self.x = rom.start_posx     # Setter x verdien til startposisjonen i rommet
                self.y = rom.start_posy     # Setter y verdien til startposisjonen i rommet
                self.y_fart = 0             # Setter y farten til 0

        self.rect = pygame.Rect(self.x, self.y, self.sx, self.sy)       # Oppdaterer informasjonen til spilleren

        return ferdig       # Returnerer ferdig
        
class rom_klasse:       # Lager Klasse for rom
    def __init__(self, vegger, hinder, ting, farge, g, start_posx, start_posy, slutt_posx, slutt_posy):     # Initsierer klassen
        self.vegger = vegger
        self.hinder = hinder
        self.ting = ting
        self. farge = farge
        self.g = g
        self.start_posx = start_posx
        self.start_posy = start_posy
        self.slutt_posx = slutt_posx
        self.slutt_posy = slutt_posy
    
    def tegn(self, bg):     # Lager funksjon for å tegne rommene 
        bg.fill(self.farge) # Tegner bakgrunen
        for v in self.vegger: v.tegn(bg)    # Tegner inn veggene
        for h in self.hinder: h.tegn(bg)    # Tegner inn hindringene

class vegg_klasse:      # Lager klasse for vegger
    def __init__(self, x, y, sx, sy, type = 0, farge = Blå):    # Initsierer klassen
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        self.type = type
        self.farge = farge
    
    def tegn(self, bg):     # lager funksjon for å tegne vegger
        if self.type == 0:      # Sjekker hvilken type veggen er
            pygame.draw.rect(bg, self.farge, (self.x, self.y, self.sx, self.sy))        # Tegner type 0 vegger
        elif self.type == 1:    # Sjekker hvilken type veggen er
            pygame.draw.rect(bg, self.farge, (self.x, self.y, self.sx, self.sy), 8)     # Tegner type 1 vegger

class hinder_klasse:    # Lager en klasse for hindre
    def __init__(self, x, y, sx, sy, farge = Rød):      # Initsierer klassen
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        self.rect = pygame.Rect(x, y, sx, sy)
        self.farge = farge

    def tegn(self, bg):     # Lager funksjon for å tegne hindringene
        pygame.draw.rect(bg, self.farge, self.rect)
    

def lag_rom():  # lager rom
   
    alle_rom = [] # lager tom liste som skal inholde alle rommene

    vegger = [] # lager tom liste med alle veger til rommet
    
    # legger til hovedveggene
    vegger.append(vegg_klasse(0, 0, 50, scr_y))
    vegger.append(vegg_klasse(0, 0, scr_x, 50))
    vegger.append(vegg_klasse(scr_x - 50, 150, 50, scr_y - 150))
    vegger.append(vegg_klasse(0, 150, 250, 30))
    vegger.append(vegg_klasse(350, 150, scr_x - 350, 30))
    vegger.append(vegg_klasse(0, scr_y - 50, 500, 50))
    
    # legger til platformer
    vegger.append(vegg_klasse(450, 500, 100, 30))
    vegger.append(vegg_klasse(650, 450, 100, 30))
    vegger.append(vegg_klasse(900, 450, 100, 30))
    vegger.append(vegg_klasse(950, 350, 100, 30))
    vegger.append(vegg_klasse(750, 270, 100, 30))
    vegger.append(vegg_klasse(570, 320, 100, 30))
    vegger.append(vegg_klasse(370, 300, 100, 30))
    vegger.append(vegg_klasse(250, 250, 80, 30))
    
    # legger til platformer som kan hoppes gjenom
    vegger.append(vegg_klasse(250, 150, 100, 30, 1))

    hinder = [] # lager liste til alle hinderene

    alle_rom.append(rom_klasse(vegger, hinder, [], Hvit, 0.03, 100, scr_y - 100, scr_x, 150)) # lager romet og legger det til lista med rom


    vegger = [] # tømmer lista for gammle vegger

    # legger til hovedveggene
    vegger.append(vegg_klasse(0, scr_y - 50, scr_x, 50))
    vegger.append(vegg_klasse((scr_x/2)-25, 0, 50, scr_y - 150))
    vegger.append(vegg_klasse(0, 0, scr_x, 50))
    vegger.append(vegg_klasse(0, 150, 50, scr_y - 150))
    vegger.append(vegg_klasse(scr_x - 50, 150, 50, scr_y - 150))
    vegger.append(vegg_klasse(-51, 50, 50, 150))
    
    # legger til platformer
    vegger.append(vegg_klasse(100, 200, 100, 30))
    vegger.append(vegg_klasse(350, 200, 100, 30))
    vegger.append(vegg_klasse(320, 400, 100, 30))
    vegger.append(vegg_klasse(scr_x - 300, scr_y -250, 50, 30))
    vegger.append(vegg_klasse((scr_x/2) + 25, 400, 50, 30))
    vegger.append(vegg_klasse(scr_x/2 + 225, 250, 100, 30))
    vegger.append(vegg_klasse(((scr_x-300)-(scr_x/2 + 25))/2 + scr_x/2 + 45, 450, 10, 10))
    vegger.append(vegg_klasse(scr_x - 150, 175, 10, 10))
    
    # legger til platformer som kan hoppes gjenom
    vegger.append(vegg_klasse(scr_x-200, scr_y - 150, 50, 30, 1))
    vegger.append(vegg_klasse(scr_x/2 + 25, 300, 50, 30, 1))

    hinder = [] # tømmer lista for gammle hindere

    # legger til alle hinderene
    hinder.append(hinder_klasse(50, 230, 400, 15))
    hinder.append(hinder_klasse(50, 430, 100, 15))
    hinder.append(hinder_klasse(200, 430, (scr_x/2)-225, 15))
    hinder.append(hinder_klasse(scr_x-200, scr_y - 250, 150, 30))
    hinder.append(hinder_klasse(scr_x/2 + 125, 250, 100, 30))

    alle_rom.append(rom_klasse(vegger, hinder, [], Hvit, 0.03, 0, 100, scr_x, 100)) # legger til romet i lista med alle rommene

    vegger = [] # tømmer lista for gammle vegger

    # legger til hovedveggene
    vegger.append(vegg_klasse(0, scr_y - 50, scr_x, 50))
    vegger.append(vegg_klasse(0, 0, scr_x, 50))
    vegger.append(vegg_klasse(0, 150, 50, scr_y - 150))
    vegger.append(vegg_klasse(scr_x - 50, 0, 50, scr_y/2 - 50))
    vegger.append(vegg_klasse(scr_x - 50, scr_y/2 + 50, 50, scr_y/2 - 50))
    vegger.append(vegg_klasse(-51, 50, 50, 150))
    vegger.append(vegg_klasse(scr_x + 1, scr_y/2 - 50, 50, 100))

    # legger til platformer
    vegger.append(vegg_klasse(100, 350, 70, 30))
    vegger.append(vegg_klasse(370, 400, 30, 30))
    vegger.append(vegg_klasse(530, 370, 30, 30))
    vegger.append(vegg_klasse(600, 340, 30, 30))
    vegger.append(vegg_klasse(750, 370, 10, 10))
    vegger.append(vegg_klasse(900, 320, 5, 5))

    # legger til platformer som kan hoppes gjenom

    hinder = [] # tømmer lista for gammle hindere

    # legger til alle hinderene
    hinder.append(hinder_klasse(50, scr_y - 65, scr_x - 100, 15))
    hinder.append(hinder_klasse(70, 50, scr_x - 120, 15))
    hinder.append(hinder_klasse(50, 150, 15, scr_y - 200))
    hinder.append(hinder_klasse(scr_x - 65, 50, 15, scr_y/2 - 100))
    hinder.append(hinder_klasse(scr_x -65, scr_y/2 + 50, 15, scr_y/2 - 100))

    alle_rom.append(rom_klasse(vegger, hinder, [], Hvit, 0.03, 0, 100, scr_x, 100)) # legger til romet i lista med alle rommene


    
    return alle_rom # returnerer lista med alle rommene


def spill():    # Utfører alt som trengs for at ting skal skje i spilet

    fortsett = True         # Brukes for å drive en while løkke

    alle_rom = lag_rom()    # Henter ut lista med alle rom

    rom_nr = 0              # Brukes til å gå mellom rom

    rom = alle_rom[rom_nr]  # Setter nåverende rom
    
    
    def tegn_brett():       # tegner brettet
        rom.tegn(bg)        # tegner romet
        spiller.tegn(bg)    # tegner spilerern
        
        pygame.display.update()     # Utfører tegningen

    pygame.init() # Initsierer ting til pygame

    clock = pygame.time.Clock()     # Lager en kloke spile kans kjøre på
    fps = 200                       # Lager en variabel som skal kontrolere hvor raskt spile skal går

    bg = pygame.display.set_mode((scr_x, scr_y))    # Lager skjermen du spiller på
    pygame.display.set_caption("celeste??")         # Lager navn på skjermen
    
    spiller = spiller_klasse(rom.start_posx, rom.start_posy, 25, 50, Lilla, True, 0, 0)     # Lager spileren


    while fortsett:     # Lager en løke som kan kjøre for altdi
        
        for klikk in pygame.event.get():            # Henter informasjon om handlinger
            
            if klikk.type == pygame.QUIT:           # Når man klikker på X-en så ståper while løka
                fortsett = False
            
            if klikk.type == pygame.KEYDOWN:        # Gjør at man kan brukke tastetrykk
                if klikk.key == pygame.K_ESCAPE:    # Gjør at while løkka stopper når man klikker escape
                    fortsett = False
                
                if klikk.key == pygame.K_1:         # Sjekker om du klikker på 1
                    rom_nr = 0                      # Endrer rom_nr til 0
                    rom = alle_rom[rom_nr]          # Endrer nåværende rom
                    spiller.x = rom.start_posx      # Eendrer x posisjonen til spileren til startposisjnen på nåværende rom
                    spiller.y = rom.start_posy      # Eendrer y posisjonen til spileren til startposisjnen på nåværende rom
                
                if klikk.key == pygame.K_2:         # Gjør det samme som over bare for tast 2
                    rom_nr = 1
                    rom = alle_rom[rom_nr]
                    spiller.x = rom.start_posx
                    spiller.y = rom.start_posy
                
                if klikk.key == pygame.K_3:         # Samme bare for 3
                    rom_nr = 2
                    rom = alle_rom[rom_nr]
                    spiller.x = rom.start_posx
                    spiller.y = rom.start_posy
        
        spiller.bevegelse()                 # Kjører funksjonen for spillerens bevegelse
        ferdig = spiller.oppdater(rom)      # Kjører oppdaterfunksjonen mens den henter ut verdien til ferdig
        if ferdig:
            rom_nr += 1                     # Endrer rom_nr med 1
            rom = alle_rom[rom_nr]          # Setter rom til rom_nr
            spiller.x = rom.start_posx      # Eendrer x posisjonen til spileren til startposisjnen på nåværende rom
            spiller.y = rom.start_posy      # Eendrer y posisjonen til spileren til startposisjnen på nåværende rom
            spiller.y_fart = 0              # setter y farten til 0
        tegn_brett()                        # kjører funksjonen som tegner brettet

        clock.tick(fps)                     # Får klokka til å gå i tempoet som er bestemt

    pygame.quit()       # Luker programet når While løka stopper

spill() # kjører spilet



# To Do


#to do later
"""
lage brett
flere rom
liv??
moren til jakob
ting
start meny
grafikk
"""