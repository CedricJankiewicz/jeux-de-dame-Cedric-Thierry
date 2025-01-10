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
    """
    display the grid with white and gray square
    """
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
    """
    display pawn with their color black or white
    """
    if not konami:
        for i in range (20):
            if bknd.black_pawn[i].color == "black" and not bknd.black_pawn[i].queen == 1:
                bknd.black_pawn[i].pawn = pawn_black_image

        for i in range (20):
            if bknd.white_pawn[i].color == "white" and not bknd.white_pawn[i].queen == 1:
                bknd.white_pawn[i].pawn = pawn_white_image
    else:
        current_time = pygame.time.get_ticks()
        for i in range(20):
            if bknd.black_pawn[i].color == "black" and not bknd.black_pawn[i].queen == 1:
                for c, pawn in enumerate(bknd.black_pawn):
                    color_index = (current_time // 100 + c) % len(black_rainbow)
                    bknd.black_pawn[i].pawn = black_rainbow[color_index]

        for i in range(20):
            if bknd.white_pawn[i].color == "white" and not bknd.white_pawn[i].queen == 1:
                for c, pawn in enumerate(bknd.white_pawn):
                    color_index = (current_time // 100 + c) % len(white_rainbow)
                    bknd.white_pawn[i].pawn = white_rainbow[color_index]


def display_queens():
    """
    if the pawn is a queen change the texture of the pawn with a new one
    """
    if not konami:
        for i in range (20):
            if bknd.black_pawn[i].queen == 1:
                bknd.black_pawn[i].pawn = pawn_black_queen_image

        for i in range (20):
            if bknd.white_pawn[i].queen == 1:
                bknd.white_pawn[i].pawn = pawn_white_queen_image
    else:
        current_time = pygame.time.get_ticks()
        for i in range(20):
            if bknd.black_pawn[i].queen == 1:
                for c, pawn in enumerate(bknd.black_pawn):
                    color_index = (current_time // 100 + c) % len(black_rainbow)
                    bknd.black_pawn[i].pawn = black_queen_rainbow[color_index]

        for i in range(20):
            if bknd.white_pawn[i].queen == 1:
                for c, pawn in enumerate(bknd.white_pawn):
                    color_index = (current_time // 100 + c) % len(white_rainbow)
                    bknd.white_pawn[i].pawn = white_queen_rainbow[color_index]


def display_pawns():
    """
    display the pawn if they are not captured if they are they'll be hide
    """
    for i in range (20):
        if bknd.black_pawn[i].captured == 0:
            screen.blit(bknd.black_pawn[i].pawn, (bknd.black_pawn[i].x, bknd.black_pawn[i].y))

    for i in range (20):
        if bknd.white_pawn[i].captured == 0:
            screen.blit(bknd.white_pawn[i].pawn, (bknd.white_pawn[i].x, bknd.white_pawn[i].y))


def display_selection():
    """
    display a square around the pawn if selected
    """
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

    for i in range (20):
        if bknd.black_pawn[i].is_jumped == 1:
            pygame.draw.rect(screen, (0, 0, 255), (bknd.black_pawn[i].x, bknd.black_pawn[i].y, 100, 100), 5)

    for i in range (20):
        if bknd.white_pawn[i].is_jumped == 1:
            pygame.draw.rect(screen, (0, 0, 255), (bknd.white_pawn[i].x, bknd.white_pawn[i].y, 100, 100), 5)


def draw_board():
    """
    clear the screen and put every thing back
    """
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 1010, 1010))
    display_grid()
    display_queens()
    display_color()
    display_pawns()
    display_selection()


def display_info():
    """
    display info on the side of the screen
    """
    #reset info side
    pygame.draw.rect(screen, (0, 0, 0), (1010, 10, 400, 1000))

    pygame.time.delay(10)
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

    #manoury notation
    manoury_y = 710
    txt_manoury_title = font.render("Manoury Notation", True, (255, 255, 255))
    screen.blit(txt_manoury_title, (1060, manoury_y-50))
    if len(bknd.manoury) > 9:
        bknd.manoury.pop(0)
    for i in range(len(bknd.manoury)):
        if not i == len(bknd.manoury)-1:
            txt_manoury = font.render(f"{bknd.manoury[i]}", True, (255, 255, 255))
            screen.blit(txt_manoury, (1060, manoury_y+30*i))
        else:
            txt_manoury = font.render(f"{bknd.manoury[i]}", True, (255, 255, 100))
            screen.blit(txt_manoury, (1060, manoury_y+30*i))


def display_title_screen():
    """
    display the title screen with a blinking text
    """
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 150)
    tiny_font = pygame.font.Font(None, 50)
    txt_title = font.render("Checkers Game", True, (255, 255, 255))
    screen.blit(txt_title, (100, 100))
    txt_author = tiny_font.render("by Cédric and Thierry", True, (255, 255, 255))
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
    """
    display the win screen with a blinking text and change the message depending on which one win
    """
    font = pygame.font.Font(None, 100)
    tiny_font = pygame.font.Font(None, 50)
    txt_wht = font.render("white win", True, (255, 255, 255))
    txt_blk = font.render("black win", True, (255, 255, 255))
    if bknd.winner == "white":
        screen.fill((0, 0, 0))
        screen.blit(txt_wht, (110, 100))
    if bknd.winner == "black":
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
    """
    initialise everything
    """
    bknd.init_pawns()
    pygame.init()


def select_pawns(event):
    """
    allow the player to select a pawn and draw the board after it
    """
    bknd.select_pawns(event)
    draw_board()


def move_pawns(event):
    """
    allow the player to move a pawn and draw the board after it
    """
    bknd.move_pawns(event)
    draw_board()


def mainloop():
    """
    make the mainloop for the window and detect input
    """
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
            #input for easter egg
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    bknd.input_konami.append("up")
                elif event.key == pygame.K_DOWN:
                    bknd.input_konami.append("down")
                elif event.key == pygame.K_LEFT:
                    bknd.input_konami.append("left")
                elif event.key == pygame.K_RIGHT:
                    bknd.input_konami.append("right")
                elif event.key == pygame.K_a:
                    bknd.input_konami.append("a")
                elif event.key == pygame.K_b:
                    bknd.input_konami.append("b")
                elif event.key == pygame.K_RETURN:
                    global konami
                    konami = bknd.detect_for_konami()
                elif event.key == pygame.K_p:
                    bknd.make_selected_to_queen()
                elif event.key == pygame.K_o:
                    bknd.capture_selected()

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


#game window
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

#easter egg
konami = False

pawn_white_red_image = pygame.image.load(".resources\\rainbow\\MA-24_pion_white_red.png")
pawn_white_red_image = pygame.transform.scale(pawn_white_red_image, (100, 100))

pawn_white_orange_image = pygame.image.load(".resources\\rainbow\\MA-24_pion_white_orange.png")
pawn_white_orange_image = pygame.transform.scale(pawn_white_orange_image, (100, 100))

pawn_white_yellow_image = pygame.image.load(".resources\\rainbow\\MA-24_pion_white_yellow.png")
pawn_white_yellow_image = pygame.transform.scale(pawn_white_yellow_image, (100, 100))

pawn_white_green_image = pygame.image.load(".resources\\rainbow\\MA-24_pion_white_green.png")
pawn_white_green_image = pygame.transform.scale(pawn_white_green_image, (100, 100))

pawn_white_blue_image = pygame.image.load(".resources\\rainbow\\MA-24_pion_white_blue.png")
pawn_white_blue_image = pygame.transform.scale(pawn_white_blue_image, (100, 100))

pawn_white_purple_image = pygame.image.load(".resources\\rainbow\\MA-24_pion_white_purple.png")
pawn_white_purple_image = pygame.transform.scale(pawn_white_purple_image, (100, 100))

white_rainbow =[pawn_white_red_image,pawn_white_orange_image,pawn_white_yellow_image,
                pawn_white_green_image,pawn_white_blue_image,pawn_white_purple_image]

pawn_black_red_image = pygame.image.load(".resources\\rainbow\\MA-24_pion_black_red.png")
pawn_black_red_image = pygame.transform.scale(pawn_black_red_image, (100, 100))

pawn_black_orange_image = pygame.image.load(".resources\\rainbow\\MA-24_pion_black_orange.png")
pawn_black_orange_image = pygame.transform.scale(pawn_black_orange_image, (100, 100))

pawn_black_yellow_image = pygame.image.load(".resources\\rainbow\\MA-24_pion_black_yellow.png")
pawn_black_yellow_image = pygame.transform.scale(pawn_black_yellow_image, (100, 100))

pawn_black_green_image = pygame.image.load(".resources\\rainbow\\MA-24_pion_black_green.png")
pawn_black_green_image = pygame.transform.scale(pawn_black_green_image, (100, 100))

pawn_black_blue_image = pygame.image.load(".resources\\rainbow\\MA-24_pion_black_blue.png")
pawn_black_blue_image = pygame.transform.scale(pawn_black_blue_image, (100, 100))

pawn_black_purple_image = pygame.image.load(".resources\\rainbow\\MA-24_pion_black_purple.png")
pawn_black_purple_image = pygame.transform.scale(pawn_black_purple_image, (100, 100))

black_rainbow =[pawn_black_red_image,pawn_black_orange_image,pawn_black_yellow_image,
                pawn_black_green_image,pawn_black_blue_image,pawn_black_purple_image]

pawn_white_queen_red_image = pygame.image.load(".resources\\rainbow\\MA-24_pion_white_queen_red.png")
pawn_white_queen_red_image = pygame.transform.scale(pawn_white_queen_red_image, (100, 100))

pawn_white_queen_orange_image = pygame.image.load(".resources\\rainbow\\MA-24_pion_white_queen_orange.png")
pawn_white_queen_orange_image = pygame.transform.scale(pawn_white_queen_orange_image, (100, 100))

pawn_white_queen_yellow_image = pygame.image.load(".resources\\rainbow\\MA-24_pion_white_queen_yellow.png")
pawn_white_queen_yellow_image = pygame.transform.scale(pawn_white_queen_yellow_image, (100, 100))

pawn_white_queen_green_image = pygame.image.load(".resources\\rainbow\\MA-24_pion_white_queen_green.png")
pawn_white_queen_green_image = pygame.transform.scale(pawn_white_queen_green_image, (100, 100))

pawn_white_queen_blue_image = pygame.image.load(".resources\\rainbow\\MA-24_pion_white_queen_blue.png")
pawn_white_queen_blue_image = pygame.transform.scale(pawn_white_queen_blue_image, (100, 100))

pawn_white_queen_purple_image = pygame.image.load(".resources\\rainbow\\MA-24_pion_white_queen_purple.png")
pawn_white_queen_purple_image = pygame.transform.scale(pawn_white_queen_purple_image, (100, 100))

white_queen_rainbow =[pawn_white_queen_red_image,pawn_white_queen_orange_image,pawn_white_queen_yellow_image,
                pawn_white_queen_green_image,pawn_white_queen_blue_image,pawn_white_queen_purple_image]

pawn_black_queen_red_image = pygame.image.load(".resources\\rainbow\\MA-24_pion_black_queen_red.png")
pawn_black_queen_red_image = pygame.transform.scale(pawn_black_queen_red_image, (100, 100))

pawn_black_queen_orange_image = pygame.image.load(".resources\\rainbow\\MA-24_pion_black_queen_orange.png")
pawn_black_queen_orange_image = pygame.transform.scale(pawn_black_queen_orange_image, (100, 100))

pawn_black_queen_yellow_image = pygame.image.load(".resources\\rainbow\\MA-24_pion_black_queen_yellow.png")
pawn_black_queen_yellow_image = pygame.transform.scale(pawn_black_queen_yellow_image, (100, 100))

pawn_black_queen_green_image = pygame.image.load(".resources\\rainbow\\MA-24_pion_black_queen_green.png")
pawn_black_queen_green_image = pygame.transform.scale(pawn_black_queen_green_image, (100, 100))

pawn_black_queen_blue_image = pygame.image.load(".resources\\rainbow\\MA-24_pion_black_queen_blue.png")
pawn_black_queen_blue_image = pygame.transform.scale(pawn_black_queen_blue_image, (100, 100))

pawn_black_queen_purple_image = pygame.image.load(".resources\\rainbow\\MA-24_pion_black_queen_purple.png")
pawn_black_queen_purple_image = pygame.transform.scale(pawn_black_queen_purple_image, (100, 100))

black_queen_rainbow =[pawn_black_queen_red_image,pawn_black_queen_orange_image,pawn_black_queen_yellow_image,
                pawn_black_queen_green_image,pawn_black_queen_blue_image,pawn_black_queen_purple_image]