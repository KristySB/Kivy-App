
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDButton, MDButtonIcon, MDButtonText
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.metrics import dp
from kivy.uix.relativelayout import RelativeLayout
from add_widgets import add_toolbar, add_background_image, add_back_icon, add_menu
from change_screens import Screens

class Bible(MDApp):
    def back_to_precedent_screen(self, screen_name):
        self.screen_manager.current = screen_name
        self.screen_manager.transition.direction = 'right'

    def get_to_screens(self, screen_name):
        self.navigation_drawer.set_state('close')
        self.screen_manager.current = screen_name
        self.screen_manager.transition.direction = 'left'

    def open_verse(self):
        print(self.verse_for_today)

    def menu_options(self):
        self.navigation_drawer = add_menu(lambda x: self.get_to_screens('MainScreen'), lambda x: self.open_bible('OpenBible'))
        self.screen_manager.current_screen.add_widget(self.navigation_drawer)
        self.navigation_drawer.set_state('toggle')
        self.nav_drawer_status = True

    def find_chapter(self, instance):
        self.chapter_number = instance._button_text.text
        self.open_chapter('OpenChapter')

    def open_chapter(self, name):
        self.screens.open_chapter(self, screen_manager = self.screen_manager, name = name, screen = self.screen4, chapter_number = self.chapter_number, ch_name = self.chapter_name, func = lambda x: self.back_to_precedent_screen('OpenBook'), toolbar_func = lambda x: self.menu_options())
        

    def find_book_name(self, instance):
        self.chapter_name = instance._button_text.text
        self.open_book('OpenBook')
        return self.chapter_name
    
    def open_book(self, name):
        self.screens.open_book(self, screen_manager = self.screen_manager, name = name, ch_name = self.chapter_name, func = self.find_chapter, screen = self.screen3, func2 = lambda x: self.back_to_precedent_screen('OpenBible'), toolbar_func = lambda x: self.menu_options())
        

    def open_bible(self, name):
        if self.nav_drawer_status == True:
            self.navigation_drawer.set_state('close')
        
        self.screens.open_bible(self, screen_manager = self.screen_manager, name = name, func = self.find_book_name, screen = self.screen2, func2 = lambda x: self.back_to_precedent_screen('MainScreen'), toolbar_func = lambda x: self.menu_options())

    def build(self):
        self.screens = Screens
        self.nav_drawer_status = False
        self.screen_manager = ScreenManager()
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = 'Slategrey'

        # MAIN SCREEN
        self.screen = MDScreen(name = 'MainScreen', md_bg_color = self.theme_cls.secondaryContainerColor)
        self.screen.clear_widgets()

        main_layout = MDBoxLayout(
            orientation = 'vertical',
            padding = dp(10),
            spacing = dp(10)
        )
        relative_layout = RelativeLayout()
        button = MDButton(
            MDButtonText(
                text = 'Open Bible'
            ),
            MDButtonIcon(
                icon = 'book-open-variant-outline'
            ),
            pos_hint = {'center_x': 0.5, 'center_y': 0.55},
            style = 'elevated',
            on_press = lambda x: self.open_bible('OpenBible')
        )

        bible_image = add_background_image('book.jpg')
        toolbar = add_toolbar(lambda x: self.menu_options())
        main_layout.add_widget(toolbar)
        relative_layout.add_widget(bible_image)
        relative_layout.add_widget(button)
        main_layout.add_widget(relative_layout)
        
        self.screen.add_widget(main_layout)
        self.screen_manager.add_widget(self.screen)

        # OTHER SCREENS
        self.screen2 = MDScreen(name = 'OpenBible', md_bg_color = self.theme_cls.secondaryContainerColor)
        self.screen_manager.add_widget(self.screen2)
        self.screen3 = MDScreen(name = 'OpenBook', md_bg_color = self.theme_cls.secondaryContainerColor)
        self.screen_manager.add_widget(self.screen3)
        self.screen4 = MDScreen(name = 'OpenChapter', md_bg_color = self.theme_cls.secondaryContainerColor)
        self.screen_manager.add_widget(self.screen4)

        self.screen_manager.current = 'MainScreen'
        return self.screen_manager
Bible().run()