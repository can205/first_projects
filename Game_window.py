from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button

class Game_Window(GridLayout):
  
    def __init__(self, **kwargs):
       super().__init__(**kwargs)
       self.cols = 1
       self.size_hint=(1 , 1)
       self.pos_hint = {
        "center_x": 0.5,
        "center_y": 0.5,
       }
        # define white background
       self.background_color = (1, 1, 1, 1)  # Initial color (white = full brightness)

        # Set up canvas to handle background color changes
       with self.canvas.before:
            self.bg_color = Color(*self.background_color)
            self.rect = Rectangle(size=self.size, pos=self.pos)

       self.bind(size=self.on_size, pos=self.on_size)
                           
       self.Title = Label(
          text = "Number Guesser",
          font_size=(35),
          pos_hint={
          "center_x":0.5,
          "ceneter_y":0.7},
          color="#33cccc"
          )
       self.add_widget(self.Title)
       
       self.question = Label(
          text = "choose your number range",
          font_size=(30),
          color="#33cccc")
       
       self.add_widget(self.question)
       
                
       self.input = TextInput(
           multiline=False,
           padding_y=(28),
           padding_x=(320),
           font_size=(30),
           size_hint=(0.6 , 0.6),
           )
       self.add_widget(self.input)

       

       self.options_button = Button(
          text = "Options",
          size_hint=(0.6, 0.6),
          font_size=(30)
       )

       self.options_button.bind(on_press = self.options_button_behavior)
       self.add_widget(self.options_button)

       self.start_button = Button (
           text = "Start",
           size_hint = (0.6, 0.6),
           pos=(1,1),
           padding_x=(200),
           font_size=(30)
           )
       self.start_button.bind(on_press = self.start_button_behavior)
       self.add_widget(self.start_button)
       return 
    def on_size(self, *args):
        """Update the rectangle position and size when the layout size changes."""
        self.rect.pos = self.pos
        self.rect.size = self.size
    def options_button_behavior(self, *args):
       app.screen_manager.current = "Options_Menue"

   

    def start_button_behavior(self, *args):
        app.screen_manager.current = "InGame"

   

    def brightness_button_behavior(self, *args):
        """Change the brightness when the button is pressed"""
        app = App.get_running_app()
        app.change_brightness()  # Call the shared method in MyApp

    def change_brightness(self):
        """Change the screen's background color to simulate brightness change"""
        app = App.get_running_app()

        # Toggle brightness state
        if app.brightness_state == (1, 1, 1, 1):  # Full brightness (white)
            app.brightness_state = (0.5, 0.5, 0.5, 1)  # Dim (gray)
        elif app.brightness_state == (0.5, 0.5, 0.5, 1):  # Dim (gray)
            app.brightness_state = (0.0, 0.0, 0.0, 1)  # Very dark
        elif app.brightness_state == (0.0, 0.0, 0.0, 1):  # Very dark
            app.brightness_state = (1, 1, 1, 1)  # Full brightness (white)

        # Update the color on the canvas in this screen
        self.bg_color.rgba = app.brightness_state

        # Recalculate the size and position of the rectangle
        self.rect.pos = self.pos
        self.rect.size = self.size