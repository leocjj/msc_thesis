# -*- coding: utf-8 -*-
"""
Container Example
==============
This example shows how to add a container to our screen. A container is simply an empty
place on the screen which could be filled with any other content from a .kv file.
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
# Keep this. Importing the main class with all events handler. Is then used in root.kv
from rootwidget import RootWidget
from kivy import require

require("2.1.0")


class IconButton(ButtonBehavior, Image):
    """https://kivy.org/doc/stable/api-kivy.uix.behaviors.html#behavior-mixin-classes"""
    pass


class Virtual_EuclidesApp(App):
    """This is the app itself"""

    def build(self):
        """This method loads the root.kv file automatically"""
        self.root = Builder.load_file("pages/root.kv")
        # Call to intro screen.
        self.next_screen("intro")

    def next_screen(self, screen):
        """Clear the container and load the given screen object from file in pages folder.
        """
        try:
            # unload the content of the .kv file, it could have data from previous calls
            Builder.unload_file("pages/" + screen + ".kv")
            # clear the container
            self.root.container.clear_widgets()
            # load the content of the .kv file
            screen = Builder.load_file("pages/" + screen + ".kv")
        except:
            screen = Builder.load_file("pages/default.kv")
        # add the content of the .kv file to the container
        self.root.container.add_widget(screen)


if __name__ == "__main__":
    Virtual_EuclidesApp().run()