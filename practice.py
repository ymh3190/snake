import pygame


class Cube(object):
    def __init__(self, start, dx=1, dy=0, color=(255, 0, 0)):
        pass

    def move(self, dx, dy):
        pass

    def draw(self, surface, eyes=False):
        pass


class Snake(object):
    def __init__(self, color, pos):
        pass

    def move(self):
        pass

    def reset(self, pos):
        pass

    def add_cube(self):
        pass


def draw_grid(w, rows, surface):
    sizeBtn = w // rows

    x = 0
    y = 0

    for _ in range(sizeBtn):
        """ 그리드를 그릴때 초기값+증가값, 즉 등차수열로 표현된다. """
        x += sizeBtn
        y += sizeBtn

        # (x, 0), (x, w): x축 일직선
        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        # (0, y), (w, y): y축 일직선
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))


def re_draw_window(surface):
    global width, rows
    surface.fill((0, 0, 0))
    draw_grid(width, rows, surface)
    pygame.display.update()


def random_snake(rows, item):
    pass


def message_box(subject, content):
    pass


def main():
    global width, rows
    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))

    clock = pygame.time.Clock()
    flag = True

    while flag:
        pygame.time.delay(50)
        clock.tick(10)

        re_draw_window(win)


main()

""" 
    1. 화면 그리기:
        pygame.display.set_mode(size=(0, 0), flags=0, depth=0, display=0, vsync=0) -> Surface: 창 설정
        pygame.time.delay()
        pygame.time.Clock() fps를 설정
        pygame.display.update() 변경 사항만 업데이트
        pygame.Surface.fill(color, rect=None, special_flags=0) -> Rect: 단색으로 창을 채운다
        pygame.draw.line(surface, color, start_pos, end_pos, width) -> Rect: 선 그리기
 """
