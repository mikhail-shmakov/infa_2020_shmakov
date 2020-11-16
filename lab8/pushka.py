from random import randrange as rnd, choice, randint
import tkinter as tk
import math
import time

# print (dir(math))

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)


class ball:
    def __init__(self, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )
        self.live = 300

    def set_coords(self):
        canv.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.x += self.vx
        self.y -= self.vy

        if self.x + self.r + 10 > 800 or self.x - self.r - 10 < 0:
            self.vx = -self.vx
        if self.y + self.r > 550 or self.y - self.r - 10 < 0:
            self.vy = -self.vy
        if self.y + self.r >= 549:
            self.vy /= 1.3
            self.vx /= 1.3
        else:
            self.vy -= 1
        self.set_coords()

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if ((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 > (self.r + obj.r) ** 2) and self.vx != 0 and self.vy != 0:
            return False
        else:
            return True

    def check_time(self):
        self.live -= 1
        if self.live <= 0:
            canv.coords(self.id, 0, 0, 0, 0)


class gun:
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20, 450, 50, 420, width=7)

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = ball()
        new_ball.r += 5
        self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targeting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.y - 450) / (event.x - 20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class target:
    def __init__(self):
        self.points = 0
        self.live = 1
        self.id = canv.create_oval(0, 0, 0, 0)
        self.id_points = canv.create_text(30, 30, text=self.points, font='28')
        self.new_target()
        self.time = 30
        self.color = 'red'
        r = self.r = 0
        x = self.x = 0
        y = self.y = 0
        self.v = 0
        self.a = 0
        self.live = 1

    def new_target(self):
        """ Инициализация новой цели. """
        r = self.r = rnd(10, 50)
        x = self.x = rnd(600 + r, 780 - r)
        y = self.y = rnd(300 + r, 550 - r)
        self.v = randint(1, 10)
        self.a = randint(0, 360)
        color = self.color = 'red'
        canv.coords(self.id, x - r, y - r, x + r, y + r)
        canv.itemconfig(self.id, fill=color)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.v = 0
        self.r = 0
        self.y = 0
        self.x = 0
        self.live = 0
        canv.coords(self.id, 0, 0, 0, 0)
        self.points += points
        canv.itemconfig(self.id_points, text=self.points)

    def time_check(self):
        canv.itemconfig(screen1, text='')
        self.new_target()
        canv.bind('<Button-1>', g1.fire2_start)
        canv.bind('<ButtonRelease-1>', g1.fire2_end)
        canv.bind('<Motion>', g1.targeting)
        self.live = 1

    def set_coords(self):
        canv.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )

    def move(self):

        if self.live == 1:
            self.v *= rnd(90, 110) / 100
            self.a += math.radians(rnd(0, 10) - 5)
            if self.v < 0.8:
                self.v = randint(1, 6)
            if self.v > 7:
                self.v = randint(1, 6)
            self.x += round(self.v * math.cos(self.a))
            self.y -= round(self.v * math.sin(self.a))

            if self.x + self.r > 800:
                self.a = math.radians(90 + randint(10, 170))
            if self.x - self.r < 0:
                self.a = math.radians(randint(10, 170) - 90)
            if self.y + self.r > 500:
                self.a = math.radians(randint(10, 170))
            if self.y - self.r < 0:
                self.a = math.radians(randint(10, 170) - 180)
            self.set_coords()


t1 = target()
t2 = target()
screen1 = canv.create_text(400, 300, text='', font='28')
g1 = gun()
bullet = 0
balls = []


def new_game(event=''):
    global gun, t1, t2, screen1, balls, bullet
    t1.new_target()
    t2.new_target()
    bullet = 0
    balls = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targeting)
    t1.live = 1
    t2.live = 1
    while t1.live or balls or t2.live:
        for b in balls:
            b.move()
            t1.move()
            t2.move()
            b.check_time()
            if (b.hittest(t1) and t1.live) or (b.hittest(t2) and t2.live):
                t1.live = 0
                t1.hit()
                t2.live = 0
                t2.hit()
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
                canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')
                root.after(2000, t1.time_check)
                root.after(2000, t2.time_check)
                bullet = 0
        canv.update()
        time.sleep(0.03)
        g1.targeting()
        g1.power_up()
    canv.delete(gun)
    root.after(750, new_game)


new_game()
