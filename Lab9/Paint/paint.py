import pygame
import math
 
pygame.init()
 
WIDTH = 800
HEIGHT = 600
 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
 
# Colors
current_color = (0, 0, 0)
 
colorBLACK = (0, 0, 0)
colorWHITE = (255, 255, 255)
colorGREY = (128, 128, 128)
colorGREEN = (0, 255, 0)
colorRED = (255, 0, 0)
colorBLUE = (0, 0, 255)
colorPURPLE = (128, 0, 128)
 
# Modes
MODE_LINE = 0
MODE_RECTANGLE = 1
MODE_CIRCLE = 2
MODE_SQUARE = 3
MODE_RIGHT_TRIANGLE = 4
MODE_EQUILATERAL_TRIANGLE = 5
MODE_RHOMBUS = 6
MODE_ERASER = 7
 
current_mode = MODE_LINE
 
THICKNESS = 5
LMBpressed = False
 
currX = 0
currY = 0
 
prevX = 0
prevY = 0
 
# Layers
line_layer = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
rectangle_layer = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
circle_layer = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
square_layer = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
right_triangle_layer = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
equilateral_triangle_layer = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
rhombus_layer = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
eraser_layer = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
 
# Function to draw
def draw_line(x1, y1, x2, y2, thickness):
    pygame.draw.line(line_layer, current_color, (x1, y1), (x2, y2), thickness)
 
def draw_rectangle(x1, y1, x2, y2, thickness):
    pygame.draw.rect(rectangle_layer, current_color, (x1, y1, x2 - x1, y2 - y1), thickness)
 
def draw_circle(x, y, radius, thickness):
    pygame.draw.circle(circle_layer, current_color, (x, y), radius, thickness)
 
def draw_square(x1, y1, x2, y2, thickness):
    size = max(abs(x2 - x1), abs(y2 - y1))
    if x2 < x1:
        x1 -= size
    if y2 < y1:
        y1 -= size
    pygame.draw.rect(square_layer, current_color, (x1, y1, size, size), thickness)
 
def draw_right_triangle(x1, y1, x2, y2, thickness):
    pygame.draw.polygon(right_triangle_layer, current_color, [(x1, y1), (x2, y1), (x1, y2)], thickness)
 
def draw_equilateral_triangle(x, y, size, thickness):
    height = (3 ** 0.5 / 2) * size
    p1 = (x, y - height / 2)
    p2 = (x + size / 2, y + height / 2)
    p3 = (x - size / 2, y + height / 2)
    pygame.draw.polygon(equilateral_triangle_layer, current_color, [p1, p2, p3], thickness)
 
def draw_rhombus(x1, y1, x2, y2, thickness):
    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2
 
    width = abs(x2 - x1)
    height = abs(y2 - y1)
 
    top = (center_x, y1)
    right = (x2, center_y)
    bottom = (center_x, y2)
    left = (x1, center_y)
 
    pygame.draw.polygon(rhombus_layer, colorBLACK, [top, right, bottom, left], thickness)
 
def draw_eraser(x, y, thickness):
    eraser_layer.fill((0, 0, 0, 0))  # Clear the eraser layer
    radius = thickness // 2
    border_radius = radius + 2
    pygame.draw.circle(eraser_layer, colorGREY, (x, y), border_radius)
    pygame.draw.circle(eraser_layer, colorWHITE, (x, y), radius)
 
    # Erase content from other drawing layers within the eraser circle
    erase_rect = pygame.Rect(x - radius, y - radius, thickness, thickness)
    line_layer.fill((0, 0, 0, 0), erase_rect)
    rectangle_layer.fill((0, 0, 0, 0), erase_rect)
    circle_layer.fill((0, 0, 0, 0), erase_rect)
    square_layer.fill((0, 0, 0, 0), erase_rect)
    right_triangle_layer.fill((0, 0, 0, 0), erase_rect)
    equilateral_triangle_layer.fill((0, 0, 0, 0), erase_rect)
    rhombus_layer.fill((0, 0, 0, 0), erase_rect)
 
def clear_eraser_layer():
    eraser_layer.fill((0, 0, 0, 0))
 
# Font setup
font = pygame.font.Font(None, 36)
 
done = False
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                LMBpressed = True
                prevX, prevY = event.pos
 
                if current_mode == MODE_RECTANGLE:
                    start_pos = event.pos  # Store the start position for drawing rectangle
                elif current_mode == MODE_CIRCLE:
                    start_pos = event.pos  # Store the center position for drawing circle
                elif current_mode == MODE_SQUARE:
                    start_pos = event.pos  # Store the start position for drawing square
                elif current_mode == MODE_RIGHT_TRIANGLE:
                    start_pos = event.pos  # Store the start position for drawing right triangle
                elif current_mode == MODE_EQUILATERAL_TRIANGLE:
                    start_pos = event.pos  # Store the center position for drawing equilateral triangle
                elif current_mode == MODE_RHOMBUS:
                    start_pos = event.pos  # Store the start position for drawing rhombus
 
            elif event.button == 3:  # Right mouse button
                if current_mode == MODE_ERASER:
                    LMBpressed = True
                    prevX, prevY = event.pos
 
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                LMBpressed = False
 
                if current_mode == MODE_RECTANGLE:
                    end_pos = event.pos  # Store the end position for drawing rectangle
                    draw_rectangle(start_pos[0], start_pos[1], end_pos[0], end_pos[1], THICKNESS)
                    rectangle_layer.blit(rectangle_layer, (0, 0))  # Merge drawn rectangle onto the main layer
 
                elif current_mode == MODE_CIRCLE:
                    end_pos = event.pos  # Store the end position for drawing circle
                    radius = int(math.hypot(end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
                    draw_circle(start_pos[0], start_pos[1], radius, THICKNESS)
                    circle_layer.blit(circle_layer, (0, 0))  # Merge drawn circle onto the main layer
 
                elif current_mode == MODE_SQUARE:
                    end_pos = event.pos  # Store the end position for drawing square
                    draw_square(start_pos[0], start_pos[1], end_pos[0], end_pos[1], THICKNESS)
                    square_layer.blit(square_layer, (0, 0))  # Merge drawn square onto the main layer
 
                elif current_mode == MODE_RIGHT_TRIANGLE:
                    end_pos = event.pos  # Store the end position for drawing right triangle
                    draw_right_triangle(start_pos[0], start_pos[1], end_pos[0], end_pos[1], THICKNESS)
                    right_triangle_layer.blit(right_triangle_layer, (0, 0))  # Merge drawn triangle onto the main layer
 
                elif current_mode == MODE_EQUILATERAL_TRIANGLE:
                    end_pos = event.pos  # Store the end position for drawing equilateral triangle
                    size = int(math.hypot(end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
                    draw_equilateral_triangle(start_pos[0], start_pos[1], size, THICKNESS)
                    equilateral_triangle_layer.blit(equilateral_triangle_layer, (0, 0))  # Merge drawn triangle onto the main layer
 
                elif current_mode == MODE_RHOMBUS:
                    end_pos = event.pos  # Store the end position for drawing rhombus
                    draw_rhombus(start_pos[0], start_pos[1], end_pos[0], end_pos[1], THICKNESS)
                    rhombus_layer.blit(rhombus_layer, (0, 0))  # Merge drawn rhombus onto the main layer
 
            elif event.button == 3:  # Right mouse button
                if current_mode == MODE_ERASER:
                    LMBpressed = False
 
        elif event.type == pygame.MOUSEMOTION:
            if LMBpressed:
                currX, currY = event.pos
                if current_mode == MODE_LINE:
                    draw_line(currX, currY, prevX, prevY, THICKNESS)
                    prevX, prevY = currX, currY
                elif current_mode == MODE_ERASER:
                    draw_eraser(currX, currY, THICKNESS)
 
        elif event.type == pygame.KEYDOWN:
            # Change thickness regardless of the drawing mode
            if event.key == pygame.K_EQUALS:
                THICKNESS += 1
            elif event.key == pygame.K_MINUS:
                THICKNESS = max(1, THICKNESS - 1)
 
            # Change color
            elif event.key == pygame.K_r:
                current_color = colorRED
            elif event.key == pygame.K_g:
                current_color = colorGREEN
            elif event.key == pygame.K_b:
                current_color = colorBLUE
            elif event.key == pygame.K_BACKSPACE:
                current_color = colorBLACK
            elif event.key == pygame.K_p:
                current_color = colorPURPLE
 
            # Change drawing mode
            elif event.key == pygame.K_1:
                current_mode = MODE_LINE
            elif event.key == pygame.K_2:
                current_mode = MODE_RECTANGLE
            elif event.key == pygame.K_3:
                current_mode = MODE_CIRCLE
            elif event.key == pygame.K_4:
                current_mode = MODE_SQUARE
            elif event.key == pygame.K_5:
                current_mode = MODE_RIGHT_TRIANGLE
            elif event.key == pygame.K_6:
                current_mode = MODE_EQUILATERAL_TRIANGLE
            elif event.key == pygame.K_7:
                current_mode = MODE_RHOMBUS
            elif event.key == pygame.K_e:
                current_mode = MODE_ERASER
 
    # Drawing help text
    help_text = [
        "1: Line",
        "2: Rectangle",
        "3: Circle",
        "4: Square",
        "5: Right Triangle",
        "6: Equilateral Triangle",
        "7: Rhombus",
        "e: Eraser",
        "Change Color: r, g, b, p, Backspace"
    ]
 
    # Render help text onto a surface
    help_surface = pygame.Surface((200, 300), pygame.SRCALPHA)
    y_offset = 0
    for text in help_text:
        help_render = font.render(text, True, colorBLACK)
        help_surface.blit(help_render, (0, y_offset))
        y_offset += 30
 
    screen.fill(colorWHITE)
 
    # Blit layers onto the screen
    screen.blit(line_layer, (0, 0))
    screen.blit(rectangle_layer, (0, 0))
    screen.blit(circle_layer, (0, 0))
    screen.blit(square_layer, (0, 0))
    screen.blit(right_triangle_layer, (0, 0))
    screen.blit(equilateral_triangle_layer, (0, 0))
    screen.blit(rhombus_layer, (0, 0))
    screen.blit(eraser_layer, (0, 0))
 
    # Draw help text on the top right corner
    screen.blit(help_surface, (WIDTH - help_surface.get_width(), 0))
 
    pygame.display.flip()
 
pygame.quit()


