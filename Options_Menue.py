from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.app import App

class Options_Menue(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.size_hint = (1, 1)
        self.pos_hint = {
            "center_x": 0.5,
            "center_y": 0.5
        }
        self.background_color = App.get_running_app().brightness_state
        # Set up canvas to handle background color changes
        with self.canvas.before:
            self.bg_color = Color(1, 1, 1, 1)  # Initial white background
            self.rect = Rectangle(size=self.size, pos=self.pos)
        
        self.bind(size=self.on_size, pos=self.on_size)
   
        # Adding buttons
        self.volume_button = Button(
            text="Volume",
            size_hint=(0.6, 0.3),
            pos_hint=(0.05, 0.2),
            font_size=(35)
        )
        self.add_widget(self.volume_button)

        self.brightness_button = Button(
            text="Brightness",
            size_hint=(0.6,0.3),
            pos_hint=(0.45, 0.5),
            font_size=(35)
        )
        self.brightness_button.bind(on_press=self.brightness_button_behavior)
        self.add_widget(self.brightness_button)

        self.theme_button = Button(
            text="Theme",
            size_hint=(0.5, 0.3),
            pos_hint=(0.25, 0.5),
            font_size=(35)
        )
        self.add_widget(self.theme_button)

        self.back_to_menue_button = Button(
            text="Back to Menu",
            size_hint=(0.6, 0.3),
            pos_hint=(0.65, 0.5),
            font_size=(35)
        )
        self.add_widget(self.back_to_menue_button)
        self.back_to_menue_button.bind(on_press=self.back_to_menue_button_behavior)

    def on_size(self, *args):
        """Update the rectangle position and size when the layout size changes."""
        self.rect.pos = self.pos
        self.rect.size = self.size

    def brightness_button_behavior(self,*args):
     """Change the brightness when the button is pressed"""
     #  Access the current background color and call the change_brightness method without extra arguments
     app.game_window.change_brightness()  
    def change_brightness(self):
     """Change the screen's background color to simulate brightness change"""
     if self.background_color == (1, 1, 1, 1):  # Full brightness (white)
        self.background_color = (0.5, 0.5, 0.5, 1)  # Dim (gray)
     elif self.background_color == (0.5, 0.5, 0.5, 1):  # Dim (gray)
        self.background_color = (0.0, 0.0, 0.0, 1)  # Very dark
     elif self.background_color == (0.0, 0.0, 0.0, 1):  # Very dark
        self.background_color = (1, 1, 1, 1)  # Full brightness (white)

     # Update the color on the canvas
     self.bg_color.rgba = self.background_color

     # Recalculate the size and position of the rectangle
     self.rect.pos = self.pos
     self.rect.size = self.size



    def back_to_menue_button_behavior(self, *args):
        Clock.schedule_once(self.switch_to_last_view)

    def switch_to_last_view(self, *kwargs):
        app.screen_manager.current = "game_window"

  