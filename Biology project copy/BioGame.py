import pygame
from sys import exit


lives_lost = 0
level = 1
incorrect_timer = 0
incorrect = False

pygame.mixer.init() 
bg_music = pygame.mixer.Sound('audio/bgmusic.mp3')
bg_music.set_volume(0.5)
answer_sound = pygame.mixer.Sound('audio/answer.mp3')
inc_answer_sound = pygame.mixer.Sound('audio/wrong_answer.mp3')

def display_text(surface, text, pos, font, color):
        collection = [word.split(' ') for word in text.splitlines()]
        space = font.size(' ')[0]
        x,y = pos
        for lines in collection:
            for words in lines:
                word_surface = font.render(words, True, color)
                word_width , word_height = word_surface.get_size()
                if x + word_width >= 800:
                    x = pos[0]
                    y += word_height
                surface.blit(word_surface, (x,y))
                x += word_width + space
            x = pos[0]
            y += word_height


def check(rect, incorrect_rect):
        global level, lives_lost, incorrect
    
        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect.collidepoint(mouse_pos):
                    pygame.mixer.Channel(0).play(answer_sound)
                    level += 1
                elif incorrect_rect.collidepoint(mouse_pos):
                    pygame.mixer.Channel(1).play(inc_answer_sound)
                    incorrect = True
                    lives_lost += 1
                    

# Hearts
class Lives(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        hearts_full = pygame.image.load("graphics/heart1.png")
        hearts_2 = pygame.image.load("graphics/heart2.png")
        hearts_1 = pygame.image.load("graphics/heart3.png")
        hearts_0 = pygame.image.load("graphics/heart4.png")
        self.lives_list = [hearts_full, hearts_2, hearts_1, hearts_0]
        self.image = self.lives_list[0]
        self.rect = self.image.get_rect(center = (700, 20))

    def lose_life(self):
        global lives_lost

        if lives_lost >= 3:
            lives_lost = 3
        self.image = self.lives_list[lives_lost]  

    def update(self):
        self.lose_life()

# Levels
class Level1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("graphics/nasal_cavity.png")
        self.text = "True or false: The respiratory system begins with gas entering the nasal cavity"
        
        self.rect = self.image.get_rect(center = (300, 350))

    def update(self):
        display_text(screen, self.text, (500,80), game_font, 'Black')

class Level2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("graphics/trachea.png")
        self.rect = self.image.get_rect(center = (405, 350))

        self.text = "Does oxygen enter the esophagus or the windpipe?"
        

    def update(self):
        pygame.draw.rect(screen, 'White', [50,60,700,50], 0, 20)
        display_text(screen, self.text, (50,60), game_font, 'Black')

class Level3(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("graphics/bronchi_alveoli.png")
        self.text = "Does oxygen first travel through the bronchi or alveoli?"

        self.rect = self.image.get_rect(center = (410, 350))

    def update(self):
        pygame.draw.rect(screen, 'White', [50,70,700,50], 0, 20)
        display_text(screen, self.text, (50,70), game_font, 'Black')

class Level4(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("graphics/capilliary.png")
        self.text = "It is most likely that oxygen will be..."

        self.rect = self.image.get_rect(center = (400, 350))

    def update(self):
        display_text(screen, self.text, (50,60), game_font, 'Black')

class Level5(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("graphics/tissue_heart.png")
        self.text = "Does oxygen first get tranported to the heart, or tissues?"

        self.rect = self.image.get_rect(center = (400, 390))

    def update(self):
        pygame.draw.rect(screen, 'White', [50,55,700,55], 0, 20)
        display_text(screen, self.text, (50,55), game_font, 'Black')
    
    #used to have function
  

# Questions
class Options1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = game_font.render("True", False, "Black")
        self.incorrect = game_font.render("False", False, "Black")

        self.rect = self.image.get_rect(topleft = (520, 300))
        self.cbox = pygame.rect.Rect([520, 290, 100, 50])
        self.ibox = pygame.rect.Rect([520, 390, 100, 50])
        self.incorrect_rect = self.incorrect.get_rect(topleft = (520, 400))
          

    def update(self):
        #pygame.draw.rect(screen, 'White', )
        #pygame.draw.rect(screen, 'Salmon', self.incorrect_rect)
        screen.blit(self.image, self.rect)
        screen.blit(self.incorrect, self.incorrect_rect)
        check(self.cbox, self.ibox)

class Options2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = game_font.render("Windpipe", False, "Black")
        self.incorrect = game_font.render("Esophagus", False, "Black")

        self.rect = self.image.get_rect(center = (400, 450))
        self.cbox = pygame.rect.Rect([300,425,190,50])
        self.ibox = pygame.rect.Rect([300,150,190,50])
        self.incorrect_rect = self.incorrect.get_rect(center = (400, 170))
    
   
    def update(self):
        pygame.draw.rect(screen, 'White', [300,145,190,50], 0, 5)
        #pygame.draw.rect(screen, 'White', [300,150,190,50], 0, 5)
        screen.blit(self.image, self.rect)
        screen.blit(self.incorrect, self.incorrect_rect)
        check(self.cbox, self.ibox)

class Options3(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = game_font.render("Bronchi", False, "Black")
        self.incorrect = game_font.render("Alveoli", False, "Black")

        self.rect = self.image.get_rect(center = (400, 250))
        self.incorrect_rect = self.incorrect.get_rect(center = (400, 550))
        self.cbox = pygame.rect.Rect([300,225,200,50])
        self.ibox = pygame.rect.Rect([300,525,200,50])

    def update(self):
        pygame.draw.rect(screen, 'White', [300,225,200,50], 0, 10)
        pygame.draw.rect(screen, 'White', [300,525,200,50], 0, 10)
        screen.blit(self.image, self.rect)
        screen.blit(self.incorrect, self.incorrect_rect)
        check(self.cbox, self.ibox)

class Options4(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.incorrect = game_font.render("Dissolved in plasma", False, "Black")
        self.image = game_font.render("Attatched to hemoglobin", False, "Black")

        self.rect = self.image.get_rect(center = (400, 550))
        self.incorrect_rect = self.incorrect.get_rect(center = (400, 450))
        self.cbox = pygame.rect.Rect([225,525,350,50])
        self.ibox = pygame.rect.Rect([225,425,350,50])

    def update(self):
        pygame.draw.rect(screen, 'White', [225,425,350,50], 0, 10)
        pygame.draw.rect(screen, 'White', [225,525,350,50], 0, 10)
        screen.blit(self.image, self.rect)
        screen.blit(self.incorrect, self.incorrect_rect)
        check(self.cbox, self.ibox)

class Options5(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = game_font.render("Tissues", False, "Black")
        self.incorrect = game_font.render("Heart", False, "Black")

        self.rect = self.image.get_rect(center = (400, 225))
        self.incorrect_rect = self.incorrect.get_rect(center = (400, 450))
        self.cbox = pygame.rect.Rect([300,200,200,50])
        self.ibox = pygame.rect.Rect([300,425,200,50])

    def update(self):
        pygame.draw.rect(screen, 'White', [300,200,200,50], 0, 10)
        pygame.draw.rect(screen, 'White', [300,425,200,50], 0, 10)
        screen.blit(self.image, self.rect)
        screen.blit(self.incorrect, self.incorrect_rect)
        check(self.cbox, self.ibox)

# Starting Variables
pygame.init()
screen = pygame.display.set_mode((800, 700))
pygame.display.set_caption('Respiratory Journey')
clock = pygame.time.Clock()
game_active = False
game_font = pygame.font.Font("fonts/VCR_OSD_MONO_1.001 copy.ttf", 30)

#music
pygame.mixer.Channel(2).play(bg_music, -1)

# Groups
levels = pygame.sprite.GroupSingle()
options = pygame.sprite.GroupSingle()
lives = pygame.sprite.GroupSingle()

lives.add(Lives())

# Cursor
pygame.mouse.set_visible(False)
cursor_img = pygame.image.load("graphics/oxygen.png")
cursor_img_scaled = pygame.transform.scale(cursor_img, (60,60))
cursor_img_rect = cursor_img_scaled.get_rect()

# Starting screen
title_surf = game_font.render("Respiratory Journey", False, "Black")
title_surf_scaled = pygame.transform.rotozoom(title_surf, 0, 1.5)
title_rect = title_surf_scaled.get_rect(center = (400, 100))

oxygen_surf = pygame.image.load('graphics/oxygen.png').convert_alpha()
oxygen_surf_scaled = pygame.transform.rotozoom(oxygen_surf, 0, 1.5)
coordinates = (400, 350)
oxygen_surf_rect = oxygen_surf_scaled.get_rect(center = coordinates)

instruct_surf = game_font.render("Press space to start", False, "Black")
instruct_surf_scaled = pygame.transform.rotozoom(instruct_surf, 0, 1.5)
instruct_rect = instruct_surf_scaled.get_rect(center = (400, 600))

# Win screen
win_surf = game_font.render("You Won!", False, "Black")
win_surf_scaled = pygame.transform.scale(win_surf, (600,100))
win_rect = win_surf_scaled.get_rect(center = (400,350))

# Lose screen
lose_surf = game_font.render("You Lost", False, "Salmon")
lose_surf_scaled = pygame.transform.rotozoom(lose_surf, 0, 2)
lose_rect = lose_surf_scaled.get_rect(center = (400, 250))

inst2_surf = game_font.render("Press space to restart", False, "Salmon")
inst2_surf_scaled = pygame.transform.rotozoom(inst2_surf, 0, 1.5)
inst2_rect = inst2_surf_scaled.get_rect(center = (400, 450))

# Post event


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if game_active:
            if lives_lost >= 3:
                game_active = False

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if level != 6:
                    lives_lost = 0
                    level = 1
                    game_active = True

    if game_active:
        if level == 1:
            levels.add(Level1())
            options.add(Options1())

        elif level == 2:
            levels.empty()
            options.empty()

            levels.add(Level2())
            options.add(Options2())
            

        elif level == 3:
            levels.empty()
            options.empty()

            levels.add(Level3())
            options.add(Options3())
          
        elif level == 4:
            levels.empty()
            options.empty()

            levels.add(Level4())
            options.add(Options4())
          

        elif level == 5:
            levels.empty()
            options.empty()

            levels.add(Level5())
            options.add(Options5())


        screen.fill("White")

        levels.draw(screen)
        levels.update()

        options.draw(screen) 
        options.update()
        
        lives.draw(screen)
        lives.update()

        if incorrect and lives_lost < 3:
            if incorrect_timer >= 20:
                incorrect = False
                incorrect_timer = 0
            else: 
                incorrect_timer += 1.8
                screen.fill("Red")

        elif incorrect and lives_lost >= 3:
            incorrect = False

        if lives_lost >= 3:
            game_active = False
        
        if level == 6:
           game_active = False 

    else:
        if lives_lost != 3 and level == 1:
            screen.fill("White")
            screen.blit(title_surf_scaled, title_rect)
            screen.blit(oxygen_surf_scaled, oxygen_surf_rect)
            screen.blit(instruct_surf_scaled, instruct_rect)

        elif lives_lost == 3:
            screen.fill("Black")
            screen.blit(lose_surf_scaled, lose_rect)
            screen.blit(inst2_surf_scaled, inst2_rect)

        elif level == 6:
            screen.fill("White")
            screen.blit(win_surf_scaled, win_rect)

    cursor_img_rect.center = pygame.mouse.get_pos()  # update position 
    screen.blit(cursor_img_scaled, cursor_img_rect)    
    pygame.display.update()
    clock.tick(60)
