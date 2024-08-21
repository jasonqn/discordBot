from nicegui import ui


def set_background():
    with ui.header(elevated=True).style('background-color: black;').classes('items-center justify-between'):
        ui.label('HEADER')
        ui.button(on_click=lambda: right_drawer.toggle(), icon='menu').props('flat color=white')
    with ui.right_drawer(fixed=False).style('background-color: #ebf1fa').props('bordered') as right_drawer:
        ui.label('RIGHT DRAWER')
    with ui.footer(elevated=True).style('background-color: black;'):
        ui.label('FOOTER')


def background_image():
    ui.image().style('position: absolute;'  # Position it absolutely to cover the screen
                     'top: 0;'
                     'left: 0;'
                     'width: 100vw;'  # Full width of the viewport
                     'height: 100vh;'  # Full height of the viewport
                     'background-image: url("webapp/images/TavernLandingPage.jpg");'
                     'background-repeat: no-repeat;'
                     'background-position: center;'
                     'background-size: cover;'
                     'background-color: black;'
                     'filter: blur(3px);'
                     'margin: 0;'
                     'padding: 0;'
                     'z-index: -1;')  # Ensure it's behind other elements
