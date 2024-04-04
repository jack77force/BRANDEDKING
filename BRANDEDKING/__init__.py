from BRANDED.core.bot import BRANDED.core.bot
from BRANDED.core.bot.core.dir import dirr
from BRANDED.core.bot.core.git import git
from BRANDED.core.bot.core.userbot import Userbot
from BRANDED.core.bot.misc import dbb, heroku, sudo

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = BRANDED.core.bot()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
