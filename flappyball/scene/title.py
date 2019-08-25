import sys

import pygame

from flappyball.config import *
from flappyball.scene.game import Game


class Title(object):
    def __init__(self, screen):
        self._screen = screen
        self._font = pygame.font.SysFont(None, title_font_size)
        self._highest_score = 0

    def run(self):
        self._show_title()
        clock = pygame.time.Clock()
        while True:
            clock.tick(game_frame) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit()
                if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    self._highest_score = Game(self._screen, self._highest_score).run()
                    self._show_title()

    def _show_title(self):
        self._screen.fill(game_background_color)
        title_text = self._font.render(game_name, True, text_color)
        self._screen.blit(title_text, (0, 0))
        score_text = self._font.render('highest: ' + str(self._highest_score), True, text_color)
        self._screen.blit(score_text, (0, 20))
        pygame.display.update()
