import os
from decouple import config
from Config.Singleton import Singleton
from Config.Folder import Folder


class VConfigs(Singleton):
    def __init__(self) -> None:
        if not super().created:
            self.BOT_PREFIX = '!'
            try:
                self.BOT_TOKEN = config('BOT_TOKEN')
                self.SPOTIFY_ID = config('SPOTIFY_ID')
                self.SPOTIFY_SECRET = config('SPOTIFY_SECRET')
                self.BOT_PREFIX = config('BOT_PREFIX')
            except:
                print(
                    '[ERROR] -> You must create and .env file with all required fields, see documentation for help')

            self.CLEANER_MESSAGES_QUANT = 5
            self.ACQUIRE_LOCK_TIMEOUT = 10
            self.QUEUE_VIEW_TIMEOUT = 120
            self.COMMANDS_FOLDER_NAME = 'DiscordCogs'
            self.COMMANDS_PATH = f'{Folder().rootFolder}{self.COMMANDS_FOLDER_NAME}'
            self.VC_TIMEOUT = 300

            self.CHANCE_SHOW_PROJECT = 15
            self.PROJECT_URL = ''
            self.SUPPORTING_ICON = ''

            self.MAX_PLAYLIST_LENGTH = 50
            self.MAX_PLAYLIST_FORCED_LENGTH = 5
            self.MAX_SONGS_IN_PAGE = 10
            self.MAX_PRELOAD_SONGS = 15
            self.MAX_SONGS_HISTORY = 15

            self.INVITE_MESSAGE = """Чтобы пригласить вику на свой собственный сервер, нажмите [here]({}). 
            Или используйте этот прямой URL: {}"""

            self.MY_ERROR_BAD_COMMAND = 'Эта строка служит для проверки, была ли какая-то ошибка вызвана мной намеренно'
            self.INVITE_URL = 'https://discord.com/api/oauth2/authorize?client_id={}&permissions=8&scope=bot'

    def getProcessManager(self):
        return self.__manager

    def setProcessManager(self, newManager):
        self.__manager = newManager
