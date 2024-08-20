from nicegui import ui


def set_background():
    ui.query('body').style(f'background-image: url("webapp/images/TavernLandingPage.jpg");'
                           f'background-repeat: no-repeat;'
                           f'background-position: center;'
                           f'background-blend-mode: lighten;'
                           f'background-color: black;')
