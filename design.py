from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput

class WelcomeView (GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.size_hint = (0.6 , 0.7)
        self.pos_hint = {
            "center_x": 0.5,
            "center_y":  0.5
         }

        self.add_widget(Image(source = "./number.Guesser.drawio.png"))
        self.greeting = Label (text = "Wie heißt du",
                                font_size=30,
                                color = "#33cccc",)
        self.add_widget(self.greeting)

        self.user = TextInput( 
             multiline=False,
             padding_y = (25, 25),
             size_hint = (1, 0.5),
             )
        
        self.add_widget(self.user)

        self.entrance_Button = Button (
             text = "Eintreten",
             size_hint = (1, 0.5),
             bold=True,
             background_color="#33cccc",
             background_normal="",
             )
        self.entrance_Button.bind(on_press = self.entrance_Button_behavior)
        self.add_widget(self.entrance_Button)
   
    def entrance_Button_behavior(self,*args):
         self.greeting.text = f"Herzlich Wilkommen {self.user.text}"
         Clock.schedule_once(self.switch_to_next_view, 1)

    def switch_to_next_view(self,*args):
     #     self.get_root_window().children[0].current = "stockview"  #test this
         app.screen_manager.current = "stockview"

class Stockview(GridLayout):
     def __init__(self,**kwargs):
         super().__init__(**kwargs)  
         self.cols = 1
         self.size_hint = (0.9, 0.9)
         self.pos_hint ={
             "center_x": 0.5,
              "center_y": 0.5,
          }
         """
           Ticker      Name        Preis      Löschen     
           Ticker      Name        Preis      Löschen
          ------------------------
          Label  Tickereingabe               Zufügen
          """
         
         self.stock_view = ScrollView(size_hint = (1, 0.9))
         self.stock_list = GridLayout (
              cols = 4,
              size_hint = (1, None),
              height = 30,
          #     height = self.minimum_height,
          #     row_default_height = 30,
          #     row_force_default = True,
              )
         # Bind minimum height to the height property
         self.stock_list.bind(minimum_height=self.stock_list.setter('height')) # test this
   
         self.stock_view.add_widget(self.stock_list)
         self.add_widget(self.stock_view)
         self.stock_add = GridLayout(cols = 3, size_hint = (1, 0.1))
         self.add_widget(self.stock_add)

         self.ticker_text = Label(
              text = "Symbol/Ticker:",
              size_hint = (0.2, 0.5),
              )
      
         self.stock_add.add_widget(self.ticker_text)

         self.ticker_input = TextInput(
              multiline = False,
              padding_y = (18, 5),
              size_hint = (0.6, 0.5),
              )
        
         self.stock_add.add_widget(self.ticker_input)
         self.ticker_add = Button(
              text = "Zufügen",
              size_hint = (0.2, 0.5),
              bold = True,
              background_color = "#33cccc",
              background_normal = "",
              )
        
         self.ticker_add.bind(on_press = self.add_ticker_symbol)
         self.stock_add.add_widget(self.ticker_add)

     # def add_ticker_symbol(self, *args):
     #      symbol = self.ticker_input.text.strip()
     #      if not symbol:
     #           return
     #      try:
     #            stock = yfinance.Ticker(ticker = symbol)
     #            data = stock.info
     #            self.add_ticker_row(data["symbol"], data["longName"], data["regularMarketPrice"])
     #      except Exception as e:
     #          print(f"Could not retrieve data for symbol: {symbol}. Error {e}")


          

     def add_ticker_row(self, ticker, name, price):
          
          ticker = Label(text = str(ticker), size_hint_x = 0.2)
          self.stock_list.add_widget(ticker)

          name = Label(text = str(name), size_hint_x = 0.4)
          self.stock_list.add_widget(name)

          price = Label(text = str(price), size_hint_x = 0.2)
          self.stock_list.add_widget(price)

          delete = Button(text = "Enfernen", size_hint_x = 0.2)
          delete.bind(on_press = self.remove_ticker_row)
          self.stock_list.add_widget(delete)

     def remove_ticker_row(self, instance, *args):
          row_index = self.stock_list.children.index(instance)
        
          print("Entfernen Button funktioniert")
          for _ in range(4):
            if self.stock_list.children:
                self.stock_list.remove_widget(self.stock_list.children[row_index])



class MyApp(App):
     def build(self):
         self.screen_manager = ScreenManager()

         self.welcome_view = WelcomeView()
         screen = Screen(name = "welcome_view")
         screen.add_widget(self.welcome_view)
         self.screen_manager.add_widget(screen)

         self.stock_view = Stockview()
         screen = Screen(name = "stockview")
         screen .add_widget(self.stock_view)
         self.screen_manager.add_widget(screen)

         self.screen_manager.current = "welcome_view"
         return self.screen_manager

     #     self.stock_view = Stockview()
     #     screen = Screen(name = "Stockview")
     #     screen.add_widget(self.stock_view)
     #     self.screen_manager.add_widget(screen)


       


if __name__ == "__main__":
    app = MyApp()
    app.run()