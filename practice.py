import pygame
from pygame.constants import K_LEFT


class Cube(object):
    def __init__(self, start, dx=1, dy=0, color=(255, 0, 0)):
        pass

    def move(self, dx, dy):
        pass

    def draw(self, surface, eyes=False):
        pass


class Snake(object):
    body = []
    turns = {}

    def __init__(self, color, pos):
        self.color = color
        self.head = Cube(pos)
        self.body.append(self.head)
        self.dx = 0
        self.dy = 1

    def move(self):
        """ 
            예를들어 뱀이 왼쪽으로 방향을 바꿨다고 가정하면, 머리부분을 제외한 나머지 부분은 여전히 앞으로 향한다.
            뱀의 나머지부분(머리제외)이 그 포인트 지점에 도착하면 그제서 왼쪽으로 방향을 바꾼다.
         """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for _ in keys:
                if keys[pygame.K_LEFT]:
                    self.dx = -1
                    self.dy = 0
                    """ 
                        방향전환했을 때 위치와 방향을 기억해야된다.
                        그래야 방향을 바꾼 지점에 나머지 부분이 도착하면 방향을 바꿀 수 있다
                     """
                    self.turns[self.head.pos[:]] = [self.dx, self.dy]

                elif keys[pygame.K_RIGHT]:
                    self.dx = 1
                    self.dy = 0
                    self.turns[self.head.pos[:]] = [self.dx, self.dy]

                elif keys[pygame.K_UP]:
                    self.dx = 0
                    self.dy = -1
                    self.turns[self.head.pos[:]] = [self.dx, self.dy]

                elif keys[pygame.K_DOWN]:
                    self.dx = 0
                    self.dy = 1
                    self.turns[self.head.pos[:]] = [self.dx, self.dy]

        for i, c in enumerate(self.body):  # c: cube
            p = c.pos[:]  # p: position
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body)-1:
                    self.turns.pop(p)
            else:
                """ 경계선 체크 """
                if c.dx == -1 and c.pos[0] <= 0:
                    c.pos = (c.rows-1, c.pos[1])
                elif c.dx == 1 and c.pos[0] >= c.rows-1:
                    c.pos = (0, c.pos[1])
                elif c.dy == 1 and c.pos[1] >= c.rows-1:
                    c.pos = (c.pos[0], 0)
                elif c.dy == -1 and c.pos[1] <= 0:
                    c.pos = (c.pos[0], c.rows-1)
                else:
                    c.move(c.dx, c.dy)

    def reset(self, pos):
        pass

    def add_cube(self):
        pass


def draw_grid(w, rows, surface):
    sizeBtn = w // rows

    x = 0
    y = 0

    for _ in range(rows):
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

    2. 스네이크 설정:
        pygame.event.get(eventtype=None) -> Eventlist: 모든 메시지를 가져오고. 타입 또는 타입 시퀀스가 주어지면 해당 메시지만 대기열에서 제거된다.
        ※ pygame에서 세로가 x방향 가로가 y 방향
        pygame.key.get_pressed() -> bools: 모든 키보드 버튼의 상태를 얻는다. 눌리면 True
 """
