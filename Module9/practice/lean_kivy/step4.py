from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle


class MyLabel(Label):
    def __init__(self, **kwargs):
        bg_color = kwargs.get('bg_color')
        if bg_color:
            self.bg_color = bg_color
            del kwargs['bg_color']
        else:
            self.bg_color = (0, 0, 0)
        super(MyLabel, self).__init__(**kwargs)

    def on_size(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*self.bg_color)
            Rectangle(pos=self.pos, size=self.size)


class MyApp(App):
    def build(self):
        box = BoxLayout(padding=20, spacing=40)
        lbl1 = MyLabel(
            text='Метка с фоном',
            font_size="40",
            color=(0, 1, 0),
            bg_color=(0, 0, 1),
        )
        lbl2 = Label(
            text="Обычная метка",
        )

        box.add_widget(lbl1)
        box.add_widget(lbl2)
        return box


app = MyApp()

app.run()
