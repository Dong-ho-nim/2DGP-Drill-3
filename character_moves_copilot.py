from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def draw_scene(x, y):
    clear_canvas()
    grass.draw(400, 30)
    character.draw(x, y)
    update_canvas()
    delay(0.01)

def move_rectangle():
    # 상단(왼쪽->오른쪽)
    for x in range(50, 750 + 1, 5):
        draw_scene(x, 550)
    # 우측(위->아래)
    for y in range(550, 50 - 1, -5):
        draw_scene(750, y)
    # 하단(오른쪽->왼쪽)
    for x in range(750, 50 - 1, -5):
        draw_scene(x, 50)
    # 좌측(아래->위)
    for y in range(50, 550 + 1, 5):
        draw_scene(50, y)

def move_circle():
    cx, cy, r = 400, 300, 250
    for deg in range(0, 360):
        x = cx + r * math.cos(math.radians(deg))
        y = cy + r * math.sin(math.radians(deg))
        draw_scene(x, y)

def move_triangle():
    # 1. 아래 변 (왼쪽 -> 오른쪽)
    for x in range(90, 710 + 1, 5):
        draw_scene(x, 100)
    # 2. 오른쪽 꼭짓점 -> 위 꼭짓점
    steps = 100
    for i in range(steps + 1):
        t = i / steps
        x = 710 + (400 - 710) * t
        y = 100 + (500 - 100) * t
        draw_scene(x, y)
    # 3. 위 꼭짓점 -> 왼쪽 꼭짓점
    for i in range(steps + 1):
        t = i / steps
        x = 400 + (90 - 400) * t
        y = 500 + (100 - 500) * t
        draw_scene(x, y)

def main():
    while True:
        move_rectangle()
        move_circle()
        move_triangle()

    close_canvas()

if __name__ == "__main__":
    main()
