import random
import arcade
from math import pi, sin, cos, acos

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_COLOR = arcade.color.CATALINA_BLUE

class Cross_hare:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.texturecrosshair = arcade.load_texture("img/crosshair.png")

    def draw(self):
       #arcade.draw_point(self.x, self.y, [0, 200, 200], 10)
        self.texturecrosshair.draw(self.x, self.y, 30, 30)
        # arcade.draw_text(str(self.get_degree()), self.x + 5, self.y + 5,[200, 0, 0], 14)

    def move_to(self, x, y):
        self.x = x
        self.y = y

    def get_degree(self):
        dx = self.x - SCREEN_WIDTH / 2
        dy = self.y - 0
        r = (dx ** 2 + dy ** 2) ** 0.5
        return acos(dx / r) * 180 / pi



class Duck:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = 50
        self.degrees = random.randint(30, 150)
        self.speed = 2
        self.dx = cos(self.degrees * pi / 180)
        self.dy = sin(self.degrees * pi / 180)
        self.texture = arcade.load_texture("img/duck.png")
        self.texture2 = arcade.load_texture("img/duck2.png")


    def move(self):
        self.x += self.dx * self.speed
        self.y += self.dy * self.speed

    def draw(self):
        if self.degrees >= 90 :
            self.texture.draw(self.x, self.y, 70, 70, self.degrees - 180,)
        else:
            self.texture2.draw(self.x, self.y, 70, 70, self.degrees)


        # arcade.draw_point(self.x, self.y, [200, 0, 0], 50)

class MyGame(arcade.Window):
    """ Главный класс приложения. """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(SCREEN_COLOR)
        self.set_mouse_visible(False)
        self.textureGrass = arcade.load_texture("img/grass.png")
        self.texturegun = arcade.load_texture("img/guntest.png")

    def setup(self):
        # Настроить игру здесь
        self.duck = Duck()
        self.cross_hare = Cross_hare()

    def on_draw(self):
        """ Отрендерить этот экран. """
        arcade.start_render()

        self.textureGrass.draw(400, 100, 900, 200)
        self.texturegun.draw(500, 0, 500, 310, self.cross_hare.get_degree() + 240,)
        self.duck.draw()
        self.cross_hare.draw()
        # Здесь код рисунка

    def update(self, delta_time):
        """ Здесь вся игровая логика и логика перемещения."""
        self.duck.move()
        pass

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.cross_hare.move_to(x, y)

    #def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()