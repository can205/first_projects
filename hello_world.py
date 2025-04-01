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
                           
       self.Title = Label(
          text = "Number Guesser",
          font_size=(35),
          pos_hint={
          "x":1000,
          "y":100000,
          })
       self.add_widget(self.Title)
       
       self.question = Label(
          text = "choose your number range",
          font_size=(20))
       
       self.add_widget(self.question)
        
                
       self.input = TextInput(
           multiline=False,
           padding_y=(38),
           padding_x=(850),
           font_size=(40),
           size_hint=(0.7 , 0.7),
           )
       self.add_widget(self.input)

       

       self.options_button = Button(
          text = "Options",
          size_hint=(0.7, 0.7),
       )

       self.options_button.bind(on_press = self.options_button_behavior)
       self.add_widget(self.options_button)

       self.start_button = Button (
           text = "Start",
           size_hint = (0.7, 0.7),
           pos=(1,1),
           padding_x=(200)
           )
       self.start_button.bind(on_press = self.start_button_behavior)
       self.add_widget(self.start_button)
       return 
       
    def options_button_behavior(self, *args):
       Clock.schedule_once(self.switch_to_next_view,0.1)

 
    def switch_to_next_view (self,*args):
       print("hi")
    #    app.screen_manager.current = "options_menue"

   

    def start_button_behavior(self, *args):
         self.Title.text = f"Guess Number:"
         

        

# class In_Game(GridLayout):
#    def 
    
# class options_menue(GridLayout):
#    def   


class MyApp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        self.game_window = Game_Window()
        screen = Screen(name = "game_window")
        screen.add_widget(self.game_window)
        self.screen_manager.add_widget(screen)
        self.screen_manager.current = 'game_window'


        Clock.schedule_once(self.move_question,120  )
   
        
            
        return self.screen_manager
    def move_question(self, dt  ):
     minutes = dt / 60
     print(f"second is {minutes} minutes")
     self.game_window.question.pos=(0 , 20)


     
      

      


if __name__ == "__main__":
  app =MyApp()
  app.run()
    
 
 


