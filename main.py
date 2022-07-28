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
offset = 3  # Half of the point_size value in .kv files, to drow the points correctly.


class RootWidget(BoxLayout):
    """Create a controller that receives a custom widget from the kv lang file.
    Add actions to be called from a kv file.
    """

    slider_1 = NumericProperty(0.0)
    slider_2 = NumericProperty(0.0)
    # slider_alto2 = NumericProperty(0.0)
    # label_wid = ObjectProperty()
    p_0 = ListProperty([0, 0])
    p_1 = ListProperty([0, 0, 0, 0])
    p_2 = ListProperty([0, 0, 0, 0])

    def cap1_sec1_pag1_x(self, f):
        """Control horizontal slider event (x)"""
        Clock.schedule_interval(self.update_points, 0.01)
        self.slider_1 = f  # Receive and update the value from the slider.
        self.p_1 = [
            self.width / 8 * (1 + self.slider_1 * 5),
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
        self.p_0 = (  # Offset added and conditional to avoid None
            [i[0] - offset, i[1] - offset] if i else (0, 0)
        )

    def cap1_sec1_pag1_y(self, f):
        """Control vertical slider event (y)"""
        Clock.schedule_interval(self.update_points, 0.01)
        self.slider_2 = f  # Receive and update the value from the slider.
        self.p_2 = [
            self.width / 8,
            self.height * (11 + self.slider_2 * 4) / 16,
            self.width * 14 / 16,
            self.height * 11 / 16,
        ]
        a = (self.p_1[0], self.p_1[1])
        b = (self.p_1[2], self.p_1[3])
        c = (self.p_2[0], self.p_2[1])
        d = (self.p_2[2], self.p_2[3])
        i = Vector.segment_intersection(a, b, c, d)
        self.p_0 = (  # Offset added and conditional to avoid None
            [i[0] - offset, i[1] - offset] if i else (0, 0)
        )

    def cap1_sec1_pag2_x(self, f):
        """Control horizontal slider event (x)"""
        Clock.schedule_interval(self.update_points, 0.01)
        self.slider_1 = f  # Receive and update the value from the slider.
        # To set to zero the first time or update the value next times.
        self.slider_2 = self.slider_2 if self.slider_2 else 0
        self.p_0 = [
            self.width / 2 * (1 + self.slider_1) - offset,
            self.height * (3 + self.slider_2) / 4 - offset,
        ]
        self.label_wid.text = (
            f"Coordenadas: ({(self.slider_1*10):.1f}, {(self.slider_2*10):.1f})"
        )

    def cap1_sec1_pag2_y(self, f):
        """Control vertical slider event (y)"""
        Clock.schedule_interval(self.update_points, 0.01)
        self.slider_2 = f  # Receive and update the value from the slider.
        # To set to zero the first time or update the value next times.
        self.slider_1 = self.slider_1 if self.slider_1 else 0
        self.p_0 = [
            self.width / 2 * (1 + self.slider_1) - offset,
            self.height * (3 + self.slider_2) / 4 - offset,
        ]
        self.label_wid.text = (
            f"Coordenadas: ({(self.slider_1*10):.1f}, {(self.slider_2*10):.1f})"
        )

    def cap1_sec2_pag1(self):
        """Control sliders events"""
        Clock.schedule_interval(self.update_points, 0.01)
        slider_alto1 = self.slider_y1.value
        slider_alto2 = self.slider_y2.value

        self.p_0 = [
            self.width / 10,
            self.height * 3 / 4,
            self.width / 4,
            self.height * (3 + slider_alto1) / 4,
            self.width * 3 / 4,
            self.height * (3 + slider_alto2) / 4,
            self.width * 8 / 10,
            self.height * 3 / 4,
        ]
        self.label_wid.text = (
            f"Curvatura izq.: {(slider_alto1):.2f}  Curvatura der.: {(slider_alto2):.2f}"
            + (
                "\n Esto es una línea... recta!!!"
                if slider_alto1 == slider_alto2 == 0.0
                else ""
            )
        )

    def cap1_sec2_pag2(self):
        """Control sliders events"""
        Clock.schedule_interval(self.update_points, 0.01)
        slider_left = self.slider_y1.value
        slider_right = self.slider_y2.value

        self.p_0 = [
            self.width * (2 + slider_left) / 10,
            self.height * 6 / 8,
            self.width * (8 + slider_right) / 10,
            self.height * 3 / 4,
        ]

        if slider_left == self.slider_y1.min and slider_right == self.slider_y2.max:
            self.label_wid.text = "Recta infinita (ambos lados)"
        elif slider_left != self.slider_y1.min and slider_right == self.slider_y2.max:
            self.label_wid.text = "Semirecta infinita a la derecha"
        elif slider_left == self.slider_y1.min and slider_right != self.slider_y2.max:
            self.label_wid.text = "Semirecta infinita a la izquierda"
        elif slider_left != self.slider_y1.min and slider_right != self.slider_y2.max:
            self.label_wid.text = "Semirecta finita"

    container = ObjectProperty(None)

    def update_points(self, dt):
        pass


class Virtual_EuclidesApp(App):
    """This is the app itself"""

    def build(self):
        """This method loads the root.kv file automatically"""
        self.root = Builder.load_file("pages/root.kv")
        # Call to intro screen.
        self.next_screen("1.2.2")

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
