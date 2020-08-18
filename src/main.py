from kivy.app import App
from kivy.lang import Builder
from kivy.factory import Factory
import cv2


KV = '''
#:import cv2 cv2
Label:
    text: 'opencv {} imported successfully'.format(cv2.version)
'''


class Application(App):
    def build(self):
        return Builder.load_string(KV)


if __name__ == "__main__":
    Application().run()
