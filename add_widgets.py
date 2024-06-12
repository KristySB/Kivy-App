from kivymd.uix.appbar import MDTopAppBar, MDTopAppBarTitle, MDActionTopAppBarButton, MDTopAppBarLeadingButtonContainer
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.metrics import dp
from kivy.uix.image import Image
from kivymd.uix.navigationdrawer import( 
    MDNavigationDrawer,
    MDNavigationDrawerMenu,
    MDNavigationDrawerLabel,
    MDNavigationDrawerItem,
    MDNavigationDrawerItemText,
    MDNavigationDrawerDivider
)

def add_toolbar(func):
    toolbar = MDTopAppBar(
        MDTopAppBarLeadingButtonContainer(
            MDActionTopAppBarButton(
                id = 'menud',
                icon = 'menu',
                on_release = func
            )
        ),
        MDTopAppBarTitle(
            text = 'The Bible',
            pos_hint = {'center_x': 0.5, 'center_y': 0.5},
            theme_text_color = 'Custom',
            text_color = '053f8a',
            theme_font_name = 'Custom',
            font_name = 'RobotoBlack'
        ),
        type = 'small',
        pos_hint = {'top': 1}
    )
    return toolbar

def add_menu(func1, func2):
        navigation_drawer = MDNavigationDrawer(
            MDNavigationDrawerMenu(
                MDNavigationDrawerLabel(
                    text = 'MENU',
                    theme_text_color = 'Custom',
                    text_color = '053f8a'
                ),
                MDNavigationDrawerItem(
                    MDNavigationDrawerItemText(
                        text = 'Main page',
                        theme_text_color = 'Custom',
                        text_color = '053f8a'
                    ),
                    on_release = func1
                ),
                MDNavigationDrawerDivider(
                ),
                MDNavigationDrawerItem(
                    MDNavigationDrawerItemText(
                        text = 'Open Bible',
                        theme_text_color = 'Custom',
                        text_color = '053f8a'
                    ),
                    on_release = func2
                )
            ),
            id = 'drawer',
            radius = (0, dp(16), dp(16), 0)
        )
        return navigation_drawer

def add_background_image(name):
    paper_image = Image(
            source = name,
            allow_stretch = True,
            keep_ratio = False
        )
    return paper_image

def add_back_icon(func):
    back_icon = MDActionTopAppBarButton(
            icon = 'backup-restore',
            on_press = func
    )
    return back_icon

def add_box_layout():
    main_layout = MDBoxLayout(
            orientation = 'vertical',
            padding = dp(10),
            spacing = dp(10)
        )
    return main_layout

def add_grid_layout(cols, rows):
    grid_layout = GridLayout(
            cols = cols,
            rows = rows,
            padding = (dp(20), dp(20), dp(20), dp(20)),
            spacing = dp(20),
            size_hint_y = None
        )
    grid_layout.bind(minimum_height = grid_layout.setter('height'))
    return grid_layout