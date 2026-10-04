import pygame

pygame.init()
pygame.display.set_caption('Rocket In Space')

screen_width = 700
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Images/rocket.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (70,100))
        self.rect = self.image.get_rect() 

    def update(self, pressed_keys):
        if pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0,-5)
        if pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0,5)
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-5,0)
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5,0)

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 700:
            self.rect.right = 700
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= 500:
            self.rect.bottom = 500

sprite = pygame.sprite.Group()

def startgame():
    player = Player()
    sprite.add(player)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        screen.blit(pygame.image.load('Images/space.png'),(0,0))
        sprite.draw(screen)
        pygame.display.update()

startgame()