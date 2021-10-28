import pgzrun
import math

HEIGHT = 700
WIDTH = 1000

class Pocisk(Actor):
    def __init__(self, x, y, angle):
        super(Pocisk, self).__init__("tankbullert", (x, y))
        self.angle = angle
        self.doUsuniecia = False
    def ruch(self):
        self.x += 4*math.cos(math.radians(self.angle))
        self.y -= 4*math.sin(math.radians(self.angle))


class Czolg:
    def __init__(self, x, y):
        self.body = Actor("tankbody", (x, y))
        self.gasienica = Actor("gasienice", (x, y+24.5))
        self.lufa = Actor("lufa", anchor=(0, 1), topleft=(x-7, y-22.5))
        self.pociski = []
        self.blokadaStrzalu = False
    def draw(self):
        self.gasienica.draw()
        self.lufa.draw()
        self.body.draw()
        for i in self.pociski:
            i.draw()
    def update(self):
        for i in self.pociski:
            i.ruch()
            if i.x>WIDTH or i.y<0:
                i.doUsuniecia = True
        tmp = []
        for i in self.pociski:
            if i.doUsuniecia == False:
                tmp.append(i)
        self.pociski = tmp
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
    def zdejmijBlokade(self):
        self.blokadaStrzalu = False

    def wystrzel(self):
        if not self.blokadaStrzalu:
            self.pociski.append(Pocisk(self.lufa.x, self.lufa.y, self.lufa.angle))
            self.blokadaStrzalu = True
            clock.schedule_unique(self.zdejmijBlokade, 1)


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
    if keyboard.SPACE:
        czolg.wystrzel()
    czolg.update()
    print(czolg.pociski)


pgzrun.go()
