from Config.Singleton import Singleton


class VEmojis(Singleton):
    def __init__(self) -> None:
        if not super().created:
            self.SKIP = "<:next:1066245701648007198>"
            self.BACK = "<:forward:1066245699580198952>"
            self.PAUSE = "<:pause:1066245706135904337>"
            self.PLAY = "<:play:1066245703627702324>"
            self.STOP = "<:stoping:1066247843288985631>"
            self.LOOP_ONE = "<:repeaone:1066245709160005642>"
            self.LOOP_OFF = "<:loopofff:1066248002852880394>"
            self.LOOP_ALL = "<:repea:1066245707645861928>"
            self.SHUFFLE = "<:shufle:1066247973782175834>"
            self.QUEUE = "<:discovery:1028852558049067088>"
            self.MUSIC = "<:verify:1066249197432619038>"
            self.ERROR = "<:no:1066247935857279069>"
            self.DOWNLOADING = "<:Downloading:1066247870195445863>"
            self.SUCCESS = "<:yes:1066247917419114587>"
