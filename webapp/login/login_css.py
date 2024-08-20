from nicegui import ui


def set_background():
    ui.query('body').style(f'background-image: url("webapp/images/TavernLandingPage.jpg");'
                           f'background-repeat: no-repeat;'
                           f'background-position: center;'
                           f'background-size: cover'
                           f'background-color: black;'
                           f'filter: blur(8px);')

    with ui.header(elevated=True).style('background-color: black').classes('items-center justify-between'):
        ui.label('HEADER')
        ui.button(on_click=lambda: right_drawer.toggle(), icon='menu').props('flat color=white')
    with ui.right_drawer(fixed=False).style('background-color: #ebf1fa').props('bordered') as right_drawer:
        ui.label('RIGHT DRAWER')
    with ui.footer().style('background-color: black'):
        ui.label('FOOTER')

