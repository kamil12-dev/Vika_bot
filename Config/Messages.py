from Config.Singleton import Singleton
from Config.Configs import VConfigs
from Config.Emojis import VEmojis


class Messages(Singleton):
    def __init__(self) -> None:
        if not super().created:
            self.__emojis = VEmojis()
            configs = VConfigs()
            self.STARTUP_MESSAGE = 'Запуск vika...'
            self.STARTUP_COMPLETE_MESSAGE = 'vika теперь работает.'

            self.SONGINFO_UPLOADER = "Загрузил: "
            self.SONGINFO_DURATION = "Продолжительность: "
            self.SONGINFO_REQUESTER = 'Запросил: '
            self.SONGINFO_POSITION = 'Позиция: '

            self.SONGS_ADDED = 'Загрузка `{}` песен для добавления в очередь'
            self.SONG_ADDED = 'Загрузка песни `{}` для добавления в очередь'
            self.SONG_ADDED_TWO = f'Песня добавлена в очередь'
            self.SONG_PLAYING = f' Сейчас играет песня'
            self.SONG_PLAYER = f' Проигрыватель песен'
            self.QUEUE_TITLE = f' Песни в очереди'
            self.ONE_SONG_LOOPING = f'Зацикливание одной песни'
            self.ALL_SONGS_LOOPING = f' Зацикливание всех песен'
            self.SONG_PAUSED = f'{self.__emojis.PAUSE} Песня остановилась'
            self.SONG_RESUMED = f'{self.__emojis.PLAY} Воспроизведение песни'
            self.SONG_SKIPPED = f'{self.__emojis.SKIP} Песня пропущена'
            self.RETURNING_SONG = f'{self.__emojis.BACK} Воспроизведение предыдущей песни'
            self.STOPPING = f'{self.__emojis.STOP} Игрок остановился'
            self.EMPTY_QUEUE = f'{self.__emojis.QUEUE} Очередь песен пуста, используйте {configs.BOT_PREFIX}воспроизводите, чтобы добавлять новые песни'
            self.SONG_DOWNLOADING = f'{self.__emojis.DOWNLOADING} Загрузка...'
            self.PLAYLIST_CLEAR = f' Список воспроизведения теперь пуст'

            self.HISTORY_TITLE = f' Проигрываемые песни'
            self.HISTORY_EMPTY = f'{self.__emojis.QUEUE} В истории нет музыки'

            self.SONG_MOVED_SUCCESSFULLY = 'Песня `{}` в положении `{}` перемещен на позицию `{}` успешно'
            self.SONG_REMOVED_SUCCESSFULLY = 'Песня `{}` удалено успешно'

            self.LOOP_ALL_ON = f'{self.__emojis.ERROR} Вика зацикливает все песни, используйте {configs.BOT_PREFIX}отключите цикл, чтобы сначала отключить этот цикл'
            self.LOOP_ONE_ON = f'{self.__emojis.ERROR} Вика зацикливает одну песню, используйте {configs.BOT_PREFIX}отключите цикл, чтобы сначала отключить этот цикл'
            self.LOOP_ALL_ALREADY_ON = f'{self.__emojis.LOOP_ALL} Вика уже зацикливает все песни'
            self.LOOP_ONE_ALREADY_ON = f'{self.__emojis.LOOP_ONE} Вика уже зацикливает текущую песню'
            self.LOOP_ALL_ACTIVATE = f'{self.__emojis.LOOP_ALL} Зацикливание всех песен'
            self.LOOP_ONE_ACTIVATE = f'{self.__emojis.LOOP_ONE} Зацикливание текущей песни'
            self.LOOP_DISABLE = f'{self.__emojis.LOOP_OFF} Цикл отключен'
            self.LOOP_ALREADY_DISABLE = f'{self.__emojis.ERROR} Цикл уже отключен'
            self.LOOP_ON = f'{self.__emojis.ERROR} Эта команда не может быть вызвана при активированном цикле. Воспользуйся {configs.BOT_PREFIX}отключение цикла для отключения цикла'
            self.BAD_USE_OF_LOOP = f"""{self.__emojis.ERROR} Недопустимые аргументы команды цикла. Воспользуйся {configs.BOT_PREFIX}справочный цикл для получения дополнительной информации.
                                -> Available Arguments: ["all", "off", "one", ""]"""

            self.SONGS_SHUFFLED = f'{self.__emojis.SHUFFLE} Песни успешно перемешаны'
            self.ERROR_SHUFFLING = f'{self.__emojis.ERROR} Ошибка при перемешивании песен'
            self.ERROR_MOVING = f'{self.__emojis.ERROR} Ошибка при перемещении песен'
            self.LENGTH_ERROR = f'{self.__emojis.ERROR} Число должно быть от 1 до длины очереди, используйте -1 для последней песни'
            self.ERROR_NUMBER = f'{self.__emojis.ERROR} Для этой команды требуется число'
            self.ERROR_PLAYING = f'{self.__emojis.ERROR} Ошибка при воспроизведении песен'
            self.COMMAND_NOT_FOUND = f'{self.__emojis.ERROR} Команда не найдена, введите {configs.BOT_PREFIX}помощь, чтобы увидеть все команды'
            self.UNKNOWN_ERROR = f'{self.__emojis.ERROR} Неизвестная ошибка, при необходимости используйте {configs.BOT_PREFIX}сброс, чтобы сбросить проигрыватель на вашем сервере'
            self.ERROR_MISSING_ARGUMENTS = f'{self.__emojis.ERROR} Отсутствующие аргументы в этой команде. Введите {configs.BOT_PREFIX}справка "команда", чтобы увидеть больше информации об этой команде'
            self.NOT_PREVIOUS = f'{self.__emojis.ERROR} Нет предыдущей песни, которую можно было бы воспроизвести'
            self.PLAYER_NOT_PLAYING = f'{self.__emojis.ERROR} Песня не играет. Введите {configs.BOT_PREFIX}воспроизведение, чтобы запустить проигрыватель'
            self.IMPOSSIBLE_MOVE = 'Это невозможно :('
            self.ERROR_TITLE = 'Ошибка :-('
            self.COMMAND_NOT_FOUND_TITLE = 'Странно :-('
            self.NO_CHANNEL = 'Чтобы воспроизвести музыку, сначала подключитесь к голосовому каналу.'
            self.NO_GUILD = f'На этом сервере нет проигрывателя, попробуйте {configs.BOT_PREFIX}сброс'
            self.INVALID_INPUT = f'Неправильный URL, попробуйте что-то другое или введите {configs.BOT_PREFIX}помощь играть'
            self.INVALID_INDEX = f'Неверный индекс, переданный в качестве аргумента.'
            self.INVALID_ARGUMENTS = f'Недопустимые аргументы, переданные команде.'
            self.DOWNLOADING_ERROR = f"{self.__emojis.ERROR} Невозможно загрузить и воспроизвести это видео"
            self.EXTRACTING_ERROR = f'{self.__emojis.ERROR} Произошла ошибка при поиске песен'

            self.ERROR_IN_PROCESS = f"{self.__emojis.ERROR} Из-за внутренней ошибки ваш проигрыватель был перезапущен, пропустив песню."
            self.MY_ERROR_BAD_COMMAND = 'Эта строка служит для проверки, была ли какая-то ошибка вызвана мной намеренно'
            self.BAD_COMMAND_TITLE = 'Злоупотребление властью'
            self.BAD_COMMAND = f'{self.__emojis.ERROR} Неправильное использование этой команды, введите {configs.BOT_PREFIX}помощь "команда", чтобы лучше понять команду'
            self.VIDEO_UNAVAILABLE = f'{self.__emojis.ERROR} Извините. Это недоступно для скачивания.'
            self.ERROR_DUE_LOOP_ONE_ON = f'{self.__emojis.ERROR} Эта команда не может быть выполнена при активированном первом цикле. Воспользуйтесь {configs.BOT_PREFIX}отключите цикл, чтобы отключить цикл.'


class SearchMessages(Singleton):
    def __init__(self) -> None:
        if not super().created:
            config = VConfigs()
            self.UNKNOWN_INPUT = f'Этот тип ввода был слишком странным, попробуйте что-нибудь другое или введите {config.BOT_PREFIX}помощь играть'
            self.UNKNOWN_INPUT_TITLE = 'Ничего не найдено'
            self.GENERIC_TITLE = 'URL-адрес не удалось обработать'
            self.SPOTIFY_NOT_FOUND = 'Spotify не смог обработать ни одну песню с этим вводом, подтвердите вашу ссылку или повторите попытку позже.'
            self.YOUTUBE_NOT_FOUND = 'YouTube не смог обработать ни одну песню с помощью этого ввода, подтвердите вашу ссылку или повторите попытку позже.'
            self.DEEZER_NOT_FOUND = 'Deezer не смог обработать ни одну песню с помощью этого ввода, подтвердите вашу ссылку или повторите попытку позже.'


class SpotifyMessages(Singleton):
    def __init__(self) -> None:
        if not super().created:
            self.INVALID_SPOTIFY_URL = 'URL-адрес не удалось обработать'
            self.GENERIC_TITLE = 'URL-адрес не удалось обработать'


class DeezerMessages(Singleton):
    def __init__(self) -> None:
        if not super().created:
            self.INVALID_DEEZER_URL = 'Неверный URL Deezer, подтвердите вашу ссылку.'
            self.GENERIC_TITLE = 'URL-адрес не удалось обработать'
