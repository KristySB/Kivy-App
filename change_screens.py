from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.label import MDLabel
from kivymd.uix.scrollview import MDScrollView
from kivy.uix.relativelayout import RelativeLayout
from kivy.metrics import dp
from add_widgets import add_toolbar, add_background_image, add_back_icon, add_box_layout, add_grid_layout

class Screens:
    def open_bible(self, screen_manager, name, func, screen, func2, toolbar_func):
        screen_manager.transition.direction = 'left'
        screen_manager.current = name
        screen_manager.current_screen.clear_widgets()

        # ADD BACKGROUND IMAGE
        paper_image = add_background_image('paper5.jpg')
        screen_manager.current_screen.add_widget(paper_image)

        # ADD LAYOUTS
        main_layout = add_box_layout()
        screen_manager.current_screen.add_widget(main_layout)
        relative_layout = RelativeLayout()

        # ADD TOOLBAR
        toolbar = add_toolbar(toolbar_func)
        main_layout.add_widget(toolbar)
        main_layout.add_widget(relative_layout)

        # CREATE CHAPTER BUTTTONS IN GRID LAYOUT
        grid_layout = add_grid_layout(3, 9)

        book_names = ['Matthew', 'Mark', 'Luke', 'John', 'Acts', 'Romans', '1 Corint', '2 Corint',
            'Galatians', 'Ephesians', 'Philippians', 'Colossians', '1 Thess', '2 Thess',
            '1 Timothy', '2 Timothy', 'Titus', 'Philemon', 'Hebrews', 'James', '1 Peter', '2 Peter',
            '1 John', '2 John', '3 John', 'Jude', 'Revelation']
        num = 0
        for x in range(27):
            button = MDButton(
                MDButtonText(
                    text = book_names[num],
                    pos_hint = {'center_x': 0.5, 'center_y': 0.5}                   
                ),
                theme_width = 'Custom',
                height = dp(45),
                style = 'elevated',
                on_press = func
            )
            grid_layout.add_widget(button)
            num += 1

        # ADD SCROLLVIEW
        scroll_view = MDScrollView(size_hint = (1,1))
        scroll_view.add_widget(grid_layout)
        relative_layout.add_widget(scroll_view)

        # ADD BACK ICON
        back_icon = add_back_icon(func2)
        toolbar.add_widget(back_icon)
    
    def open_book(self, screen_manager, name, ch_name, func, screen, func2, toolbar_func):
        screen_manager.transition.direction = 'left'
        screen_manager.current = name
        screen_manager.current_screen.clear_widgets()

        # ADD BACKGROUND IMAGE
        paper_image = add_background_image('paper5.jpg')
        screen_manager.current_screen.add_widget(paper_image)

        # ADD LAYOUTS
        main_layout = add_box_layout()
        screen_manager.current_screen.add_widget(main_layout)
        relative_layout = RelativeLayout()

        # ADD TOOLBAR
        toolbar = add_toolbar(toolbar_func)
        main_layout.add_widget(toolbar)
        main_layout.add_widget(relative_layout)

        # CREATE NUMBER BUTTONS
        chapters_numbers = {'Matthew': 28, 'Mark': 16, 'Luke': 24, 'John': 21, 'Acts': 28, 'Romans': 16, '1 Corint': 16, '2 Corint': 13, 'Galatians': 6, 'Ephesians': 6, 'Philippians': 4, 'Colossians': 4, '1 Thess': 5, '2 Thess': 3, '1 Timothy': 6, '2 Timothy': 4, 'Titus': 3, 'Philemon': 1, 'Hebrews': 13, 'James': 5, '1 Peter': 5, '2 Peter': 3, '1 John': 5, '2 John': 1, '3 John': 1, 'Jude': 1, 'Revelation': 22}

        verses = []
        chapter_name = ch_name
        number = chapters_numbers[chapter_name]

        grid_layout = add_grid_layout(4, 7)

        if number > 3:
            for x in range(0, number):
                button = MDButton(
                    MDButtonText(
                        text = str(x + 1),
                        pos_hint = {'center_x': 0.5, 'center_y': 0.5}
                    ),
                    theme_width = 'Custom',
                    height = dp(40),
                    style = 'elevated',
                    on_press = func
                )
                grid_layout.add_widget(button)
        else:
            for x in range(0, number):
                button = MDButton(
                    MDButtonText(
                        text = str(x + 1),
                        pos_hint = {'center_x': 0.5, 'center_y': 0.5}
                    ),
                    theme_width = 'Custom',
                    size_hint_x = None,
                    width = dp(60),
                    height = dp(40),
                    style = 'elevated',
                    on_press = func
                )
                grid_layout.add_widget(button)

        # ADD SCROLLVIEW
        scroll_view = MDScrollView(size_hint = (1,1))
        scroll_view.add_widget(grid_layout)
        relative_layout.add_widget(scroll_view)

        # ADD BACK ICON
        back_icon = add_back_icon(func2)
        toolbar.add_widget(back_icon)
    
    def open_chapter(self, screen_manager, name, screen, chapter_number, ch_name, func, toolbar_func):
        screen_manager.transition.direction = 'left'
        screen_manager.current = name
        screen_manager.current_screen.clear_widgets()

        # ADD BACKGROUND IMAGE
        paper_image = add_background_image('paper5.jpg')
        screen_manager.current_screen.add_widget(paper_image)

        # ADD LAYOUTS
        main_layout = add_box_layout()
        screen_manager.current_screen.add_widget(main_layout)
        relative_layout = RelativeLayout()

        # ADD TOOLBAR
        toolbar = add_toolbar(toolbar_func)
        main_layout.add_widget(toolbar)
        main_layout.add_widget(relative_layout)

        # ADD TEXT
        chapter = chapter_number
        chapter_name = ch_name
        if chapter_name == '1 Corint':
            chapter_name = '1 Corinthians'
        if chapter_name == '2 Corint':
            chapter_name = '2 Corinthians'
        if chapter_name == '1 Thess':
            chapter_name = '1 Thessalonians'
        if chapter_name == '2 Thess':
            chapter_name = '2 Thessalonians'
        chapter_starts_with = chapter_name + ' ' + chapter

        chapter_text = ''
        with open('bibbia.txt', 'r') as b:
            for line in b:
                if chapter_starts_with in line:
                    for x in line.split(chapter_starts_with)[1]:
                        if x == ':':
                            chapter_text += line
                        else:
                            break

        chapter_text = chapter_text.replace('\t', ' ')

        # ADD SCROLLVIEW
        read_chapter = MDScrollView(
                MDLabel(
                    text = chapter_text,
                    theme_text_color = 'Custom',
                    text_color = '000d4d',
                    adaptive_height = True,
                    pos_hint = {'center_x': 0.5, 'center_y': 0.5},
                    padding = (dp(10), dp(10)),
                    halign = 'left',
                    valign = 'top' 
                )
                )
        
        relative_layout.add_widget(read_chapter)

        # ADD BACK ICON
        back_icon = add_back_icon(func)
        toolbar.add_widget(back_icon)