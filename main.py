#!/usr/bin/env python3

import sys
import random
import pygame
from sprites import *

pygame.init()

PIPE_POS_1 = -100
PIPE_POS_2 = -135
PIPE_POS_3 = -180
PIPE_POS_4 = -255
PIPE_POS_5 = -300
PIPE_POS_6 = -80
PIPE_POS_7 = -335
PIPE_POS_8 = -200

position_arr = [
                PIPE_POS_1, PIPE_POS_2,
                PIPE_POS_3, PIPE_POS_4,
                PIPE_POS_5, PIPE_POS_6,
                PIPE_POS_7, PIPE_POS_8
                ]

size = width, height = 650, 750
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

font = pygame.font.Font('assets/OCRA.ttf', 24)

pipe_group = pygame.sprite.Group()
background_1 = Background(0,0)
background_2 = Background(background_1.rect.right, 0)
floor_1 = Ground(0, 680)
floor_2 = Ground(floor_1.rect.right, 680)
player = Birb()

def main_menu():
    pipe = Pipe()
    logo = Logo()
    player._set_position(100, 250)
    player.menu = True
    intro_label = font.render("Press Enter to Start", True, (70, 84, 65))

    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event is None:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    intro = False

        screen.blit(background_1.image, background_1.rect)
        screen.blit(player.image, player.rect)
        screen.blit(pipe.image, pipe.rect)
        screen.blit(floor_1.image, floor_1.rect)
        screen.blit(logo.image, logo.rect)
        screen.blit(intro_label, (10, 500))
        logo.update()
        player.update()
        clock.tick(15)
        pygame.display.flip()

    player.menu = False


def game_loop():
    # If mode == True --> Allow player to input commands
    # Else --> Don't allow new commands
    score = 0
    mode = True
    pipe_counter = 0

    player._set_position(153, 250)

    while True:

        """  Event Checking   """
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event == None:
                pygame.quit()
                sys.exit(0)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and player._godmode:
                    player.go_up()

                elif event.key == pygame.K_s and player._godmode:
                    player.go_down()

                elif event.key == pygame.K_d and player._godmode:
                    player.go_right()

                elif event.key == pygame.K_a and player._godmode:
                    player.go_left()

                if event.key == pygame.K_SPACE and mode and not player._godmode:
                    player.jump()

            if event.type == pygame.KEYUP and player._godmode:
                player.stop()

        """ Infinite Scrolling Solution """
        pipe_counter = pipe_counter
        rand_pos = random.randint(0, 7)

        # Spawn a pipeset every 165 frames as long as < 5 exist
        if pipe_counter % 115 == 0 and len(pipe_group) <= 3:
            pipe_group.add(PipeSet(position_arr[rand_pos]))
            pipe_counter = 0

        pipe_counter += 1

        # If background 1's position is less than the left bound of the
        # screen + its width --> set background 1 as the child of background 2
        if background_1.rect.left < -1528:
            background_1.rect.x = background_2.rect.right

        if floor_1.rect.right < 0:
            floor_1.rect.x = floor_2.rect.right

        # If background 2's position is less than the left bound of the
        # screen + its width --> set background 2 as the child of background 1
        if background_2.rect.left < -1528:
            background_2.rect.x = background_1.rect.right

        if floor_2.rect.right < 0:
            floor_2.rect.x = floor_1.rect.right


        """ Collison Checking """
        pipe_hit_list = pygame.sprite.spritecollide(player, pipe_group, False)

        # If player hits the floor or the top of the screen --> kill the player
        if player.rect.centery >= (floor_1.rect.top + 150) or player.rect.centery >= floor_2.rect.top:
            mode = False
            player.die()

        for each in pipe_hit_list:
            # If the player is not within the middle section of the pipe and
            # the player hits a pipe --> kill the player
            if player.rect.centery <= each.rect.top+390 or player.rect.centery >= each.rect.bottom-440:
                mode = False
                player.die()

            # If the player passes the right edge of a pipe without dying
            # increase the score by 1
            # The plus three is the last point before the next iteration of pipe starts
            if player.rect.x + 3 == each.rect.right and player.alive:
                score += 1

        """  Score Update   """
        score_label = font.render("Score: "+str(score), True, (70, 84, 65))

        """ Sprite Update Methods """
        screen.blit(background_1.image, background_1.rect)
        screen.blit(background_2.image, background_2.rect)
        pipe_group.draw(screen)
        screen.blit(floor_1.image, floor_1.rect)
        screen.blit(floor_2.image, floor_2.rect)
        screen.blit(player.image, player.rect)
        screen.blit(score_label, (50, 50))

        # If player has hit a pipe and is dead --> rotate the image as it falls
        if not player.alive:
            player.image = pygame.transform.rotate(player.image, -1.75)

        background_1.update()
        background_2.update()
        pipe_group.update()
        floor_1.update()
        floor_2.update()
        player.update()

        clock.tick(60)
        pygame.display.flip()

main_menu()
game_loop()
