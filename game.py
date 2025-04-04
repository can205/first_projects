class MyApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.brightness_state = (1, 1, 1, 1)  # Default to full brightness

    def build(self):
        self.screen_manager = ScreenManager()

        # Add your screens
        game_window = Game_Window()
        game_screen = Screen(name="game_window")
        game_screen.add_widget(game_window)
        self.screen_manager.add_widget(game_screen)

        options_menue = Options_Menue()
        options_screen = Screen(name="Options_Menue")
        options_screen.add_widget(options_menue)
        self.screen_manager.add_widget(options_screen)

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

        # Notify all screens to update their background colors
        for screen in self.screen_manager.screens:
            if isinstance(screen, FloatLayout):
                screen.change_brightness()
