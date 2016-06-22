#!/usr/bin/env python


import pygame
import pygame.gfxdraw

def main():
    pygame.init()
    win = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Gavolot_Window")
    surf = pygame.Surface(win.get_size(), pygame.SRCALPHA, 32)
    win.blit(surf, (0, 0))
    pygame.display.flip()
    try:
        while 1:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.unicode == 'q':
                    break
            pygame.display.flip()
    finally:
        pygame.quit()

if __name__ == '__main__':
    main()
