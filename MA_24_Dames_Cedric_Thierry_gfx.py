"""
Program name : MA_24_Dames_Cedric_Thierry_gfx.py
Author : Cédric Jankiewicz and Thierry Perroud
Date : 06.12.2024
"""

#import of the backend
import MA_24_Dames_Cedric_Thierry_bknd as bknd

#import of pygame
import pygame


def display_grid():
    location_y = 5
    for i in range(0,5):
        location_x = 5
        for j in range(0,5):
            pygame.draw.rect(screen, (255, 255, 255), (location_x, location_y, 100, 100), 0)
            location_x +=100
            pygame.draw.rect(screen, (150, 150, 150), (location_x, location_y, 100, 100), 0)
            location_x +=100

        location_y += 100
        location_x = 5
        for j in range(0,5):
            pygame.draw.rect(screen, (150, 150, 150), (location_x, location_y, 100, 100), 0)
            location_x +=100
            pygame.draw.rect(screen, (255, 255, 255), (location_x, location_y, 100, 100), 0)
            location_x +=100

        location_y += 100


def display_color():
    for i in range (20):
        if bknd.black_pawn[i].color == "black":
            bknd.black_pawn[i].pawn = pygame.image.load(".resources\\MA-24_pion_black.png")
        bknd.black_pawn[i].pawn = pygame.transform.scale(bknd.black_pawn[i].pawn, (100, 100))

    for i in range (20):
        if bknd.white_pawn[i].color == "white":
            bknd.white_pawn[i].pawn = pygame.image.load(".resources\\MA-24_pion_white.png")
        bknd.white_pawn[i].pawn = pygame.transform.scale(bknd.white_pawn[i].pawn, (100, 100))


def display_queens():
    for i in range (20):
        if bknd.black_pawn[i].queen == 1:
            bknd.black_pawn[i].pawn = pygame.image.load(".resources\\MA-24_pion_black_queen.png")
            bknd.black_pawn[i].pawn = pygame.transform.scale(bknd.black_pawn[i].pawn, (100, 100))

    for i in range (20):
        if bknd.white_pawn[i].queen == 1:
            bknd.white_pawn[i].pawn = pygame.image.load(".resources\\MA-24_pion_white_queen.png")
            bknd.white_pawn[i].pawn = pygame.transform.scale(bknd.white_pawn[i].pawn, (100, 100))


def display_pawns():
    for i in range (20):
        if bknd.black_pawn[i].captured == 0:
            screen.blit(bknd.black_pawn[i].pawn, (bknd.black_pawn[i].x, bknd.black_pawn[i].y))

    for i in range (20):
        if bknd.white_pawn[i].captured == 0:
            screen.blit(bknd.white_pawn[i].pawn, (bknd.white_pawn[i].x, bknd.white_pawn[i].y))


def display_selection():
    for i in range (20):
        if bknd.black_pawn[i].selected == 1:
            pygame.draw.rect(screen, (255, 0, 100), (bknd.black_pawn[i].x, bknd.black_pawn[i].y, 100, 100), 5)

    for i in range (20):
        if bknd.white_pawn[i].selected == 1:
            pygame.draw.rect(screen, (255, 0, 100), (bknd.white_pawn[i].x, bknd.white_pawn[i].y, 100, 100), 5)


def draw_board():
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 1010, 1010))
    display_grid()
    display_queens()
    display_color()
    display_pawns()
    display_selection()


def display_info():
    #reset info side
    pygame.draw.rect(screen, (0, 0, 0), (1010, 10, 400, 1000))

    bknd.timer()
    bknd.check_pawn_left_queen()

    #text font
    font = pygame.font.Font(None, 36)

    #global info
    global_y = 305
    txt_turn = font.render(f"turn {bknd.turn}", True, (255, 255, 255))
    screen.blit(txt_turn, (1060, global_y))


    txt_timer = font.render(bknd.global_time , True, (255, 255, 255))
    screen.blit(txt_timer, (1060, (global_y + 30)))

    #black info
    blk_y = 55
    txt_black = font.render("black", True, (255, 255, 255))
    screen.blit(txt_black, (1060, blk_y))
    txt_blk_timer = font.render(bknd.black_time, True, (255, 255, 255))
    screen.blit(txt_blk_timer, (1060, (blk_y + 50)))
    txt_blk_remain_pawn = font.render(f"{bknd.black_pawn_left} pawns left", True, (255, 255, 255))
    screen.blit(txt_blk_remain_pawn, (1060, (blk_y + 80)))
    txt_blk_remain_pawn = font.render(f"{bknd.black_pawn_queen} queens", True, (255, 255, 255))
    screen.blit(txt_blk_remain_pawn, (1060, (blk_y + 110)))

    #white info
    wht_y = 505
    txt_white = font.render("white", True, (255, 255, 255))
    screen.blit(txt_white, (1060, wht_y))
    txt_wht_timer = font.render(bknd.white_time, True, (255, 255, 255))
    screen.blit(txt_wht_timer, (1060, (wht_y + 50)))
    txt_wht_remain_pawn = font.render(f"{bknd.white_pawn_left} pawns left", True, (255, 255, 255))
    screen.blit(txt_wht_remain_pawn, (1060, (wht_y + 80)))
    txt_wht_remain_pawn = font.render(f"{bknd.white_pawn_queen} queens", True, (255, 255, 255))
    screen.blit(txt_wht_remain_pawn, (1060, (wht_y + 110)))


def win():
    font = pygame.font.Font(None, 50)
    txt_wht = font.render("white win", True, (255, 255, 255))
    txt_blk = font.render("black win", True, (255, 255, 255))
    if bknd.black_pawn_left == 0:
        screen.fill((0, 0, 0))
        screen.blit(txt_wht, (100, 100))
    if bknd.white_pawn_left == 0:
        screen.fill((0, 0, 0))
        screen.blit(txt_blk, (100, 100))


def init():
    bknd.init_pawns()
    pygame.init()
    draw_board()


def select_pawns(event):
    bknd.select_pawns(event, screen)
    draw_board()


def move_pawns(event):
    bknd.move_pawns(event, screen)
    draw_board()


def mainloop():
    running = True
    while running:
        display_info()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                select_pawns(event)
                move_pawns(event)
        pygame.display.update()
    pygame.quit()


screen = pygame.display.set_mode((1410,1010))
