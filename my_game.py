from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image


class MyApp(App):
    def build():
        window = GridLayout()
        window.cols = 1

        window.add_widget(Image(source= "./number.Guesser.drawio.png"))
                               

        return window
                
    
if __name__ == "__main__":
 
    app = MyApp()
    app.run()


