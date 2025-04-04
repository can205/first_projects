from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
import random
from kivy.core.audio import SoundLoader



class Game_Window(FloatLayout):
    def __init__(self, **kwargs):
       super().__init__(**kwargs)
       self.click_sound = SoundLoader.load("./click-234708.mp3")
       self.cols = 1
       self.size_hint=(1 , 1)
       self.pos_hint = {"center_x":0.5, "center_y":0.5}
       self.background_color = (1, 1, 1, 1) 

       with self.canvas.before:
            self.bg_color = Color(*self.background_color)
            self.rect = Rectangle(size=self.size, pos=self.pos)

       self.bind(size=self.on_size, pos=self.on_size)
                           
       self.Title = Label(
          text = "Number Guesser",
          font_size=(35),
          pos_hint={"center_x":0.5,"center_y":0.85},
          color="#33cccc"
          )
       self.add_widget(self.Title)

       

       self.input =TextInput(
           multiline=False,
           padding_y=(30),
           padding_x=(195),
           size_hint=(0.8, 0.15),
           font_size=(25),
           pos_hint={"center_x":0.5 , "center_y":0.60}
       )
       self.add_widget(self.input)

       self.question = Label(
           text="Number Range:1-",
           size_hint=(0.8 , 0.15),
           font_size=(25),
           pos_hint={"center_x": 0.2225, "center_y":0.6},
           color="#33cccc"              
           )
       self.add_widget(self.question)

       self.gamemode_button = Button(
            text="Gamemode",
            size_hint=(0.8, 0.15),
            pos_hint={"center_x":0.5, "center_y":0.45},
            font_size=(35)
        )
       self.add_widget(self.gamemode_button)
       self.gamemode_button.bind(on_press=self.gamemode_button_behavior)
       self.options_button = Button(
          text = "Options",
          size_hint=(0.8, 0.15),
          font_size=(30),
          pos_hint={"center_x": 0.5 , "center_y" :0.30}
       )

       self.options_button.bind(on_press = self.options_button_behavior)
       self.add_widget(self.options_button)

       self.start_button = Button (
           text = "Start",
           size_hint = (0.8, 0.15),
           pos_hint={"center_x":0.5 , "center_y":0.15},
           padding_x=(200),
           font_size=(30)
           )
       self.start_button.bind(on_press = self.start_button_behavior)
       self.add_widget(self.start_button)
       return 
    
    def start_button_behavior(self, *args):
        max_number= int(self.input.text)
        in_game = InGame(max_number)
        in_game_screen = Screen(name="InGame")
        in_game_screen.add_widget(in_game)
        app.screen_manager.add_widget(in_game_screen)
        app.screen_manager.current = "InGame"
        self.play_click_sound()
        
    def options_button_behavior(self, *args):
       app.screen_manager.current = "Options_Menue"
       self.play_click_sound()

    def gamemode_button_behavior(self,*args):
        self.play_click_sound()
    
    def update_background_color(self, color):
        """Update the background color to match the brightness state"""
        self.background_color = color
        self.bg_color.rgba = color
        self.rect.pos = self.pos
        self.rect.size = self.size

    def on_size(self, *args):
        """Update the rectangle position and size when the layout size changes."""
        self.rect.pos = self.pos
        self.rect.size = self.size
    
    def brightness_button_behavior(self, *args):
        """Change the brightness when the button is pressed"""
        app = App.get_running_app()
        app.change_brightness()
        self.play_click_sound()

    def change_brightness(self):
        """Change the screen's background color to simulate brightness change"""
        app = App.get_running_app()
       
        if app.brightness_state == (1, 1, 1, 1):  
            app.brightness_state = (0.5, 0.5, 0.5, 1)  
        elif app.brightness_state == (0.5, 0.5, 0.5, 1):  
            app.brightness_state = (0.0, 0.0, 0.0, 1)  
        elif app.brightness_state == (0.0, 0.0, 0.0, 1):  
            app.brightness_state = (1, 1, 1, 1)  

       
        self.bg_color.rgba = app.brightness_state

       
        self.rect.pos = self.pos
        self.rect.size = self.size
     
    def play_click_sound(self):
        if self.click_sound:
            self.click_sound.play()



class Options_Menue(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.click_sound = SoundLoader.load('./click-234708.mp3')
        self.cols = 1
        self.size_hint = (1, 1)
        self.pos_hint = {
            "center_x": 0.5,
            "center_y": 0.5
        }
        self.background_color = (1, 1, 1, 1) 
        self.background_color = App.get_running_app().brightness_state

        with self.canvas.before:
            self.bg_color = Color(*self.background_color)  
            self.rect = Rectangle(size=self.size, pos=self.pos)
        
        self.bind(size=self.on_size, pos=self.on_size)
   
        self.volume_button = Button(
            text="Volume",
            size_hint=(0.8, 0.2),
            pos_hint={"center_x":0.5 , "center_y":0.7},
            font_size=(35)
        )
        self.add_widget(self.volume_button)
        self.volume_button.bind(on_press=self.volume_button_behavior)

        self.brightness_button = Button(
            text="Brightness",
            size_hint=(0.8,0.2),
            pos_hint={"center_x":0.5 , "center_y":0.5},
            font_size=(35)
        )
        self.brightness_button.bind(on_press=self.brightness_button_behavior)
        self.add_widget(self.brightness_button)

        self.back_to_menue_button = Button(
            text="Back to Menu",
            size_hint=(0.8, 0.2),
            pos_hint={"center_x":0.5, "center_y":0.3},
            font_size=(35)
        )
        self.add_widget(self.back_to_menue_button)
        self.back_to_menue_button.bind(on_press=self.back_to_menue_button_behavior)

    def update_background_color(self, color):
        """Update the background color to match the brightness state"""
        self.background_color = color
        self.bg_color.rgba = color
        self.rect.pos = self.pos
        self.rect.size = self.size

    def on_size(self, *args):
        """Update the rectangle position and size when the layout size changes."""
        self.rect.pos = self.pos
        self.rect.size = self.size

    def brightness_button_behavior(self,*args):
     """Change the brightness when the button is pressed"""
     app= App.get_running_app()
     app.change_brightness()
     self.play_click_sound()  

    def change_brightness(self):
     """Change the screen's background color to simulate brightness change"""
     app= App.get_running_app()
     if self.background_color == (1, 1, 1, 1): 
         self.background_color = (0.5, 0.5, 0.5, 1)  
     elif self.background_color == (0.5, 0.5, 0.5, 1):  
        self.background_color = (0.0, 0.0, 0.0, 1)  
     elif self.background_color == (0.0, 0.0, 0.0, 1): 
        self.background_color = (1, 1, 1, 1)

    
     self.bg_color.rgba = self.background_color

    
     self.rect.pos = self.pos
     self.rect.size = self.size



    def back_to_menue_button_behavior(self, *args):
        app.screen_manager.current = "game_window"
        self.play_click_sound()
    
    def volume_button_behavior(self, *args):
         self.play_click_sound()
    
    def play_click_sound(self):
        if self.click_sound:
            self.click_sound.play()


class InGame(FloatLayout):
    def __init__(self,max_number,**kwargs):
        self.the_searched_number = random.randint(1, max_number)
        self.click_sound = SoundLoader.load('./click-234708.mp3')
        self.count = 1
        super().__init__(**kwargs)
        self.cols = 3
        self.size_hint = (1, 1)
        self.background_color = (1, 1, 1, 1) 
        app = App.get_running_app() 
        self.background_color = app.brightness_state 

        with self.canvas.before:
            self.bg_color = Color(*self.background_color)              
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self.on_size, pos=self.on_size)


        self.bestaetigen_button = Button(
            text="Bestätigen",
            size_hint=(0.27 , 0.2),
            pos_hint={"center_x": 0.5,"center_y": 0.32}
        )
       
        self.bestaetigen_button.bind(on_press=lambda instance: self.bestaetigen_button_behavior(self.the_searched_number))
        self.add_widget(self.bestaetigen_button)     
   
        self.guess_nummber_label=Label(
            text="Guess Number:",
            font_size=(30),
            pos_hint={"center_x": 0.5, "center_y": 0.63},
            color="#33cccc"
            )
        self.add_widget(self.guess_nummber_label)

        self.tries = Label(
            text="tries",
            pos_hint={"center_x": 0.85, "center_y":0.85},
            font_size=(30),
            color="#33cccc"
        )
        self.add_widget(self.tries)

        self.comparison = Label(
            text="comparison",
            font_size=(30),
            pos_hint={"center_x": 0.15 , "center_y": 0.85},
            color="#33cccc",
        )

        self.add_widget(self.comparison)

       
        self.exit_button = Button(
            text="Exit",
            font_size=(10),
            size_hint=(0.1 , 0.1),
            pos_hint={"center_x": 0.05 , "center_y": 0.95}
        )
        self.add_widget(self.exit_button)
        self.exit_button.bind(on_press=self.exit_button_behavior)

        self.guessed_number= TextInput(
            multiline=False,
            padding_y=(40),
            padding_x=(50),
            font_size=(30),
            size_hint=(0.27 , 0.2),  
            pos_hint={"center_x": 0.5,"center_y": 0.5},
            input_filter="int")
        self.add_widget(self.guessed_number)
         
    
        self.message_label = Label(
            text="",
            font_size=20,
            pos_hint={"center_x": 0.5, "center_y": 0.9},
            color="#33cccc"
        )
        self.add_widget(self.message_label)

    def on_size(self, *args):
        """Update the rectangle position and size when the layout size changes."""
        self.rect.pos = self.pos
        self.rect.size = self.size

    def brightness_button_behavior(self, *args):
        """Change the brightness when the button is pressed"""
        app = App.get_running_app()
        app.change_brightness()
        self.play_click_sound()  # Trigger the global brightness change

    def change_brightness(self):
        """Update the background color based on the current brightness state."""
        app = App.get_running_app()

        # Check and toggle brightness state
        if app.brightness_state == (1, 1, 1, 1):  
            app.brightness_state = (0.5, 0.5, 0.5, 1)  
        elif app.brightness_state == (0.5, 0.5, 0.5, 1):  
            app.brightness_state = (0.0, 0.0, 0.0, 1)  
        elif app.brightness_state == (0.0, 0.0, 0.0, 1):  
            app.brightness_state = (1, 1, 1, 1)  

        # Update the background color of the canvas
        self.bg_color.rgba = app.brightness_state

        # Redraw the background
        self.rect.pos = self.pos
        self.rect.size = self.size
   
    
    def bestaetigen_button_behavior(self, the_searched_number):
        guessed_number_text = self.guessed_number.text
        self.play_click_sound()
        try:
            guessed_number = int(guessed_number_text)

    
            if guessed_number > the_searched_number:
                self.display_message(f"The searched number is smaller. Tries: {self.count}")
                self.count += 1
                self.guessed_number.text=''
                return
            elif guessed_number < the_searched_number:
                self.display_message(f"The searched number is bigger. Tries: {self.count}")
                self.guessed_number.text=''
                self.count += 1
                return
            elif guessed_number == the_searched_number:
                self.display_message(f"Congratulations! You found the number {the_searched_number} in {self.count} tries.")
                self.count = 1
                self.guessed_number.text =""
                return
        except ValueError:
            self.display_message("Please enter a valid number!")
            return


    def display_message(self,message):
        self.message_label.text = message

    def update_background_color(self, color):
        """Update the background color to match the brightness state"""
        self.background_color = color
        self.bg_color.rgba = color
        self.rect.pos = self.pos
        self.rect.size = self.size

    def on_size(self, *args):
        """ Update the rectangle position and size when the layout size changes. """
        self.rect.pos = self.pos
        self.rect.size = self.size
    
    def exit_button_behavior(self,*args):
        self.play_click_sound()
        app.screen_manager.current="game_window" 
   
    

 
    def change_brightness(self):
        """Change the screen's background color to simulate brightness change"""
        app = App.get_running_app()

       
        if app.brightness_state == (1, 1, 1, 1): 
            app.brightness_state = (0.5, 0.5, 0.5, 1)  
        elif app.brightness_state == (0.5, 0.5, 0.5, 1):  
            app.brightness_state = (0.0, 0.0, 0.0, 1)  
        elif app.brightness_state == (0.0, 0.0, 0.0, 1):  
            app.brightness_state = (1, 1, 1, 1) 


        self.bg_color.rgba = app.brightness_state

        
        self.rect.pos = self.pos
        self.rect.size = self.size

    def play_click_sound(self):
        if self.click_sound:
            self.click_sound.play()

        else:
            print("gi")



    
class MyApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.brightness_state = (1, 1, 1, 1)  # Default to full brightness

    def build(self):
        self.screen_manager = ScreenManager()

        # Create and add game window
        game_window = Game_Window()
        game_screen = Screen(name="game_window")
        game_screen.add_widget(game_window)
        self.screen_manager.add_widget(game_screen)

        # Create and add options menu
        options_menue = Options_Menue()
        options_screen = Screen(name="Options_Menue")
        options_screen.add_widget(options_menue)
        self.screen_manager.add_widget(options_screen)

        # Create and add in-game screen
        in_game_screen = InGame(max_number=100)  # Example max number
        in_game_screen_widget = Screen(name="InGame")
        in_game_screen_widget.add_widget(in_game_screen)
        self.screen_manager.add_widget(in_game_screen_widget)

        self.screen_manager.current = 'game_window'

        return self.screen_manager

    def change_brightness(self):
        """Change the screen's background color to simulate brightness change."""
        if self.brightness_state == (1, 1, 1, 1):  
            self.brightness_state = (0.5, 0.5, 0.5, 1)  
        elif self.brightness_state == (0.5, 0.5, 0.5, 1):  
            self.brightness_state = (0.0, 0.0, 0.0, 1)  
        elif self.brightness_state == (0.0, 0.0, 0.0, 1):  
            self.brightness_state = (1, 1, 1, 1)

        # Iterate over all screens and update the layout background color
        for screen in self.screen_manager.screens:
            for widget in screen.walk():
                if isinstance(widget, (Game_Window, Options_Menue, InGame)):
                    widget.update_background_color(self.brightness_state)



if __name__ == "__main__": 
     app = MyApp()
     app.run()
