import sys
import random
import pygame
from Background import Background
from PipeSet import PipeSet
from Ground import Ground
from Birb import Birb

PIPE_POS_1 = -100
PIPE_POS_2 = -135
PIPE_POS_3 = -180
PIPE_POS_4 = -255
PIPE_POS_5 = -300

position_arr = [
                PIPE_POS_1, PIPE_POS_2,
                PIPE_POS_3, PIPE_POS_4,
                PIPE_POS_5
                ]

pygame.init()
size = width, height = 650, 750
screen = pygame.display.set_mode(size)
cur_time = pygame.time.get_ticks()
clock = pygame.time.Clock()

pipe_group = pygame.sprite.Group()
background_1 = Background(0,0)
background_2 = Background(background_1.rect.right, 0)
floor_1 = Ground(0, 680)
floor_2 = Ground(floor_1.rect.right, 680)
player = Birb(250, 250)

def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.quit(0)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    break


def game_loop():
    # If mode == True --> Allow player to input commands
    # Else --> Don't allow new commands
    mode = True
    show_menu = True
    pipe_counter = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and player.godmode:
                    player.go_up()

                if event.key == pygame.K_s and player.godmode:
                    player.go_down()

                if event.key == pygame.K_d and player.godmode:
                    player.go_right()

                if event.key == pygame.K_a and player.godmode:
                    player.go_left()

                if event.key == pygame.K_SPACE and mode:
                    player.jump()

            if event.type == pygame.KEYUP and player.godmode:
                if event.key == pygame.K_w or event.key == pygame.K_d or event.key == pygame.K_a or event.key == pygame.K_s:
                    player.stop()

        if show_menu:
            main_menu()


        """ Infinite Scrolling Solution """
        pipe_counter = pipe_counter
        rand_pos = random.randint(0, 4)

        if pipe_counter % 165 == 0 and len(pipe_group) < 5:
            pipe_group.add(PipeSet(position_arr[rand_pos]))
            pipe_counter = 0

        pipe_counter += 1

        if background_1.rect.left < -1528:
            background_1.rect.x = background_2.rect.right

        if floor_1.rect.right < 0:
            floor_1.rect.x = floor_2.rect.right

        if background_2.rect.left < -1528:
            background_2.rect.x = background_1.rect.right

        if floor_2.rect.right < 0:
            floor_2.rect.x = floor_1.rect.right


        """ Collison Checking """
        pipe_hit_list = pygame.sprite.spritecollide(player, pipe_group, False)

        if player.rect.centery >= floor_1.rect.top or player.rect.centery >= floor_2.rect.top:
            mode = False
            player.die()

        for each in pipe_hit_list:
            #print(each.rect.top)
            #print(each.rect.bottom)

            if player.rect.centery <= each.rect.top+390 or player.rect.centery >= each.rect.bottom-440:
                mode = False
                player.die()


        """ Sprite Update Methods """
        screen.blit(background_1.image, background_1.rect)
        screen.blit(background_2.image, background_2.rect)
        pipe_group.draw(screen)
        screen.blit(floor_1.image, floor_1.rect)
        screen.blit(floor_2.image, floor_2.rect)
        screen.blit(player.image, player.rect)

        #pygame.draw.circle(screen, [250, 0, 0], [player.rect.centerx + 20, player.rect.centery], 20)

        background_1.update()
        background_2.update()
        pipe_group.update()
        floor_1.update()
        floor_2.update()
        player.update()

        #pygame.draw.circle(screen, [150, 150, 0], [player.rect.centerx, player.rect.centery], 20)

        clock.tick(120)
        pygame.display.flip()

game_loop()
sys.exit(0)
