from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle


class Game_Window(GridLayout):
    def __init__(self, **kwargs):
       super().__init__(**kwargs)
       self.cols = 1
       self.size_hint=(0.8 , 0.8)
       self.pos_hint = {
        "center_x": 0.5,
        "center_y": 0.5,
       }
       self.background_Color= (1,1,1,1)
       with self.canvas.before:
            self.bg_Color = Color(*self.background_Color)
            self.rect = Rectangle(size=self.size, pos=self.pos)


       self.Title = Label(
          text = "Number Guesser",
          font_size=(35),
          color = "#33cccc",
          pos_hint={
          "x":1000,
          "y":100000,
          })
       self.add_widget(self.Title)
       
       self.question = Label(
          text = "choose your number range",
          font_size=(30))
       
       self.add_widget(self.question)
        
                
       self.input = TextInput(
           multiline=False,
           padding_y=(25),
           padding_x=(250),
           font_size=(20),
           size_hint=(0.6 , 0.6),
           )
       self.add_widget(self.input)

       

       self.options_button = Button(
          text = "Options",
          size_hint=(0.6, 0.6),
          font_size=(30)
       )

       self.options_button.bind(on_release = self.options_button_behavior)
       self.add_widget(self.options_button)

       self.start_button = Button (
           text = "Start",
           size_hint = (0.6, 0.6),
           pos=(1,1),
           padding_x=(200),
           font_size=(30)
           )
       self.start_button.bind(on_release = self.start_button_behavior)
       self.add_widget(self.start_button)
       return 
    
    def options_button_behavior(self, *args):
       Clock.schedule_once(self.switch_to_next_view,0.1)

 
    def switch_to_next_view (self,*args):
       app.screen_manager.current = "Options_Menue"

   

    def start_button_behavior(self, *args):
       Clock.schedule_once(self.switch_next_view)

    def switch_next_view(self,*args):
       app.screen_manager.current = "InGame"

       def change_brightness(self, brightness):
        """Change the screen's background color to simulate brightness change"""
        if brightness == "bright":
            self.background_color = (1, 1, 1, 1)  # Full brightness (white)
        elif brightness == "dim":
            self.background_color = (0.5, 0.5, 0.5, 1)  # Dim (gray)
        else:
            self.background_color = (0.2, 0.2, 0.2, 1)  # Very dark

        self.bg_color.rgba = self.background_color
        self.rect = Rectangle(size=self.size, pos=self.pos)
        
class InGame(FloatLayout):
   def  __init__(self, **kwargs):
       super().__init__(**kwargs)
       self.cols=3
       self.size_hint=(1 , 1)
      
       self.guess_number=TextInput(
          multiline=False,
          padding_y=(30),
          font_size=(20),
          size_hint=(0.27 , 0.15),
          pos_hint={
             "center_x": 0.5,
             "center_y": 0.54,
          }
       )
       self.add_widget(self.guess_number)

       self.bestätigen_button = Button(
          text = "Bestätigen",
          size_hint=(0.27 , 0.15),
          pos_hint={
            "center_x": 0.5,
            "center_y": 0.39,
          }
          )
       
       self.bestätigen_button.bind(on_release= self.bestätigen_button_behavior)
       self.add_widget(self.bestätigen_button)

   def bestätigen_button_behavior(self,*kwargs):
      print("works")




class Options_Menue (GridLayout):
   def  __init__(self, **kwargs):
       super().__init__(**kwargs)
       self.cols = 1
       self.size_hint = (0.8 , 0.8)
       self.pos_hint = {
          "center_x": 0.5,
          "center_y": 0.5
       }
    #    self.background_Color=(1 , 1 , 1 , 1)


       
       self.volume_button = Button(
          text="volume",
          size_hint=(0.6 , None),
          height=(120),
          pos_hint=(0.15 , 0.2),
          font_size=(35)
          )
       self.add_widget(self.volume_button)

       self.brightness_button = Button(
          text="brigthness",
          size_hint=(0.6 , None),
          height=(120),
          pos_hint=(0.55 , 0.5),
          font_size=(35)
       )
       self.add_widget(self.brightness_button)

       self.theme_button = Button(
          text="Theme",
          size_hint = (0.5 , None),
          height=(120),
          pos_hint = (0.35 , 0.5),
          font_size=(35)
       )
       self.add_widget(self.theme_button)

       self.back_to_menue_button = Button(
          text="back to menue",
          size_hint = (0.6 ,None),
          height=(120),
          pos_hint=(0.75 , 0.5),
          font_size=(35)
       )
       self.add_widget(self.back_to_menue_button)
       self.back_to_menue_button.bind(on_release=self.back_to_menue_button_behavior)


   def change_brightness(self, instance):
        """Change brightness when the button is pressed"""
        app.game_window.change_brightness("dim")  # Change to dim

   def back_to_menue_button_behavior(self,*args):
          Clock.schedule_once(self.switch_to_last_view)

   def switch_to_last_view(self,*kwargs):
          app.screen_manager.current = "game_window"
          
       
       



class MyApp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        self.game_window = Game_Window()
        screen = Screen(name = "game_window")
        screen.add_widget(self.game_window)
        self.screen_manager.add_widget(screen)
        

        self.in_game = InGame()
        screen = Screen(name = "InGame")
        screen.add_widget(self.in_game)
        self.screen_manager.add_widget(screen)
        
        self.options_menue = Options_Menue()
        screen = Screen(name = "Options_Menue")
        screen.add_widget(self.options_menue)
        self.screen_manager.add_widget(screen)
        
        Clock.schedule_once(self.move_question,120  )
   
        
        self.screen_manager.current = 'game_window'
        return self.screen_manager
    



    def move_question(self, dt  ):
     minutes = dt / 60
     print(f"second is {minutes} minutes")
     self.game_window.question.pos=(0 , 20)


     
      
 


if __name__ == "__main__":
  app =MyApp()
  app.run()
    
 
 


