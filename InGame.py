class InGame(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3
        self.size_hint = (1, 1)

        
        app = App.get_running_app()  # Get the current app instance
        self.background_color = app.brightness_state  # Use the current brightness state

        with self.canvas.before:
            self.bg_color = Color(*self.background_color)  # Set initial color based on brightness_state
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self.on_size, pos=self.on_size)


        self.bestaetigen_button = Button(
            text="Bestätigen",
            size_hint=(0.27 , 0.2),
            pos_hint={
                "center_x": 0.5,
                "center_y": 0.32,
            }
        )
       
        self.bestaetigen_button.bind(on_press=self.bestaetigen_button_behavior)
        self.add_widget(self.bestaetigen_button)     
   
        self.guess_nummber_label=Label(
            text="Guess Number:",
            font_size=(30),
            pos_hint={
            "center_x": 0.5,
            "center_y": 0.63},
            color="#33cccc"
            )
        self.add_widget(self.guess_nummber_label)

        self.tries = Label(
            text="tries",
            pos_hint={"center_x": 0.85, "center_y":0.9},
            font_size=(30),
            color="#33cccc"
        )
        self.add_widget(self.tries)

        self.comparison = Label(
            text="comparison",
            font_size=(30),
            pos_hint={"center_x": 0.15 , "center_y": 0.87},
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
         
       # This label will be used to display the message (result of comparison)
        self.message_label = Label(
            text="",
            font_size=20,
            pos_hint={"center_x": 0.5, "center_y": 0.9},
            color="#33cccc"
        )
        self.add_widget(self.message_label)

    def on_size(self, *args):
        """ Update the rectangle position and size when the layout size changes. """
        self.rect.pos = self.pos
        self.rect.size = self.size

    def exit_button_behavior(self,*args):
        Clock.schedule_once(self.switch_last_view, 0.1)

    def switch_last_view(self, *args):
        app.screen_manager.current="game_window" 
    
    def bestaetigen_button_behavior(self,*kwargs ):
     
     guessed_number_text =self.guessed_number.text
     count = 1
     the_searched_number = random.randint(1, 10)
    
     is_guessing=True
     try: 
           
            guessed_number = int(guessed_number_text) 
 
     except ValueError:
            self.display_message("Please enter a valid number!")
            return
     if guessed_number == the_searched_number:
         random.randint(1,10)
     while is_guessing==True:
         
      
      
      if  guessed_number >  the_searched_number:
           self.display_message(f"The searched number is smaller. Tries: {count}")
           count += 1
           return
      
      elif guessed_number < the_searched_number:
           self.display_message(f"The searched number is bigger. Tries: {count}")
           count += 1
           return

      elif guessed_number == the_searched_number:
          self.display_message(f"Congratulations! You found the number {the_searched_number} in {count} tries.")
          is_guessing=False
          return

    def display_message(self,message):
        self.message_label.text = message
        return
   
    def brightness_button_behavior(self,*args):
     """Change the brightness when the button is pressed"""
     #  Access the current background color and call the change_brightness method without extra arguments
     app.game_window.change_brightness()  # Simply call the method without arguments

    def change_brightness(self,):
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