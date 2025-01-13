"""
Program name : MA_24_Dames_Cedric_Thierry_bknd.py
Author : Cédric Jankiewicz and Thierry Perroud
Date : 06.12.2024
"""


class Pawn:
    x = 0
    y = 0
    color = ""
    selected = 0
    pawn = None
    is_jumped = 0
    captured = 0
    queen = 0
    has_to_move = 0
    force_select = 0
    is_in_danger = 0
    locked_direction = ""
    pawn_to_capture_distance = 0


    def __init__(self, x=0, y=0, color="black"):
        self.x = x
        self.y = y
        self.color = color


    def change_to_queen(self):
        if self.color == "black":
            if 895 <= self.y <= 905:
                self.queen = 1
        if self.color == "white":
            if 0 <= self.y <= 10:
                self.queen = 1


    def move_up_left(self):
        if self.x > 5 and self.y > 5:
            self.x -= 100
            self.y -= 100


    def move_up_right(self):
        if self.x < 905 and self.y > 5:
            self.x += 100
            self.y -= 100


    def move_down_left(self):
        if self.x > 5 and self.y < 905:
            self.x -= 100
            self.y += 100


    def move_down_right(self):
        if self.x < 905 and self.y < 905:
            self.x += 100
            self.y += 100


    def select_pawn(self, event):
        check_all_pawns_for_capture()

        if self.x <= event.pos[0] <= self.x + 100 and self.y <= event.pos[1] <= self.y + 100:
            black_force_capture = False
            white_force_capture = False

            if self.captured == 1:
                return

            for i in range(20):
                if black_pawn[i].force_select == 1 or white_pawn[i].force_select == 1:
                    return

                if black_pawn[i].is_in_danger == 1 or white_pawn[i].is_in_danger == 1:
                    return

                if black_pawn[i].has_to_move == 1 and not black_force_capture:
                    black_force_capture = True

                if white_pawn[i].has_to_move == 1 and not white_force_capture:
                    white_force_capture = True

            if self.selected == 0:
                if (self.color == "black" and self.has_to_move == 0 and black_force_capture or
                    self.color == "white" and self.has_to_move == 0 and white_force_capture):

                    return

                unselect_all()
                self.selected = 1

            else:
                self.selected = 0


    def move_pawn(self, event):
        global turn

        has_captured = 0

        if self.selected:
            if self.queen == 0:
                if self.x - 100 <= event.pos[0] <= self.x and self.y - 100 <= event.pos[1] <= self.y:
                    can_capture = check_if_pawn_can_capture_directly(self, "up_left", event)
                    can_capture_elsewhere = check_if_pawn_can_capture_elsewhere(self, "up_left", event)

                    if self.color == "black":
                        if not can_capture:
                            return

                        elif can_capture:
                            for i in range (20):
                                if (white_pawn[i].x <= event.pos[0] <= white_pawn[i].x + 100 and
                                    white_pawn[i].y <= event.pos[1] <= white_pawn[i].y + 100 and
                                    white_pawn[i].captured == 0 and white_pawn[i].is_jumped == 0):

                                    white_pawn[i].is_jumped = 1
                                    start = (self.x, self.y)
                                    self.move_up_left()
                                    self.move_up_left()
                                    end = (self.x, self.y)
                                    show_capture(start,end,self.color)
                                    has_captured = 1
                                    break

                            if has_captured == 1:
                                can_capture_again = check_if_pawn_can_capture_again(self, "up_left", event)

                                if can_capture_again:
                                    self.force_select = 1

                                if not can_capture_again:
                                    self.selected = 0
                                    self.force_select = 0
                                    change_to_queen()

                                    for i in range(20):
                                        if white_pawn[i].is_jumped == 1:
                                            white_pawn[i].is_jumped = 0
                                            white_pawn[i].captured = 1

                                    turn += 1

                            return

                    elif self.color == "white":
                        if can_capture:
                            for i in range(20):
                                if (black_pawn[i].x <= event.pos[0] <= black_pawn[i].x + 100 and
                                    black_pawn[i].y <= event.pos[1] <= black_pawn[i].y + 100 and
                                    black_pawn[i].captured == 0 and black_pawn[i].is_jumped == 0):

                                    black_pawn[i].is_jumped = 1
                                    start = (self.x, self.y)
                                    self.move_up_left()
                                    self.move_up_left()
                                    end = (self.x, self.y)
                                    show_capture(start, end, self.color)
                                    has_captured = 1
                                    break

                            if has_captured == 1:
                                can_capture_again = check_if_pawn_can_capture_again(self, "up_left", event)

                                if can_capture_again:
                                    self.force_select = 1

                                if not can_capture_again:
                                    self.selected = 0
                                    self.force_select = 0
                                    change_to_queen()

                                    for i in range(20):
                                        if black_pawn[i].is_jumped == 1:
                                            black_pawn[i].is_jumped = 0
                                            black_pawn[i].captured = 1

                                    turn += 1

                            return

                        elif not can_capture:
                            if can_capture_elsewhere:
                                return

                            for i in range(20):
                                if (black_pawn[i].x <= event.pos[0] <= black_pawn[i].x + 100 and
                                    black_pawn[i].y <= event.pos[1] <= black_pawn[i].y + 100 and
                                    black_pawn[i].captured == 0):

                                    return

                    start = (self.x, self.y)
                    self.selected = 0
                    self.move_up_left()
                    end = (self.x, self.y)
                    show_move(start, end, self.color)
                    change_to_queen()
                    turn += 1

                if self.x + 100 <= event.pos[0] <= self.x + 200 and self.y - 100 <= event.pos[1] <= self.y:
                    can_capture = check_if_pawn_can_capture_directly(self, "up_right", event)
                    can_capture_elsewhere = check_if_pawn_can_capture_elsewhere(self, "up_right", event)

                    if self.color == "black":
                        if not can_capture:
                            return

                        elif can_capture:
                            for i in range (20):
                                if (white_pawn[i].x <= event.pos[0] <= white_pawn[i].x + 100 and
                                    white_pawn[i].y <= event.pos[1] <= white_pawn[i].y + 100 and
                                    white_pawn[i].captured == 0 and white_pawn[i].is_jumped == 0):

                                    white_pawn[i].is_jumped = 1
                                    start = (self.x, self.y)
                                    self.move_up_right()
                                    self.move_up_right()
                                    end = (self.x, self.y)
                                    show_capture(start, end, self.color)
                                    has_captured = 1
                                    break

                            if has_captured == 1:
                                can_capture_again = check_if_pawn_can_capture_again(self, "up_right", event)

                                if can_capture_again:
                                    self.force_select = 1

                                if not can_capture_again:
                                    self.selected = 0
                                    self.force_select = 0
                                    change_to_queen()

                                    for i in range(20):
                                        if white_pawn[i].is_jumped == 1:
                                            white_pawn[i].is_jumped = 0
                                            white_pawn[i].captured = 1

                                    turn += 1

                            return

                    elif self.color == "white":
                        if can_capture:
                            for i in range(20):
                                if (black_pawn[i].x <= event.pos[0] <= black_pawn[i].x + 100 and
                                    black_pawn[i].y <= event.pos[1] <= black_pawn[i].y + 100 and
                                    black_pawn[i].captured == 0 and black_pawn[i].is_jumped == 0):

                                    black_pawn[i].is_jumped = 1
                                    start = (self.x, self.y)
                                    self.move_up_right()
                                    self.move_up_right()
                                    end = (self.x, self.y)
                                    show_capture(start, end, self.color)
                                    has_captured = 1
                                    break

                            if has_captured == 1:
                                can_capture_again = check_if_pawn_can_capture_again(self, "up_right", event)

                                if can_capture_again:
                                    self.force_select = 1

                                if not can_capture_again:
                                    self.selected = 0
                                    self.force_select = 0
                                    change_to_queen()

                                    for i in range(20):
                                        if black_pawn[i].is_jumped == 1:
                                            black_pawn[i].is_jumped = 0
                                            black_pawn[i].captured = 1

                                    turn += 1

                            return

                        elif not can_capture:
                            if can_capture_elsewhere:
                                return

                            for i in range(20):
                                if (black_pawn[i].x <= event.pos[0] <= black_pawn[i].x + 100 and
                                    black_pawn[i].y <= event.pos[1] <= black_pawn[i].y + 100 and
                                    black_pawn[i].captured == 0):
                                    return

                    self.selected = 0
                    start = (self.x, self.y)
                    self.move_up_right()
                    change_to_queen()
                    end = (self.x, self.y)
                    show_move(start, end, self.color)
                    turn += 1

                if self.x - 100 <= event.pos[0] <= self.x and self.y + 100 <= event.pos[1] <= self.y + 200:
                    can_capture = check_if_pawn_can_capture_directly(self, "down_left", event)
                    can_capture_elsewhere = check_if_pawn_can_capture_elsewhere(self, "down_left", event)

                    if self.color == "white":
                        if not can_capture:
                            return

                        elif can_capture:
                            for i in range (20):
                                if (black_pawn[i].x <= event.pos[0] <= black_pawn[i].x + 100 and
                                    black_pawn[i].y <= event.pos[1] <= black_pawn[i].y + 100 and
                                    black_pawn[i].captured == 0 and black_pawn[i].is_jumped == 0):

                                    black_pawn[i].is_jumped = 1
                                    start = (self.x, self.y)
                                    self.move_down_left()
                                    self.move_down_left()
                                    end = (self.x, self.y)
                                    show_capture(start, end, self.color)
                                    has_captured = 1
                                    break

                            if has_captured == 1:
                                can_capture_again = check_if_pawn_can_capture_again(self, "down_left", event)

                                if can_capture_again:
                                    self.force_select = 1

                                if not can_capture_again:
                                    self.selected = 0
                                    self.force_select = 0
                                    change_to_queen()

                                    for i in range(20):
                                        if black_pawn[i].is_jumped == 1:
                                            black_pawn[i].is_jumped = 0
                                            black_pawn[i].captured = 1

                                    turn += 1

                            return

                    elif self.color == "black":
                        if can_capture:
                            for i in range(20):
                                if (white_pawn[i].x <= event.pos[0] <= white_pawn[i].x + 100 and
                                    white_pawn[i].y <= event.pos[1] <= white_pawn[i].y + 100 and
                                    white_pawn[i].captured == 0 and white_pawn[i].is_jumped == 0):

                                    white_pawn[i].is_jumped = 1
                                    start = (self.x, self.y)
                                    self.move_down_left()
                                    self.move_down_left()
                                    end = (self.x, self.y)
                                    show_capture(start, end, self.color)
                                    has_captured = 1
                                    break

                            if has_captured == 1:
                                can_capture_again = check_if_pawn_can_capture_again(self, "down_left", event)

                                if can_capture_again:
                                    self.force_select = 1

                                if not can_capture_again:
                                    self.selected = 0
                                    self.force_select = 0
                                    change_to_queen()

                                    for i in range(20):
                                        if white_pawn[i].is_jumped == 1:
                                            white_pawn[i].is_jumped = 0
                                            white_pawn[i].captured = 1

                                    turn += 1

                            return

                        elif not can_capture:
                            if can_capture_elsewhere:
                                return

                            for i in range(20):
                                if (white_pawn[i].x <= event.pos[0] <= white_pawn[i].x + 100 and
                                    white_pawn[i].y <= event.pos[1] <= white_pawn[i].y + 100 and
                                    white_pawn[i].captured == 0):

                                    return

                    self.selected = 0
                    start = (self.x, self.y)
                    self.move_down_left()
                    end = (self.x, self.y)
                    show_move(start, end, self.color)
                    change_to_queen()
                    turn += 1

                if self.x + 100 <= event.pos[0] <= self.x + 200 and self.y + 100 <= event.pos[1] <= self.y + 200:
                    can_capture = check_if_pawn_can_capture_directly(self, "down_right", event)
                    can_capture_elsewhere = check_if_pawn_can_capture_elsewhere(self, "down_right", event)

                    if self.color == "white":
                        if not can_capture:
                            return

                        elif can_capture:
                            for i in range (20):
                                if (black_pawn[i].x <= event.pos[0] <= black_pawn[i].x + 100 and
                                    black_pawn[i].y <= event.pos[1] <= black_pawn[i].y + 100 and
                                    black_pawn[i].captured == 0 and black_pawn[i].is_jumped == 0):

                                    black_pawn[i].is_jumped = 1
                                    start = (self.x, self.y)
                                    self.move_down_right()
                                    self.move_down_right()
                                    end = (self.x, self.y)
                                    show_capture(start, end, self.color)
                                    has_captured = 1
                                    break

                            if has_captured == 1:
                                can_capture_again = check_if_pawn_can_capture_again(self, "down_right", event)

                                if can_capture_again:
                                    self.force_select = 1

                                if not can_capture_again:
                                    self.selected = 0
                                    self.force_select = 0
                                    change_to_queen()

                                    for i in range(20):
                                        if black_pawn[i].is_jumped == 1:
                                            black_pawn[i].is_jumped = 0
                                            black_pawn[i].captured = 1

                                    turn += 1

                            return

                    elif self.color == "black":
                        if can_capture:
                            for i in range(20):
                                if (white_pawn[i].x <= event.pos[0] <= white_pawn[i].x + 100 and
                                    white_pawn[i].y <= event.pos[1] <= white_pawn[i].y + 100 and
                                    white_pawn[i].captured == 0 and white_pawn[i].is_jumped == 0):

                                    white_pawn[i].is_jumped = 1
                                    start = (self.x, self.y)
                                    self.move_down_right()
                                    self.move_down_right()
                                    end = (self.x, self.y)
                                    show_capture(start, end, self.color)
                                    has_captured = 1
                                    break

                            if has_captured == 1:
                                can_capture_again = check_if_pawn_can_capture_again(self, "down_right", event)

                                if can_capture_again:
                                    self.force_select = 1

                                if not can_capture_again:
                                    self.selected = 0
                                    self.force_select = 0
                                    change_to_queen()

                                    for i in range(20):
                                        if white_pawn[i].is_jumped == 1:
                                            white_pawn[i].is_jumped = 0
                                            white_pawn[i].captured = 1

                                    turn += 1

                            return

                        elif not can_capture:
                            if can_capture_elsewhere:
                                return

                            for i in range(20):
                                if (white_pawn[i].x <= event.pos[0] <= white_pawn[i].x + 100 and
                                    white_pawn[i].y <= event.pos[1] <= white_pawn[i].y + 100 and
                                    white_pawn[i].captured == 0):

                                    return

                    self.selected = 0
                    start = (self.x, self.y)
                    self.move_down_right()
                    change_to_queen()
                    end = (self.x, self.y)
                    show_move(start, end, self.color)
                    turn += 1

            if self.queen == 1:
                pos_x = self.x + 50
                pos_y = self.y + 50
                loops = 0
                ignore = False
                ignored = 0

                if event.pos[0] <= self.x and event.pos[1] <= self.y:
                    if (self.locked_direction == "up_right" or self.locked_direction == "down_left" or
                        self.locked_direction == "down_right"):

                        return

                    while 0 <= pos_x - 100 and 0 <= pos_y - 100:
                        pos_x -= 100
                        pos_y -= 100
                        loops += 1
                        pawn_hit = check_for_pawn_in_the_way(self, pos_x, pos_y)

                        if pos_x <= event.pos[0] <= pos_x + 100 and pos_y <= event.pos[1] <= pos_y + 100:
                            if self.pawn_to_capture_distance != 0:
                                if loops < self.pawn_to_capture_distance:
                                    return

                                elif loops > self.pawn_to_capture_distance:
                                    if not pawn_hit:
                                        queen_capture(self, loops)
                                        can_capture_again = check_if_queen_can_capture_again(self)

                                        if can_capture_again:
                                            self.force_select = 1

                                        elif not can_capture_again:
                                            self.selected = 0
                                            self.force_select = 0

                                            for i in range(20):
                                                if white_pawn[i].is_jumped == 1:
                                                    white_pawn[i].is_jumped = 0
                                                    white_pawn[i].captured = 1

                                                if black_pawn[i].is_jumped == 1:
                                                    black_pawn[i].is_jumped = 0
                                                    black_pawn[i].captured = 1

                                            turn += 1

                                        return

                            can_capture = check_if_pawn_can_capture_directly(self, "up_left", event)

                            if pawn_hit and can_capture and ignored == 0:
                                select_pawn_in_danger(self, "up_left", loops, event)
                                break

                            elif pawn_hit and not can_capture:
                                break

                            if ignored == 1:
                                break

                            if self.force_select == 1:
                                break

                            if self.has_to_move == 1:
                                break

                            self.selected = 0

                            start = (self.x, self.y)
                            for i in range(loops):
                                self.move_up_left()
                            end = (self.x, self.y)
                            show_move(start, end, self.color)
                            turn += 1
                            break

                        for i in range(20):
                            if (black_pawn[i].is_in_danger == 1 and loops <= self.pawn_to_capture_distance or
                                white_pawn[i].is_in_danger == 1 and loops <= self.pawn_to_capture_distance):

                                ignore = True
                                ignored = 1

                        if pawn_hit and not ignore:
                            break

                if self.x + 100 <= event.pos[0] and event.pos[1] <= self.y:
                    if (self.locked_direction == "up_left" or self.locked_direction == "up_left" or
                        self.locked_direction == "down_right"):

                        return

                    while pos_x + 100 <= 1010 and 0 <= pos_y - 100:
                        pos_x += 100
                        pos_y -= 100
                        loops += 1
                        pawn_hit = check_for_pawn_in_the_way(self, pos_x, pos_y)

                        if pos_x <= event.pos[0] <= pos_x + 100 and pos_y <= event.pos[1] <= pos_y + 100:
                            if self.pawn_to_capture_distance != 0:
                                if loops < self.pawn_to_capture_distance:
                                    return

                                elif loops > self.pawn_to_capture_distance:
                                    if not pawn_hit:
                                        queen_capture(self, loops)
                                        can_capture_again = check_if_queen_can_capture_again(self)

                                        if can_capture_again:
                                            self.force_select = 1

                                        elif not can_capture_again:
                                            self.selected = 0
                                            self.force_select = 0

                                            for i in range(20):
                                                if white_pawn[i].is_jumped == 1:
                                                    white_pawn[i].is_jumped = 0
                                                    white_pawn[i].captured = 1

                                                if black_pawn[i].is_jumped == 1:
                                                    black_pawn[i].is_jumped = 0
                                                    black_pawn[i].captured = 1

                                            turn += 1

                                        return

                            can_capture = check_if_pawn_can_capture_directly(self, "up_right", event)

                            if pawn_hit and can_capture and ignored == 0:
                                select_pawn_in_danger(self, "up_right", loops, event)
                                break

                            elif pawn_hit and not can_capture:
                                break

                            if ignored == 1:
                                break

                            if self.force_select == 1:
                                break

                            if self.has_to_move == 1:
                                break

                            self.selected = 0

                            start = (self.x, self.y)
                            for i in range(loops):
                                self.move_up_right()
                            end = (self.x, self.y)
                            show_move(start, end, self.color)
                            turn += 1
                            break

                        for i in range(20):
                            if (black_pawn[i].is_in_danger == 1 and loops <= self.pawn_to_capture_distance or
                                white_pawn[i].is_in_danger == 1 and loops <= self.pawn_to_capture_distance):

                                ignore = True
                                ignored = 1

                        if pawn_hit and not ignore:
                            break

                if event.pos[0] <= self.x and self.y + 100 <= event.pos[1]:
                    if (self.locked_direction == "up_left" or self.locked_direction == "up_right" or
                        self.locked_direction == "down_right"):

                        return

                    while 0 <= pos_x - 100 and pos_y + 100 <= 1010:
                        pos_x -= 100
                        pos_y += 100
                        loops += 1
                        pawn_hit = check_for_pawn_in_the_way(self, pos_x, pos_y)

                        if pos_x <= event.pos[0] <= pos_x + 100 and pos_y <= event.pos[1] <= pos_y + 100:
                            if self.pawn_to_capture_distance != 0:
                                if loops < self.pawn_to_capture_distance:
                                    return

                                elif loops > self.pawn_to_capture_distance:
                                    if not pawn_hit:
                                        queen_capture(self, loops)
                                        can_capture_again = check_if_queen_can_capture_again(self)

                                        if can_capture_again:
                                            self.force_select = 1

                                        elif not can_capture_again:
                                            self.selected = 0
                                            self.force_select = 0

                                            for i in range(20):
                                                if white_pawn[i].is_jumped == 1:
                                                    white_pawn[i].is_jumped = 0
                                                    white_pawn[i].captured = 1

                                                if black_pawn[i].is_jumped == 1:
                                                    black_pawn[i].is_jumped = 0
                                                    black_pawn[i].captured = 1

                                            turn += 1

                                        return

                            can_capture = check_if_pawn_can_capture_directly(self, "down_left", event)

                            if pawn_hit and can_capture and ignored == 0:
                                select_pawn_in_danger(self, "down_left", loops, event)
                                break

                            elif pawn_hit and not can_capture:
                                break

                            if ignored == 1:
                                break

                            if self.force_select == 1:
                                break

                            if self.has_to_move == 1:
                                break

                            self.selected = 0

                            start = (self.x, self.y)
                            for i in range(loops):
                                self.move_down_left()
                            end = (self.x, self.y)
                            show_move(start, end, self.color)

                            turn += 1
                            break

                        for i in range(20):
                            if (black_pawn[i].is_in_danger == 1 and loops <= self.pawn_to_capture_distance or
                                white_pawn[i].is_in_danger == 1 and loops <= self.pawn_to_capture_distance):

                                ignore = True
                                ignored = 1

                        if pawn_hit and not ignore:
                            break

                if self.x + 100 <= event.pos[0] and self.y + 100 <= event.pos[1]:
                    if (self.locked_direction == "up_left" or self.locked_direction == "up_right" or
                        self.locked_direction == "down_left"):

                        return

                    while pos_x + 100 <= 1010 and pos_y + 100 <= 1010:
                        pos_x += 100
                        pos_y += 100
                        loops += 1
                        pawn_hit = check_for_pawn_in_the_way(self, pos_x, pos_y)

                        if pos_x <= event.pos[0] <= pos_x + 100 and pos_y <= event.pos[1] <= pos_y + 100:
                            if self.pawn_to_capture_distance != 0:
                                if loops < self.pawn_to_capture_distance:
                                    return

                                elif loops > self.pawn_to_capture_distance:
                                    if not pawn_hit:
                                        queen_capture(self, loops)
                                        can_capture_again = check_if_queen_can_capture_again(self)

                                        if can_capture_again:
                                            self.force_select = 1

                                        elif not can_capture_again:
                                            self.selected = 0
                                            self.force_select = 0

                                            for i in range(20):
                                                if white_pawn[i].is_jumped == 1:
                                                    white_pawn[i].is_jumped = 0
                                                    white_pawn[i].captured = 1

                                                if black_pawn[i].is_jumped == 1:
                                                    black_pawn[i].is_jumped = 0
                                                    black_pawn[i].captured = 1

                                            turn += 1

                                        return

                            can_capture = check_if_pawn_can_capture_directly(self, "down_right", event)

                            if pawn_hit and can_capture and ignored == 0:
                                select_pawn_in_danger(self, "down_right", loops, event)
                                break

                            elif pawn_hit and not can_capture:
                                break

                            if ignored == 1:
                                break

                            if self.force_select == 1:
                                break

                            if self.has_to_move == 1:
                                break

                            self.selected = 0

                            start = (self.x, self.y)
                            for i in range(loops):
                                self.move_down_right()
                            end = (self.x, self.y)
                            show_move(start, end, self.color)
                            turn += 1
                            break

                        for i in range(20):
                            if (black_pawn[i].is_in_danger == 1 and loops <= self.pawn_to_capture_distance or
                                white_pawn[i].is_in_danger == 1 and loops <= self.pawn_to_capture_distance):

                                ignore = True
                                ignored = 1

                        if pawn_hit and not ignore:
                            break


def timer():
    global global_mill_sec_time, global_sec_time, global_min_time, global_time,\
        black_mill_sec_time, black_sec_time, black_min_time, black_time,\
        white_mill_sec_time, white_sec_time, white_min_time, white_time,\
        turn

    if global_mill_sec_time >= 99:
        global_mill_sec_time = 0
        global_sec_time += 1
        if global_sec_time > 59:
            global_sec_time = 0
            global_min_time += 1
    else:
        global_mill_sec_time += 1

    global_time = f"{global_min_time:02d}:{global_sec_time:02d}:{global_mill_sec_time:02d}"

    if turn % 2 == 0:
        if black_mill_sec_time >= 99:
            black_mill_sec_time = 0
            black_sec_time += 1
            if black_sec_time > 59:
                black_sec_time = 0
                black_min_time += 1
        else:
            black_mill_sec_time += 1

    black_time = f"{black_min_time:02d}:{black_sec_time:02d}:{black_mill_sec_time:02d}"

    if turn % 2 == 1:
        if white_mill_sec_time >= 99:
            white_mill_sec_time = 0
            white_sec_time += 1
            if white_sec_time > 59:
                white_sec_time = 0
                white_min_time += 1
        else:
            white_mill_sec_time += 1

    white_time = f"{white_min_time:02d}:{white_sec_time:02d}:{white_mill_sec_time:02d}"


def check_pawn_left_queen():
    global black_pawn_left,white_pawn_left,black_pawn_queen,white_pawn_queen
    black_pawn_left = 20
    white_pawn_left = 20
    for i in range(20):
        if white_pawn[i].captured == 1:
            white_pawn_left -= 1

        if black_pawn[i].captured == 1:
            black_pawn_left -= 1
    black_pawn_queen = 0
    white_pawn_queen = 0
    for i in range(20):
        if white_pawn[i].queen == 1 and not white_pawn[i].captured == 1:
            white_pawn_queen += 1

        if black_pawn[i].queen == 1 and not black_pawn[i].captured == 1:
            black_pawn_queen += 1


def unselect_all():
    for i in range (20):
        black_pawn[i].selected = 0

    for i in range (20):
        white_pawn[i].selected = 0


def init_black_pawns(x, y, low_range, high_range):
    for i in range(low_range, high_range):
        black_pawn[i] = Pawn(x, y, "black")
        x += 200


def init_white_pawns(x, y, low_range, high_range):
    for i in range(low_range, high_range):
        white_pawn[i] = Pawn(x, y, "white")
        x += 200


def init_pawns():
    init_black_pawns(105, 5, 0, 5)
    init_black_pawns(5, 105, 5, 10)
    init_black_pawns(105, 205, 10, 15)
    init_black_pawns(5, 305, 15, 20)

    init_white_pawns(105, 605, 0, 5)
    init_white_pawns(5, 705, 5, 10)
    init_white_pawns(105, 805, 10, 15)
    init_white_pawns(5, 905, 15, 20)


def select_pawns(event):
    if turn % 2 == 0:
        for i in range (20):
            black_pawn[i].select_pawn(event)
    if turn % 2 == 1:
        for i in range (20):
            white_pawn[i].select_pawn(event)


def move_pawns(event):
    for i in range (20):
        black_pawn[i].move_pawn(event)

    for i in range (20):
        white_pawn[i].move_pawn(event)


def check_if_pawn_can_capture_directly(pawn, attempted_move, event):
    can_capture = False

    for i in range(20):
        if pawn.color == "black":
            if (white_pawn[i].x <= event.pos[0] <= white_pawn[i].x + 100 and
                white_pawn[i].y <= event.pos[1] <= white_pawn[i].y + 100 and
                white_pawn[i].captured == 0 and white_pawn[i].is_jumped == 0):

                if attempted_move == "up_left":
                    can_capture = check_if_pawn_can_capture(-100, -100, event)
                    break
                elif attempted_move == "up_right":
                    can_capture = check_if_pawn_can_capture(100, -100, event)
                    break
                elif attempted_move == "down_left":
                    can_capture = check_if_pawn_can_capture(-100, 100, event)
                    break
                elif attempted_move == "down_right":
                    can_capture = check_if_pawn_can_capture(100, 100, event)
                    break

        elif pawn.color == "white":
            if (black_pawn[i].x <= event.pos[0] <= black_pawn[i].x + 100 and
                black_pawn[i].y <= event.pos[1] <= black_pawn[i].y + 100 and
                black_pawn[i].captured == 0 and black_pawn[i].is_jumped == 0):

                if attempted_move == "up_left":
                    can_capture = check_if_pawn_can_capture(-100, -100, event)
                    break
                elif attempted_move == "up_right":
                    can_capture = check_if_pawn_can_capture(100, -100, event)
                    break
                elif attempted_move == "down_left":
                    can_capture = check_if_pawn_can_capture(-100, 100, event)
                    break
                elif attempted_move == "down_right":
                    can_capture = check_if_pawn_can_capture(100, 100, event)
                    break

    return can_capture


def check_if_pawn_can_capture_elsewhere(pawn, attempted_move, event):
    can_capture = False

    if attempted_move == "up_left":
        if pawn.color == "black":
            for i in range(20):
                if (white_pawn[i].x <= event.pos[0] + 200 <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] <= white_pawn[i].y + 100 and
                    white_pawn[i].captured == 0 and white_pawn[i].is_jumped == 0):

                    can_capture = check_if_pawn_can_capture(300, -100, event)
                    if can_capture:
                        break

                if (white_pawn[i].x <= event.pos[0] <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] + 200 <= white_pawn[i].y + 100 and
                    white_pawn[i].captured == 0 and white_pawn[i].is_jumped == 0):

                    can_capture = check_if_pawn_can_capture(-100, 300, event)
                    if can_capture:
                        break

                if (white_pawn[i].x <= event.pos[0] + 200 <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] + 200 <= white_pawn[i].y + 100 and
                    white_pawn[i].captured == 0 and white_pawn[i].is_jumped == 0):

                    can_capture = check_if_pawn_can_capture(300, 300, event)
                    if can_capture:
                        break

        elif pawn.color == "white":
            for i in range(20):
                if (black_pawn[i].x <= event.pos[0] + 200 <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] <= black_pawn[i].y + 100 and
                    black_pawn[i].captured == 0 and black_pawn[i].is_jumped == 0):

                    can_capture = check_if_pawn_can_capture(300, -100, event)
                    if can_capture:
                        break

                if (black_pawn[i].x <= event.pos[0] <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] + 200 <= black_pawn[i].y + 100 and
                    black_pawn[i].captured == 0 and black_pawn[i].is_jumped == 0):

                    can_capture = check_if_pawn_can_capture(-100, 300, event)
                    if can_capture:
                        break

                if (black_pawn[i].x <= event.pos[0] + 200 <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] + 200 <= black_pawn[i].y + 100 and
                    black_pawn[i].captured == 0 and black_pawn[i].is_jumped == 0):

                    can_capture = check_if_pawn_can_capture(300, 300, event)
                    if can_capture:
                        break

    if attempted_move == "up_right":
        if pawn.color == "black":
            for i in range(20):
                if (white_pawn[i].x <= event.pos[0] - 200 <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] <= white_pawn[i].y + 100 and
                    white_pawn[i].captured == 0 and white_pawn[i].is_jumped == 0):

                    can_capture = check_if_pawn_can_capture(-300, -100, event)
                    if can_capture:
                        break

                if (white_pawn[i].x <= event.pos[0] - 200 <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] + 200 <= white_pawn[i].y + 100 and
                    white_pawn[i].captured == 0 and white_pawn[i].is_jumped == 0):

                    can_capture = check_if_pawn_can_capture(-300, 300, event)
                    if can_capture:
                        break

                if (white_pawn[i].x <= event.pos[0] <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] + 200 <= white_pawn[i].y + 100 and
                    white_pawn[i].captured == 0 and white_pawn[i].is_jumped == 0):

                    can_capture = check_if_pawn_can_capture(100, 300, event)
                    if can_capture:
                        break

        elif pawn.color == "white":
            for i in range(20):
                if (black_pawn[i].x <= event.pos[0] - 200 <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] <= black_pawn[i].y + 100 and
                    black_pawn[i].captured == 0 and black_pawn[i].is_jumped == 0):

                    can_capture = check_if_pawn_can_capture(-300, -100, event)
                    if can_capture:
                        break

                if (black_pawn[i].x <= event.pos[0] - 200 <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] + 200 <= black_pawn[i].y + 100 and
                    black_pawn[i].captured == 0 and black_pawn[i].is_jumped == 0):

                    can_capture = check_if_pawn_can_capture(-300, 300, event)
                    if can_capture:
                        break

                if (black_pawn[i].x <= event.pos[0] <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] + 200 <= black_pawn[i].y + 100 and
                    black_pawn[i].captured == 0 and black_pawn[i].is_jumped == 0):

                    can_capture = check_if_pawn_can_capture(100, 300, event)
                    if can_capture:
                        break

    if attempted_move == "down_left":
        if pawn.color == "black":
            for i in range(20):
                if (white_pawn[i].x <= event.pos[0] <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] - 200 <= white_pawn[i].y + 100 and
                    white_pawn[i].captured == 0 and white_pawn[i].is_jumped == 0):

                    can_capture = check_if_pawn_can_capture(-100, -300, event)
                    if can_capture:
                        break

                if (white_pawn[i].x <= event.pos[0] + 200 <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] - 200 <= white_pawn[i].y + 100 and
                    white_pawn[i].captured == 0 and white_pawn[i].is_jumped == 0):

                    can_capture = check_if_pawn_can_capture(300, -300, event)
                    if can_capture:
                        break

                if (white_pawn[i].x <= event.pos[0] + 200 <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] <= white_pawn[i].y + 100 and
                    white_pawn[i].captured == 0 and white_pawn[i].is_jumped == 0):

                    can_capture = check_if_pawn_can_capture(300, 100, event)
                    if can_capture:
                        break

        elif pawn.color == "white":
            for i in range(20):
                if (black_pawn[i].x <= event.pos[0] <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] - 200 <= black_pawn[i].y + 100 and
                    black_pawn[i].captured == 0 and black_pawn[i].is_jumped == 0):

                    can_capture = check_if_pawn_can_capture(-100, -300, event)
                    if can_capture:
                        break

                if (black_pawn[i].x <= event.pos[0] + 200 <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] - 200 <= black_pawn[i].y + 100 and
                    black_pawn[i].captured == 0 and black_pawn[i].is_jumped == 0):

                    can_capture = check_if_pawn_can_capture(300, -300, event)
                    if can_capture:
                        break

                if (black_pawn[i].x <= event.pos[0] + 200 <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] <= black_pawn[i].y + 100 and
                    black_pawn[i].captured == 0 and black_pawn[i].is_jumped == 0):

                    can_capture = check_if_pawn_can_capture(300, 100, event)
                    if can_capture:
                        break

    if attempted_move == "down_right":
        if pawn.color == "black":
            for i in range(20):
                if (white_pawn[i].x <= event.pos[0] - 200 <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] - 200 <= white_pawn[i].y + 100 and
                    white_pawn[i].captured == 0 and white_pawn[i].is_jumped == 0):

                    can_capture = check_if_pawn_can_capture(-300, -300, event)
                    if can_capture:
                        break

                if (white_pawn[i].x <= event.pos[0] <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] - 200 <= white_pawn[i].y + 100 and
                    white_pawn[i].captured == 0 and white_pawn[i].is_jumped == 0):

                    can_capture = check_if_pawn_can_capture(100, -300, event)
                    if can_capture:
                        break

                if (white_pawn[i].x <= event.pos[0] - 200 <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] <= white_pawn[i].y + 100 and
                    white_pawn[i].captured == 0 and white_pawn[i].is_jumped == 0):

                    can_capture = check_if_pawn_can_capture(-300, 100, event)
                    if can_capture:
                        break

        elif pawn.color == "white":
            for i in range(20):
                if (black_pawn[i].x <= event.pos[0] - 200 <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] - 200 <= black_pawn[i].y + 100 and
                    black_pawn[i].captured == 0 and black_pawn[i].is_jumped == 0):

                    can_capture = check_if_pawn_can_capture(-300, -300, event)
                    if can_capture:
                        break

                if (black_pawn[i].x <= event.pos[0] <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] - 200 <= black_pawn[i].y + 100 and
                    black_pawn[i].captured == 0 and black_pawn[i].is_jumped == 0):

                    can_capture = check_if_pawn_can_capture(100, -300, event)
                    if can_capture:
                        break

                if (black_pawn[i].x <= event.pos[0] - 200 <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] <= black_pawn[i].y + 100 and
                    black_pawn[i].captured == 0 and black_pawn[i].is_jumped == 0):

                    can_capture = check_if_pawn_can_capture(-300, 100, event)
                    if can_capture:
                        break

    return can_capture


def check_if_pawn_can_capture(pos_x, pos_y, event):
    if event is not None:
        for i in range(20):
            if (not (5 <= event.pos[0] + pos_x <= 1005) or not (5 <= event.pos[1] + pos_y <= 1005) or
                black_pawn[i].x <= event.pos[0] + pos_x <= black_pawn[i].x + 100 and
                black_pawn[i].y <= event.pos[1] + pos_y <= black_pawn[i].y + 100 and black_pawn[i].captured == 0 or
                white_pawn[i].x <= event.pos[0] + pos_x <= white_pawn[i].x + 100 and
                white_pawn[i].y <= event.pos[1] + pos_y <= white_pawn[i].y + 100 and white_pawn[i].captured == 0):

                return False

    elif event is None:
        for i in range(20):
            if (not (5 <= pos_x <= 1005) or not (5 <= pos_y <= 1005) or
                black_pawn[i].x <= pos_x <= black_pawn[i].x + 100 and
                black_pawn[i].y <= pos_y <= black_pawn[i].y + 100 and black_pawn[i].captured == 0 or
                white_pawn[i].x <= pos_x <= white_pawn[i].x + 100 and
                white_pawn[i].y <= pos_y <= white_pawn[i].y + 100 and white_pawn[i].captured == 0):

                return False

    return True


def check_if_pawn_can_capture_again(pawn, previous_move, event):
    can_capture_again = False

    if previous_move == "up_left":
        if pawn.color == "black":
            for i in range(20):
                if (white_pawn[i].x <= event.pos[0] - 200 <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] - 200 <= white_pawn[i].y + 100 and
                    white_pawn[i].captured == 0 and white_pawn[i].is_jumped == 0):

                    can_capture_again = check_if_pawn_can_capture(-300, -300, event)
                    if can_capture_again:
                        break

                if (white_pawn[i].x <= event.pos[0] <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] - 200 <= white_pawn[i].y + 100 and
                    white_pawn[i].captured == 0 and white_pawn[i].is_jumped == 0):

                    can_capture_again = check_if_pawn_can_capture(100, -300, event)
                    if can_capture_again:
                        break

                if (white_pawn[i].x <= event.pos[0] - 200 <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] <= white_pawn[i].y + 100 and
                    white_pawn[i].captured == 0 and white_pawn[i].is_jumped == 0):

                    can_capture_again = check_if_pawn_can_capture(-300, 100, event)
                    if can_capture_again:
                        break

        elif pawn.color == "white":
            for i in range(20):
                if (black_pawn[i].x <= event.pos[0] - 200 <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] - 200 <= black_pawn[i].y + 100 and
                    black_pawn[i].captured == 0 and black_pawn[i].is_jumped == 0):

                    can_capture_again = check_if_pawn_can_capture(-300, -300, event)
                    if can_capture_again:
                        break

                if (black_pawn[i].x <= event.pos[0] <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] - 200 <= black_pawn[i].y + 100 and
                    black_pawn[i].captured == 0 and black_pawn[i].is_jumped == 0):

                    can_capture_again = check_if_pawn_can_capture(100, -300, event)
                    if can_capture_again:
                        break

                if (black_pawn[i].x <= event.pos[0] - 200 <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] <= black_pawn[i].y + 100 and
                    black_pawn[i].captured == 0 and black_pawn[i].is_jumped == 0):

                    can_capture_again = check_if_pawn_can_capture(-300, 100, event)
                    if can_capture_again:
                        break

    elif previous_move == "up_right":
        if pawn.color == "black":
            for i in range(20):
                if (white_pawn[i].x <= event.pos[0] <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] - 200 <= white_pawn[i].y + 100 and
                    white_pawn[i].captured == 0 and white_pawn[i].is_jumped == 0):

                    can_capture_again = check_if_pawn_can_capture(-100, -300, event)
                    if can_capture_again:
                        break

                if (white_pawn[i].x <= event.pos[0] + 200 <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] - 200 <= white_pawn[i].y + 100 and
                    white_pawn[i].captured == 0 and white_pawn[i].is_jumped == 0):

                    can_capture_again = check_if_pawn_can_capture(300, -300, event)
                    if can_capture_again:
                        break

                if (white_pawn[i].x <= event.pos[0] + 200 <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] <= white_pawn[i].y + 100 and
                    white_pawn[i].captured == 0 and white_pawn[i].is_jumped == 0):

                    can_capture_again = check_if_pawn_can_capture(300, 100, event)
                    if can_capture_again:
                        break

        elif pawn.color == "white":
            for i in range(20):
                if (black_pawn[i].x <= event.pos[0] <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] - 200 <= black_pawn[i].y + 100 and
                    black_pawn[i].captured == 0 and black_pawn[i].is_jumped == 0):

                    can_capture_again = check_if_pawn_can_capture(-100, -300, event)
                    if can_capture_again:
                        break

                if (black_pawn[i].x <= event.pos[0] + 200 <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] - 200 <= black_pawn[i].y + 100 and
                    black_pawn[i].captured == 0 and black_pawn[i].is_jumped == 0):

                    can_capture_again = check_if_pawn_can_capture(300, -300, event)
                    if can_capture_again:
                        break

                if (black_pawn[i].x <= event.pos[0] + 200 <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] <= black_pawn[i].y + 100 and
                    black_pawn[i].captured == 0 and black_pawn[i].is_jumped == 0):

                    can_capture_again = check_if_pawn_can_capture(300, 100, event)
                    if can_capture_again:
                        break

    elif previous_move == "down_left":
        if pawn.color == "black":
            for i in range(20):
                if (white_pawn[i].x <= event.pos[0] - 200 <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] <= white_pawn[i].y + 100 and
                    white_pawn[i].captured == 0 and white_pawn[i].is_jumped == 0):

                    can_capture_again = check_if_pawn_can_capture(-300, -100, event)
                    if can_capture_again:
                        break

                if (white_pawn[i].x <= event.pos[0] - 200 <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] + 200 <= white_pawn[i].y + 100 and
                    white_pawn[i].captured == 0 and white_pawn[i].is_jumped == 0):

                    can_capture_again = check_if_pawn_can_capture(-300, 300, event)
                    if can_capture_again:
                        break

                if (white_pawn[i].x <= event.pos[0] <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] + 200 <= white_pawn[i].y + 100 and
                    white_pawn[i].captured == 0 and white_pawn[i].is_jumped == 0):

                    can_capture_again = check_if_pawn_can_capture(100, 300, event)
                    if can_capture_again:
                        break

        elif pawn.color == "white":
            for i in range(20):
                if (black_pawn[i].x <= event.pos[0] - 200 <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] <= black_pawn[i].y + 100 and
                    black_pawn[i].captured == 0 and black_pawn[i].is_jumped == 0):

                    can_capture_again = check_if_pawn_can_capture(-300, -100, event)
                    if can_capture_again:
                        break

                if (black_pawn[i].x <= event.pos[0] - 200 <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] + 200 <= black_pawn[i].y + 100 and
                    black_pawn[i].captured == 0 and black_pawn[i].is_jumped == 0):

                    can_capture_again = check_if_pawn_can_capture(-300, 300, event)
                    if can_capture_again:
                        break

                if (black_pawn[i].x <= event.pos[0] <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] + 200 <= black_pawn[i].y + 100 and
                    black_pawn[i].captured == 0 and black_pawn[i].is_jumped == 0):

                    can_capture_again = check_if_pawn_can_capture(100, 300, event)
                    if can_capture_again:
                        break

    elif previous_move == "down_right":
        if pawn.color == "black":
            for i in range(20):
                if (white_pawn[i].x <= event.pos[0] + 200 <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] <= white_pawn[i].y + 100 and
                    white_pawn[i].captured == 0 and white_pawn[i].is_jumped == 0):

                    can_capture_again = check_if_pawn_can_capture(300, -100, event)
                    if can_capture_again:
                        break

                if (white_pawn[i].x <= event.pos[0] <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] + 200 <= white_pawn[i].y + 100 and
                    white_pawn[i].captured == 0 and white_pawn[i].is_jumped == 0):

                    can_capture_again = check_if_pawn_can_capture(-100, 300, event)
                    if can_capture_again:
                        break

                if (white_pawn[i].x <= event.pos[0] + 200 <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] + 200 <= white_pawn[i].y + 100 and
                    white_pawn[i].captured == 0 and white_pawn[i].is_jumped == 0):

                    can_capture_again = check_if_pawn_can_capture(300, 300, event)
                    if can_capture_again:
                        break

        elif pawn.color == "white":
            for i in range(20):
                if (black_pawn[i].x <= event.pos[0] + 200 <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] <= black_pawn[i].y + 100 and
                    black_pawn[i].captured == 0 and black_pawn[i].is_jumped == 0):

                    can_capture_again = check_if_pawn_can_capture(300, -100, event)
                    if can_capture_again:
                        break

                if (black_pawn[i].x <= event.pos[0] <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] + 200 <= black_pawn[i].y + 100 and
                    black_pawn[i].captured == 0 and black_pawn[i].is_jumped == 0):

                    can_capture_again = check_if_pawn_can_capture(-100, 300, event)
                    if can_capture_again:
                        break

                if (black_pawn[i].x <= event.pos[0] + 200 <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] + 200 <= black_pawn[i].y + 100 and
                    black_pawn[i].captured == 0 and black_pawn[i].is_jumped == 0):

                    can_capture_again = check_if_pawn_can_capture(300, 300, event)
                    if can_capture_again:
                        break

    return can_capture_again


def change_to_queen():
    for i in range (20):
        black_pawn[i].change_to_queen()

    for i in range (20):
        white_pawn[i].change_to_queen()


def check_for_pawn_in_the_way(pawn, pos_x, pos_y):
    for i in range(20):
        if pawn.color == "black":
            if (white_pawn[i].x <= pos_x <= white_pawn[i].x + 100 and
                white_pawn[i].y <= pos_y <= white_pawn[i].y + 100 and
                white_pawn[i].captured == 0 and white_pawn[i].is_jumped == 0):

                return True

        if pawn.color == "white":
            if (black_pawn[i].x <= pos_x <= black_pawn[i].x + 100 and
                black_pawn[i].y <= pos_y <= black_pawn[i].y + 100 and
                black_pawn[i].captured == 0 and black_pawn[i].is_jumped == 0):

                return True

    return False


def check_win():
    global white_win, black_win, winner

    if black_pawn_left == 0:
        white_win +=1
        winner = "white"
        return True

    if white_pawn_left == 0:
        black_win +=1
        winner = "black"
        return True

    if check_if_all_pawns_are_blocked():
        if turn % 2 == 0:
            white_win += 1
            winner = "white"

        if turn % 2 == 1:
            black_win += 1
            winner = "black"

        return True

    return False


def select_pawn_in_danger(pawn, move, loops, event):
    if pawn.color == "black":
        for i in range (20):
            if (white_pawn[i].x <= event.pos[0] <= white_pawn[i].x + 100 and
                white_pawn[i].y <= event.pos[1] <= white_pawn[i].y + 100 and
                white_pawn[i].captured == 0 and white_pawn[i].is_jumped == 0):

                if white_pawn[i].is_in_danger == 0:
                    white_pawn[i].is_in_danger = 1
                    pawn.locked_direction = move
                    pawn.pawn_to_capture_distance = loops

                elif white_pawn[i].is_in_danger == 1:
                    white_pawn[i].is_in_danger = 0
                    pawn.locked_direction = ""
                    pawn.pawn_to_capture_distance = 0

    if pawn.color == "white":
        for i in range (20):
            if (black_pawn[i].x <= event.pos[0] <= black_pawn[i].x + 100 and
                black_pawn[i].y <= event.pos[1] <= black_pawn[i].y + 100 and
                black_pawn[i].captured == 0 and black_pawn[i].is_jumped == 0):

                if black_pawn[i].is_in_danger == 0:
                    black_pawn[i].is_in_danger = 1
                    pawn.locked_direction = move
                    pawn.pawn_to_capture_distance = loops

                elif black_pawn[i].is_in_danger == 1:
                    black_pawn[i].is_in_danger = 0
                    pawn.locked_direction = ""
                    pawn.pawn_to_capture_distance = 0


def queen_capture(pawn, loops):
    global turn

    direction = pawn.locked_direction

    for i in range(20):
        if black_pawn[i].is_in_danger == 1 or white_pawn[i].is_in_danger == 1:
            if black_pawn[i].is_in_danger == 1:
                black_pawn[i].is_jumped = 1
                black_pawn[i].is_in_danger = 0

            if white_pawn[i].is_in_danger == 1:
                white_pawn[i].is_jumped = 1
                white_pawn[i].is_in_danger = 0

            pawn.locked_direction = ""
            pawn.pawn_to_capture_distance = 0

            start = (pawn.x, pawn.y)
            for j in range(loops):
                if direction == "up_left":
                    pawn.move_up_left()

                elif direction == "up_right":
                    pawn.move_up_right()

                elif direction == "down_left":
                    pawn.move_down_left()

                elif direction == "down_right":
                    pawn.move_down_right()
            end = (pawn.x, pawn.y)
            show_capture(start, end, pawn.color)

            return


def restart():
    global turn,global_mill_sec_time,global_sec_time,global_min_time,global_time,black_mill_sec_time,black_sec_time,\
    black_min_time,black_time,white_mill_sec_time,white_sec_time,white_min_time,white_time,winner,manoury
    init_pawns()
    for i in range (20):
        black_pawn[i].captured = 0
        white_pawn[i].captured = 0
        black_pawn[i].queen = 0
        white_pawn[i].queen = 0
    turn = 1
    # timer variable
    global_mill_sec_time = 0
    global_sec_time = 0
    global_min_time = 0
    global_time = ""

    black_mill_sec_time = 0
    black_sec_time = 0
    black_min_time = 0
    black_time = ""

    white_mill_sec_time = 0
    white_sec_time = 0
    white_min_time = 0
    white_time = ""

    winner = ""

    manoury.clear()


def check_if_queen_can_capture_again(pawn):
    pos_x = pawn.x + 50
    pos_y = pawn.y + 50
    can_capture_again = False

    while 0 <= pos_x - 100 and 0 <= pos_y - 100:
        pos_x -= 100
        pos_y -= 100
        pawn_hit = check_for_pawn_in_the_way(pawn, pos_x, pos_y)

        if pawn_hit:
            can_capture = check_if_pawn_can_capture(pos_x - 100, pos_y - 100, None)

            if can_capture:
                can_capture_again = True
                break

            elif not can_capture:
                break

    pos_x = pawn.x + 50
    pos_y = pawn.y + 50

    while pos_x + 100 <= 1010 and 0 <= pos_y - 100 and not can_capture_again:
        pos_x += 100
        pos_y -= 100
        pawn_hit = check_for_pawn_in_the_way(pawn, pos_x, pos_y)

        if pawn_hit:
            can_capture = check_if_pawn_can_capture(pos_x + 100, pos_y - 100, None)

            if can_capture:
                can_capture_again = True
                break

            elif not can_capture:
                break

    pos_x = pawn.x + 50
    pos_y = pawn.y + 50

    while 0 <= pos_x - 100 and pos_y + 100 <= 1010 and not can_capture_again:
        pos_x -= 100
        pos_y += 100
        pawn_hit = check_for_pawn_in_the_way(pawn, pos_x, pos_y)

        if pawn_hit:
            can_capture = check_if_pawn_can_capture(pos_x - 100, pos_y + 100, None)

            if can_capture:
                can_capture_again = True
                break

            elif not can_capture:
                break

    pos_x = pawn.x + 50
    pos_y = pawn.y + 50

    while pos_x + 100 <= 1010 and pos_y + 100 <= 1010 and not can_capture_again:
        pos_x += 100
        pos_y += 100
        pawn_hit = check_for_pawn_in_the_way(pawn, pos_x, pos_y)

        if pawn_hit:
            can_capture = check_if_pawn_can_capture(pos_x + 100, pos_y + 100, None)

            if can_capture:
                can_capture_again = True
                break

            elif not can_capture:
                break

    return can_capture_again


def detect_for_konami():
    global input_konami
    konami_code = ["up", "up", "down", "down", "left", "right", "left", "right", "b", "a"]

    # Check if the input length is sufficient
    if len(input_konami) >= len(konami_code):
        # Compare the last inputs with the Konami code
        if input_konami[-len(konami_code):] == konami_code:
            return True

    return False


def make_selected_to_queen():
    """
    promote to queen the selected pawn //debug//
    """
    for i in range (20):
        if black_pawn[i].selected == 1:
            black_pawn[i].queen = 1

    for i in range (20):
        if white_pawn[i].selected == 1:
            white_pawn[i].queen = 1


def capture_selected():
    """
    capture the selected pawn //debug//
    """
    for i in range (20):
        if black_pawn[i].selected == 1:
            black_pawn[i].captured = 1

    for i in range (20):
        if white_pawn[i].selected == 1:
            white_pawn[i].captured = 1


def check_if_all_pawns_are_blocked():
    blocked_pawns = 0
    if turn % 2 == 0:
        for i in range(20):
            up_left = True
            up_right = True
            down_left = True
            down_right = True

            if black_pawn[i].captured == 0:
                if not 5 <= black_pawn[i].x + 50 - 100 <= 1005 and 5 <= black_pawn[i].y + 50 - 100 <= 1005:
                    up_left = False

                if not 5 <= black_pawn[i].x + 50 + 100 <= 1005 and 5 <= black_pawn[i].y + 50 - 100 <= 1005:
                    up_right = False

                if not 5 <= black_pawn[i].x + 50 - 100 <= 1005 and 5 <= black_pawn[i].y + 50 + 100 <= 1005:
                    down_left = False

                if not 5 <= black_pawn[i].x + 50 + 100 <= 1005 and 5 <= black_pawn[i].y + 50 + 100 <= 1005:
                    down_right = False

                if black_pawn[i].queen == 0:
                    pawn_hit_up_left = check_for_pawn_in_the_way(black_pawn[i], black_pawn[i].x + 50 - 100,
                                                                 black_pawn[i].y + 50 - 100)
                    pawn_hit_up_right = check_for_pawn_in_the_way(black_pawn[i], black_pawn[i].x + 50 + 100,
                                                                  black_pawn[i].y + 50 - 100)
                    pawn_hit_down_left = check_for_pawn_in_the_way(black_pawn[i], black_pawn[i].x + 50 - 100,
                                                                   black_pawn[i].y + 50 + 100)
                    pawn_hit_down_right = check_for_pawn_in_the_way(black_pawn[i], black_pawn[i].x + 50 + 100,
                                                                    black_pawn[i].y + 50 + 100)

                    if up_left and pawn_hit_up_left:
                        up_left = check_if_pawn_can_capture(black_pawn[i].x + 50 - 200,
                                                            black_pawn[i].y + 50 - 200,None)

                    elif up_left and not pawn_hit_up_left:
                        up_left = False

                    if up_right and pawn_hit_up_right:
                        up_right = check_if_pawn_can_capture(black_pawn[i].x + 50 + 200,
                                                             black_pawn[i].y + 50 - 200, None)

                    elif up_right and not pawn_hit_up_right:
                        up_right = False

                    for j in range(20):
                        if (down_left and (pawn_hit_down_left or
                            black_pawn[j].x <= black_pawn[i].x + 50 - 100 <= black_pawn[j].x + 100 and
                            black_pawn[j].y <= black_pawn[i].y + 50 + 100 <= black_pawn[j].y + 100 and
                            black_pawn[j].captured == 0)):

                            if pawn_hit_down_left:
                                down_left = check_if_pawn_can_capture(black_pawn[i].x + 50 - 200,
                                                                      black_pawn[i].y + 50 + 200, None)

                            elif not pawn_hit_down_left:
                                down_left = False

                        if (down_right and (pawn_hit_down_right or
                            black_pawn[j].x <= black_pawn[i].x + 50 + 100 <= black_pawn[j].x + 100 and
                            black_pawn[j].y <= black_pawn[i].y + 50 + 100 <= black_pawn[j].y + 100 and
                            black_pawn[j].captured == 0)):

                            if pawn_hit_down_right:
                                down_right = check_if_pawn_can_capture(black_pawn[i].x + 50 + 200,
                                                                       black_pawn[i].y + 50 + 200, None)

                            elif not pawn_hit_down_right:
                                down_right = False

                    if not up_left and not up_right and not down_left and not down_right:
                        blocked_pawns += 1

                elif black_pawn[i].queen == 1:
                    pawn_hit_up_left = check_for_pawn_in_the_way(black_pawn[i], black_pawn[i].x + 50 - 100,
                                                                 black_pawn[i].y + 50 - 100)
                    pawn_hit_up_right = check_for_pawn_in_the_way(black_pawn[i], black_pawn[i].x + 50 + 100,
                                                                  black_pawn[i].y + 50 - 100)
                    pawn_hit_down_left = check_for_pawn_in_the_way(black_pawn[i], black_pawn[i].x + 50 - 100,
                                                                   black_pawn[i].y + 50 + 100)
                    pawn_hit_down_right = check_for_pawn_in_the_way(black_pawn[i], black_pawn[i].x + 50 + 100,
                                                                    black_pawn[i].y + 50 + 100)
                    for j in range(20):
                        if (up_left and (pawn_hit_up_left or
                            black_pawn[j].x <= black_pawn[i].x + 50 - 100 <= black_pawn[j].x + 100 and
                            black_pawn[j].y <= black_pawn[i].y + 50 - 100 <= black_pawn[j].y + 100 and
                            black_pawn[j].captured == 0)):

                            if pawn_hit_up_left:
                                up_left = check_if_pawn_can_capture(black_pawn[i].x + 50 - 200,
                                                                    black_pawn[i].y + 50 - 200,None)

                            elif not pawn_hit_up_left:
                                up_left = False

                        if (up_right and (pawn_hit_up_right or
                            black_pawn[j].x <= black_pawn[i].x + 50 + 100 <= black_pawn[j].x + 100 and
                            black_pawn[j].y <= black_pawn[i].y + 50 - 100 <= black_pawn[j].y + 100 and
                            black_pawn[j].captured == 0)):

                            if pawn_hit_up_right:
                                up_right = check_if_pawn_can_capture(black_pawn[i].x + 50 + 200,
                                                                     black_pawn[i].y + 50 - 200, None)

                            elif not pawn_hit_up_right:
                                up_right = False

                        if (down_left and (pawn_hit_down_left or
                            black_pawn[j].x <= black_pawn[i].x + 50 - 100 <= black_pawn[j].x + 100 and
                            black_pawn[j].y <= black_pawn[i].y + 50 + 100 <= black_pawn[j].y + 100 and
                            black_pawn[j].captured == 0)):

                            if pawn_hit_down_left:
                                down_left = check_if_pawn_can_capture(black_pawn[i].x + 50 - 200,
                                                                      black_pawn[i].y + 50 + 200, None)

                            elif not pawn_hit_down_left:
                                down_left = False

                        if (down_right and (pawn_hit_down_right or
                            black_pawn[j].x <= black_pawn[i].x + 50 + 100 <= black_pawn[j].x + 100 and
                            black_pawn[j].y <= black_pawn[i].y + 50 + 100 <= black_pawn[j].y + 100 and
                            black_pawn[j].captured == 0)):

                            if pawn_hit_down_right:
                                down_right = check_if_pawn_can_capture(black_pawn[i].x + 50 + 200,
                                                                       black_pawn[i].y + 50 + 200, None)

                            elif not pawn_hit_down_right:
                                down_right = False

                    if not up_left and not up_right and not down_left and not down_right:
                        blocked_pawns += 1

        if black_pawn_left <= blocked_pawns:
            return True

    if turn % 2 == 1:
        for i in range(20):
            up_left = True
            up_right = True
            down_left = True
            down_right = True

            if white_pawn[i].captured == 0:
                if not 5 <= white_pawn[i].x + 50 - 100 <= 1005 and 5 <= white_pawn[i].y + 50 - 100 <= 1005:
                    up_left = False

                if not 5 <= white_pawn[i].x + 50 + 100 <= 1005 and 5 <= white_pawn[i].y + 50 - 100 <= 1005:
                    up_right = False

                if not 5 <= white_pawn[i].x + 50 - 100 <= 1005 and 5 <= white_pawn[i].y + 50 + 100 <= 1005:
                    down_left = False

                if not 5 <= white_pawn[i].x + 50 + 100 <= 1005 and 5 <= white_pawn[i].y + 50 + 100 <= 1005:
                    down_right = False

                if white_pawn[i].queen == 0:
                    pawn_hit_up_left = check_for_pawn_in_the_way(white_pawn[i], white_pawn[i].x + 50 - 100,
                                                                 white_pawn[i].y + 50 - 100)
                    pawn_hit_up_right = check_for_pawn_in_the_way(white_pawn[i], white_pawn[i].x + 50 + 100,
                                                                  white_pawn[i].y + 50 - 100)
                    pawn_hit_down_left = check_for_pawn_in_the_way(white_pawn[i], white_pawn[i].x + 50 - 100,
                                                                   white_pawn[i].y + 50 + 100)
                    pawn_hit_down_right = check_for_pawn_in_the_way(white_pawn[i], white_pawn[i].x + 50 + 100,
                                                                    white_pawn[i].y + 50 + 100)

                    for j in range(20):
                        if (up_left and (pawn_hit_up_left or
                            white_pawn[j].x <= white_pawn[i].x + 50 - 100 <= white_pawn[j].x + 100 and
                            white_pawn[j].y <= white_pawn[i].y + 50 - 100 <= white_pawn[j].y + 100 and
                            white_pawn[j].captured == 0)):

                            if pawn_hit_up_left:
                                up_left = check_if_pawn_can_capture(white_pawn[i].x + 50 - 200,
                                                                    white_pawn[i].y + 50 - 200,None)

                            elif not pawn_hit_up_left:
                                up_left = False

                        if (up_right and (pawn_hit_up_right or
                            white_pawn[j].x <= white_pawn[i].x + 50 + 100 <= white_pawn[j].x + 100 and
                            white_pawn[j].y <= white_pawn[i].y + 50 - 100 <= white_pawn[j].y + 100 and
                            white_pawn[j].captured == 0)):

                            if pawn_hit_up_right:
                                up_right = check_if_pawn_can_capture(white_pawn[i].x + 50 + 200,
                                                                     white_pawn[i].y + 50 - 200, None)

                            elif not pawn_hit_up_right:
                                up_right = False

                    if down_left and pawn_hit_down_left:
                        down_left = check_if_pawn_can_capture(white_pawn[i].x + 50 - 200,
                                                              white_pawn[i].y + 50 + 200, None)

                    elif down_left and not pawn_hit_down_left:
                        down_left = False

                    if down_right and pawn_hit_down_right:
                        down_right = check_if_pawn_can_capture(white_pawn[i].x + 50 + 200,
                                                               white_pawn[i].y + 50 + 200, None)

                    elif down_right and not pawn_hit_down_right:
                        down_right = False

                    if not up_left and not up_right and not down_left and not down_right:
                        blocked_pawns += 1

                elif white_pawn[i].queen == 1:
                    pawn_hit_up_left = check_for_pawn_in_the_way(white_pawn[i], white_pawn[i].x + 50 - 100,
                                                                 white_pawn[i].y + 50 - 100)
                    pawn_hit_up_right = check_for_pawn_in_the_way(white_pawn[i], white_pawn[i].x + 50 + 100,
                                                                  white_pawn[i].y + 50 - 100)
                    pawn_hit_down_left = check_for_pawn_in_the_way(white_pawn[i], white_pawn[i].x + 50 - 100,
                                                                   white_pawn[i].y + 50 + 100)
                    pawn_hit_down_right = check_for_pawn_in_the_way(white_pawn[i], white_pawn[i].x + 50 + 100,
                                                                    white_pawn[i].y + 50 + 100)
                    for j in range(20):
                        if (up_left and (pawn_hit_up_left or
                            white_pawn[j].x <= white_pawn[i].x + 50 - 100 <= white_pawn[j].x + 100 and
                            white_pawn[j].y <= white_pawn[i].y + 50 - 100 <= white_pawn[j].y + 100 and
                            white_pawn[j].captured == 0)):

                            if pawn_hit_up_left:
                                up_left = check_if_pawn_can_capture(white_pawn[i].x + 50 - 200,
                                                                    white_pawn[i].y + 50 - 200,None)

                            elif not pawn_hit_up_left:
                                up_left = False

                        if (up_right and (pawn_hit_up_right or
                            white_pawn[j].x <= white_pawn[i].x + 50 + 100 <= white_pawn[j].x + 100 and
                            white_pawn[j].y <= white_pawn[i].y + 50 - 100 <= white_pawn[j].y + 100 and
                            white_pawn[j].captured == 0)):

                            if pawn_hit_up_right:
                                up_right = check_if_pawn_can_capture(white_pawn[i].x + 50 + 200,
                                                                     white_pawn[i].y + 50 - 200, None)

                            elif not pawn_hit_up_right:
                                up_right = False

                        if (down_left and (pawn_hit_down_left or
                            white_pawn[j].x <= white_pawn[i].x + 50 - 100 <= white_pawn[j].x + 100 and
                            white_pawn[j].y <= white_pawn[i].y + 50 + 100 <= white_pawn[j].y + 100 and
                            white_pawn[j].captured == 0)):

                            if pawn_hit_down_left:
                                down_left = check_if_pawn_can_capture(white_pawn[i].x + 50 - 200,
                                                                      white_pawn[i].y + 50 + 200, None)

                            elif not pawn_hit_down_left:
                                down_left = False

                        if (down_right and (pawn_hit_down_right or
                            white_pawn[j].x <= white_pawn[i].x + 50 + 100 <= white_pawn[j].x + 100 and
                            white_pawn[j].y <= white_pawn[i].y + 50 + 100 <= white_pawn[j].y + 100 and
                            white_pawn[j].captured == 0)):

                            if pawn_hit_down_right:
                                down_right = check_if_pawn_can_capture(white_pawn[i].x + 50 + 200,
                                                                       white_pawn[i].y + 50 + 200, None)

                            elif not pawn_hit_down_right:
                                down_right = False

                    if not up_left and not up_right and not down_left and not down_right:
                        blocked_pawns += 1

        if white_pawn_left <= blocked_pawns:
            return True

    return False


def change_location_to_case(x,y):
    y_loc = 0
    x_loc = 0
    case = 0
    for i in range(10):
        if (i*100) > y < (i*100)+10:
            y_loc = i
            break
    for i in range(10):
        if (i*100) > x < (i*100)+10:
            x_loc = i
            break
    print(y_loc-1)
    if y_loc % 2 == 0 and x_loc % 2 == 1:
        case = (x_loc+1)//2 + (y_loc-1)*5
    elif y_loc % 2 == 1 and x_loc % 2 == 0:
        case = x_loc//2 + (y_loc-1)*5
    if case == 0:
        case = 50
    return case


def show_move(start,end,color):
    global manoury
    start_case = change_location_to_case(start[0], start[1])
    end_case = change_location_to_case(end[0],end[1])
    if color == "black":
        manoury += [f"({start_case}-{end_case})"]
    elif color == "white":
        manoury += [f"{start_case}-{end_case}"]


def show_capture(start,end,color):
    global manoury
    start_case = change_location_to_case(start[0], start[1])
    end_case = change_location_to_case(end[0], end[1])
    if color == "black":
        manoury += [f"({start_case}x{end_case})"]
    elif color == "white":
        manoury += [f"{start_case}x{end_case}"]


def check_all_pawns_for_capture():
    for i in range(20):
        black_pawn[i].has_to_move = 0
        white_pawn[i].has_to_move = 0

    for i in range(20):
        if black_pawn[i].captured == 0:
            pos_x = black_pawn[i].x + 50
            pos_y = black_pawn[i].y + 50
            can_capture = False

            if black_pawn[i].queen == 0:
                pawn_hit = check_for_pawn_in_the_way(black_pawn[i], pos_x - 100, pos_y - 100)

                if pawn_hit:
                    can_capture = check_if_pawn_can_capture(pos_x - 200, pos_y - 200, None)

                pawn_hit = check_for_pawn_in_the_way(black_pawn[i], pos_x + 100, pos_y - 100)

                if pawn_hit and not can_capture:
                    can_capture = check_if_pawn_can_capture(pos_x + 200, pos_y - 200, None)

                pawn_hit = check_for_pawn_in_the_way(black_pawn[i], pos_x - 100, pos_y + 100)

                if pawn_hit and not can_capture:
                    can_capture = check_if_pawn_can_capture(pos_x - 200, pos_y + 200, None)

                pawn_hit = check_for_pawn_in_the_way(black_pawn[i], pos_x + 100, pos_y + 100)

                if pawn_hit and not can_capture:
                    can_capture = check_if_pawn_can_capture(pos_x + 200, pos_y + 200, None)

                if can_capture:
                    break

            elif black_pawn[i].queen == 1:
                while 0 <= pos_x - 100 and 0 <= pos_y - 100 and not can_capture:
                    pos_x -= 100
                    pos_y -= 100
                    pawn_hit = check_for_pawn_in_the_way(black_pawn[i], pos_x, pos_y)

                    if pawn_hit:
                        can_capture = check_if_pawn_can_capture(pos_x - 100, pos_y - 100, None)
                        break

                pos_x = black_pawn[i].x
                pos_y = black_pawn[i].y

                while pos_x + 100 <= 1010 and 0 <= pos_y - 100 and not can_capture:
                    pos_x += 100
                    pos_y -= 100
                    pawn_hit = check_for_pawn_in_the_way(black_pawn[i], pos_x, pos_y)

                    if pawn_hit:
                        can_capture = check_if_pawn_can_capture(pos_x + 100, pos_y - 100, None)
                        break

                pos_x = black_pawn[i].x
                pos_y = black_pawn[i].y

                while 0 <= pos_x - 100 and pos_y + 100 <= 1010 and not can_capture:
                    pos_x -= 100
                    pos_y += 100
                    pawn_hit = check_for_pawn_in_the_way(black_pawn[i], pos_x, pos_y)

                    if pawn_hit:
                        can_capture = check_if_pawn_can_capture(pos_x - 100, pos_y + 100, None)
                        break

                pos_x = black_pawn[i].x
                pos_y = black_pawn[i].y

                while pos_x + 100 <= 1010 and pos_y + 100 <= 1010 and not can_capture:
                    pos_x += 100
                    pos_y += 100
                    pawn_hit = check_for_pawn_in_the_way(black_pawn[i], pos_x, pos_y)

                    if pawn_hit:
                        can_capture = check_if_pawn_can_capture(pos_x + 100, pos_y + 100, None)
                        break

            if can_capture:
                black_pawn[i].has_to_move = 1

        if white_pawn[i].captured == 0:
            pos_x = white_pawn[i].x + 50
            pos_y = white_pawn[i].y + 50
            can_capture = False

            if white_pawn[i].queen == 0:
                pawn_hit = check_for_pawn_in_the_way(white_pawn[i], pos_x - 100, pos_y - 100)

                if pawn_hit:
                    can_capture = check_if_pawn_can_capture(pos_x - 200, pos_y - 200, None)

                pawn_hit = check_for_pawn_in_the_way(white_pawn[i], pos_x + 100, pos_y - 100)

                if pawn_hit and not can_capture:
                    can_capture = check_if_pawn_can_capture(pos_x + 200, pos_y - 200, None)

                pawn_hit = check_for_pawn_in_the_way(white_pawn[i], pos_x - 100, pos_y + 100)

                if pawn_hit and not can_capture:
                    can_capture = check_if_pawn_can_capture(pos_x - 200, pos_y + 200, None)

                pawn_hit = check_for_pawn_in_the_way(white_pawn[i], pos_x + 100, pos_y + 100)

                if pawn_hit and not can_capture:
                    can_capture = check_if_pawn_can_capture(pos_x + 200, pos_y + 200, None)

                if can_capture:
                    break

            elif white_pawn[i].queen == 1:
                while 0 <= pos_x - 100 and 0 <= pos_y - 100 and not can_capture:
                    pos_x -= 100
                    pos_y -= 100
                    pawn_hit = check_for_pawn_in_the_way(white_pawn[i], pos_x, pos_y)

                    if pawn_hit:
                        can_capture = check_if_pawn_can_capture(pos_x - 100, pos_y - 100, None)
                        break

                pos_x = white_pawn[i].x
                pos_y = white_pawn[i].y

                while pos_x + 100 <= 1010 and 0 <= pos_y - 100 and not can_capture:
                    pos_x += 100
                    pos_y -= 100
                    pawn_hit = check_for_pawn_in_the_way(white_pawn[i], pos_x, pos_y)

                    if pawn_hit:
                        can_capture = check_if_pawn_can_capture(pos_x + 100, pos_y - 100, None)
                        break

                pos_x = white_pawn[i].x
                pos_y = white_pawn[i].y

                while 0 <= pos_x - 100 and pos_y + 100 <= 1010 and not can_capture:
                    pos_x -= 100
                    pos_y += 100
                    pawn_hit = check_for_pawn_in_the_way(white_pawn[i], pos_x, pos_y)

                    if pawn_hit:
                        can_capture = check_if_pawn_can_capture(pos_x - 100, pos_y + 100, None)
                        break

                pos_x = white_pawn[i].x
                pos_y = white_pawn[i].y

                while pos_x + 100 <= 1010 and pos_y + 100 <= 1010 and not can_capture:
                    pos_x += 100
                    pos_y += 100
                    pawn_hit = check_for_pawn_in_the_way(white_pawn[i], pos_x, pos_y)

                    if pawn_hit:
                        can_capture = check_if_pawn_can_capture(pos_x + 100, pos_y + 100, None)
                        break

            if can_capture:
                white_pawn[i].has_to_move = 1


def get_save_data():
    """
    get all variable and all param for each pawn
    """
    global save
    save = ""

    # Save general variables, exclude 'save'
    variables = {k: v for k, v in globals().items() if not callable(v) and not k.startswith("__") and k != "save"}
    for var_name, var_value in variables.items():
        save += f"{var_name} = {repr(var_value)}\n"

    # Save black pawns (save attributes instead of the object reference)
    for i, pawn in enumerate(black_pawn):
        save += f"black_pawn[{i}] = {{'x': {pawn.x}, 'y': {pawn.y}, 'color': '{pawn.color}', 'captured': {pawn.captured}, 'queen': {pawn.queen}}}\n"

    # Save white pawns (save attributes instead of the object reference)
    for i, pawn in enumerate(white_pawn):
        save += f"white_pawn[{i}] = {{'x': {pawn.x}, 'y': {pawn.y}, 'color': '{pawn.color}', 'captured': {pawn.captured}, 'queen': {pawn.queen}}}\n"


def write_save_file():
    """
    write all save data in a text file
    """
    get_save_data()
    with open("save/save.txt", "w") as file:
        file.write(save)


def load_save_file():
    """
    read and load the save file
    """
    global black_pawn, white_pawn

    # Initialize empty pawn lists
    black_pawn = [Pawn() for _ in range(20)]
    white_pawn = [Pawn() for _ in range(20)]

    with open("save/save.txt", "r") as file:
        lines = file.readlines()

    for line in lines:
        # Skip empty lines or lines that do not contain relevant information
        if not line.strip():
            continue

        # Load pawn data from the save file for black pawns
        if "black_pawn" in line:
            try:
                index = int(line.split("[")[1].split("]")[0])

                attributes = eval(line.split(" = ")[1])

                black_pawn[index].x = attributes['x']
                black_pawn[index].y = attributes['y']
                black_pawn[index].color = attributes['color']
                black_pawn[index].captured = attributes['captured']
                black_pawn[index].queen = attributes['queen']

            except (IndexError, ValueError, SyntaxError) as e:
                print(f"Error processing black pawn line: {line} - {e}")

        # Load pawn data from the save file for white pawns
        elif "white_pawn" in line:
            try:
                index = int(line.split("[")[1].split("]")[0])

                attributes = eval(line.split(" = ")[1])

                white_pawn[index].x = attributes['x']
                white_pawn[index].y = attributes['y']
                white_pawn[index].color = attributes['color']
                white_pawn[index].captured = attributes['captured']
                white_pawn[index].queen = attributes['queen']

            except (IndexError, ValueError, SyntaxError) as e:
                print(f"Error processing white pawn line: {line} - {e}")

        elif "=" in line:
            try:
                var_name, var_value = line.split(" = ")
                var_value = eval(var_value.strip())
                globals()[var_name.strip()] = var_value
            except Exception as e:
                print(f"Error processing global variable line: {line} - {e}")


save = ""

black_pawn = [Pawn] * 20
white_pawn = [Pawn] * 20

turn = 1

black_pawn_left = 20
white_pawn_left = 20

black_pawn_queen = 0
white_pawn_queen = 0

black_win = 0
white_win = 0

winner = ""

#timer variable
global_mill_sec_time = 0
global_sec_time = 0
global_min_time = 0
global_time = ""

black_mill_sec_time = 0
black_sec_time = 0
black_min_time = 0
black_time = ""

white_mill_sec_time = 0
white_sec_time = 0
white_min_time = 0
white_time = ""

manoury = []

input_konami = []