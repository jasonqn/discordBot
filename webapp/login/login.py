from pathlib import Path
from urllib.parse import parse_qs
from urllib.parse import urlparse

from nicegui import app, Client
from nicegui import ui
from zenora import APIClient

from database.sql_queries import WebAppLogin
from webapp import config
from webapp.login import login_css as css

folder = Path(__file__).parent

discordClient = APIClient(config.TOKEN, client_secret=config.CLIENT_SECRET)
discordId = ''  # Leave empty
discordName = ''  # Leave empty

# Serve static files
app.add_static_files('/webapp/images', 'images')


# Future Jay, you're having trouble because you have put this into a class. Possibly try making the db connection
# its own function or if you use classes make the db connection a static function outside a class and just
# pull it in as needed :)


def logOut():
    ui.open('/')


@ui.page('/')
async def main_page(client: Client):
    # Link the external CSS file
    ui.add_css(css.set_background())
    ui.add_css(css.background_image())

    await client.connected()
    print("login page connected")

    with ui.card().classes('absolute-center'):
        with ui.link(target=config.OAUTH_URL):  # Button that links us to our Oauth Link.
            ui.button('Log in')


@ui.page('/home')
async def app_page(client: Client):

    await client.connected()

    with ui.card().classes('absolute-center'):
        ui.label('Logged In.')
        ui.label(f' Welcome Back: {discordName}')  # Show our new Discord Name
        ui.button('Log Out', on_click=logOut)
    try:
        async with db_connection.acquire() as connection:
            print(f"Connection made")
            # await connection.execute(CreateUsers.INSERT_USER, self.username, self.user_id)
            await connection.execute(WebAppLogin.CREATE_TABLE_WEBAPP_LOGINS)
        print("")

    except Exception as e:
        print(f"Error inserting character into database: {e}")


@ui.page('/oauth/callback')  # Set up a page for Oauth Callback
async def index(client: Client):
    await client.connected()
    url = await ui.run_javascript('window.location.href')  # Call Run JS to get the current Url
    try:
        parsed_url = urlparse(url)  # Retreive the entire URL (including the code from the  Discord Oauth processs)
        code = parse_qs(parsed_url.query)['code'][0]  # Get just the code portion from the url
        access_token = discordClient.oauth.get_access_token(code,
                                                            config.REDIRECT_URL).access_token  # Get Discord Access token using the code retreived.
        bearer_client = APIClient(access_token, bearer=True)
        current_user = bearer_client.users.get_current_user()  # Our logged in user
        global discordName
        global discordId
        discordName = current_user.username  # set Discord name string to our current username
        discordId = current_user.id  # set Discord name string to our current user id
        ui.open('/home')  # Open logged in
    except Exception as e:
        print(e)
        ui.notify(f'Error Encountered: {e}')  # Catch error.


ui.run(host='localhost', native=False)
