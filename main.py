import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.core.audio import SoundLoader
from kivy.uix.bubble import Bubble
from kivy.uix.camera import Camera

Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')
kivy.require('2.0.0')

class Cronometro(Widget):
    sound = SoundLoader.load('bruh.mp3')
    temporizador = ObjectProperty(None)

    # Esta función toma un string '00:02:00' y le retrocede 1 segundo
    def tiempo(self, instance):
        self.s = self.temporizador.text.split(':')[2]
        self.m = self.temporizador.text.split(':')[1]
        self.h = self.temporizador.text.split(':')[0]
        if int(self.m) == int(self.h) == int(self.s) == 0:
            # Cuando llegue a 0 esta linea se va a reproducir
            self.sound.play()
            Clock.unschedule(self.inicio)
        if int(self.h) > 0:
            if int(self.m) == int(self.s) == 0:
                self.m = '59'
                self.s = '59'
                self.h = str(int(self.h) - 1)
                self.temporizador.text = f'{self.h.zfill(2)}:{self.m.zfill(2)}:{self.s.zfill(2)}'
                return
        if int(self.s) > 0:
            self.s = str(int(self.s) - 1)
            self.temporizador.text = f'{self.h.zfill(2)}:{self.m.zfill(2)}:{self.s.zfill(2)}'
            return
        if int(self.s) == 0 and int(self.m) > 0:
            self.s = '59'
            self.m = str(int(self.m) - 1)
            self.temporizador.text = f'{self.h.zfill(2)}:{self.m.zfill(2)}:{self.s.zfill(2)}'
            return

    def plus(self):
        self.s = self.temporizador.text.split(':')[2]
        self.m = self.temporizador.text.split(':')[1]
        self.h = self.temporizador.text.split(':')[0]

    def minus(self):
        self.cam = Camera(play=True)

    def start(self):
        # Programa que cada 1 segundo se llame a la funcion tiempo()
        self.inicio = Clock.schedule_interval(self.tiempo, 1)
        
    
    # Detener el tiempo y dejar el útimo string que queda
    def stop(self):
        Clock.unschedule(self.inicio)
        #self.inicio.cancel()

class Test(App):
    def build(self):
        return Cronometro()

if __name__ == '__main__':
    Test().run()