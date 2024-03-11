import sys
import cv2
import pygame

screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
def test_mode_main():
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, int(screen_height * 0.05))
    loading_text = font.render("it works", True, (255, 255, 255))