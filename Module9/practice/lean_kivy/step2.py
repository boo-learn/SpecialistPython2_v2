from kivy.app import App
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        btn = Button(
            text="Click me",
            font_size = 40,
        )
        btn.bind(on_press=on_btn_click)
        # Button: https://kivy.org/doc/stable/api-kivy.uix.button.html#module-kivy.uix.button
        # btn = Button(text="Click me",pos=(100, 100), size=(200, 100), size_hint=(None, None))
        return btn


# callback
def on_btn_click(instance):
    print(f"Press on {instance}")
    instance.text = "Clicked"


if __name__ == "__main__":
    app = MyApp()
    app.run()
