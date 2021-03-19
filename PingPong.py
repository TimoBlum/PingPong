import pygame, random, math

pygame.init()

x = 800
y = 500
win = pygame.display.set_mode((x, y))
pygame.display.set_caption("Ping Pong")
run = True
smack = 1
score = 0
WHITE = (255, 255, 255)
clock = pygame.time.Clock()
winner = 0


class Ball:
    def __init__(self, radius):
        self.xvel = 3
        self.yvel = random.randint(2, 5)
        diry = random.randint(0, 1)
        dirx = random.randint(0, 1)
        if dirx == 1:
            self.xvel = - self.xvel
        if diry == 1:
            self.yvel = - self.yvel
        self.x = x // 2
        self.y = y // 2
        self.radius = radius

    def draw(self):
        pygame.draw.circle(win, (255, 170, 0), (self.x, self.y), self.radius, width=100)

    def check(self):
        global winner, smack, score
        # Bounce off the top and bottom
        if self.y >= y - self.radius:
            self.yvel = - self.yvel
        if self.y <= self.radius:
            self.yvel = - self.yvel

        # Bounce off the Players
        if self.x > x - P2.width - self.radius - self.xvel:
            if not self.y > P2.y + P2.height and not self.y < P2.y:
                self.xvel = 1.1 * - self.xvel
                smack += 0.1
                score += 1
            else:
                winner = 1

        if self.x < P1.width + self.radius:
            if not self.y > P1.y + P1.height and not self.y < P1.y:
                self.xvel = 1.1 * - self.xvel
                smack += 0.1
                score += 1
            else:
                winner = 2

    def move(self):
        self.x += self.xvel
        self.y += self.yvel


class Player:
    def __init__(self, color, nr):
        self.color = color
        self.width = 20
        self.height = 100
        self.vel = 5
        self.nr = nr
        if self.nr == 1:
            self.x = 0
        elif self.nr == 2:
            self.x = x - self.width
        self.y = y // 2

    def draw(self):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

    def move(self):
        global x, y, smack
        keys = pygame.key.get_pressed()
        if self.nr == 1:
            if keys[pygame.K_w] and self.y >= self.vel:
                self.y -= self.vel * smack
            if keys[pygame.K_s] and self.y <= y - self.height:
                self.y += self.vel * smack
        elif self.nr == 2:
            if keys[pygame.K_o] and self.y >= self.vel:
                self.y -= self.vel * smack
            if keys[pygame.K_l] and self.y <= y - self.height:
                self.y += self.vel * smack


P1 = Player((255, 0, 0), 1)
P2 = Player((0, 0, 255), 2)
ball = Ball(10)


def euclidian(x1, y1, x2, y2):
    return math.sqrt(((x2 - x1) ** 2) + (y2 - y1) ** 2)


def redrawWin():
    global run
    win.fill(WHITE)
    if winner != 1 or 2:
        P1.draw()
        P1.move()
        P2.draw()
        P2.move()
        ball.check()
        ball.draw()
        ball.move()
    if winner == 1:
        win.fill((255, 0, 0))
        pygame.display.update()
        pygame.time.wait(4000)
        run = False
    elif winner == 2:
        win.fill((0, 0, 255))
        pygame.display.update()
        pygame.time.wait(4000)
        run = False
    print("Current score is: ", score)
    pygame.display.update()


def main():
    global run
    while run:
        clock.tick(5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        if run:
            redrawWin()


main()
