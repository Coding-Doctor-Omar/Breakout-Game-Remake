import pygame

pygame.mixer.init()

ball_hit = pygame.mixer.Sound(file="sound_effects/ball_hit.mp3")
lose_life = pygame.mixer.Sound(file="sound_effects/lose_life.mp3")
lose_game = pygame.mixer.Sound(file="sound_effects/game_over.mp3")
win_game = pygame.mixer.Sound(file="sound_effects/win_game_classic.mp3")

def play_bounce_sound():
    ball_hit.play()

def play_life_deduction_sound():
    lose_life.play()

def play_lose_game_sound():
    lose_game.play()

def play_win_game_sound():
    win_game.play()