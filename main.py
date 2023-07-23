from Music.AyameInitializer import AyameInitializer
from Config.Folder import Folder

if __name__ == '__main__':
    folder = Folder()
    initializer = AyameInitializer(willListen=True)
    AyameBot = initializer.getBot()
    AyameBot.startBot()
