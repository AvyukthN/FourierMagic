import pygame
import sys
import math

WIDTH, HEIGHT = 1800, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.init()

PI = math.pi

def main():
    angle = 0
    wave = []

    tran1 = WIDTH/8 + 200
    tran2 = HEIGHT/2

    # circle = Circle('circle 1', 20, (WIDTH/8 + 50, HEIGHT/2))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        wave_start = (WIDTH/4) + 400

        screen.fill((0, 0, 0))

        x = 0
        y = 0

        num = 10

        for i in range(num):
            prevx = x
            prevy = y

            n = (i * 2) + 1

            radius = 170 * (4 / (n * PI))
            x += radius * math.cos(n * angle)
            y += radius * math.sin(n * angle)

            pygame.draw.circle(screen, pygame.Color(97, 97, 97), (prevx + (tran1), prevy + (HEIGHT/2)), radius, width = 1)
            pygame.draw.line(screen, "white", (prevx + (tran1), prevy + (HEIGHT/2)), ((x + (tran1)), (y + (HEIGHT/2))), width = 2)
            # pygame.draw.circle(screen, "blue", ((x + (WIDTH/2)), (y + (HEIGHT/2))), 5, width = 0)
            if i == (num - 1):
                pygame.draw.line(screen, "white", ((x + tran1), (y + (HEIGHT/2))), (wave_start, y + (HEIGHT/2)), width = 2)

        wave.insert(0, y)
        if (len(wave) > (WIDTH - wave_start)):
            wave.pop()

        for i in range(len(wave)):
            pygame.draw.circle(screen, "white", ((wave_start + i), (wave[i] + (HEIGHT/2))), 1, width = 0)

        angle += 0.01
     
        pygame.display.update()

"""
class Circle():
    def __init__(self, identifier, radius, center):
        self.identifier = identifier
        self.radius = radius
        self.center = center

        p1 = str(center[0])
        p2 = str(center[1])

        length = 11 + len(p1) + len(p2)

        break_arr = []
        for i in range(length):
            break_arr.append('-')

        self.break_line = ''.join(break_arr)

    def __repr__(self):
        return('\n{}\n{}\nradius {}\ncenter {}'.format(self.identifier.upper(), self.break_line, self.radius, self.center))
"""

if __name__ == '__main__':
    main()

