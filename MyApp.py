class MyApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Define the initial brightness state
        self.brightness_state = (1, 1, 1, 1)  # Full brightness (white)
        
    def build(self):
        self.screen_manager = ScreenManager()

        self.game_window = Game_Window()  # Create Game_Window object
        screen = Screen(name="game_window")
        screen.add_widget(self.game_window)
        self.screen_manager.add_widget(screen)

        # Create the InGame screen
        self.in_game = InGame()  # Create InGame object
        screen = Screen(name="InGame")
        screen.add_widget(self.in_game)
        self.screen_manager.add_widget(screen)

        # Create the Options Menu screen
        self.options_menue = Options_Menue()  # Create Options_Menue object
        screen = Screen(name="Options_Menue")
        screen.add_widget(self.options_menue)
        self.screen_manager.add_widget(screen)

        self.screen_manager.current = 'game_window'
        
        return self.screen_manager