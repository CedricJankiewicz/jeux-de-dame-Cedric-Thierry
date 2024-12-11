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
        if bknd.black_pawn[i].color == "black" and not bknd.black_pawn[i].queen == 1:
            bknd.black_pawn[i].pawn = pawn_black_image

    for i in range (20):
        if bknd.white_pawn[i].color == "white" and not bknd.white_pawn[i].queen == 1:
            bknd.white_pawn[i].pawn = pawn_white_image


def display_queens():
    for i in range (20):
        if bknd.black_pawn[i].queen == 1:
            bknd.black_pawn[i].pawn = pawn_black_queen_image

    for i in range (20):
        if bknd.white_pawn[i].queen == 1:
            bknd.white_pawn[i].pawn = pawn_white_queen_image


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

    for i in range (20):
        if bknd.black_pawn[i].is_in_danger == 1:
            pygame.draw.rect(screen, (0, 255, 100), (bknd.black_pawn[i].x, bknd.black_pawn[i].y, 100, 100), 5)

    for i in range (20):
        if bknd.white_pawn[i].is_in_danger == 1:
            pygame.draw.rect(screen, (0, 255, 100), (bknd.white_pawn[i].x, bknd.white_pawn[i].y, 100, 100), 5)


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
    txt_black_win = font.render(f"{bknd.black_win}", True, (255, 255, 255))
    screen.blit(txt_black_win, (1130, blk_y))
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
    txt_white_win = font.render(f"{bknd.white_win}", True, (255, 255, 255))
    screen.blit(txt_white_win, (1130, wht_y))
    txt_wht_timer = font.render(bknd.white_time, True, (255, 255, 255))
    screen.blit(txt_wht_timer, (1060, (wht_y + 50)))
    txt_wht_remain_pawn = font.render(f"{bknd.white_pawn_left} pawns left", True, (255, 255, 255))
    screen.blit(txt_wht_remain_pawn, (1060, (wht_y + 80)))
    txt_wht_remain_pawn = font.render(f"{bknd.white_pawn_queen} queens", True, (255, 255, 255))
    screen.blit(txt_wht_remain_pawn, (1060, (wht_y + 110)))


def display_title_screen():
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 150)
    tiny_font = pygame.font.Font(None, 50)
    txt_title = font.render("Checkers Game", True, (255, 255, 255))
    screen.blit(txt_title, (100, 100))
    txt_author = tiny_font.render("by Cédric and thierry", True, (255, 255, 255))
    screen.blit(txt_author, (110, 200))
    #blinking text
    current_time = pygame.time.get_ticks()
    if current_time // 500 % 2 == 0:
        txt_press = tiny_font.render("Press any key to continue", True, (255, 255, 255))
    else:
        txt_press = tiny_font.render("Press any key to continue", True, (255, 255, 100))
    screen.blit(txt_press, (110, 300))

    pygame.display.update()


def display_win_screen():
    font = pygame.font.Font(None, 100)
    tiny_font = pygame.font.Font(None, 50)
    txt_wht = font.render("white win", True, (255, 255, 255))
    txt_blk = font.render("black win", True, (255, 255, 255))
    if bknd.black_pawn_left == 18:
        screen.fill((0, 0, 0))
        screen.blit(txt_wht, (110, 100))
    if bknd.white_pawn_left == 18:
        screen.fill((0, 0, 0))
        screen.blit(txt_blk, (110, 100))

    #blinking text
    current_time = pygame.time.get_ticks()
    if current_time // 500 % 2 == 0:
        txt_press = tiny_font.render("Press any key to start a new game", True, (255, 255, 255))
    else:
        txt_press = tiny_font.render("Press any key to start a new game", True, (255, 255, 100))
    screen.blit(txt_press, (110, 200))

    pygame.display.update()


def init():
    bknd.init_pawns()
    pygame.init()


def select_pawns(event):
    bknd.select_pawns(event)
    draw_board()


def move_pawns(event):
    bknd.move_pawns(event)
    draw_board()

def mainloop():
    running = True
    title = True
    while running:
        while title:
            display_title_screen()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    title = False
                elif event.type == pygame.KEYDOWN:
                    title = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    title = False
        if not running:
            break
        draw_board()
        display_info()
        win = bknd.check_win()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                select_pawns(event)
                move_pawns(event)
        pygame.display.update()
        while win:
            display_win_screen()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    win = False
                    running = False
                elif event.type == pygame.KEYDOWN:
                    bknd.restart()
                    win = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    bknd.restart()
                    win = False
    pygame.quit()


screen = pygame.display.set_mode((1410,1010))

#images
pawn_black_image = pygame.image.load(".resources\\MA-24_pion_black.png")
pawn_black_image = pygame.transform.scale(pawn_black_image, (100, 100))

pawn_white_image = pygame.image.load(".resources\\MA-24_pion_white.png")
pawn_white_image = pygame.transform.scale(pawn_white_image, (100, 100))

pawn_black_queen_image = pygame.image.load(".resources\\MA-24_pion_black_queen.png")
pawn_black_queen_image = pygame.transform.scale(pawn_black_queen_image, (100, 100))

pawn_white_queen_image = pygame.image.load(".resources\\MA-24_pion_white_queen.png")
pawn_white_queen_image = pygame.transform.scale(pawn_white_queen_image, (100, 100))
