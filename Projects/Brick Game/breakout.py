"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.gui.events.mouse import onmouseclicked, onmousemoved
from campy.gui.events.timer import pause
from campy.graphics.gobjects import GOval, GRect, GLabel
from breakoutgraphics import BreakoutGraphics
import random

FRAME_RATE = 1000 / 40  # 120 frames per second.
NUM_LIVES = 3
graphics = BreakoutGraphics(brick_cols=10, brick_rows=10)
SCORE = 0
p = graphics.paddle()
w = graphics.window
ball = graphics.ball()
vx = graphics.get_dx()
vy = graphics.get_dy()
brick_o = graphics.brick()
COUNT = 0
life_left = NUM_LIVES
score_count = SCORE
life_ui = GLabel(f"Life: {life_left}")
score_ui = GLabel(f"Score: {score_count}")
WIN_SCORE = graphics.brick_count() + 7
laser1 = graphics.laser1(ball)
laser2 = graphics.laser2(ball)
TIE_FIGHTER_PART = 7


def main():
    opening()
    life_ui.font = "-15"
    score_ui.font = "-15"
    w.add(life_ui, x=w.width - life_ui.width, y=w.height - life_ui.height)
    w.add(score_ui, x=0, y=w.height - score_ui.height)
    onmousemoved(mouse_move)
    onmouseclicked(main_game)


def opening():
    black_cover = GRect(w.width, w.height, x=0, y=0)
    black_cover.filled = True
    black_cover.fill_color = "black"
    w.add(black_cover)
    far = GLabel("A long time ago in a galaxy far, \nfar away...")
    far.color = "blue"
    far.font = "-20"
    w.add(far, x=w.width / 2 - far.width / 2 + 60, y=w.height / 2)
    pause(1200)
    w.remove(far)
    main_title = GLabel("STAR\nWARS")
    main_title.color = "yellow"
    for i in range(20):
        size = (160 // (int(i) + 1))
        size = -size
        main_title.font = str(size)
        w.add(main_title, x=w.width / 2 - main_title.width / 4, y=w.height / 2)
        pause(FRAME_RATE * 6)
        w.remove(main_title)
    opening_crawl = GLabel("It   is   a   period  of   civil   war\n"
                           "Princess Leia races home abroad\n"
                           "her   spaceship   but   was   later\n"
                           "captured   by   Empires's  agents\n"
                           "Use  your  lightsaber  to destroy\n"
                           "the   force   field   to   save  the\n"
                           "princess")
    opening_crawl.color = "yellow"
    opening_crawl.font = "-15"
    w.add(opening_crawl, x=w.width / 2 - 130, y=w.height + 1)
    for i in range(50):
        opening_crawl.move(0, -10)
        pause(FRAME_RATE * 6)
    w.remove(black_cover)
    w.remove(opening_crawl)


# Animation loop start here：
def mouse_move(m):
    global p
    global w
    if m.x + p.width / 2 >= w.width:
        p.x = w.width - p.width
    elif m.x - p.width / 2 <= 0:
        p.x = 0
    else:
        p.x = m.x - p.width / 2


def main_game(e):
    # run this when user click
    global COUNT, life_ui, score_ui, vx, vy, score_count, life_left, ball
    # create life count ui
    if is_at_original_point():
        # check if the game started
        if life_left > 0 and score_count < WIN_SCORE:
            while ball.y < w.height:
                # game loop: keep the game going if ball doesn't fall out of the border
                if score_count < WIN_SCORE/2:
                    ball.move(vx, vy)
                    pause(FRAME_RATE)
                    check_if_ball_hit_sth()
                else:
                    boss_fight()
                    break
                w.remove(score_ui)
                score_ui = update_score()
            life_left -= 1
            w.remove(ball)
            if score_count >= WIN_SCORE:
                over = GLabel("YOU WON")
                over.font = "-60"
                w.add(over, w.width / 2 - over.width / 2, w.height / 2)
            elif life_left <= 0:
                game_over()
            else:
                ball = graphics.ball()
                w.remove(life_ui)
                life_ui = update_life()
    else:
        pass


def is_at_original_point():
    # return true if ball on the starting point
    return ball.x == (w.width / 2 - ball.width / 2) and ball.y == (w.height / 2 - ball.width / 2)


def update_life():
    # to update the life count
    life_new = GLabel(f"Life: {life_left}")
    life_new.font = "-15"
    w.add(life_new, x=w.width - life_new.width, y=w.height - life_ui.height)
    return life_new


def update_score():
    # to update the score count
    score_new = GLabel(f"Score: {score_count}")
    score_new.font = "-15"
    w.add(score_new, x=0, y=w.height - life_ui.height)
    return score_new


def game_over():
    # print "game over" on the window
    over = GLabel("GAME OVER")
    over.font = "-60"
    w.add(over, w.width / 2 - over.width / 2, w.height / 2)


def enter_tie_fighter():
    # create opening effect when tie_fighter enter the canvas
    cover = GRect(w.width, w.height, x=0, y=0)
    cover.filled = True
    cover.fill_color = "red"
    w.add(cover)
    pause(100)
    cover.filled = True
    cover.fill_color = "black"
    pause(100)
    w.remove(cover)


def warning():
    # create warning effect when tie fighter enter the canvas
    warning_s = GLabel("Warning!!")
    warning_s.font = "-60"
    w.add(warning_s, x=w.width / 2 - warning_s.width / 2, y=w.height / 2)
    return warning_s


def boss_fight():
    # game
    global COUNT, life_left, life_ui, vx, vy, SCORE, ball, score_ui
    hull = graphics.tie_fighter_hull()
    hull_window = graphics.tie_fighter_hull_window()
    hull_window2 = graphics.tie_fighter_hull_window2()
    r_skeleton = graphics.tie_fighter_r_skeleton(hull)
    r_wing = graphics.tie_fighter_r_wing(r_skeleton)
    l_skeleton = graphics.tie_fighter_l_skeleton(hull)
    l_wing = graphics.tie_fighter_l_wing(l_skeleton)
    warning_sign = warning()
    for i in range(10):
        # enter tie fighter from ( x: w.width/2 - hull.width/2, y: w.height/2- hull.height/2 - 400 )
        enter_tie_fighter()
        hull.move(0, 40)
        r_wing.move(0, 40)
        l_wing.move(0, 40)
        hull_window.move(0, 40)
        hull_window2.move(0, 40)
        r_skeleton.move(0, 40)
        l_skeleton.move(0, 40)
        pause(FRAME_RATE)
        # after for loop, tie fighter will be at ( x: w.width/2 - hull.width/2, y: w.height/2- hull.height/2 )
    w.remove(warning_sign)
    # laser1 = graphics.laser1(ball)
    # laser2 = graphics.laser2(ball)
    tie_dx = vx
    tie_dy = vy / 2
    while True:
        while ball.y < w.height:
            COUNT += 1
            if l_wing.x + l_wing.width >= w.width or r_wing.x <= 0:
                tie_dx = -tie_dx
            if l_wing.y + l_wing.height >= w.height / 2 + 100 or l_wing.y <= w.height / 2 - 200:
                tie_dy = -tie_dy
            hull.move(tie_dx, tie_dy)
            hull_window.move(tie_dx, tie_dy)
            hull_window2.move(tie_dx, tie_dy)
            r_skeleton.move(tie_dx, tie_dy)
            r_wing.move(tie_dx, tie_dy)
            l_wing.move(tie_dx, tie_dy)
            l_skeleton.move(tie_dx, tie_dy)
            ball.move(vx, vy)
            check_if_ball_hit_sth()
            w.remove(score_ui)
            score_ui = update_score()
            if COUNT % 50 == 0 and COUNT < 1000:
                w.add(laser1, x=hull.x, y=hull.y)
                w.add(laser2, x=hull.x + hull.width, y=hull.y)
            check_if_laser_hit_paddle()
            laser1.move(0, 10)
            laser2.move(0, 10)
            pause(FRAME_RATE)
            if life_left <= 0 or score_count >= WIN_SCORE:
                break
        life_left -= 1
        w.remove(ball)
        if life_left <= 0:
            break
        else:
            ball = graphics.ball()
            w.remove(life_ui)
            life_ui = update_life()


def check_if_ball_hit_sth():
    # check if the ball hit something
    global score_count, vx, vy, TIE_FIGHTER_PART
    if ball.x <= 0 or ball.x + ball.width >= w.width:
        vx = -vx
    elif ball.y <= 0:
        vy = -vy
    elif ball.y >= w.height:
        pass
    else:
        pass
    obj = w.get_object_at(ball.x, ball.y)
    if obj is not None:
        if obj == p:
            if ball.x == (p.x + p.width):
                w.add(ball, x=p.x + p.width + 10, y=ball.y)
                vx = -vx
            else:
                w.add(ball, x=ball.x, y=p.y - ball.height)
                vy = -vy
        elif obj == life_ui or obj == score_ui or obj == laser1 or obj == laser2:
            pass
        else:
            w.remove(obj)
            vy = -vy * (1 + score_count / 10000)
            score_count += 1
    else:
        obj = w.get_object_at(ball.x, ball.y + ball.width)
        if obj is not None:
            if obj == p:
                if ball.x == (p.x + p.width):
                    w.add(ball, x=p.x + p.width + 10, y=ball.y)
                    vx = -vx
                else:
                    w.add(ball, x=ball.x, y=p.y - ball.height)
                    vy = -vy
            elif obj == life_ui or obj == score_ui or obj == laser1 or obj == laser2:
                pass
            else:
                w.remove(obj)
                vy = -vy * (1 + score_count / 10000)
                score_count += 1
        else:
            obj = w.get_object_at(ball.x + ball.width, ball.y + ball.width)
            if obj is not None:
                if obj == p:
                    if ball.x + ball.width == p.x:
                        vx = -vx
                    else:
                        w.add(ball, x=ball.x, y=p.y - ball.height)
                        vy = -vy
                elif obj == life_ui or obj == score_ui or obj == laser1 or obj == laser2:
                    pass
                else:
                    w.remove(obj)
                    vy = -vy * (1 + score_count / 10000)
                    score_count += 1

            else:
                obj = w.get_object_at(ball.x + ball.width, ball.y)
                if obj is not None:
                    if obj == p:
                        if obj == p:
                            if ball.x + ball.width == p.x:
                                vx = -vx
                            else:
                                w.add(ball, x=ball.x, y=p.y - ball.height)
                                vy = -vy
                    elif obj == life_ui or obj == score_ui or obj == laser1 or obj == laser2:
                        pass
                    else:
                        w.remove(obj)
                        vy = -vy * (1 + score_count / 10000)
                        score_count += 1
                else:
                    pass


def check_if_laser_hit_paddle():
    global life_left, life_ui
    a = w.get_object_at(laser1.x, laser1.y + laser1.height + 1)
    b = w.get_object_at(laser2.x, laser2.y + laser2.height + 1)
    if a is not None:
        if a == p or b == p:
            if life_left >= 1:
                life_left -= 1
                w.remove(life_ui)
                life_ui = update_life()
            else:
                pass
    else:
        a = w.get_object_at(laser1.x + laser1.width, laser1.y + laser1.height + 1)
        b = w.get_object_at(laser2.x + laser2.width, laser2.y + laser2.height + 1)
        if a == p or b == p:
            if life_left >= 1:
                life_left -= 1
                w.remove(life_ui)
                life_ui = update_life()
            else:
                pass








if __name__ == '__main__':
    main()
