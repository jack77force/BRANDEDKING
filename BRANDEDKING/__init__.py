from TOXIC.core.bot import TOXIC
from TOXIC.core.dir import dirr
from TOXIC.core.git import git
from TOXIC.core.userbot import Userbot
from TOXIC.misc import dbb, heroku, sudo

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = TOXIC()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
