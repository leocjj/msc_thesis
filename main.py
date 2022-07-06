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
from kivy.properties import ObjectProperty
import kivy

kivy.require("2.1.0")


class RootWidget(BoxLayout):
    """Create a controller that receives a custom widget from the kv lang file.
    Add an action to be called from a kv file.
    """

    container = ObjectProperty(None)


class Virtual_EuclidesApp(App):
    """This is the app itself"""

    def build(self):
        """This method loads the root.kv file automatically"""
        self.root = Builder.load_file("pages/root.kv")
        # Call to intro screen.
        self.next_screen("0")

    def next_screen(self, screen):
        """Clear container and load the given screen object from file in kv folder.
        :param screen: str name of the screen object made from the loaded .kv file
        """
        # Extract the filename from the first part of the text received (screen).
        filename = screen.split(" ")[0] + ".kv"
        # unload the content of the .kv file, it could have data from previous calls
        Builder.unload_file("pages/" + filename)
        # clear the container
        self.root.container.clear_widgets()
        # load the content of the .kv file
        try:
            screen = Builder.load_file("pages/" + filename)
        except:
            return
        # add the content of the .kv file to the container
        self.root.container.add_widget(screen)


if __name__ == "__main__":
    Virtual_EuclidesApp().run()
