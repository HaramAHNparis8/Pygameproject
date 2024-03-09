import pygame
import os
import math

from pygame import display



class Galgori(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.rect = image.get_rect(center=position)
        self.original_image =  image
        self.offset = pygame.math.Vector2(default_offset_x_galgori,0)
        self.position = position

        self.direction = LEFT # la direction de gagori
        self.angle_speed = 2.5 #le mouvement de galgori 
        self.angle = 10 #l'angle initiale
        
    def update(self,to_x):
        if self.direction == LEFT:
            self.angle += self.angle_speed
        elif self.direction == RIGHT:
            self.angle -= self.angle_speed
        
        if self.angle > 175:
            self.angle = 175
            self.set_direction(RIGHT)
            self.direction = RIGHT

        elif self.angle < 10:
            self.angle = 10
            self.direction =LEFT
            self.set_direction(LEFT)
            
        self.offset.x += to_x
        self.rotate()
        

    def set_direction(self, direction):
        self.direction = direction
        #print(self.angle, self.direction) #calculer l'angle de galgori
        # rect_center = self.position + self.offset
        # self.rect = self.image.get_rect(center=rect_center)
    def rotate(self):

        self.image = pygame.transform.rotozoom(self.original_image, -self.angle, 1)

        offset_rotated = self.offset.rotate(self.angle)
        #print(offset_rotated)
        self.rect = self.image.get_rect(center=self.position + offset_rotated)
    def draw(self, screen):
         screen.blit(self.image, self.rect)
         #pygame.draw.circle(screen, RED, self.position,3)
         pygame.draw.line(screen,BLACK, self.position, self.rect.center, 5)
    def set_init_state(self):
        self.offset.x = default_offset_x_galgori
        self.angle = 10
        self.direction = LEFT


class Poisson(pygame.sprite.Sprite):
    def __init__(self,image,position,price,speed):
        super().__init__()
        self.image = image
        self.rect = image.get_rect(center=position)
        self.price = price
        self.speed = speed

    def set_position(self, position, angle):
        r = self.rect.size[0] // 2 #pie
        rad_angle = math.radians(angle) #angle
        to_x = r * math.cos(rad_angle) #suface de triologe
        to_y = r * math.sin(rad_angle) # hight de triologe

        self.rect.center = (position[0] + to_x, position[1] + to_y)


def setup_possion():
    poisson_vert, poisson_vitesse = 300, 2
    possion_petit_price,poisson_petit_vitesse = 400, 6
    poisson_moyen_price,poisson_moyen_vitesse = 200, 5
    soju_price,soju_vitesse = 10, 5
    empechement_price, empechement_vitesse = -10, 2
    # small_poisson = (Poisson(les_images[0],(400,700),possion_petit_price,poisson_petit_vitesse))
    # image_group.add(small_poisson)
    image_group.add(Poisson(les_images[0], (400,700),possion_petit_price,poisson_petit_vitesse))
    image_group.add(Poisson(les_images[0], (300,420),possion_petit_price,poisson_petit_vitesse))
    image_group.add(Poisson(les_images[0], (440,500),possion_petit_price,poisson_petit_vitesse))
    image_group.add(Poisson(les_images[0], (500,550),possion_petit_price,poisson_petit_vitesse))
    image_group.add(Poisson(les_images[0], (550,600),possion_petit_price,poisson_petit_vitesse))
    image_group.add(Poisson(les_images[1], (330,500),poisson_moyen_price,poisson_moyen_vitesse))
    image_group.add(Poisson(les_images[2], (390,600),poisson_vert, poisson_vitesse))
    image_group.add(Poisson(les_images[2], (200,600),poisson_vert, poisson_vitesse))
    image_group.add(Poisson(les_images[3], (900,420),possion_petit_price,poisson_petit_vitesse))
    image_group.add(Poisson(les_images[4], (330,540),soju_price,soju_vitesse))
    image_group.add(Poisson(les_images[4], (800,540),soju_price,soju_vitesse))
    image_group.add(Poisson(les_images[4], (800,510),soju_price,soju_vitesse))
    image_group.add(Poisson(les_images[4], (950,500),soju_price,soju_vitesse))
    image_group.add(Poisson(les_images[4], (1000,500),soju_price,soju_vitesse))
    image_group.add(Poisson(les_images[5], (700,620),empechement_price, empechement_vitesse))
    image_group.add(Poisson(les_images[5], (740,530),empechement_price, empechement_vitesse))
    image_group.add(Poisson(les_images[5], (780,630),empechement_price, empechement_vitesse))
    image_group.add(Poisson(les_images[5], (660,620),empechement_price, empechement_vitesse))
    image_group.add(Poisson(les_images[5], (680,640),empechement_price, empechement_vitesse))
    image_group.add(Poisson(les_images[5], (680,500),empechement_price, empechement_vitesse))
    image_group.add(Poisson(les_images[5], (680,450),empechement_price, empechement_vitesse))
   


def update_score(score):
    global curr_score
    curr_score += score
def display_score():
    txt_curr_score = game_font.render(f"le point courrant :{curr_score:,}", True, RED)
    screen.blit(txt_curr_score,(50,20))

    txt_goal_score = game_font.render(f"le point goal : {goal_score:,}",True, RED)
    screen.blit(txt_goal_score,(50,80))
def display_time(time):
    txt_timer = game_font.render(f"Le temps : {time}", True, RED)
    screen.blit(txt_timer,(1000,40))

def display_game_over():
    game_font = pygame.font.SysFont('verdana',60)
    tex_game_over = game_font.render(game_result, True, RED)
    screen.blit(tex_game_over,(500,500))


pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("séoulien")
game_font = pygame.font.SysFont('verdana', 30)

# les valeurs de points
goal_score = 1500
curr_score = 0

# les résultats
game_result = None
total_time = 30
start_ticks = pygame.time.get_ticks()

#le valeur concernant jeu
default_offset_x_galgori = 40
to_x = 0 #bouger le galgori avec le standard du valeur de X
pris_poisson = None #mémoriser les poissons pris

#la vitesse
move_speed = 12
return_speed = 20

LEFT = -1
STOP = 0 # stopper les galgori
RIGHT = 1

RED = (250,0,0)
BLACK =(0,0,0)
clock = pygame.time.Clock()
#appeler background
current_path = os.path.dirname(__file__)
background =pygame.image.load(os.path.join(current_path,"background_modifi_size.gif"))
running = True
#appeler les images(poission,empêchement)
les_images =[
    pygame.image.load(os.path.join(current_path,"possion_puple_resize_25x25.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_path,"poisson_resize_45x45.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_path,"poisson_resize_160x160.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_path,"poisson_orange_resize_35x35.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_path,"soju_screen.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_path,"empechement.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_path,"personnage.png")).convert_alpha()]

image_group = pygame.sprite.Group()
#appeler les images(des poissons, empêchement)
setup_possion()

galgori_image = pygame.image.load(os.path.join(current_path,"galgori_re.png")).convert_alpha()
galgori = Galgori(galgori_image,(1100, 420))
character = pygame.image.load(os.path.join(current_path,"personnage.png"))
#character = pygame.image.load("/Users/anharam/Desktop/Pygame/personnage.png")
# character_size = character.get_rect().size
# character_width = character_size[0]
# character_height = character_size[1]



while running:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            galgori.set_direction(STOP)
            to_x = move_speed #bouger avec la vitesse du valeur de méthode

    if galgori.rect.left < 0 or galgori.rect.right > screen_width or galgori.rect.bottom > screen_height:
        to_x = - return_speed
    
    if galgori.offset.x < default_offset_x_galgori:
        to_x = 0
        galgori.set_init_state()

        if pris_poisson:
            update_score(pris_poisson.price)
            image_group.remove(pris_poisson)
            pris_poisson = None

    #la collusion
    if not pris_poisson:
        for Poisson in image_group:
            if pygame.sprite.collide_mask(galgori,Poisson):
                pris_poisson = Poisson
                pris_poisson = Poisson # les informations de poisson pris
                to_x = -Poisson.speed
                break
    if pris_poisson:
        pris_poisson.set_position(galgori.rect.center, galgori.angle)





    screen.blit(background,(0,0))

    screen.blit(character,(1095,405))

    galgori.update(to_x)
    galgori.draw(screen)
    image_group.draw(screen) # dessiner les sprites sur l'écran

    #montrer les points gangné
    display_score()
    
    #calculer le temps
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    display_time(total_time - int(elapsed_time))

    if total_time - int(elapsed_time) <= 0:
        running = False
        if curr_score >= goal_score:
            game_result = "FÉlicit!"

        else:
            game_result = "Game Over"
        
        # afficher les messages de jeu
        display_game_over()



    pygame.display.update()
pygame.time.delay(2000)
pygame.quit()