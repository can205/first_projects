from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock

class Game_Window(GridLayout):
  
    def __init__(self, **kwargs):
       super().__init__(**kwargs)
       self.cols = 1
       self.size_hint=(1 , 1)
       self.pos_hint = {
        "center_x": 0.5,
        "center_y": 0.5,
       }



       self.add_widget(Image(source ="./number.Guesser.drawio.png"))
                       
       self.Title = Label(text = "Number Guesser",
                          font_size=(35),
                          pos_hint={
                          "x":1000,
                          "y":100000,
                          })
       self.add_widget(self.Title)
       
       
      

      
      

       self.input = TextInput(multiline=False,
           padding_y=(40),
           font_size=(20),
           size_hint=(1,1),
           )
       self.add_widget(self.input)

       self.start_button = Button (
           text = "Start",
           size_hint = (0.7, 0.7),
           )
       self.start_button.bind(on_press = self.start_button_behavior)
       self.add_widget(self.start_button)
    def start_button_behavior(self, *args):
       self.Title.text = f"Guess Number:"
       return
   

class MyApp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        self.game_window = Game_Window()
        screen = Screen(name = "game_window")
        screen.add_widget(self.game_window)
        self.screen_manager.add_widget(screen)
        self.screen_manager.current = 'game_window'
       
   
        
            
        return self.screen_manager
    
self.question = Label(text = "choose your number range")
self.add_widget(self.question)
        
Clock.schedule_once(self.move_question, 1 )
def move_question(self, dt):
            self.question.pos={20 , 20}
      

      # Test Kommentar zum pushen


if __name__ == "__main__":
  app =MyApp()
  app.run()
    
 
 


