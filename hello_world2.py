
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Create a label
        self.label = Label(text="Hello, World!", font_size=32)
        layout.add_widget(self.label)

        # Create a button to move the label
        button = Button(text="Move Label",
                        size_hint=(0.1,0.1))
        button.bind(on_press=self.move_label)
        layout.add_widget(button)
        

        return layout

    def move_label(self, instance):
        # Change the position of the label
        self.label.pos = (0, -300)  # Change to desired x, y coordinates

if __name__ == '__main__':
    MyApp().run()

