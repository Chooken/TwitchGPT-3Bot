import random
import pygame, sys
import pmtext.para
import pmtext.util_pygame

draw_group = pygame.sprite.Group()

class Instantiate(pygame.sprite.Sprite):
    def __init__(self, refimage, numOfSprites, aniSpeed):
        super().__init__()
        self.sprites = []

        for imageNum in range(1, numOfSprites -1):
            self.sprites.append(pygame.image.load("Sprites/" + refimage + str(imageNum) + ".png"))

        self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]
        self.rect = self.image.get_rect()
        self.rect.topleft = [0, 0]
        self.animationSpeed = aniSpeed
        draw_group.add(self)

    def update(self):

        self.current_sprite += self.animationSpeed

        if int(self.current_sprite) >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]

class Color():
    PINK = (238, 56, 172)
    GREEN = (65, 238, 172)
    NAVY = (8, 23, 26)
    WHITE = (255, 255, 255)

def tobyMessage(p, name, question, answer):
    t = pmtext.para.Typewriter(p)
    t.color(Color.PINK[0], Color.PINK[1], Color.PINK[2])
    t.string(name + ': ')
    t.color(Color.WHITE[0], Color.WHITE[1], Color.WHITE[2])
    t.string(question)
    t.newline()
    t.newline()
    t.color(Color.GREEN[0], Color.GREEN[1], Color.GREEN[2])
    t.string('TOBY: ')
    t.color(Color.WHITE[0], Color.WHITE[1], Color.WHITE[2])
    t.string(answer)
    return t

def main():

    pygame.init()
    clock = pygame.time.Clock()

    SCREEN_SIZE = width, height = 1920, 1080

    screen = pygame.display.set_mode(SCREEN_SIZE, pygame.FULLSCREEN)

    screen.fill(Color.NAVY)

    # pmtext font
    font = pmtext.util_pygame.TTF('Retrómon.ttf', 80)
    p = pmtext.para.Graph(font)

    t = tobyMessage(p, "TOM", "Whats up?", "i dont funking know")

    Instantiate("THINGY", 14, 1)

    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw_group.draw(screen)

        draw_group.update()
        
        t.pulse()
        t.draw(screen, 730, 130)

        pygame.display.flip()
        clock.tick(10)

if __name__ == "__main__":
    main()

