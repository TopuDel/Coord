import math
import random

import kivy
from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.text import Label as CoreLabel
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import (Color, Ellipse, Line, Rectangle)
from kivy.graphics.instructions import InstructionGroup
from kivy.properties import \
    ObjectProperty,  \
    NumericProperty, \
    ListProperty, \
    BooleanProperty, \
    OptionProperty, \
    ReferenceListProperty
from kivy.uix.screenmanager import ScreenManager, Screen

n = 25
h = 640
w = 480
    
from kivy.config import Config
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', str(w))
Config.set('graphics', 'height', str(h))

x0 = 0
y0 = 0

class PainterWidget(Widget):
##    mylabel = CoreLabel(text="-7   -6    -5    -4    -3    -2    -1     0     1     2     3     4     5     6     7", font_size=25, color=(0, 0, 0, 1))
##    print('1')
##    mylabel.refresh()
##    print('2')
##    texture = mylabel.texture
##    print('3')
##    print(texture)
##    texture_size = list(texture.size)
##    print('4')
    
    def draw(self):
        self.bg = InstructionGroup()
        self.bg.add(Color(1, 1, 1, 1))
        self.bg.add(Rectangle(pos=self.pos, size=self.size))
        
        self.bg.add(Color(0, 0, 0, 1))
        self.bg.add(Line(points=[self.x + (self.width / 2), self.y + 0, self.x + (self.width / 2), self.y + self.height], width=2))
        for i in range (-8, 9):
            self.bg.add(Line(points=[self.x + (self.width / 2) + 25 * i, self.y + 0, self.x + (self.width / 2) + 25 * i, self.y + self.height], width=1))
        self.bg.add(Line(points=[self.x + 0, self.y + (self.height / 2), self.x + self.width, self.y + (self.height / 2)], width=2))
        for i in range (-6, 7):
            self.bg.add(Line(points=[self.x + 0, self.y + (self.height / 2) + 25 * i, self.x + self.width, self.y + (self.height / 2) + 25 * i], width=1))
        self.bg.add(Line(points=[self.x + self.width, self.y + (self.height / 2), self.x + self.width - 10, self.y + (self.height / 2) - 10], width=2))
        self.bg.add(Line(points=[self.x + self.width, self.y + (self.height / 2), self.x + self.width - 10, self.y + (self.height / 2) + 10], width=2))
        self.bg.add(Line(points=[self.x + (self.width / 2), self.y + self.height, self.x + (self.width / 2) - 10, self.y + self.height - 10], width=2))
        self.bg.add(Line(points=[self.x + (self.width / 2), self.y + self.height, self.x + (self.width / 2) + 10, self.y + self.height - 10], width=2))

        for i in range(-8, 9):
            mylabel = CoreLabel(text=str(i), font_size=16, color=(1, 0, 0, 1))
            mylabel.refresh()
            texture = mylabel.texture
            texture_size = list(texture.size)
            self.bg.add(Rectangle(texture=texture, size=texture_size, pos=((i + 9) * 25, 300)))
        mylabel = CoreLabel(text='X', font_size=16, color=(1, 0, 0, 1))
        mylabel.refresh()
        texture = mylabel.texture
        texture_size = list(texture.size)
        self.bg.add(Rectangle(texture=texture, size=texture_size, pos=((9 + 9) * 25, 293)))
        for i in range(-6, 7):
            mylabel = CoreLabel(text=str(i), font_size=16, color=(1, 0, 0, 1))
            mylabel.refresh()
            texture = mylabel.texture
            texture_size = list(texture.size)
            self.bg.add(Rectangle(texture=texture, size=texture_size, pos=(225, (i + 12) * 25)))
        mylabel = CoreLabel(text='Y', font_size=16, color=(1, 0, 0, 1))
        mylabel.refresh()
        texture = mylabel.texture
        texture_size = list(texture.size)
        self.bg.add(Rectangle(texture=texture, size=texture_size, pos=(220, (7 + 12) * 25)))
        
class Playground(Widget):
    global x0, y0
    score_t = 0
    score_f = 0
    x0 = random.randint(-7,8)
    y0 = random.randint(-5,6)
    txt = "(" + str(x0) + "; " + str(y0) + ")"
    
    def start(self):
        self.score_t = 0
        self.score_f = 0
        self.lbl_t.text = str(self.score_t)
        self.lbl_f.text = str(self.score_f)
        with self.canvas:
            self.pw.draw()
        
        
    
    def press_btn(self):
        CoordApp.screen_manager.current = "welcome_screen"

    def on_touch_down(self, touch):
        global n, x0, y0
        with self.canvas:
            r = 20
            if self.pw.x + r/2 <= touch.x <= self.pw.x - r/2 + self.pw.width and self.pw.y + r/2 <= touch.y <= self.pw.y + self.pw.height - r/2:
                x = round((touch.x - 20 - 440/2) / n)
                y = round((touch.y - 146 - 348/2) / n)
                if x == x0 and y == y0:
                    self.score_t += 1
                    self.pw.draw()
                    x0 = random.randint(-7,8)
                    y0 = random.randint(-5,6)
                    self.txt = "(" + str(x0) + "; " + str(y0) + ")"
                    self.lbl.text = self.txt
                    self.lbl_t.text = str(self.score_t)
                else:
                    self.score_f += 1
                    self.lbl_f.text = str(self.score_f)
                    Color(1, 0, 0, 1)
                    Ellipse (pos = (x * n + (20 + 440/2) - r / 2, y * n + (146 + 348/2) - r / 2), size = (r, r))
            elif self.btn.x <= touch.x <= self.btn.x + self.btn.width and self.btn.y <= touch.y <= self.btn.y + self.btn.height:
                CoordApp.screen_manager.current = "welcome_screen"


class Playground2(Widget):
    score_t = 0
    score_f = 0
    
    def start(self):
        self.score_t = 0
        self.score_f = 0
        self.lbl_t.text = str(self.score_t)
        self.lbl_f.text = str(self.score_f)
        with self.canvas:
            self.pw.draw()
        self.point()
        self.ti1.text = ''
        self.ti2.text = ''

    def press_btn(self):
        CoordApp.screen_manager.current = "welcome_screen"

    def point(self):
        global n, x0, y0
        x0 = random.randint(-7,8)
        y0 = random.randint(-5,6)
        print (x0, y0)
        with self.canvas:
            r = 20
            Color(0, 0, 1, 1)
            Ellipse (pos = (x0 * n + (20 + 440/2) - r / 2, y0 * n + (146 + 348/2) - r / 2), size = (r, r))

    def press_ok_btn(self):
        global x0, y0
        a = self.ti1.text
        b = self.ti2.text
        print (a, b)
        if a == '':
            a = '0'
            self.ti1.text = '0'
        if b == '':
            b = '0'
            self.ti2.text = '0'
        x = int(a)
        y = int(b)
        if x == x0 and y == y0:
            self.score_t += 1
            self.lbl_t.text = str(self.score_t)
            with self.canvas:
                self.pw.draw()
            self.ti1.text = ''
            self.ti2.text = ''
            self.point()
        else:
            self.score_f += 1
            self.lbl_f.text = str(self.score_f)

class WelcomeScreen(Screen):
    pass

class PlaygroundScreen2(Screen):
    game_engine2 = ObjectProperty(None)

    def on_enter(self):
        self.game_engine2.start()

class PlaygroundScreen(Screen):
    game_engine = ObjectProperty(None)

    def on_enter(self):
        self.game_engine.start()




class CoordApp(App):
    screen_manager = ObjectProperty(None)

    def build(self):
        CoordApp.screen_manager = ScreenManager()

        ws = WelcomeScreen(name="welcome_screen")
        ps = PlaygroundScreen(name="playground_screen")
        ps2 = PlaygroundScreen2(name="playground_screen2")

        self.screen_manager.add_widget(ws)
        self.screen_manager.add_widget(ps)
        self.screen_manager.add_widget(ps2)

        return self.screen_manager

if __name__ == "__main__":
    CoordApp().run()
