import pygame
import math
import random
import sys

# --- AYARLAR ---
WIDTH, HEIGHT = 1000, 600
FPS = 60

FIELD_COLOR = (30, 130, 70)
LINE_COLOR = (230, 230, 230)

ROBOT_RADIUS = 20
ROBOT_WHEEL_BASE = 36   # mm scale in simulation units (affects rotation)
MAX_WHEEL_SPEED = 120.0  # units per second for wheel velocity (arbitrary units)
WHEEL_EFFECT = 1.0

BALL_RADIUS = 10
BALL_FRICTION = 0.99

SCORE_FONT_SIZE = 28

# Team colors
TEAM_US = (40, 180, 99)   # green
TEAM_US2 = (60, 140, 200) # blue
TEAM_THEM = (200, 60, 60) # red
TEAM_THEM2 = (180, 80, 140)# purple
BALL_COLOR = (240, 200, 60)

GOAL_WIDTH = 160
GOAL_DEPTH = 40

# --- PYGAME İNİT ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Robot Soccer Simulation")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, SCORE_FONT_SIZE)

# --- YARDIMCI FONKSİYONLAR ---
def clamp(x, a, b):
    return max(a, min(b, x))

def vec_len(x, y):
    return math.hypot(x, y)

# --- SINIFLAR ---
class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0.0
        self.vy = 0.0
        self.r = BALL_RADIUS

    def update(self, dt):
        # Basit hareket + sürtünme
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.vx *= BALL_FRICTION
        self.vy *= BALL_FRICTION

        # Saha sınır çarpışması (duvarlar)
        if self.x - self.r < 0:
            self.x = self.r
            self.vx = -self.vx * 0.7
        if self.x + self.r > WIDTH:
            self.x = WIDTH - self.r
            self.vx = -self.vx * 0.7
        if self.y - self.r < 0:
            self.y = self.r
            self.vy = -self.vy * 0.7
        if self.y + self.r > HEIGHT:
            self.y = HEIGHT - self.r
            self.vy = -self.vy * 0.7

    def draw(self, surf):
        pygame.draw.circle(surf, BALL_COLOR, (int(self.x), int(self.y)), self.r)

class Robot:
    def __init__(self, x, y, heading, color, name="R"):
        self.x = x
        self.y = y
        self.theta = heading  # radians
        self.color = color
        self.name = name

        # Wheel speeds (left, right) in simulation units (units/sec)
        self.wl = 0.0
        self.wr = 0.0

        # Robot parameters
        self.r = ROBOT_RADIUS
        self.wheel_base = ROBOT_WHEEL_BASE

        # Simple inertia / damping
        self.linear_damping = 0.99
        self.angular_damping = 0.99

    def set_wheel_speeds(self, wl, wr):
        # clamp to max wheel speed
        self.wl = clamp(wl, -MAX_WHEEL_SPEED, MAX_WHEEL_SPEED)
        self.wr = clamp(wr, -MAX_WHEEL_SPEED, MAX_WHEEL_SPEED)

    def update(self, dt):
        # Differential drive kinematics:
        # linear velocity v = (vr + vl)/2
        # angular velocity omega = (vr - vl)/wheel_base
        v = (self.wr + self.wl) * 0.5 * WHEEL_EFFECT
        omega = (self.wr - self.wl) / (self.wheel_base if self.wheel_base != 0 else 1.0)

        # integrate pose
        self.x += v * math.cos(self.theta) * dt
        self.y += v * math.sin(self.theta) * dt
        self.theta += omega * dt

        # keep angle normalized
        self.theta = (self.theta + math.pi) % (2 * math.pi) - math.pi

        # simple world boundary keep-in
        self.x = clamp(self.x, self.r, WIDTH - self.r)
        self.y = clamp(self.y, self.r, HEIGHT - self.r)

    def draw(self, surf):
        # body
        pygame.draw.circle(surf, self.color, (int(self.x), int(self.y)), self.r)
        # heading line
        hx = self.x + math.cos(self.theta) * self.r
        hy = self.y + math.sin(self.theta) * self.r
        pygame.draw.line(surf, (10,10,10), (self.x, self.y), (hx, hy), 3)
        # wheels (visual only)
        left_dx = math.cos(self.theta + math.pi/2) * (self.r * 0.6)
        left_dy = math.sin(self.theta + math.pi/2) * (self.r * 0.6)
        right_dx = -left_dx
        right_dy = -left_dy
        pygame.draw.rect(surf, (80,80,80), pygame.Rect(self.x + left_dx - 3, self.y + left_dy - 10, 6, 20))
        pygame.draw.rect(surf, (80,80,80), pygame.Rect(self.x + right_dx - 3, self.y + right_dy - 10, 6, 20))

    def push_ball(self, ball):
        # if robot overlaps ball, push it
        dx = ball.x - self.x
        dy = ball.y - self.y
        dist = math.hypot(dx, dy)
        if dist < self.r + ball.r:
            # push direction normalized
            if dist == 0:
                nx, ny = math.cos(self.theta), math.sin(self.theta)
            else:
                nx, ny = dx / dist, dy / dist
            # impart velocity to ball proportionally to robot forward speed
            # Robot forward speed estimate from wheels:
            v_forward = (self.wr + self.wl) * 0.5 * WHEEL_EFFECT
            # add some kick
            kick = clamp(v_forward * 0.3 + 40, 20, 200)
            ball.vx += nx * kick
            ball.vy += ny * kick
            # separate so they don't stick
            overlap = (self.r + ball.r) - dist
            ball.x += nx * overlap
            ball.y += ny * overlap

# --- SAHA VE OYUNCU AYARLARI ---
def draw_field(surf):
    surf.fill(FIELD_COLOR)
    # orta çizgi
    pygame.draw.line(surf, LINE_COLOR, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 4)
    # orta daire
    pygame.draw.circle(surf, LINE_COLOR, (WIDTH // 2, HEIGHT // 2), 60, 3)
    # sınır
    pygame.draw.rect(surf, LINE_COLOR, pygame.Rect(5, 5, WIDTH - 10, HEIGHT - 10), 4)
    # kaleler (solda ve sağda)
    gy = (HEIGHT - GOAL_WIDTH) // 2
    pygame.draw.rect(surf, (200,200,200), pygame.Rect(0, gy, GOAL_DEPTH, GOAL_WIDTH), 0)
    pygame.draw.rect(surf, (200,200,200), pygame.Rect(WIDTH - GOAL_DEPTH, gy, GOAL_DEPTH, GOAL_WIDTH), 0)

# --- OYUN KURULUMU ---
def reset_positions():
    # Return list of robots and ball
    robots = []
    # Our team (left side)
    r1 = Robot(WIDTH * 0.2, HEIGHT * 0.4, 0.0, TEAM_US, "A1")
    r2 = Robot(WIDTH * 0.2, HEIGHT * 0.6, 0.0, TEAM_US2, "A2")
    # Opponents (right side)
    r3 = Robot(WIDTH * 0.8, HEIGHT * 0.4, math.pi, TEAM_THEM, "B1")
    r4 = Robot(WIDTH * 0.8, HEIGHT * 0.6, math.pi, TEAM_THEM2, "B2")
    robots.extend([r1, r2, r3, r4])
    ball = Ball(WIDTH // 2, HEIGHT // 2)
    return robots, ball

robots, ball = reset_positions()
score_us = 0
score_them = 0

# --- BASİT AI: rakipler topa yönelir ---
def simple_ai_control(robot, ball):
    # Aim to point toward the ball and drive forward
    dx = ball.x - robot.x
    dy = ball.y - robot.y
    target_angle = math.atan2(dy, dx)
    angle_diff = (target_angle - robot.theta + math.pi) % (2 * math.pi) - math.pi

    # Proportional steering
    kp_turn = 80.0
    # forward base speed reduced if turning significantly
    forward = 80.0 * (1.0 - min(abs(angle_diff) / (math.pi/2), 1.0))
    turn = clamp(kp_turn * angle_diff, -MAX_WHEEL_SPEED, MAX_WHEEL_SPEED)

    wl = forward - turn
    wr = forward + turn
    robot.set_wheel_speeds(wl, wr)

# --- ANA DÖNGÜ ---
running = True
# for controlling two robots via keyboard, store wheel speed targets
while running:
    dt = clock.tick(FPS) / 1000.0  # saniye
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False
        elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_q:
            running = False

    # --- KULLANICI GİRDİSİ ---
    keys = pygame.key.get_pressed()
    # Player controls for our two robots:
    # Robot 0 (A1) -> W/S forward/back, A/D turn left/right
    w_forward = 0.0
    if keys[pygame.K_w]: w_forward += 100.0
    if keys[pygame.K_s]: w_forward -= 100.0
    turn_left = keys[pygame.K_a]
    turn_right = keys[pygame.K_d]
    if turn_left and not turn_right:
        # left turn -> reduce left wheel speed
        robots[0].set_wheel_speeds(w_forward * 0.3, w_forward)
    elif turn_right and not turn_left:
        robots[0].set_wheel_speeds(w_forward, w_forward * 0.3)
    else:
        robots[0].set_wheel_speeds(w_forward, w_forward)

    # Robot 1 (A2) -> I/K forward/back, J/L turn
    w2_forward = 0.0
    if keys[pygame.K_i]: w2_forward += 100.0
    if keys[pygame.K_k]: w2_forward -= 100.0
    if keys[pygame.K_j] and not keys[pygame.K_l]:
        robots[1].set_wheel_speeds(w2_forward * 0.3, w2_forward)
    elif keys[pygame.K_l] and not keys[pygame.K_j]:
        robots[1].set_wheel_speeds(w2_forward, w2_forward * 0.3)
    else:
        robots[1].set_wheel_speeds(w2_forward, w2_forward)

    # Opponents (robots[2], robots[3]) use AI
    simple_ai_control(robots[2], ball)
    simple_ai_control(robots[3], ball)

    # --- UPDATE FİZİK ---
    for r in robots:
        r.update(dt)
        r.push_ball(ball)

    ball.update(dt)

    # Gol kontrolü: top sol kalenin içinde -> THEM skor atmış (sağ takım öküzem)
    gy = (HEIGHT - GOAL_WIDTH) // 2
    # Left goal
    if ball.x - ball.r <= GOAL_DEPTH and gy <= ball.y <= gy + GOAL_WIDTH:
        score_them += 1
        robots, ball = reset_positions()
        # small delay optional - just reset positions
    # Right goal
    if ball.x + ball.r >= WIDTH - GOAL_DEPTH and gy <= ball.y <= gy + GOAL_WIDTH:
        score_us += 1
        robots, ball = reset_positions()

    # --- ÇİZİM ---
    draw_field(screen)
    ball.draw(screen)
    for r in robots:
        r.draw(screen)

    # scoreboard
    score_text = font.render(f"US {score_us}  -  THEM {score_them}", True, (250,250,250))
    screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, 8))

    # kontrol yardımcı notları
    help_text = font.render("WASD -> Team A Robot1   IJKL -> Team A Robot2   Q -> Quit", True, (220,220,220))
    screen.blit(help_text, (10, HEIGHT - 34))

    pygame.display.flip()

pygame.quit()
sys.exit()
