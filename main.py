# -*- coding: utf-8 -*-
"""
Container Example
==============
This example shows how to add a container to our screen. A container is simply an empty
place on the screen which could be filled with any other content from a .kv file.
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import (
    ObjectProperty,
    NumericProperty,
    ListProperty,
)
from kivy.clock import Clock
from kivy.vector import Vector

from kivy import require

require("2.1.0")


class RootWidget(BoxLayout):
    """Create a controller that receives a custom widget from the kv lang file.
    Add actions to be called from a kv file.
    """

    slider_ancho = NumericProperty(0.0)
    slider_alto = NumericProperty(0.0)
    # label_wid = ObjectProperty()
    p_0 = ListProperty([0, 0])
    p_1 = ListProperty([0, 0, 0, 0])
    p_2 = ListProperty([0, 0, 0, 0])

    def cap1_sec1_pag1_x(self, f):
        Clock.schedule_interval(self.update_points, 0.01)
        self.slider_ancho = f
        self.p_1 = [
            self.width / 8 * (1 + self.slider_ancho * 5),
            self.height * 10 / 16,
            self.width * 13 / 16,
            self.height * 14 / 16,
        ]
        # self.label_wid.text = str(f)
        a = (self.p_1[0], self.p_1[1])
        b = (self.p_1[2], self.p_1[3])
        c = (self.p_2[0], self.p_2[1])
        d = (self.p_2[2], self.p_2[3])
        i = Vector.segment_intersection(a, b, c, d)
        self.p_0 = [i[0] - 3, i[1] - 3] if i else (0, 0)  # Offset and avoid None

    def cap1_sec1_pag1_y(self, f):
        Clock.schedule_interval(self.update_points, 0.01)
        self.slider_alto = f
        self.p_2 = [
            self.width / 8,
            self.height * (11 + self.slider_alto * 4) / 16,
            self.width * 14 / 16,
            self.height * 11 / 16,
        ]
        a = (self.p_1[0], self.p_1[1])
        b = (self.p_1[2], self.p_1[3])
        c = (self.p_2[0], self.p_2[1])
        d = (self.p_2[2], self.p_2[3])
        i = Vector.segment_intersection(a, b, c, d)
        self.p_0 = [i[0] - 3, i[1] - 3] if i else (0, 0)  # Offset and avoid None

    def cap1_sec1_pag2_x(self, f):
        Clock.schedule_interval(self.update_points, 0.01)
        self.slider_ancho = f
        self.slider_alto = self.slider_alto if self.slider_alto else 0
        self.p_0 = [
            self.width / 2 * (1 + self.slider_ancho),
            self.height * (3 + self.slider_alto) / 4 + 20,
        ]
        self.label_wid.text = (
            f"Coordenadas: ({self.slider_ancho:.2f}, {self.slider_alto:.2f})"
        )

    def cap1_sec1_pag2_y(self, f):
        Clock.schedule_interval(self.update_points, 0.01)
        self.slider_alto = f
        self.slider_ancho = self.slider_ancho if self.slider_ancho else 0
        self.p_0 = [
            self.width / 2 * (1 + self.slider_ancho),
            self.height * (3 + self.slider_alto) / 4 + 20,
        ]
        self.label_wid.text = (
            f"Coordenadas: ({self.slider_ancho:.2f}, {self.slider_alto:.2f})"
        )

    container = ObjectProperty(None)

    def update_points(self, dt):
        pass


class Virtual_EuclidesApp(App):
    """This is the app itself"""

    def build(self):
        """This method loads the root.kv file automatically"""
        self.root = Builder.load_file("pages/root.kv")
        # Call to intro screen.
        self.next_screen("intro")

    def next_screen(self, screen):
        """Clear container and load the given screen object from file in kv folder.
        :param screen: str name of the screen object made from the loaded .kv file
        """
        # Extract the filename from the first part of the text received (screen).
        filename = screen.split(" ")[0]
        if not filename:
            return
        filename = filename + ".kv"
        # unload the content of the .kv file, it could have data from previous calls
        Builder.unload_file("pages/" + filename)
        # clear the container
        self.root.container.clear_widgets()
        # load the content of the .kv file
        try:
            screen = Builder.load_file("pages/" + filename)
        except:
            screen = Builder.load_file("pages/default.kv")
        # add the content of the .kv file to the container
        self.root.container.add_widget(screen)


if __name__ == "__main__":
    Virtual_EuclidesApp().run()
