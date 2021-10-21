import pgzrun

HEIGHT = 700
WIDTH = 1000

class Czolg:
    def __init__(self, x, y):
        self.body = Actor("tankbody", (x, y))
        self.gasienica = Actor("gasienice", (x, y+24.5))
        self.lufa = Actor("lufa", anchor=(0, 0), topleft=(x-7, y-22.5))
    def draw(self):
        self.gasienica.draw()
        self.lufa.draw()
        self.body.draw()
    def prawo(self):
        self.gasienica.x += 2
        self.lufa.x += 2
        self.body.x += 2
    def lewo(self):
        self.gasienica.x -= 2
        self.lufa.x -= 2
        self.body.x -= 2
    def lufagora(self):
        if self.lufa.angle < 90:
            self.lufa.angle += 2
    def lufadol(self):
        if self.lufa.angle > 0:
            self.lufa.angle -= 2


czolg = Czolg(200,630-24.5-15)
def draw():
    screen.fill((100, 120, 35))
    for i in range(WIDTH//70 + 1):
        screen.blit('grass', (i*70, 630))
    czolg.draw()

def update():
    if keyboard.RIGHT:
        czolg.prawo()
    if keyboard.LEFT:
        czolg.lewo()
    if keyboard.UP:
        czolg.lufagora()
    if keyboard.DOWN:
        czolg.lufadol()



pgzrun.go()
