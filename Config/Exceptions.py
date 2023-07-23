from Config.Messages import Messages


class AyameError(Exception):
    def __init__(self, message='', title='', *args: object) -> None:
        self.__message = message
        self.__title = title
        super().__init__(*args)

    @property
    def message(self) -> str:
        return self.__message

    @property
    def title(self) -> str:
        return self.__title


class ImpossibleMove(AyameError):
    def __init__(self, message='', title='', *args: object) -> None:
        message = Messages()
        if title == '':
            title = message.IMPOSSIBLE_MOVE
        super().__init__(message, title, *args)


class MusicUnavailable(AyameError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)


class YoutubeError(AyameError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)


class BadCommandUsage(AyameError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)


class DownloadingError(AyameError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)


class SpotifyError(AyameError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)


class DeezerError(AyameError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)


class UnknownError(AyameError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)


class InvalidInput(AyameError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)


class WrongLength(AyameError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)


class ErrorMoving(AyameError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)


class ErrorRemoving(AyameError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)


class InvalidIndex(AyameError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)


class NumberRequired(AyameError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)
