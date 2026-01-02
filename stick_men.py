import pygame
import pymunk
import pymunk.pygame_util
import random
import math

pygame.init()

# Ekran ayarları
WIDTH, HEIGHT = 1200, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Çöp Adam Simülasyonu - Gelişmiş Kontrol")
clock = pygame.time.Clock()

# Renkler
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (135, 206, 250)
GREEN = (34, 139, 34)
BROWN = (139, 90, 43)
SKIN = (245, 220, 180)
SHIRT = (100, 150, 200)
PANTS = (60, 110, 160)

# Pymunk fizik dünyası
space = pymunk.Space()
space.gravity = (0, 900)
draw_options = pymunk.pygame_util.DrawOptions(screen)

class StickMan:
    def __init__(self, x, y):
        self.bodies = {}
        self.shapes = []
        self.constraints = []
        
        mass = 5
        
        # Kafa
        head_body = pymunk.Body(mass, pymunk.moment_for_circle(mass, 0, 15))
        head_body.position = (x, y)
        head_shape = pymunk.Circle(head_body, 15)
        head_shape.friction = 0.5
        head_shape.color = SKIN + (255,)
        space.add(head_body, head_shape)
        self.bodies['head'] = head_body
        self.shapes.append(head_shape)
        
        # Gövde (göğüs)
        chest_body = pymunk.Body(mass * 2, pymunk.moment_for_box(mass * 2, (20, 35)))
        chest_body.position = (x, y + 35)
        chest_shape = pymunk.Poly.create_box(chest_body, (20, 35))
        chest_shape.friction = 0.5
        chest_shape.color = SHIRT + (255,)
        space.add(chest_body, chest_shape)
        self.bodies['chest'] = chest_body
        self.shapes.append(chest_shape)
        
        # Kalça
        hip_body = pymunk.Body(mass * 1.5, pymunk.moment_for_box(mass * 1.5, (22, 20)))
        hip_body.position = (x, y + 65)
        hip_shape = pymunk.Poly.create_box(hip_body, (22, 20))
        hip_shape.friction = 0.5
        hip_shape.color = PANTS + (255,)
        space.add(hip_body, hip_shape)
        self.bodies['hip'] = hip_body
        self.shapes.append(hip_shape)
        
        # Sol üst kol
        l_upper_arm = pymunk.Body(mass * 0.5, pymunk.moment_for_box(mass * 0.5, (10, 28)))
        l_upper_arm.position = (x - 15, y + 32)
        l_upper_arm_shape = pymunk.Poly.create_box(l_upper_arm, (10, 28))
        l_upper_arm_shape.friction = 0.5
        l_upper_arm_shape.color = SHIRT + (255,)
        space.add(l_upper_arm, l_upper_arm_shape)
        self.bodies['l_upper_arm'] = l_upper_arm
        self.shapes.append(l_upper_arm_shape)
        
        # Sol alt kol
        l_lower_arm = pymunk.Body(mass * 0.4, pymunk.moment_for_box(mass * 0.4, (8, 28)))
        l_lower_arm.position = (x - 15, y + 56)
        l_lower_arm_shape = pymunk.Poly.create_box(l_lower_arm, (8, 28))
        l_lower_arm_shape.friction = 0.5
        l_lower_arm_shape.color = SKIN + (255,)
        space.add(l_lower_arm, l_lower_arm_shape)
        self.bodies['l_lower_arm'] = l_lower_arm
        self.shapes.append(l_lower_arm_shape)
        
        # Sağ üst kol
        r_upper_arm = pymunk.Body(mass * 0.5, pymunk.moment_for_box(mass * 0.5, (10, 28)))
        r_upper_arm.position = (x + 15, y + 32)
        r_upper_arm_shape = pymunk.Poly.create_box(r_upper_arm, (10, 28))
        r_upper_arm_shape.friction = 0.5
        r_upper_arm_shape.color = SHIRT + (255,)
        space.add(r_upper_arm, r_upper_arm_shape)
        self.bodies['r_upper_arm'] = r_upper_arm
        self.shapes.append(r_upper_arm_shape)
        
        # Sağ alt kol
        r_lower_arm = pymunk.Body(mass * 0.4, pymunk.moment_for_box(mass * 0.4, (8, 28)))
        r_lower_arm.position = (x + 15, y + 56)
        r_lower_arm_shape = pymunk.Poly.create_box(r_lower_arm, (8, 28))
        r_lower_arm_shape.friction = 0.5
        r_lower_arm_shape.color = SKIN + (255,)
        space.add(r_lower_arm, r_lower_arm_shape)
        self.bodies['r_lower_arm'] = r_lower_arm
        self.shapes.append(r_lower_arm_shape)
        
        # Sol üst bacak
        l_upper_leg = pymunk.Body(mass * 0.8, pymunk.moment_for_box(mass * 0.8, (12, 35)))
        l_upper_leg.position = (x - 8, y + 93)
        l_upper_leg_shape = pymunk.Poly.create_box(l_upper_leg, (12, 35))
        l_upper_leg_shape.friction = 0.8
        l_upper_leg_shape.color = PANTS + (255,)
        space.add(l_upper_leg, l_upper_leg_shape)
        self.bodies['l_upper_leg'] = l_upper_leg
        self.shapes.append(l_upper_leg_shape)
        
        # Sol alt bacak
        l_lower_leg = pymunk.Body(mass * 0.6, pymunk.moment_for_box(mass * 0.6, (10, 35)))
        l_lower_leg.position = (x - 8, y + 128)
        l_lower_leg_shape = pymunk.Poly.create_box(l_lower_leg, (10, 35))
        l_lower_leg_shape.friction = 0.8
        l_lower_leg_shape.color = SKIN + (255,)
        space.add(l_lower_leg, l_lower_leg_shape)
        self.bodies['l_lower_leg'] = l_lower_leg
        self.shapes.append(l_lower_leg_shape)
        
        # Sağ üst bacak
        r_upper_leg = pymunk.Body(mass * 0.8, pymunk.moment_for_box(mass * 0.8, (12, 35)))
        r_upper_leg.position = (x + 8, y + 93)
        r_upper_leg_shape = pymunk.Poly.create_box(r_upper_leg, (12, 35))
        r_upper_leg_shape.friction = 0.8
        r_upper_leg_shape.color = PANTS + (255,)
        space.add(r_upper_leg, r_upper_leg_shape)
        self.bodies['r_upper_leg'] = r_upper_leg
        self.shapes.append(r_upper_leg_shape)
        
        # Sağ alt bacak
        r_lower_leg = pymunk.Body(mass * 0.6, pymunk.moment_for_box(mass * 0.6, (10, 35)))
        r_lower_leg.position = (x + 8, y + 128)
        r_lower_leg_shape = pymunk.Poly.create_box(r_lower_leg, (10, 35))
        r_lower_leg_shape.friction = 0.8
        r_lower_leg_shape.color = SKIN + (255,)
        space.add(r_lower_leg, r_lower_leg_shape)
        self.bodies['r_lower_leg'] = r_lower_leg
        self.shapes.append(r_lower_leg_shape)
        
        # Eklemler
        self.create_joint(head_body, chest_body, (x, y + 15), 50, 50)
        self.create_joint(chest_body, hip_body, (x, y + 52), 80, 80)
        self.create_joint(chest_body, l_upper_arm, (x - 10, y + 22), 100, 100)
        self.create_joint(l_upper_arm, l_lower_arm, (x - 15, y + 46), 100, 100)
        self.create_joint(chest_body, r_upper_arm, (x + 10, y + 22), 100, 100)
        self.create_joint(r_upper_arm, r_lower_arm, (x + 15, y + 46), 100, 100)
        self.create_joint(hip_body, l_upper_leg, (x - 8, y + 75), 100, 100)
        self.create_joint(l_upper_leg, l_lower_leg, (x - 8, y + 110), 120, 120)
        self.create_joint(hip_body, r_upper_leg, (x + 8, y + 75), 100, 100)
        self.create_joint(r_upper_leg, r_lower_leg, (x + 8, y + 110), 120, 120)
        
        self.walk_phase = 0
        self.is_grounded = False
        
    def create_joint(self, body_a, body_b, pos, stiff, damp):
        joint = pymunk.PinJoint(body_a, body_b, 
                                body_a.world_to_local(pos),
                                body_b.world_to_local(pos))
        joint.error_bias = 0.15
        
        damped = pymunk.DampedRotarySpring(body_a, body_b, 0, stiff, damp)
        space.add(joint, damped)
        self.constraints.extend([joint, damped])
        
    def check_grounded(self):
        # Ayaklar yere değiyor mu kontrol et
        l_leg_y = self.bodies['l_lower_leg'].position.y
        r_leg_y = self.bodies['r_lower_leg'].position.y
        ground_level = HEIGHT - 70
        
        self.is_grounded = (l_leg_y > ground_level - 30 or r_leg_y > ground_level - 30)
        
    def apply_movement(self, direction):
        if not self.is_grounded:
            return
            
        force = 3000
        self.walk_phase += 0.15
        
        # Gövdeyi ileri it
        self.bodies['hip'].apply_force_at_world_point(
            (direction * force, 0), 
            self.bodies['hip'].position
        )
        
        self.bodies['chest'].apply_force_at_world_point(
            (direction * force * 0.8, 0), 
            self.bodies['chest'].position
        )
        
        # Bacak hareketi - daha güçlü ve koordineli
        swing = math.sin(self.walk_phase)
        
        # Sol bacak
        self.bodies['l_upper_leg'].apply_force_at_world_point(
            (direction * force * swing * 0.6, -force * 0.4),
            self.bodies['l_upper_leg'].position
        )
        self.bodies['l_lower_leg'].apply_force_at_world_point(
            (direction * force * swing * 0.4, -force * 0.2),
            self.bodies['l_lower_leg'].position
        )
        
        # Sağ bacak (ters faz)
        self.bodies['r_upper_leg'].apply_force_at_world_point(
            (direction * force * -swing * 0.6, -force * 0.4),
            self.bodies['r_upper_leg'].position
        )
        self.bodies['r_lower_leg'].apply_force_at_world_point(
            (direction * force * -swing * 0.4, -force * 0.2),
            self.bodies['r_lower_leg'].position
        )
        
        # Kollar da sallanır
        self.bodies['l_upper_arm'].apply_force_at_world_point(
            (direction * force * -swing * 0.2, 0),
            self.bodies['l_upper_arm'].position
        )
        self.bodies['r_upper_arm'].apply_force_at_world_point(
            (direction * force * swing * 0.2, 0),
            self.bodies['r_upper_arm'].position
        )
    
    def jump(self):
        if not self.is_grounded:
            return
            
        jump_force = 15000
        
        # Tüm vücut parçalarına yukarı kuvvet uygula
        self.bodies['hip'].apply_impulse_at_world_point((0, -jump_force), self.bodies['hip'].position)
        self.bodies['chest'].apply_impulse_at_world_point((0, -jump_force * 0.8), self.bodies['chest'].position)
        self.bodies['l_upper_leg'].apply_impulse_at_world_point((0, -jump_force * 0.6), self.bodies['l_upper_leg'].position)
        self.bodies['r_upper_leg'].apply_impulse_at_world_point((0, -jump_force * 0.6), self.bodies['r_upper_leg'].position)
    
    def get_position(self):
        return self.bodies['chest'].position
    
    def reset_position(self, x, y):
        # Tüm vücut parçalarını sıfırla
        offset = {
            'head': (0, 0),
            'chest': (0, 35),
            'hip': (0, 65),
            'l_upper_arm': (-15, 32),
            'l_lower_arm': (-15, 56),
            'r_upper_arm': (15, 32),
            'r_lower_arm': (15, 56),
            'l_upper_leg': (-8, 93),
            'l_lower_leg': (-8, 128),
            'r_upper_leg': (8, 93),
            'r_lower_leg': (8, 128)
        }
        
        for name, body in self.bodies.items():
            body.position = (x + offset[name][0], y + offset[name][1])
            body.velocity = (0, 0)
            body.angular_velocity = 0
            body.angle = 0

# Zemin
def create_ground():
    ground_body = pymunk.Body(body_type=pymunk.Body.STATIC)
    ground_shape = pymunk.Segment(ground_body, (0, HEIGHT - 50), (WIDTH, HEIGHT - 50), 5)
    ground_shape.friction = 1.0
    ground_shape.color = GREEN + (255,)
    space.add(ground_body, ground_shape)

# Engel
def create_obstacle(x, height, width):
    obstacle_body = pymunk.Body(body_type=pymunk.Body.STATIC)
    obstacle_shape = pymunk.Poly.create_box(obstacle_body, (width, height))
    obstacle_body.position = (x, HEIGHT - 50 - height // 2)
    obstacle_shape.friction = 0.9
    obstacle_shape.color = BROWN + (255,)
    space.add(obstacle_body, obstacle_shape)
    return obstacle_body, obstacle_shape

# Dinamik engel (iterek düşen kutu)
def create_dynamic_box(x, y, size):
    box_body = pymunk.Body(10, pymunk.moment_for_box(10, (size, size)))
    box_body.position = (x, y)
    box_shape = pymunk.Poly.create_box(box_body, (size, size))
    box_shape.friction = 0.7
    box_shape.color = RED + (255,)
    space.add(box_body, box_shape)
    return box_body, box_shape

# Oyun başlangıcı
create_ground()
stickman = StickMan(150, 100)

# Engeller
obstacles = []
obstacles.append(create_obstacle(400, 40, 60))
obstacles.append(create_obstacle(700, 60, 80))
obstacles.append(create_obstacle(1000, 35, 50))

# Dinamik kutular
boxes = []
boxes.append(create_dynamic_box(550, 300, 40))
boxes.append(create_dynamic_box(850, 250, 35))

# Ana döngü
running = True
font = pygame.font.Font(None, 32)
small_font = pygame.font.Font(None, 24)

keys_pressed = {'left': False, 'right': False}

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                keys_pressed['left'] = True
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                keys_pressed['right'] = True
            elif event.key == pygame.K_SPACE or event.key == pygame.K_UP or event.key == pygame.K_w:
                stickman.jump()
            elif event.key == pygame.K_r:
                stickman.reset_position(150, 100)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                keys_pressed['left'] = False
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                keys_pressed['right'] = False
    
    # Hareket kontrolü
    stickman.check_grounded()
    
    if keys_pressed['left']:
        stickman.apply_movement(-1)
    elif keys_pressed['right']:
        stickman.apply_movement(1)
    
    # Fizik güncelleme
    space.step(1/60.0)
    
    # Çizim
    screen.fill(BLUE)
    space.debug_draw(draw_options)
    
    # Durum bilgisi
    status = "Havada" if not stickman.is_grounded else "Yerde"
    status_color = RED if not stickman.is_grounded else GREEN
    status_text = small_font.render(f"Durum: {status}", True, status_color)
    screen.blit(status_text, (WIDTH - 150, 10))
    
    # Kontroller
    instructions = [
        "A/SOL OK: Sola git",
        "D/SAĞ OK: Sağa git",
        "W/SPACE/YUKARI: Zıpla",
        "R: Yeniden başlat"
    ]
    
    for i, text in enumerate(instructions):
        text_surface = small_font.render(text, True, WHITE)
        screen.blit(text_surface, (10, 10 + i * 30))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()