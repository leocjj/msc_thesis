import kivy
kivy.require('2.1.0')

from kivy.app import App


class Root(App):
    kv_directory = 'kv'


if __name__ == '__main__':
    Root().run()
