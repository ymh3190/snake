# pygame은 왼쪽상단에서 그린다.
import pygame


class Cube(object):
    rows = 20
    w = 500

    def __init__(self, start, dx=1, dy=0, color=(255, 0, 0)):
        self.pos = start
        self.dx = 1
        self.dy = 0
        self.color = color

    def move(self, dx, dy):
        self.dx = dx
        self.dy = dy
        self.pos(self.pos[0]+self.dx, self.pos[1]+self.dy)

    def draw(self, surface, eyes=False):
        dis = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(surface, self.color, (i*dis+1, j*dis+1, dis-2, dis-2))
        if eyes:
            # 사각형을 정확하게 그리기
            centre = dis//2
            radius = 3
            circle_middle = (i*dis+centre-radius, j*dis+8)
            circle_middle2 = (i*dis+dis-radius*2, j*dis+8)
            pygame.draw.circle(surface, (0, 0, 0), circle_middle, radius)
            pygame.draw.circle(surface, (0, 0, 0), circle_middle2, radius)


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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for key in keys:
                if key[pygame.K_LEFT]:
                    self.dx = - 1
                    self.dy = 0
                    self.turns[self.head.pos[:]] = [self.dx, self.dy]

                elif key[pygame.K_RIGHT]:
                    self.dx = 1
                    self.dy = 0
                    self.turns[self.head.pos[:]] = [self.dx, self.dy]

                elif key[pygame.K_UP]:
                    self.dx = 0
                    self.dy = -1
                    self.turns[self.head.pos[:]] = [self.dx, self.dy]

                elif key[pygame.K_DOWN]:
                    self.dx = 0
                    self.dy = 1
                    self.turns[self.head.pos[:]] = [self.dx, self.dy]

        for i, v in enumerate(self.body):
            p = v.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                v.move(turn[0], turn[1])
                if i == len(self.body)-1:
                    self.turns.pop(p)
            else:
                # 경계선 체크
                if v.dx == -1 and v.pos[0] <= 0:
                    v.pos = (v.rows-1, v.pos[1])
                elif v.dx == 1 and v.pos[0] >= v.rows-1:
                    v.pos = (0, v.pos[1])
                elif v.dy == 1 and v.pos[1] >= v.rows-1:
                    v.pos = (v.pos[0], 0)
                elif v.dy == -1 and v.pos[1] <= 0:
                    v.pos = (v.pos[0], v.rows-1)
                else:
                    v.move(v.dx, v.dy)

    def reset(self):
        pass

    def add_cube(self):
        pass

    def draw(self, surface):
        for i, v in enumerate(self.body):
            if i == 0:
                v.draw(surface, True)
            else:
                v.draw(surface)


def draw_grid(w, rows, surface):
    sizeBtn = w // rows

    x = 0
    y = 0
    for _ in range(rows):
        x = x+sizeBtn
        y = y+sizeBtn

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))


def re_draw_window(surface):
    global rows, width, s
    surface.fill((0, 0, 0))
    s.draw(surface)
    draw_grid(width, rows, surface)
    pygame.display.update()


def random_snack(rows, items):
    pass


def message_box(subject, content):
    pass


def main():
    global width, rows, s
    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
    s = Snake((255, 0, 0), (10, 10))
    flag = True

    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(50)
        clock.tick(10)  # framerate: 10(fps)

        re_draw_window(win)


main()
