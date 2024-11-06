from kivy.animation import Animation
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button

from main import MainMenu

Builder.load_file('animation.kv')


class MyLayout(MainMenu):
    def animate_it(self, widget, *args):  # noqa
        animate = Animation(background_color=(0, 0, 1, 1), duration=1)
        animate += Animation(opacity=0, duration=0.5)
        animate += Animation(size_hint=(1, 1), duration=0.5)
        animate += Animation(size_hint=(.5, .5), duration=0.5)

        animate.start(widget)


class MyApp(App):
    def build(self):
        layout = MyLayout()

        # Анимиран бутон.
        button = Button(text="Кък сте?",
                        font_size=45,
                        size_hint=(.5, .5),
                        pos_hint={"center_x": 0.5, "center_y": 0.5})

        # Свързан бутон към метода animate_it.
        button.bind(on_press=lambda instance: layout.animate_it(button))

        layout.add_widget(button)
        return layout


if __name__ == '__main__':
    MyApp().run()
