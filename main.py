from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class AlshScalperPro(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=20, **kwargs)
        self.add_widget(Label(text='Alsh Scalper Pro', font_size='28sp', bold=True))
        self.status = Label(text='Ready', font_size='18sp')
        self.add_widget(self.status)
        btn = Button(text='افحص السوق', size_hint_y=0.3, background_color=(0,0.8,0.3,1))
        btn.bind(on_press=lambda x: setattr(self.status, 'text', 'BUY Signal OK'))
        self.add_widget(btn)

class AlshApp(App):
    def build(self):
        return AlshScalperPro()

AlshApp().run()
