import pgzrun
import math

HEIGHT = 700
WIDTH = 1000

class Pocisk(Actor):
    def __init__(self, x, y, angle, kierunek = 1, sprite = "tankbullert"):
        self.kieruek = kierunek
        super(Pocisk, self).__init__(sprite, (x, y))
        self.angle = angle
        self.doUsuniecia = False
    def ruch(self):
        self.x += 4*math.cos(math.radians(self.angle)) * self.kieruek
        self.y -= 4*math.sin(math.radians(self.angle)) * self.kieruek


class Czolg:
    def __init__(self, x, y, body, gasienica, lufa):
        self.body = Actor(body, (x, y))
        self.gasienica = Actor(gasienica, (x, y+24.5))
        self.lufa = Actor(lufa, anchor=(0,0), center=(x+3, y-18))
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

class Czolg2(Czolg):
    def __init__(self, x, y, body, gasienica, lufa):
        super(Czolg2, self).__init__(x, y, body, gasienica, lufa)
        self.lufa = Actor(lufa, anchor=(60, 25), center=(x -7, y - 18))
    def lufagora(self):
        if self.lufa.angle > -90:
            self.lufa.angle -= 2
    def lufadol(self):
        if self.lufa.angle < 0:
            self.lufa.angle += 2
    def wystrzel(self):
        if not self.blokadaStrzalu:
            self.pociski.append(Pocisk(self.lufa.x, self.lufa.y, self.lufa.angle, -1, "odwrocona"))
            self.blokadaStrzalu = True
            clock.schedule_unique(self.zdejmijBlokade, 1)


czolg = Czolg(200,630-24.5-15, "tankbody", "gasienice", "lufa")
czolg2 = Czolg2(WIDTH/2, 630-24.5-15, "greenbody", "gasienice", "lufaprawa")
def draw():
    screen.fill((100, 120, 35))
    for i in range(WIDTH//70 + 1):
        screen.blit('grass', (i*70, 630))
    czolg.draw()
    czolg2.draw()

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
    if keyboard.a:
        czolg2.lewo()
    if keyboard.d:
        czolg2.prawo()
    if keyboard.w:
        czolg2.lufagora()
    if keyboard.s:
        czolg2.lufadol()
    if keyboard.r:
        czolg2.wystrzel()

    czolg.update()
    czolg2.update()



pgzrun.go()
