"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
from campy.gui.events.timer import pause
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40  # Height of a brick (in pixels).
BRICK_HEIGHT = 15  # Height of a brick (in pixels).
BRICK_ROWS = 10  # Number of rows of bricks.
BRICK_COLS = 10  # Number of columns of bricks.
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10  # Radius of the ball (in pixels).
PADDLE_WIDTH = 75  # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels).
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        self.paddle_h = paddle_height
        self.paddle_w = paddle_width
        self.paddle_off = paddle_offset

        self.ball_radius = ball_radius
        self.brick_width = brick_width
        self.brick_height = brick_height
        self.brick_spacing = brick_spacing

        self.brick_cols = brick_cols
        self.brick_rows = brick_rows


        # Create a graphical window, with some extra space.
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        self.__dy = INITIAL_Y_SPEED
        self.__dx = random.randrange(1, MAX_X_SPEED)




        # self.paddle = self.paddle()
        # self.life_ui = self.life_ui()
        # self.score_ui = self.score_ui()


    def get_dy(self):
        return self.__dy

    def get_dx(self):
        if random.random() > 0.5:
            self.__dx = -self.__dx
        return self.__dx

    def brick_count(self):
        return self.brick_cols * self.brick_rows

    def brick_smaller(self):
        if self.brick_cols > self.brick_rows:
            return self.brick_rows
        else:
            return self.brick_cols




        # Default initial velocity for the ball.


        # Initialize our mouse listeners.
        # Draw bricks.

    def paddle(self):
        # Create a paddle.
        p = GRect(self.paddle_w, self.paddle_h, x=self.window_width / 2 - self.paddle_w / 2,
                  y=self.window_height - self.paddle_off)
        # draw the paddle
        p.filled = True
        p.fill_color = "blue"
        p.color = "blue"
        self.window.add(p)
        return p

        # add the paddle to the window

    def ball(self):
        # Center a filled ball in the graphical window.
        b = GOval(self.ball_radius*2, self.ball_radius*2)
        # draw the ball
        b.filled = True
        b.fill_color = "blue"
        b.color = "blue"
        self.window.add(b, x=self.window_width/2 - self.ball_radius, y=self.window_height/2 - self.ball_radius)
        return b

    def cannon(self, hull):
        if random.randrange(0, 8) > 6:
            laser1 = GRect(self.ball_radius * 0.5, self.ball_radius * 3)
            laser2 = GRect(self.ball_radius * 0.5, self.ball_radius * 3)
            laser1.filled = True
            laser1.fill_color = "red"
            laser1.color = "red"
            laser2.filled = True
            laser2.fill_color = "red"
            laser2.color = "red"
            self.window.add(laser1, x=hull.x, y=hull.y)
            self.window.add(laser2, x=hull.x + hull.width, y=hull.y)
            for i in range(50):
                laser1.move(0, 10)
                laser2.move(0, 10)
                pause(10)

    def brick(self):
        for y in range(self.brick_rows):
            for x in range(self.brick_cols):
                brick_iterating = GRect(self.brick_width, self.brick_height)
                brick_iterating.filled = True
                if y <= 1:
                    brick_iterating.fill_color = "red"
                    brick_iterating.color = "red"
                elif 1 < y <= 3:
                    brick_iterating.fill_color = "orange"
                    brick_iterating.color = "orange"
                elif 3 < y <= 5:
                    brick_iterating.fill_color = "yellow"
                    brick_iterating.color = "yellow"
                elif 5 < y <= 7:
                    brick_iterating.fill_color = "green"
                    brick_iterating.color = "green"
                else:
                    brick_iterating.fill_color = "blue"
                    brick_iterating.color = "blue"
                self.window.add(brick_iterating, 0 + x * (self.brick_width + self.brick_spacing),
                                0 + y * (self.brick_height + self.brick_spacing))

    # BOSS
    def tie_fighter_hull(self):
        size = self.brick_smaller()
        hull = GOval(size * 6, size * 6)
        hull.filled = True
        hull.fill_color = "grey"
        hull.color = "grey"
        self.window.add(hull, x=self.window_width/2 - hull.width/2, y=self.window_height/2- hull.height/2 - 400)
        return hull

    def tie_fighter_hull_window(self):
        size = self.brick_smaller()
        hull_window = GOval(size * 5, size * 5)
        hull_window.filled = True
        hull_window.color = "wheat"
        self.window.add(hull_window, x=self.window_width/2 - hull_window.width/2, y=self.window_height/2 - hull_window.height/2 - 400)
        return hull_window

    def tie_fighter_hull_window2(self):
        size = self.brick_smaller()
        hull_window2 = GOval(size * 2, size * 2)
        hull_window2.filled = True
        hull_window2.color = "wheat"
        self.window.add(hull_window2, x=self.window_width/2 - hull_window2.width/2, y=self.window_height/2 - hull_window2.height/2 - 400)
        return hull_window2

    def tie_fighter_r_skeleton(self, hull):
        size = self.brick_smaller()
        r_skeleton = GRect(size * 3, size * 2)
        r_skeleton.filled = True
        r_skeleton.fill_color = "grey"
        r_skeleton.color = "grey"
        self.window.add(r_skeleton, x=self.window_width/2 - hull.width/2 - r_skeleton.width,
                        y=self.window_height/2 - r_skeleton.height/2 - 400)
        return r_skeleton

    def tie_fighter_l_skeleton(self, hull):
        size = self.brick_smaller()
        l_skeleton = GRect(size * 3, size * 2)
        l_skeleton.filled = True
        l_skeleton.fill_color = "grey"
        l_skeleton.color = "grey"
        self.window.add(l_skeleton, x=hull.x + hull.width,
                        y=self.window_height/2 - l_skeleton.height/2 - 400)
        return l_skeleton

    def tie_fighter_r_wing(self, r_skeleton):
        size = self.brick_smaller()
        r_wing = GRect(size / 2, size * 12)
        r_wing.filled = True
        r_wing.fill_color = "grey"
        r_wing.color = "grey"
        self.window.add(r_wing, x=r_skeleton.x - r_wing.width,
                        y=r_skeleton.y + r_skeleton.height/2 - r_wing.height/2)
        return r_wing

    def tie_fighter_l_wing(self, l_skeleton):
        size = self.brick_smaller()
        l_wing = GRect(size / 2, size * 12)
        l_wing.filled = True
        l_wing.fill_color = "grey"
        l_wing.color = "grey"
        self.window.add(l_wing, x=l_skeleton.x + l_skeleton.width,
                        y=l_skeleton.y + l_skeleton.height/2 - l_wing.height/2)
        return l_wing

    def laser1(self, ball):
        laser1 = GRect(ball.width / 2 * 0.5, ball.width / 2 * 3)
        laser1.filled = True
        laser1.fill_color = "red"
        laser1.color = "red"
        return laser1

    def laser2(self, ball):
        laser2 = GRect(ball.width / 2 * 0.5, ball.width / 2 * 3)
        laser2.filled = True
        laser2.fill_color = "red"
        laser2.color = "red"
        return laser2

