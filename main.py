# -*- coding: utf-8 -*-
"""
Container Example
==============
This example shows how to add a container to our screen. A container is simply an empty
place on the screen which could be filled with any other content from a .kv file.
"""
from os.path import exists
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

    file_name = ""

    def build(self):
        """This method loads the root.kv file automatically"""
        self.root = Builder.load_file("pages/root.kv")
        # Call to intro screen.
        self.next_screen("intro")

    def next_screen(self, screen):
        """Clear the container and load the given screen object from file in kv folder.
        :param screen: str name of the screen object made from the loaded .kv file
        """
        filename_temp = ""
        fs = self.file_name.split(".")
        if screen in ("fw", "rw") and len(fs) == 4:
            page_number = int(fs[2])
            if screen == "fw":
                page_number += 1
            elif screen == "rw":
                page_number -= 1
            filename_temp = f"{fs[0]}.{fs[1]}.{str(page_number)}.{fs[3]}"
        else:
            # Extract the filename from the first part (number) of the text received (screen)
            filename_temp = screen.split(" ")[0]
            if not filename_temp:
                return
            # If number have '<chapter>.<section>', add extra '.0' to specify the page zero.
            if len(filename_temp.split(".")) == 2:
                filename_temp = filename_temp + ".0.kv"
            else:
                filename_temp = filename_temp + ".kv"

        if filename_temp and exists("pages/" + filename_temp):
            # unload the content of the .kv file, it could have data from previous calls
            Builder.unload_file("pages/" + filename_temp)
            # clear the container
            self.root.container.clear_widgets()
            # load the content of the .kv file
            try:
                screen = Builder.load_file("pages/" + filename_temp)
                self.file_name = filename_temp
            except:
                screen = Builder.load_file("pages/default.kv")
            # add the content of the .kv file to the container
            self.root.container.add_widget(screen)


if __name__ == "__main__":
    Virtual_EuclidesApp().run()
