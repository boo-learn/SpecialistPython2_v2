from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class MyApp(App):
    def build(self):
        box = BoxLayout(orientation='vertical', padding=15)
        # BoxLayout: https://kivy.org/doc/stable/api-kivy.uix.boxlayout.html#module-kivy.uix.boxlayout
        # Widgets: https://kivy.org/doc/stable/api-kivy.uix.html
        self.input1 = TextInput(hint_text ="Enter your text here...", font_size=40)
        self.lbl = Label(text="Base text", font_size=30, color=(0, 1, 0.1))
        self.btn = Button(
            text="Click me",
            font_size=40,
            on_press=self.on_btn_click
        )
        # self.btn.bind(on_press=self.on_btn_click)
        box.add_widget(self.input1)
        box.add_widget(self.lbl)
        box.add_widget(self.btn)
        return box

    def on_btn_click(self, instance):
        self.lbl.text = self.input1.text


if __name__ == "__main__":
    app = MyApp()
    app.run()
