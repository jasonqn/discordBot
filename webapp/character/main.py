from nicegui import ui, Client, app


@ui.page('/character')
async def character_page(client: Client):

    await client.connected()
    # Set up the header
    with ui.header(elevated=True).style('background-color: #333; color: white;').classes(
            'items-center justify-between'):
        ui.label('Character Selection Page')
        with ui.row():
            ui.button(on_click=lambda: menu.toggle(), icon='menu').props('flat color=white')
        with ui.menu() as menu:
            ui.menu_item('Option 1')
            ui.menu_item('Option 2')
            ui.menu_item('Option 3')

    # Define the three-column layout below the header
    with ui.row().style('background-color: black; padding: 0; margin: 0; width: 100%; height: calc(100vh - 60px);'):
        # Left column for character list
        with ui.column().style('width: 20%; padding: 20px; background-color: #222;'):
            ui.label('Character List').style('color: white;')
            # Example character list (You can replace these with dynamic content)
            ui.button('Character 1', on_click=lambda: show_character('Character 1')).style('margin-bottom: 10px;')
            ui.button('Character 2', on_click=lambda: show_character('Character 2')).style('margin-bottom: 10px;')
            ui.button('Character 3', on_click=lambda: show_character('Character 3')).style('margin-bottom: 10px;')

        # Middle column for character display
        with ui.column().style('width: 50%; padding: 20px; background-color: #111;'):
            ui.label('Character Display').style('color: white;')
            ui.image('https://via.placeholder.com/300').style('width: 100%; height: auto;')  # Placeholder image

        # Right column for character stats and backstory
        with ui.column().style('width: 30%; padding: 20px; background-color: #222;'):
            ui.label('Character Stats & Backstory').style('color: white;')
            ui.label('Backstory:').style('color: white; margin-bottom: 10px;')
            ui.label('placeholder').style('color: white;')
            ui.label('Stats:').style('color: white; margin-bottom: 10px;')
            ui.label('Strength: 10\nDexterity: 15\nIntelligence: 12').style('color: white;')


def show_character(character_name):
    # This function would update the character display when a character is selected
    print(f'{character_name} selected')
